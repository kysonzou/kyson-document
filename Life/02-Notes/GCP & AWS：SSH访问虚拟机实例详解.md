---
category:
  - Tech
tags:
  - AWS
  - GCP
status: Done
---
### 1. 凭证类型：长期凭证 vs. 短期凭证

*   **长期凭证:**
    *   **定义:** 一旦创建，除非手动撤销或轮换，否则一直有效。
    *   **示例:**
        *   GCP: 服务账号密钥 (JSON 文件)
        *   AWS: IAM 用户的访问密钥 (Access Key ID 和 Secret Access Key)
        *   SSH: 手动生成的 SSH 密钥对 (私钥)
    *   **风险:** 容易泄露、被盗用或长期有效导致安全隐患。
*   **短期凭证:**
    *   **定义:** 具有有限的有效期，过期后自动失效。
    *   **示例:**
        *   GCP: OAuth 2.0 访问令牌 (通过服务账号或 Workload Identity 获取), OS Login 生成的短期 SSH 密钥
        *   AWS: 通过 IAM 角色 (AssumeRole) 或 STS 获取的临时安全凭证, EC2 Instance Connect 推送的短期 SSH 公钥
    *   **优势:** 降低了凭证泄露的风险，更符合最小权限原则。

**最佳实践：** 优先使用短期凭证，避免使用长期凭证。

### 2. 服务账号 (GCP) 和 IAM 角色 (AWS)

*   **服务账号 (GCP):**
    *   一种特殊的 Google 账号，代表应用程序或 VM 实例，而不是单个用户。
    *   可以分配 IAM 角色，授予其访问 GCP 资源的权限。
    *   应用程序可以使用服务账号获取 *短期* 的 OAuth 2.0 访问令牌。
    *   两种类型：
        *   **Google 管理的服务账号 (推荐):** Google 自动管理密钥轮换。
        *   **用户管理的服务账号:** 用户负责密钥管理 (不推荐，除非有特殊需求)。
*   **IAM 角色 (AWS):**
    *   一种 IAM 实体，定义了一组权限 (通过附加的 IAM 策略)。
    *   可以被 IAM 用户、AWS 服务或其他 AWS 账户 *担任* (Assume)。
    *   担任角色后，可以获得 *临时* 安全凭证 (Access Key ID, Secret Access Key, Session Token)。
    *   不包含长期凭证 (没有访问密钥)。

**最佳实践：** 使用服务账号 (GCP) 或 IAM 角色 (AWS) 来授权应用程序访问云资源，而不是使用长期凭证。

### 3. OS Login (GCP)

*   **定义:**  GCP 推荐的 VM 实例 SSH 访问管理机制。
*   **原理:**
    *   将 Google 账户的身份与 Linux 用户账户关联起来。
    *   使用 Google Compute Engine 的 *元数据服务* 提供 *短期有效* 的 SSH 密钥。
    *   通过 Google Cloud IAM 集中管理用户对 VM 的访问权限。
*   **优点:**
    *   **更安全:** 使用短期 SSH 密钥，降低密钥泄露风险。
    *   **集中管理:** 通过 IAM 控制用户访问权限。
    *   **支持两步验证:** 强制执行 Google 账户的两步验证。
    *   **自动密钥轮换:** 无需手动管理 SSH 密钥。
    *   **审计日志:** 记录所有登录事件。
*   **启用方式:** 在 VM 实例或项目级别启用 OS Login 功能。

**最佳实践：** 强烈建议在 GCP 中启用 OS Login。

### 4. EC2 Instance Connect (AWS)

*   **定义:**  AWS 提供的安全、便捷的 SSH 连接到 EC2 实例的机制。
*   **原理:**
    *   使用 IAM 身份进行身份验证和授权。
    *   通过 EC2 Instance Connect API 将 *临时* SSH 公钥 (有效期 60 秒) 推送到 EC2 实例的 *实例元数据服务* (IMDS)。
    *   EC2 实例上的 EIC 代理从 IMDS 获取公钥，并将其添加到指定用户的 `authorized_keys` 文件中。
