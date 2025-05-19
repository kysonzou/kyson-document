---
category:
  - Tech
tags:
  - AWS
  - GCP
status: Done
---
### AWS

#### 1. Web 登录

*   **AWS 账户 root 用户：**
    *   AWS 账户的最高权限拥有者，拥有对所有 AWS 资源的完全访问权限。
    *   强烈建议仅在绝对必要时使用，并启用多因素认证 (MFA)。

*   **IAM 用户：**
    *   在 AWS IAM 中创建的用户。
    *   可以分配特定权限（通常通过*担任角色*，而不是直接附加策略）来控制其对 AWS 资源的访问。
    *   直接给 IAM 用户附加策略不是最佳实践。

*   **IAM Identity Center 用户（以前称为 AWS SSO）：**
    *   通过 AWS IAM Identity Center 创建的用户。
    *   *不直接拥有* 访问密钥，而是通过 IAM Identity Center 门户或 AWS CLI/SDK *承担 IAM 角色*，获得临时凭证和访问权限。

*   **联合身份用户 (Federated Users)：**
    *   通过外部身份提供商（如 Active Directory、Google Workspace、Okta 等）进行身份验证的用户。
    *   通常不直接在 AWS 中创建，而是通过身份提供商映射到 IAM 角色，获得对 AWS 资源的访问权限。

#### 2. SSH 登录

*   **EC2 实例上的本地用户 (Linux/Windows)：**
    *   在 EC2 实例的操作系统中创建的用户（如 Linux 中的 `ubuntu`、`ec2-user`，Windows 中的 `Administrator`）。
    *   使用 SSH 密钥对或密码进行身份验证。
    *   与 AWS 的 IAM 系统是*间接*相关的（EC2 实例可能需要 IAM 角色来访问其他 AWS 资源，但这与 SSH 登录本身的用户无关）。

*   **(通过 EC2 Instance Connect) IAM 用户/角色/IAM Identity Center 用户：**
    *   如果使用 EC2 Instance Connect，你的 IAM 用户、担任角色的 IAM Identity Center 用户或角色需要 `ec2-instance-connect:SendSSHPublicKey` 权限。
    *   EC2 Instance Connect 将临时 SSH 公钥推送到实例，然后你可以使用相应的私钥连接。
    *   最终是*通过 IAM 角色*提供权限。

*   **(通过 Systems Manager Session Manager) IAM 用户/角色/IAM Identity Center 用户：**
    *   如果通过 SSM 进行连接，则要求你的 IAM 用户、担任角色的 IAM Identity Center 用户或角色有 `ssm:StartSession` 权限。
    *   EC2 *实例*需要安装 SSM Agent 并且附加具有 `ssm:UpdateInstanceInformation` 等权限的 IAM 角色。
    *   最终是*通过 IAM 角色*提供权限。

#### 3. 自动部署

*   **IAM 角色 (强烈推荐)：**
    *   在自动化脚本或工具（如 AWS CLI、Terraform、CloudFormation、Ansible 等）中，最佳实践是为 EC2 实例、Lambda 函数、容器等*分配 IAM 角色*，以便它们能够安全地访问 AWS 资源，而无需管理长期密钥。

*   **IAM 用户 (不推荐)：**
    *   理论上，可以在自动化脚本或工具中使用 IAM 用户的访问密钥/秘密密钥，但这是 *不推荐* 的做法，因为它存在安全风险（长期密钥泄露）。

*   **(通过 IAM Identity Center) IAM 角色：**
    *   如果组织使用 IAM Identity Center，自动化脚本或工具可以配置为使用 IAM Identity Center 用户的会话来 *承担 IAM 角色*，然后使用该角色的临时凭证来访问 AWS 资源。

*   **Service Role (服务角色)：**
    *   一种特殊的 IAM Role，用于给 AWS 服务授权，以代表用户访问其他服务，例如 EC2、Lambda、ECS 等。

---

### GCP

#### 1. Web 登录

*   **Google 账号 (Gmail 账号)：**
    *   用于登录 Google Cloud Console、Cloud Shell 等。

*   **Google Workspace 账号：**
    *   如果你的组织使用 Google Workspace，则可以使用 Google Workspace 账号登录。

*   **服务账号 (Service Accounts) (有限)：**
    *   服务账号主要用于应用程序和服务之间的身份验证。
    *   虽然可以通过生成密钥文件或使用 Workload Identity Federation 进行 Web 界面身份验证，但这 *不是* 服务账号的典型用法。

*   **联合身份用户 (Federated Users)：**
    *   通过外部身份提供商（例如 Active Directory、Okta 等）进行身份验证的用户。

#### 2. SSH 登录

*   **Compute Engine 实例上的本地用户 (Linux/Windows)：**
    *   在 Compute Engine 实例的操作系统中创建的用户。
    *   与 GCP 的 IAM 系统是*间接*相关的（实例可能需要服务账号来访问其他 GCP 资源，但这与 SSH 登录本身的用户无关）。

*   **(通过 OS Login) Google 账号/Google Workspace 账号：**
    *   如果启用了 OS Login，则可以使用你的 Google 账号或 Google Workspace 账号通过 SSH 连接到实例。
    *   OS Login 会将你的 SSH 公钥与你的 Google 账号关联，并根据你在 GCP IAM 中的角色授予相应的权限。
    - 需要支持OS Login的客户端（gcloud支持）

*   **(通过 `gcloud` 命令行工具) Google 账号/Google Workspace 账号/服务账号：**
    *   `gcloud compute ssh` 命令会自动处理 SSH 密钥管理，并可以使用你的 Google 账号、Google Workspace 账号或服务账号进行身份验证。

#### 3. 自动部署

*   **服务账号 (Service Accounts) (强烈推荐)：**
    *   这是在 GCP 中进行自动部署的 *主要* 方式。服务账号代表一个应用程序或服务，而不是一个用户。
    *   可以为服务账号分配特定的 IAM 角色，以控制其对 GCP 资源的访问。
    *   自动化脚本或工具（例如 Terraform、Ansible、Deployment Manager）可以使用服务账号的密钥文件或 Workload Identity Federation 进行身份验证。
* **用户管理的密钥的服务账号（不推荐）**
    * 理论上可以使用用户管理的密钥进行服务账号的认证，不推荐，有泄露风险。

---

**关键总结：**

*   **AWS 中 IAM 角色的重要性：** 在 AWS 中，无论是通过 Web 控制台、SSH 还是自动部署，IAM 角色都是权限管理的核心。IAM Identity Center 用户和联合身份用户最终都是通过承担 IAM 角色来获得权限。直接给 IAM 用户附加策略不是最佳实践。
*   **GCP 中服务账号的重要性：** 在 GCP 中，服务账号是自动部署的首选方式。虽然 Google 账号可以用于 Web 登录和 SSH（通过 OS Login 或 `gcloud`），但在自动化场景中，服务账号提供了更好的安全性和可管理性。
*   **SSH 登录的本地用户：** 无论是 AWS 还是 GCP，EC2/Compute Engine 实例上的本地用户（例如 Linux 的 `ubuntu`）与云平台的 IAM 系统是间接相关的。实例本身可能需要 IAM 角色/服务账号来访问云资源，但这与通过 SSH 登录的本地用户是分开的。
*   **不推荐使用长期密钥：** 无论是 IAM User，还是服务账号，都不推荐直接使用其长期密钥，而是使用临时密钥，或者通过扮演角色的方式，获取权限。
