---
category:
  - Tech
tags:
  - GCP
status: Done
---
**一、 引言**

当 Google Cloud 用户（使用其 Google 账号，例如 `yourname@gmail.com`）需要访问项目中的 Compute Engine 虚拟机（VM）时，其授权和认证过程与服务账号（Service Account）代表应用访问资源不同。用户访问 VM 主要涉及两个层面的检查：Google Cloud IAM 权限检查和虚拟机操作系统层面的认证/授权。

**二、 核心原则：分层检查**

用户通过 SSH 或 `gcloud` 连接 VM 的过程通常需要通过以下两层验证：

1. **GCP IAM 权限检查:** 针对发起连接的**用户账号**。
2. **VM 操作系统层面检查:** 针对尝试登录到 VM 操作系统的**用户身份**。

**三、 第一层：GCP IAM 权限检查 (用户权限)**

在使用 Google Cloud 工具（如 Cloud Console、`gcloud compute ssh`）或特定连接方式（如 IAP）时，GCP 会首先检查发起操作的**用户账号**是否拥有必要的 IAM 权限。

- **检查对象:** 当前登录并执行操作的用户 Google 账号。
- **所需权限示例:**
    - **基本信息:** 查看实例详情的权限（如 `compute.instances.get`，包含在 `Compute Viewer` 等角色中）。
    - **IAP 隧道:** 如果通过 IAP 连接（无公共 IP 的 VM），需要 `iap.tunnelInstances.accessViaIAP` 权限（包含在 `IAP-secured Tunnel User` 角色中）。IAP 会在连接前强制执行此检查。
    - **OS Login 管理:** 如果使用 OS Login，需要项目或实例级别的 `Compute OS Login`（允许登录）或 `Compute OS Admin Login`（允许登录并自动获得 `sudo` 权限）角色。
    - **元数据密钥管理:** 如果 `gcloud` 需要将用户的公钥推送到元数据，可能需要 `compute.instances.setMetadata` 等权限（包含在 `Compute Instance Admin` 等角色中）。
- **目的:** 控制用户是否有权通过 GCP 的机制**尝试**连接到该 VM 或使用特定功能（如 OS Login、IAP）。

**四、 第二层：VM 操作系统层面认证/授权**

当连接请求到达 VM 的 SSH 端口后（可能已通过 IAP 隧道），VM 本身的操作系统需要验证用户身份并授权登录。主要有两种配置方式：

1. **OS Login (操作系统登录 - 推荐方式)**
    
    - **机制:** VM 上的 OS Login 服务与 GCP IAM 集成。它会查询 GCP 以验证尝试登录用户的 IAM 角色 (`compute.osLogin` 或 `compute.osAdminLogin`)。
    - **Linux 用户账号:** **动态创建或配置**。无需在 VM 上手动管理用户。OS Login 服务根据用户的 Google 身份信息自动处理。
    - **登录和 Sudo 权限:** 由分配给用户的 IAM **角色** (`compute.osLogin` 或 `compute.osAdminLogin`) 决定。
    - **SSH 密钥:**
        - **仍然需要密钥对**进行 SSH 认证。
        - **公钥管理与 IAM 集成：** 用户的公钥与 Google 身份关联（通过 `gcloud` 添加、Cloud Shell 生成等）。登录时，GCP 在验证 IAM 权限后，**动态、安全地**将用户的公钥提供给 VM 上的 OS Login 服务用于验证。
        - **无需手动管理 `authorized_keys` 文件。**
        - 用户的 SSH 客户端在连接时**仍需使用对应的私钥**。
2. **元数据 SSH 密钥 (传统方式)**
    
    - **机制:** 依赖标准的 Linux SSH 服务 (`sshd`) 和 `~/.ssh/authorized_keys` 文件。
    - **Linux 用户账号:** 需要在 VM 上**预先存在**对应的 Linux 用户账号。
    - **登录和 Sudo 权限:** 由标准的 Linux 用户组和 `sudoers` 配置决定。
    - **SSH 密钥:**
        - 用户将自己的**公钥**上传到 GCP 项目或实例的**元数据**中。
        - GCP 负责将元数据中的公钥同步到 VM 上对应用户的 `authorized_keys` 文件。
        - 用户的 SSH 客户端连接时需要使用对应的**私钥**。

**五、 `gcloud compute ssh` 的作用**

`gcloud compute ssh` 命令是一个便捷的工具，它封装了许多步骤：

- 使用当前 `gcloud` 登录的**用户凭证**。
- 执行必要的 **IAM 权限检查**。
- 根据 VM 的配置（是否启用 OS Login）**自动处理 SSH 密钥**（查找、生成、上传或与 OS Login 交互）。
- 如果需要，通过 **IAP 建立隧道**。
- 调用本地 SSH 客户端完成连接。

**六、 权限分离场景回顾**

我们之前讨论过一个场景：用户 A 被授予了访问 VM 的权限，但没有直接访问 GCS 存储桶的权限。而该 VM 配置的服务账号拥有访问 GCS 的权限。

- 用户 A **可以**使用自己的 Google 账号权限 SSH 登录到 VM。
- 登录后，在 VM 内部执行访问 GCS 的操作时，将使用 VM **服务账号**的身份和权限，因此**可以**成功访问 GCS。
- 这体现了用户管理权限和服务运行权限的分离。

**七、 总结**

Google 用户账号通过 SSH 访问 GCP 虚拟机的授权是一个多层过程，结合了用户自身的 **IAM 权限**（用于发起连接和管理访问机制）和虚拟机操作系统配置的**认证方法**（推荐使用与 IAM 集成的 **OS Login**，或传统的基于元数据的 SSH 密钥）。`gcloud compute ssh` 简化了这一过程，但理解背后的机制有助于进行正确的权限设计和问题排查。

---