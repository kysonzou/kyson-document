---
category:
  - Tech
tags:
  - GCP
status: Done
---
IAM（Identity and Access Management）
### **1. 什么是GCP IAM？**

IAM是Google Cloud Platform（GCP）的身份和访问管理服务。它让你能够精细地控制谁（身份）对你的GCP资源（如虚拟机、数据库、存储桶等）拥有什么样的访问权限（角色）。

### **2. IAM的设计原理：最小权限原则**

IAM的核心设计原则是“最小权限原则”（Principle of Least Privilege）。这意味着：

*   **只授予必要的权限：** 用户或服务应该只被授予完成其工作所需的最低限度的权限。
*   **避免过度授权：** 不要授予用户或服务超出其职责范围的权限，以减少潜在的安全风险。

### **3. IAM的重要概念**

*   **成员（Member）：**
    *   可以是用户（通过Google账号、服务账号、Google群组、G Suite或Cloud Identity域名）
    *   也可以是服务（Google API、Cloud Functions等）
    *   总之，成员就是需要访问GCP资源的实体。

*   **角色（Role）：**
    *   角色是一组权限的集合。例如，“Compute Engine Instance Admin”角色包含了一系列管理Compute Engine虚拟机的权限。
    *   GCP提供了预定义角色，你也可以创建自定义角色。
    *   **预定义角色：**
        *   **基本角色（原始角色）：** Owner, Editor, Viewer。这三种角色权限范围广，不推荐在生产环境使用，仅适用于快速原型或学习。
        *   **预定义角色：** GCP针对各种服务和场景提供了数百个预定义角色，例如"Storage Object Viewer"（允许查看Cloud Storage对象）、"Pub/Sub Publisher"（允许向Pub/Sub主题发布消息）等。
        *   **自定义角色：** 当预定义角色无法满足需求时，你可以创建自定义角色，精确指定所需的权限。

*   **权限（Permission）：**
    *   权限定义了对特定资源执行特定操作的能力。例如，`compute.instances.start` 权限允许启动Compute Engine虚拟机实例。
    *   权限通常以 `service.resource.verb` 的格式表示。
    *   通常，你不直接授予用户权限，而是通过角色来间接授予。

*   **IAM 策略（Policy）：**
    *   IAM策略是一个JSON文档，它将一个或多个成员绑定到一个或多个角色。
    *  IAM 策略是将角色授予主体的机制。它定义了：
        * **主体 (members):**  谁被授予权限。
        * **角色 (role):**  被授予的权限类型。
        * **资源 (resource):**  策略应用的目标资源 (可以是项目、文件夹、组织或具体资源本身)。
    *  IAM 策略可以附加到不同的层级：
        * **组织级策略:**  应用于整个 GCP 组织。
        * **文件夹级策略:**  应用于文件夹及其包含的项目。
        * **项目级策略:**  应用于项目及其包含的资源。
        * **资源级策略:**  应用于单个资源 (例如，特定存储桶)。
    * **策略继承:**  子层级的资源会继承父层级的策略。如果在子层级也定义了策略，则会合并父层级策略和子层级策略。

*   **资源层次结构（Resource Hierarchy）：**
    *   GCP资源以层次结构组织：组织 > 文件夹 > 项目 > 资源。
    *   IAM策略可以在层次结构的任何级别应用。
    *   子级资源继承父级资源的策略（但可以覆盖）。

>[!info] 想象一下你家里的钥匙系统：
>
> * **主体 (Principal):**  你 (用户), 你的家人 (用户群组), 智能家居系统 (服务账号)。
> * **资源 (Resource):**  家门, 卧室门, 保险箱。
> * **角色 (Role):**  家门钥匙 (可以开家门), 卧室门钥匙 (只能开卧室门), 保险箱密码 (可以打开保险箱并进行操作)。
> * **策略 (Policy):**  你拥有一整串钥匙，可以打开所有门 (组织级/项目级策略)，你的孩子只有卧室门钥匙 (资源级策略)。

>[!question] 角色如何授予组织、文件夹、项目和资源
> - 角色不是直接“给到”组织、项目、文件夹或资源本身，而是通过 IAM 策略来实现的。 IAM 策略定义了在哪个资源层级（或具体资源上），哪些主体被授予了哪些角色。
> - 通过在该资源上创建 **IAM 策略绑定** 来实现。绑定将成员与角色关联。
> - 利用 **资源层次结构** 和 **策略继承**：子资源继承父资源的策略。
> - 示例：在组织级别授予"Project Creator"角色，允许用户在组织内创建项目；在文件夹级别授予"Compute Admin"角色，只允许管理该文件夹及其子项中的计算资源。

