---
category:
  - Tech
tags:
  - GCP
status: Done
---
**一、 引言：IAM 基础**

Google Cloud IAM (Identity and Access Management) 是一套精细化的权限管理系统，它决定了**“谁 (Who / Principal)”**可以对**“哪个 Google Cloud 资源 (Which Resource)”**执行**“什么操作 (What / Role & Permission)”**。正确理解和使用 IAM 是保障云环境安全、实现合规以及高效协作的基础。

**二、 IAM 核心组成部分 (通用概念)**

1. **主账号 (Principal / Identity - 身份“谁”):**
    
    - 代表可以被授予权限的实体。主要包括：
        - **Google 账号 (User Account):** 代表人类用户（如 `name@gmail.com`, `name@yourcompany.com`），用于控制台登录、`gcloud` 操作等人工交互。
        - **服务账号 (Service Account):** 代表非人类用户，即应用程序、虚拟机、云服务等（如 `myapp-sa@...`, `service-PROJECT_NUMBER@...`），用于程序化地、自动地访问 Google Cloud API。
        - **Google 群组 (Google Group):** 一个 Google Group 的电子邮件地址（如 `gcp-admins@yourdomain.com`），代表该群组内的所有成员（可以是用户账号或服务账号）。是管理一组身份权限的便捷方式。
        - **特殊标识符 (Special Identifiers):**
            - `allUsers`: 代表互联网上的任何人，包括未登录的匿名用户。
            - `allAuthenticatedUsers`: 代表任何登录了 Google 账号的用户（不限特定组织）。
2. **角色 (Role - 权限“能做什么”):**
    
    - 角色是**权限 (Permissions)** 的集合。权限是执行具体操作的授权（如 `compute.instances.start`, `storage.objects.list`）。角色将相关的权限打包，方便管理。
    - **角色类型:**
        - **基本角色 (Basic Roles):** Owner (`roles/owner`), Editor (`roles/editor`), Viewer (`roles/viewer`)。提供非常广泛的、跨多种服务的权限，通常作用于项目或更高层级。**应避免**使用 Editor 和 Viewer 进行日常或精细授权，仅 Owner 用于最高层级管理。
        - **预定义角色 (Predefined Roles):** 由 Google Cloud 创建和维护，针对特定服务或常见任务场景，提供比基本角色更细粒度的权限。例如 `roles/compute.osLogin`, `roles/storage.admin`, `roles/iam.serviceAccountUser`。这是**推荐优先使用**的角色类型。
        - **自定义角色 (Custom Roles):** 当预定义角色不完全符合需求（权限过大或过小）时，可以自行创建，精确组合需要的权限。
3. **资源 (Resource - 对象“对什么”):**
    
    - IAM 权限策略作用的具体 Google Cloud 实体。例如：组织 (Organization)、文件夹 (Folder)、项目 (Project)、Compute Engine 实例 (Instance)、Cloud Storage 存储桶 (Bucket)、BigQuery 数据集 (Dataset) 等。
    - 资源通常以**层级结构**组织，权限策略可以应用在层级的不同节点上。
4. **IAM 策略 / 绑定 (Policy / Binding - 规则):**
    
    - 定义了在**某个资源**上，将**哪些主账号**与**哪些角色**关联起来。一个策略包含一个或多个绑定，每个绑定将一组主账号映射到一个角色。

**三、 权限继承 (Inheritance - 通用机制)**

- IAM 策略会沿着资源层级结构**向下继承**。设置在父资源（如项目）上的策略，其效果会自动应用于其下的所有子资源（如该项目中的存储桶、虚拟机等）。
- 这意味着，被授予项目 Editor 角色的用户，通常也会拥有对该项目下大部分资源的编辑权限（除非有更具体的策略覆盖或特殊的服务行为）。
- 权限是**累加**的，用户最终拥有的权限是其在资源层级上所有被授予角色的权限总和。

**四、 身份类型应用与最佳实践 (通用)**

1. **Google 账号 (User Account):**
    
    - **用途:** 人类管理员、开发者、用户访问控制台、执行 `gcloud` 命令。
    - **最佳实践:** 根据职责授予适当的角色。管理员可能需要项目 Owner/Editor（谨慎使用 Editor），开发者可能需要特定服务的 Admin 或 Editor/Viewer 角色，普通用户可能只需要 Viewer 或更受限的角色。**优先使用群组管理用户权限。**
