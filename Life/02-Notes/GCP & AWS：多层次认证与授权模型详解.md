---
category:
  - Tech
tags:
  - AWS
  - GCP
status: Done
---
### 1. 多层次模型概述

GCP 和 AWS 的认证和授权过程可以分解为三个主要层次：

1.  **身份认证 (Authentication):**  "你是谁？"
    *   验证尝试访问云资源的 *主体* (Principal) 的身份。
2.  **授权 (Authorization):**  "你能做什么？"
    *   确定已通过身份验证的主体 *有权执行哪些操作*。
3.  **服务级访问控制 (例如 SSH):**  "如何访问特定服务？"
    *   控制对特定服务 (例如 SSH) 的访问 *方式*。

这三个层次相互依赖、层层递进，共同构建了云平台的安全访问控制体系。

### 2. 层次详解

#### 2.1 身份认证 (Authentication): "你是谁？"

*   **目标:** 验证尝试访问云资源的 *主体* (Principal) 的身份。

*   **主体 (Principal):** 可以是：
    *   **用户:**
        *   GCP: Google 账号 (Gmail, Google Workspace)
        *   AWS: IAM 用户 (用户名/密码, 访问密钥)
    *   **服务账号 (GCP) / IAM 角色 (AWS):** 用于应用程序或服务的身份。
    *   **联合身份用户:** 通过外部身份提供商 (IdP) 进行身份验证的用户 (例如，通过 SAML 或 OIDC)。

*   **机制:**
    *   **用户名/密码:** 用于登录控制台。
    *   **多因素身份验证 (MFA):** 增加额外的安全层 (例如，手机验证码、硬件安全密钥)。
    *   **访问密钥 (长期凭证):** 用于通过 CLI、SDK 或 API 进行编程访问 (应尽量避免)。
    *   **OAuth 2.0 令牌 (短期凭证):** GCP 中，通过 Google 账号或服务账号获取。
    *   **SAML/OIDC 断言:** 用于联合身份验证。

#### 2.2 授权 (Authorization): "你能做什么？"

*   **目标:** 确定已通过身份验证的主体 *有权执行哪些操作*。

*   **机制:**
    *   **GCP: Google Cloud IAM (Identity and Access Management)**
        *   **角色 (Roles):** 一组权限的集合。
        *   **成员 (Members):** 可以是用户、服务账号、Google 群组或 Google Workspace 域。
        *   **绑定 (Bindings):** 将角色授予成员。
        *   **策略 (Policies):** 定义了资源上的绑定。
        *   **权限 (Permissions):** 定义了可以执行的具体操作 (例如，`compute.instances.get`, `storage.buckets.list`)。
    *   **AWS: AWS Identity and Access Management (IAM)**
        *   **策略 (Policies):** JSON 文档，定义了一组权限。
        *   **用户 (Users):** 可以附加策略。
        *   **组 (Groups):** 用户的集合，可以附加策略。
        *   **角色 (Roles):** 可以附加策略，可以被用户、服务或其他 AWS 账户担任。

*   **关键概念:**
    *   **最小权限原则:** 仅授予主体完成任务所需的最低权限。
    *   **基于角色的访问控制 (RBAC):** 通过角色来管理权限，而不是直接将权限授予用户。

#### 2.3 服务级访问控制 (例如 SSH): "如何访问特定服务？"

*   **目标:** 控制对特定服务 (例如 SSH) 的访问 *方式*。

*   **机制 (以 SSH 为例):**
    *   **GCP (OS Login):**
        *   IAM 权限: `compute.instances.osLogin` (或更具体的角色)。
        *   元数据服务: 提供短期 SSH 密钥。
        *   Google 账户与 Linux 用户账户关联。
    *   **GCP (未启用 OS Login):**
        *   IAM 权限: `compute.instances.get`, `compute.instances.setMetadata`。
        *   SSH 密钥: 存储在 VM 实例或项目元数据中 (由 `gcloud` 或手动管理)。
    *   **AWS (EC2 Instance Connect):**
        *   IAM 权限: `ec2-instance-connect:SendSSHPublicKey`。
        *   临时 SSH 公钥: 推送到实例元数据服务 (IMDS)。
        *   EC2 Instance Connect 代理: 从 IMDS 获取公钥并配置 SSH。
    *   **AWS (传统 SSH 密钥):**
        *   IAM 权限: 通常需要 `ec2:DescribeInstances`。
        *   SSH 密钥: 在创建实例时指定，或手动添加到 `authorized_keys` 文件。

*   **关键点:**
    *   服务级访问控制通常建立在前两层 (身份验证和授权) 的基础上。
    *   不同的服务可能有不同的访问控制机制。

### 3. 流程示例 (GCP, 使用 `gcloud compute ssh` 和 OS Login)

4.  **身份验证:** 用户使用 Google 账户登录 `gcloud` (获取 OAuth 2.0 令牌)。
5.  **授权:** Google Cloud IAM 检查用户是否具有 `compute.instances.osLogin` 权限。
6.  **服务级访问:**
    *   `gcloud` 与 Google Compute Engine 元数据服务交互。
    *   元数据服务为用户的 Google 账户生成短期 SSH 密钥。
    *   `gcloud` 使用该密钥通过 SSH 连接到 VM 实例。

### 4. 多层次模型的优势

*   **安全性:** 多层验证和授权，降低了未经授权访问的风险。
*   **灵活性:** 可以根据不同的场景和需求配置不同的访问控制策略。
*   **可管理性:** 通过 IAM (GCP 和 AWS) 集中管理用户和服务的权限。
*   **可扩展性:** 可以轻松地适应组织结构和业务需求的变化。

### 5. 总结

GCP 和 AWS 的认证和授权过程采用多层次、分阶段的设计，将身份验证、授权和服务级访问控制分离，提供了强大而灵活的安全保障。 理解这个模型对于构建安全、可靠的云应用程序至关重要。 最佳实践是遵循最小权限原则，使用云平台提供的安全机制 (例如 OS Login、EC2 Instance Connect)，并通过 IAM 进行集中管理。