*   **使用方式:**
    *   AWS 管理控制台 (基于浏览器的 SSH 终端)。
    *   AWS CLI (`aws ec2-instance-connect ssh` 命令)。
    *   自定义 SSH 客户端 + EC2 Instance Connect API。
*   **优点:**
    *   **临时密钥:** 降低密钥泄露风险。
    *   **IAM 集成:** 通过 IAM 策略控制访问权限。
    *   **简化 SSH 连接:** 避免手动管理 SSH 密钥。

**最佳实践:** 推荐使用 EC2 Instance Connect 连接到 EC2 实例。

### 5. 手动 SSH 密钥管理 (不推荐)

*   **GCP (未启用 OS Login):**
    *   手动生成 SSH 密钥对。
    *   将公钥添加到 VM 实例或项目的元数据中。
    *   使用 SSH 客户端和私钥连接到 VM。
*   **AWS (未使用 EC2 Instance Connect):**
    *   手动生成 SSH 密钥对。
    *   在创建 EC2 实例时指定公钥，或手动将其添加到实例的 `authorized_keys` 文件中。
    *   使用 SSH 客户端和私钥连接到实例。
*   **缺点:**
    *   **安全性低:**  长期密钥容易泄露、管理困难。
    *   **管理繁琐:**  需要手动创建、分发、轮换和删除密钥。
    *   **难以集中管理:**  难以跟踪和控制用户对 VM 的访问权限。

**最佳实践：** 避免手动管理 SSH 密钥，除非有特殊原因无法使用 OS Login (GCP) 或 EC2 Instance Connect (AWS)。

### 6. 官方 CLI 工具 (`gcloud` 和 `aws`) 的 SSH 支持

*   **`gcloud compute ssh` (GCP):**
    *   **未启用 OS Login:** 自动生成 *临时* SSH 密钥对，将公钥添加到 VM 实例的 *实例级元数据*，使用私钥连接。
    *   **启用 OS Login:** 与 Google Compute Engine 的 *元数据服务* 交互，获取 *短期有效* 的 SSH 密钥，并使用该密钥连接。
    *   简化了 SSH 连接过程，无需手动管理密钥。
*   **`aws ec2-instance-connect ssh` (AWS):**
    *   自动生成 *临时* SSH 密钥对 (除非提供了私钥)。
    *   使用 EC2 Instance Connect API 将公钥推送到 EC2 实例的 *实例元数据服务* (IMDS)。
    *   使用生成的私钥 (或提供的私钥) 通过 SSH 连接到实例。
    *   将密钥推送和 SSH 连接整合到一个命令中。

**最佳实践：** 使用官方 CLI 工具连接到 VM 实例，它们会自动处理 SSH 密钥，提高安全性和便捷性。

### 7. 最佳实践和安全建议

*   **优先使用短期凭证:**  避免使用长期凭证 (服务账号密钥、IAM 用户访问密钥、手动管理的 SSH 密钥)。
*   **启用 OS Login (GCP):**  使用 OS Login 管理 VM 实例的 SSH 访问。
*   **使用 EC2 Instance Connect (AWS):**  使用 EC2 Instance Connect 连接到 EC2 实例。
*   **使用官方 CLI 工具:**  使用 `gcloud compute ssh` (GCP) 和 `aws ec2-instance-connect ssh` (AWS) 连接到 VM 实例。
*   **最小权限原则:**  仅授予用户或服务账号完成任务所需的最低权限。
*   **定期轮换密钥 (如果必须使用长期密钥):**  定期生成新密钥并删除旧密钥。
*   **启用 MFA (多因素身份验证):**  对于需要高安全性的场景，强制执行 MFA。
*   **监控登录活动:**  定期检查 VM 的登录日志，及时发现异常行为。
*   **使用防火墙规则:** 限制哪些 IP 地址可以连接到 VM 的 SSH 端口。
*   **考虑使用堡垒机 (Bastion Host):** 进一步限制对 VM 的访问。

### 总结

GCP 和 AWS 都提供了多种机制来安全地通过 SSH 访问 VM 实例。 最佳实践是优先使用云平台提供的安全、便捷的解决方案 (OS Login、EC2 Instance Connect、官方 CLI 工具)，避免手动管理 SSH 密钥。 这不仅可以提高安全性，还可以简化管理，降低运营成本。