2. **服务账号 (Service Account):**
    
    - **用途:** 应用、虚拟机、Cloud Functions 等服务的身份，用于访问其他 GCP API。**是实现自动化和保护用户凭证的关键。**
    - **最佳实践:**
        - **专用账号:** 为不同的应用、服务或任务创建**独立的、专用的服务账号**，而不是共用一个。
        - **最小权限:** 仅授予该服务账号完成其特定任务所必需的**最小角色和权限**。优先使用粒度细的预定义或自定义角色。
        - **最小范围:** 尽可能在服务账号需要访问的**最具体资源层面**（如特定的 Bucket、特定的 Secret）授予角色，而不是在项目层面。
        - **避免默认账号的高权限:** 特别是 Compute Engine 默认服务账号，**不应**保留其默认的 `Editor` 角色。应将其替换为专用服务账号，并移除或禁用其 `Editor` 角色。
        - **密钥管理:** 谨慎管理服务账号密钥（JSON 文件），定期轮换，优先考虑让服务直接附加服务账号身份（如 VM、Cloud Run 等），避免手动处理密钥文件。
        - **关联使用:** 服务需要被配置为**使用**（附加）相应的服务账号身份。
3. **Google 群组 (Google Group):**
    
    - **用途:** 高效管理**多个用户**的权限。
    - **最佳实践:**
        - 创建职责清晰的群组（如 `dev-team-a`, `network-admins`, `readonly-support`）。
        - 在 Google Groups 或 Google Workspace 中管理群组成员。
        - 在 GCP IAM 中，将角色授予给**群组的电子邮件地址**。
        - 人员变动时，只需调整群组成员，无需修改众多 IAM 策略。
4. **特殊标识符 (Special Identifiers):**
    
    - **用途:** 实现公共或半公共访问。
    - **最佳实践:**
        - **谨慎使用 `allUsers` 和 `allAuthenticatedUsers`。** 仅在确实需要将资源暴露给互联网或所有 Google 用户时才使用。
        - 如果使用，**务必只授予权限最小的角色**（通常是只读角色，如 `Viewer` 或 `ObjectViewer`）。
        - 确认没有敏感数据会被意外暴露。

**五、 核心原则总结 (通用)**

- **最小权限 (Least Privilege):** 只授予必要的权限，不多也不少。
- **角色选择:** 优先使用预定义角色或自定义角色，避免基本角色（Owner 除外）。
- **范围最小化:** 在最具体的资源层级授予权限。
- **身份分离:** 应用使用专用服务账号，而非用户账号或高权限默认账号。
- **使用群组:** 通过群组简化用户权限管理。
- **定期审计:** 定期检查和清理不再需要的权限。

**六、 示例：Cloud Storage 存储桶权限配置**

现在，我们将上述概念应用到一个 Cloud Storage 存储桶 `my-example-bucket` 上：

1. **初始状态:** 创建一个新的存储桶，默认是**私有**的。其权限列表可能只显示从项目继承来的权限（如 `Owners/Editors/Viewers of project ...`）。此时，`allUsers` 没有被授予任何权限。
2. **场景：授权同事只读:**
    - **方式一 (直接授权，不推荐用于多人):** 在 `my-example-bucket` 的权限设置中，添加主账号 `colleague@example.com`，授予角色 `roles/storage.objectViewer`。
    - **方式二 (使用群组，推荐):** 创建 Google Group `bucket-readers@...`，将 `colleague@example.com` 加入群组。在 `my-example-bucket` 的权限设置中，添加主账号 `bucket-readers@...`，授予角色 `roles/storage.objectViewer`。
3. **场景：授权应用写入数据:**
    - 创建一个专用服务账号 `data-writer-sa@...`。
    - 在 `my-example-bucket` 的权限设置中，添加主账号 `data-writer-sa@...`，授予角色 `roles/storage.objectAdmin` (允许读写删) 或更精确的角色组合。
    - 配置需要写入数据的应用/VM 使用 `data-writer-sa@...` 这个服务账号。
4. **场景：设置桶为公开可读:**
    - 在 `my-example-bucket` 的权限设置中，添加主账号 `allUsers`，授予角色 `roles/storage.objectViewer`。
    - 保存后，该存储桶的“Public access”状态会变为“Public to internet”。
5. **场景：移除默认服务账号的风险权限:**
    - 假设之前有个 VM 使用 Compute Engine 默认服务账号（拥有项目 Editor 权限）访问了这个桶。现在您将 VM 切换为使用上面创建的 `data-writer-sa`。之后，您在**项目 IAM 页面**移除了默认服务账号的 `Editor` 角色。
    - **结果:** VM 仍然可以通过 `data-writer-sa` 访问存储桶。默认服务账号失去了对存储桶（以及项目大部分资源）的访问权限，提高了安全性。

**七、 结语**

掌握 IAM 的核心概念——身份、角色、资源、策略和继承，并遵循最小权限、专用服务账号、使用群组等最佳实践，是确保 Google Cloud 环境安全、合规且易于管理的关键。通过具体的资源（如 Cloud Storage Bucket）来实践这些原则，可以加深理解并应用到各种云服务中。

---