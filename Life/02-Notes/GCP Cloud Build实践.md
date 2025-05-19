---
category:
  - Tech
tags:
  - GCP
status: Done
---
> 终端或者VSCode的Google Cloud Code 是通过Google账号验证然后gcloud会管理生成密钥再通过SSH去登录虚拟机的，gcloud会在本地的~/.ssh文件中保存密钥（google_compute_engine、
  google_compute_engine.pub）

好的，没问题。我将我们关于 Google Cloud Build、服务账户、SSH 认证、OS Login 等的讨论总结成一篇学习笔记，重点突出它们之间的关系：

**Google Cloud Build 部署与 SSH 连接虚拟机：深入理解**

**核心概念回顾**

*   **Google Cloud Build：** GCP 提供的全托管持续集成/持续交付 (CI/CD) 服务。
*   **服务账户：** 代表应用程序或服务（如 Cloud Build）的特殊 Google 账户，用于访问 GCP 资源。
*   **SSH（Secure Shell）：** 一种加密网络协议，用于安全地登录到远程计算机（如 GCP 虚拟机）并执行命令。
*   **OS Login：** GCP 推荐的 SSH 密钥管理方式，将 IAM 权限与 Linux 用户账户关联，简化密钥管理并提高安全性。
*   **IAM 角色：** 权限的集合，用于控制对 GCP 资源的访问。
*   **Linux 用户：** 虚拟机上的用户账户，用于执行命令和管理文件。
*   **SSH 密钥对：** 由公钥和私钥组成，用于 SSH 认证。

**Cloud Build 部署与 SSH 连接虚拟机的流程**

1.  **服务账户权限（IAM 角色）：**

    *   Cloud Build 使用服务账户来执行构建和部署任务。
    *   确保 Cloud Build 服务账户拥有足够的权限：
        *   `roles/compute.osLogin` 或 `roles/compute.osAdminLogin`：（使用 OS Login 时）允许通过 SSH 连接到虚拟机。
        *   `roles/compute.instanceAdmin.v1`：（可选）如果需要管理虚拟机本身（启动、停止等）。
        *   其他必要的角色，取决于你的构建过程需要访问的其他 GCP 资源。

2.  **Linux 用户与 SSH 密钥：**

    *   在虚拟机上，你需要一个 Linux 用户账户来执行部署操作。
    *   你可以使用现有的 Linux 用户账户，或创建一个新的。
    *   为该 Linux 用户配置 SSH 密钥：
        *   **OS Login（推荐）：**
            *   启用 OS Login 后，GCP 会自动处理 SSH 密钥的生成和管理。
            *   你只需要确保 Cloud Build 服务账户具有正确的 IAM 角色。
        *   **传统的基于元数据的 SSH 密钥（不推荐）：**
            *   手动生成 SSH 密钥对（`ssh-keygen`）。
            *   将公钥添加到项目或虚拟机的元数据中，用户名设置为 Linux 用户名。
            *   将私钥安全地存储在 Secret Manager 等位置。
        *   **连接原理**： 通过用户名来找公钥，私钥与公钥配对，则通过认证。

3.  **Cloud Build 构建步骤 (`cloudbuild.yaml`)：**  
    ...

**关键关系**

*   **Cloud Build 与服务账户：** Cloud Build 使用服务账户的身份来执行构建和部署任务，包括 SSH 连接虚拟机。
*   **服务账户权限与 SSH 认证：** 服务账户权限（IAM 角色）是 SSH 认证的前提条件（使用 OS Login 时）。服务账户需要有 `roles/compute.osLogin` 或 `roles/compute.osAdminLogin` 角色才能通过 SSH 连接。
*   **SSH 认证与 Linux 用户：** SSH 认证通过用户名查找公钥，并使用公钥/私钥对来验证连接者的身份。你用什么 Linux 用户名连接虚拟机，服务器就会查找与该用户名关联的公钥。
*   **OS Login 与传统 SSH 密钥管理：** OS Login 是 GCP 推荐的 SSH 密钥管理方式，它简化了密钥管理，提高了安全性。传统的基于元数据的 SSH 密钥管理方式需要手动管理密钥，安全性较低。

>[!warning] 虽然可以通过 Google Cloud Build 利用 SSH 部署服务到虚拟机，但这通常不是最佳实践。更推荐的方式是使用容器化部署、托管实例组、配置管理工具或 Serverless 服务。这些方式更安全、更易于扩展和维护，并且符合现代云原生应用的部署理念。

