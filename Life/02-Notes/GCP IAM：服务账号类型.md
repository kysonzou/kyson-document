---
category:
  - Knowledge
tags:
  - GCP
status: Done
---
### 1. 关键区别：服务账号类型

这是理解权限分配的关键点：

- **用户管理的服务账号 (User-Managed Service Accounts):**
    
    - **包括:** 你手动创建的服务账号，以及虚拟机默认服务账号 (格式通常为 `[PROJECT_NUMBER]-compute@developer.gserviceaccount.com`)。
    - **代表身份:** 通常代表一个应用、一个脚本或一个 VM 实例本身的身份。
    - **管理:** 由用户创建、管理密钥、授予角色、控制生命周期。
    - **可见性:** 出现在 "IAM & Admin" -> "Service Accounts" 列表中。
    - **权限应用:** 当你需要让你的应用或 VM 内的代码访问其他 GCP 资源时，应将权限授予给此类服务账号（例如，VM 访问 GCS，就给 VM 的服务账号授予 Storage 相关角色）。
- **Google 管理的服务账号 / 服务代理 (Google-Managed Service Accounts / Service Agents):**
    
    - **例子:** `[PROJECT_NUMBER]@cloudservices.gserviceaccount.com` (Google APIs Service Agent), `service-[PROJECT_NUMBER]@compute-system.iam.gserviceaccount.com` (Compute Engine Service Agent) 等。
    - **代表身份:** 代表 **Google Cloud 服务本身**（如 Compute Engine 服务、Cloud Build 服务等）在你项目中执行操作的身份。
    - **管理:** 由 Google 自动创建和管理，用户无法*管理其密钥或生命周期。
    - **可见性:** 默认不显示在 "Service Accounts" 列表中。它们会出现在**具体资源的权限策略**中（如果被授权），或者在主 **"IAM & Admin" -> "IAM"** 页面**勾选了 "Include Google-provided role grants" (包括 Google 提供的角色授权)** 选项后才可见。
    - **权限应用:** 通常由 Google 在启用服务时自动授予必要的**服务代理角色**（如 `roles/compute.serviceAgent`），以确保服务能在后台正常运行和管理资源。这些权限是给 **Google 服务后台**使用的，不是直接给你的应用代码使用的。
    >帮助理解：每个项目都关联有一个云存储服务账户。它用于执行某些后台操作：接收 PubSub 通知以及加密/解密 KMS 加密的对象。
### 2. 修改 Google 服务代理的权限

- **技术上可能:** GCP 的 IAM 界面可能显示允许编辑这些服务代理的角色绑定。
- **强烈不建议:** **绝对不要**轻易修改或移除 Google 自动授予服务代理的**默认角色**。这样做极有可能破坏对应的 Google Cloud 服务功能。控制台阻止编辑通常是为了保护服务运行。
- **例外情况:** 仅在有明确的官方文档指示下，**添加**额外的角色（例如，为 CMEK 功能给服务代理添加 KMS 相关角色）。注意是**添加**，不是替换或删除默认角色。

### 3. 风险与最小权限原则

- **风险:** 授予 Google 服务代理权限存在理论上的风险（依赖于 Google 自身的安全性），但这是使用云服务所必需的，风险由 Google 管理。可以通过 Audit Logs 监控其行为。
- **最小权限原则:**
    - 对于**用户和用户管理的服务账号**，应严格遵循，授予完成任务所需的最小权限。
    - 对于**Google 管理的服务代理**，Google 旨在授予**服务自身运行**所需的最小权限集合（体现在其特定的服务代理角色中）。虽然历史上的 `Editor` 角色较宽泛，但 Google 趋势是使用更精细的角色。
    - 用户的重点应该是管理好**自己控制的身份**的权限，并利用组织策略等其他工具进行约束。

### 4. 核心要点总结

- IAM 是 GCP 权限控制的核心，基于“谁、什么、哪里”的模型和资源层级。
- 理解“用户管理的服务账号”和“Google 管理的服务代理”之间的**根本区别**至关重要。
- **不要修改或删除** Google 为其服务代理自动配置的默认 IAM 角色。
- 将**最小权限原则**严格应用于你直接管理的用户、群组和服务账号。
- 利用 **IAM & Admin** 页面（分层级）和**具体资源**的权限设置来管理访问控制。
