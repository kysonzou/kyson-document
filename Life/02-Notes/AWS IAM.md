---
category:
  - Tech
tags:
  - AWS
status: Done
---
[官网关于IAM的文档](https://docs.aws.amazon.com/zh_cn/IAM/latest/UserGuide/introduction_identity-management.html)

### **1. 什么是 AWS IAM？**

AWS IAM (Identity and Access Management) 是 Amazon Web Services (AWS) 的身份和访问管理服务。它允许你安全地控制对 AWS 服务和资源的访问。你可以使用 IAM 来管理身份验证（Authentication，你是谁）和授权（Authorization，你被允许做什么）。

### **2. IAM 的设计原理：安全性和精细化控制**

AWS IAM 的核心设计原则围绕安全性和精细化访问控制：

*   **最小权限原则（Principle of Least Privilege）：**  与 GCP IAM 相同，AWS IAM 也强调只授予用户和应用程序完成任务所需的最小权限。
*   **精细化访问控制：**  允许你基于各种条件（例如，用户、组、角色、资源、操作、条件）来定义细粒度的权限。
*   **集中式管理：**  IAM 提供了一个集中的位置来管理 AWS 账户中的所有身份和访问权限。
*   **安全凭证管理:**  IAM 帮助你避免在代码中硬编码 AWS 凭证，并提供安全的凭证管理机制，例如角色扮演。

### **3. IAM 的重要概念**

理解以下关键概念是掌握 AWS IAM 的基础：

*   **AWS 账户 (AWS Account)：**
    *   AWS 账户是 AWS 中的根实体，是你开始使用 AWS 的起点。
    *   资源都属于 AWS 账户。
    *   IAM 在 AWS 账户级别运行。

*   **IAM 用户 (IAM User)：**
    *   代表一个个人或应用程序，用于与 AWS 进行交互。
    *   IAM 用户拥有长期凭证（访问密钥 ID 和秘密访问密钥），用于编程访问 AWS API。
    *   最佳实践是尽量避免直接使用 IAM 用户的长期凭证，而倾向于使用 IAM 角色。

*   **IAM 组 (IAM Group)：**
    *   IAM 组是 IAM 用户的集合。
    *   组本身没有身份，不能被授予权限。
    *   组用于简化权限管理，你可以将策略附加到组，组内的所有用户将继承这些权限。

*   **IAM 角色 (IAM Role)：**
    *   IAM 角色是一种临时身份，它定义了一组权限。
    *   角色不与特定的用户或组关联，而是可以被需要它的任何实体（用户、应用程序、AWS 服务）扮演 (assume)。
    *   角色是授予 AWS 服务（如 EC2 实例、Lambda 函数）权限的首选方式，也常用于委派跨账户访问权限。

- **IAM 策略 (IAM Policy):**
    - IAM 策略是一个 JSON 文档，定义了权限。策略根据其附加位置，决定了谁（主体）可以对哪些 AWS 资源执行什么操作，以及在什么条件下执行。
    - **策略类型:** IAM 策略有两种主要类型：
        - **基于身份的策略 (Identity-based Policies):** 附加到 IAM 用户、组或角色。 策略本身不指定主体，主体由策略附加到的 IAM 实体决定。    
        - **基于资源的策略 (Resource-based Policies):** 附加到 AWS 资源（例如 S3 存储桶、SQS 队列）。策略的 Principal 元素 显式指定 允许或拒绝哪些主体访问该资源。
    - **策略元素:**
        - **Effect:** Allow (允许) 或 Deny (拒绝)。显式的 Deny 总是覆盖 Allow。
        - **Action:** 允许或拒绝的 AWS 服务操作（例如 s3:GetObject、ec2:RunInstances）。
        - **Resource:** 操作作用的目标 AWS 资源（例如特定的 S3 存储桶、EC2 实例）。可以使用通配符指定资源范围。
        - **Condition (可选):** 可选的条件，用于进一步限制权限，例如基于 IP 地址、时间、MFA 状态等。
        - **Principal（仅适用于基于资源的策略）:**
            - 在基于资源的策略中，Principal 元素 显式指定 允许或拒绝哪些主体访问该资源。
            - Principal 可以是 AWS 账户 ID、IAM 用户 ARN、IAM 角色 ARN、联合身份用户 ARN、AWS 服务主体或 *（表示匿名用户，需谨慎使用）。  
                * 在基于身份的策略中，通常 不包含 Principal元素(即便包含也会被忽略)，因为主体是由策略附加到的用户/组/角色决定的.

*   **策略类型：**
    *   **身份策略 (Identity-based Policies)：**  附加到 IAM 用户、组或角色，控制主体可以执行哪些操作。
    *   **资源策略 (Resource-based Policies)：**  附加到 AWS 资源（如 S3 存储桶、IAM 角色），控制哪些主体可以访问该资源。
    *   **权限边界 (Permissions Boundaries)：**  用于限制 IAM 实体可以被授予的最大权限。
    *   **组织 SCP (Service Control Policies)：**  在 AWS Organizations 中使用，用于集中管理组织内所有 AWS 账户的权限。

- **凭证（Credentials）：**
    - 用于验证用户或应用程序身份的信息。
    - AWS IAM 支持多种类型的凭证：
        - **密码：** 用于通过 AWS 管理控制台登录。
        - **访问密钥（Access Key ID 和 Secret Access Key）：** 用于通过 AWS CLI、SDK 或 API 进行编程访问。
        - **多因素身份验证 (MFA)：** 增加额外的安全层，通常与密码一起使用。
        - **X.509 证书：** 用于某些 AWS 服务（如 Amazon EC2）。
        - **临时安全凭证：** 通过担任角色获得，具有有限的有效期。

### **4. 如何使用 IAM**

*   **通过 AWS Management Console：**
    1.  登录 AWS Management Console。
    2.  导航到 "IAM" 服务。
    3.  在控制台中，你可以创建和管理用户、组、角色、策略等。

*   **通过 AWS CLI (命令行界面)：**
    - ...

*   **通过 AWS SDK (软件开发工具包)：**
    *   可以使用各种编程语言的 AWS SDK (如 Python 的 boto3) 以编程方式管理 IAM 资源。

*   **通过 Infrastructure as Code (IaC) 工具：**
    *   可以使用 CloudFormation、Terraform 等 IaC 工具来定义和部署 IAM 资源。

### **5. 常用使用场景**

*   **团队协作：**
    *   为开发人员、运维人员、安全团队等创建 IAM 用户或组。
    *   为不同团队或职能分配不同的 IAM 角色，授予他们访问特定 AWS 资源的权限。
    *   使用 IAM 组来统一管理一组用户的权限。

*   **授予 AWS 服务权限（角色扮演）：**
    *   为 EC2 实例、Lambda 函数、ECS 任务等 AWS 服务创建 IAM 角色。
    *   将角色附加到服务，允许服务安全地访问其他 AWS 资源，而无需在代码中硬编码凭证。
    -   例如，EC2 实例上的应用程序可以使用附加的角色访问 S3 存储桶或 DynamoDB 数据库。

*   **跨账户访问委派：**
    *   使用 IAM 角色委派跨 AWS 账户的访问权限。
    *   例如，允许一个账户中的用户或服务访问另一个账户中的资源，而无需共享长期凭证。
    -   这对于组织内不同团队或部门之间的协作非常有用。

*   **精细化权限控制：**
    *   使用 IAM 策略中的条件来限制访问，例如：
        *   基于 IP 地址限制访问来源。
        *   基于时间限制访问时间段。
        *   要求使用 MFA (多因素身份验证) 才能执行敏感操作。
        *   基于资源标签 (Tags) 控制访问。

*   **审计和合规性：**
    *   使用 AWS CloudTrail 记录所有 IAM 操作和资源访问事件，用于审计和合规性目的。
    *   使用 IAM Access Analyzer 分析 IAM 策略，识别潜在的权限风险。
    *   使用 AWS Config 监控 IAM 配置变更。

- **临时访问：**
    - 使用 IAM 角色为用户或应用程序提供临时访问 AWS 资源的权限。
    - 这比长期凭证更安全，因为临时凭证会在一段时间后自动过期。

### **6. 最佳实践**

*   **始终遵循最小权限原则：**  只授予完成任务所需的最小权限。
*   **避免使用 IAM 用户长期凭证：**  尽可能使用 IAM 角色进行身份验证。
*   **使用组来管理用户权限：**  简化用户权限管理。
*   **使用角色来授予服务和跨账户权限。**
*   **定期审查和轮换 IAM 凭证和角色。**
*   **启用 MFA for privileged users：**  为具有高权限的用户启用多因素身份验证。
*   **使用权限边界来限制 IAM 实体的最大权限。**
*   **使用 AWS Organizations SCPs 进行集中式权限管理（对于多账户环境）。**
*   **监控和审计 IAM 活动。**

**总结**

AWS IAM 是一个强大且全面的身份和访问管理服务，它提供了精细化的访问控制、安全的凭证管理和集中的权限管理功能。通过理解 IAM 的核心概念和最佳实践，你可以有效地保护你的 AWS 资源，并满足安全性和合规性要求。与 GCP IAM 类似，最小权限原则也是 AWS IAM 的核心原则。