>[!question] 服务账户和google账户的关系
> - **Google 账户：** 代表真实用户，直接授权访问 GCP 资源。
> -   **服务账户：** 代表应用程序/服务，通过密钥或短期凭据验证。被授予执行特定任务的权限。
> -   **模拟服务账户：** Google 账户可以“模拟”服务账户，临时获取其权限。这是一种安全提升权限的方式。可以使用roles/iam.serviceAccountUser 或 roles/iam.serviceAccountTokenCreator 角色授权给google账户。

### **4. 如何使用IAM**

*   **通过GCP Console：**
    1.  打开GCP Console（[https://console.cloud.google.com/](https://console.cloud.google.com/)）。
    2.  导航到“IAM & Admin” > “IAM”。
    3.  在这里，你可以添加成员、授予角色、查看和修改现有策略。

*   **通过`gcloud`命令行工具：**
    ```bash
    # 为用户授予项目级别的角色
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member='user:your-email@example.com' \
        --role='roles/storage.objectViewer'

    # 为服务账号授予角色
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member='serviceAccount:your-service-account@project-id.iam.gserviceaccount.com' \
        --role='roles/compute.instanceAdmin.v1'
    ```

*   **通过客户端库（如Python）：**
    ```python 
    from google.cloud import storage
    from google.cloud import iam_v1

    # 创建IAM客户端
    iam_client = iam_v1.IAMPolicyClient()

    # 获取现有策略
    policy = iam_client.get_iam_policy(resource="projects/your-project-id")

    # 添加绑定（将成员添加到角色）
    binding = iam_v1.Binding(
        role="roles/storage.objectViewer",
        members=["user:your-email@example.com"],
    )
    policy.bindings.append(binding)

    # 设置更新后的策略
    iam_client.set_iam_policy(resource="projects/your-project-id", policy=policy)
    ```

*  **通过Terraform (基础设施即代码)：**

```terraform
resource "google_project_iam_member" "project-roles" {
  project = "your-project-id"
  role    = "roles/storage.objectViewer"
  member  = "user:your-email@example.com"
}
```

### **5. 常见使用场景**

*   **团队协作：**
    *   为开发团队成员授予“Compute Engine Instance Admin”角色，允许他们管理虚拟机。
    *   为数据分析师授予“BigQuery Data Viewer”角色，允许他们查询BigQuery数据集。
    *   为运营团队授予“Monitoring Viewer”角色，允许他们查看监控指标。

*   **服务账号：**
    *   为在Compute Engine虚拟机上运行的应用程序创建服务账号，并授予该服务账号访问Cloud Storage的权限，以便应用程序可以读取和写入存储桶中的对象。
    *   为Cloud Functions创建服务账号，并授予该服务账号访问其他GCP服务（如Cloud SQL、Pub/Sub）的权限。

*   **自动化部署：**
    *   使用服务账号进行自动化部署，例如，使用Cloud Build自动构建和部署应用程序，Cloud Build服务账号需要具有相应的权限来访问代码仓库、构建镜像、部署到目标环境（如App Engine、Cloud Run、Kubernetes Engine）。

*   **审计和合规性：**
    *   使用Cloud Audit Logs记录所有IAM策略更改，以便进行审计和跟踪。
    *   使用IAM Recommender获取有关权限的建议，帮助你优化IAM策略，遵循最小权限原则。

### **6. 最佳实践**

*   **遵循最小权限原则：** 始终只授予完成任务所需的最低限度的权限。
*   **使用预定义角色：** 尽可能使用GCP提供的预定义角色，而不是自定义角色。
*   **定期审查权限：** 定期审查和更新IAM策略，确保权限仍然有效且符合最小权限原则。
*   **使用服务账号：** 对于应用程序和服务，使用服务账号而不是用户账号。
*   **启用多因素身份验证（MFA）：** 为所有用户启用MFA，提高安全性。
*   **使用条件：** 在IAM策略中，你可以使用条件来进一步限制权限。例如，你可以限制只允许在特定时间段内或从特定IP地址访问资源。

**总结**

GCP IAM是一个强大而灵活的访问控制系统。通过理解其核心概念、设计原理和最佳实践，你可以有效地管理GCP资源访问权限，确保安全性和合规性。记住，最小权限原则是IAM的核心，始终只授予必要的权限。