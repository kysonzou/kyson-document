---
category:
  - Tech
tags:
  - AWS
status: Done
---
### **1. 什么是 AWS IAM Identity Center？**

AWS IAM Identity Center (原名 AWS Single Sign-On - AWS SSO) 是一项云服务，旨在帮助你在 **多个 AWS 账户** 和 **云应用程序** 中集中管理身份验证和授权。它主要提供 **单点登录 (SSO)** 体验，并简化跨 AWS 环境的用户访问管理。

**核心目标：**  **集中化身份管理，简化多账户访问，提供单点登录 (SSO)。**

**主要功能：**

*   **集中式身份目录：**
    *   提供内置的用户身份目录，也可以连接到外部身份源 (Identity Provider - IdP)，如 Microsoft Active Directory、Okta、Azure AD、Google Workspace 等。
    *   在一个地方管理所有用户的身份信息 (用户和组)。

*   **单点登录 (SSO)：**
    *   用户只需登录一次 IAM Identity Center 门户，即可访问所有分配给他们的 AWS 账户和云应用程序。
    *   无需为每个账户或应用程序单独输入凭证。

*   **多账户访问管理 (与 AWS Organizations 集成)：**
    *   特别适用于使用 AWS Organizations 管理多个 AWS 账户的企业。
    *   可以跨 AWS 组织中的所有账户集中管理用户访问权限。

*   **基于角色的访问控制 (权限集 - Permission Sets)：**
    *   使用 **权限集 (Permission Sets)** 定义一组权限，类似于 IAM 角色。
    *   将权限集分配给用户或组，以授予他们对特定 AWS 账户的访问权限。
    *   权限集最终转换为目标 AWS 账户中的 IAM 角色。

*   **预集成的应用程序和自定义应用程序：**
    *   预集成了许多常见的云应用程序 (如 Salesforce, Workday, ServiceNow)。
    *   支持自定义集成你自己的云应用程序。

### **2. IAM Identity Center 的重要概念**

*   **IAM Identity Center 实例 (Instance)：**  每个 AWS 区域可以创建一个 IAM Identity Center 实例，用于管理该区域的 SSO 和访问控制。

*   **身份源 (Identity Source)：**  用户身份信息的来源。可以是：
    *   **IAM Identity Center 目录：**  内置的简单用户目录。
    *   **外部身份提供商 (External Identity Provider - IdP)：**  例如，Active Directory, Okta, Azure AD, Google Workspace 等。 通过标准协议 (如 SAML, SCIM, OpenID Connect) 集成。

*   **用户 (Users) 和组 (Groups)：**  从身份源同步或在 IAM Identity Center 目录中创建的用户和组。  代表组织中的个人和用户群体。

*   **权限集 (Permission Sets)：**
    *   定义一组权限的集合，类似于 IAM 角色。
    *   在 IAM Identity Center 中创建和管理。
    *   可以基于 AWS 托管策略 (AWS managed policies) 或自定义策略创建。
    *   权限集最终会被转换为目标 AWS 账户中的 IAM 角色。

*   **AWS 账户分配 (AWS Account Assignments)：**
    *   将用户或组与特定的 AWS 账户关联起来。
    *   为每个账户分配一个或多个权限集。
    *   决定了哪些用户/组可以访问哪些 AWS 账户，以及在每个账户中拥有哪些权限。

*   **应用程序 (Applications)：**  集成的云应用程序，用户可以通过 IAM Identity Center SSO 访问。

### **3. 工作原理**

1. **配置身份源：** 选择使用 IAM Identity Center 的内置目录，或连接到外部身份提供商。
2. **创建用户和组：** 在 IAM Identity Center 中创建用户和组，或从身份源同步。
3. **创建权限集：** 定义用户或组可以访问哪些 AWS 服务和资源。
4. **将权限集分配给用户或组：** 将权限集分配给特定 AWS 账户中的用户或组。
5. **（可选）配置应用程序：** 添加你希望用户通过 SSO 访问的云应用程序。
6. **用户登录：** 用户通过 IAM Identity Center 提供的门户或应用程序登录，然后选择要访问的 AWS 账户或云应用程序。
7. **SSO 访问：** IAM Identity Center 会自动处理身份验证和授权，用户无需再次输入凭据即可访问目标资源。

### **4. IAM Identity Center 与 IAM 的关系**

*   **构建于 IAM 之上，是对 IAM 的扩展和简化：**  IAM Identity Center 不是替代 IAM，而是构建在 IAM 的基础设施之上。 它利用 IAM 的授权机制来实现跨账户的访问控制。

*   **权限集转换为 IAM 角色：**  IAM Identity Center 的权限集最终会在目标 AWS 账户中被转换为 IAM 角色。 用户通过 SSO 登录后，实际是扮演了这些 IAM 角色来访问 AWS 资源。

*   **IAM 负责精细化权限，IAM Identity Center 负责集中化管理和 SSO：**
    *   **IAM：**  负责定义精细的权限策略 (What permissions)。
    *   **IAM Identity Center：**  负责集中管理用户身份 (Who)，决定用户可以访问哪些 AWS 账户 (Where)，并提供 SSO 体验。

*   **互补而非替代：**  IAM 和 IAM Identity Center 协同工作。 IAM 提供底层的权限控制能力，IAM Identity Center 在此基础上提供更高级别的多账户管理和 SSO 功能。

### **5. IAM Identity Center 的使用场景**

*   **管理多 AWS 账户 (AWS Organizations)：**  核心使用场景，简化跨组织账户的访问管理。

*   **企业单点登录 (SSO)：**  为用户提供统一的登录入口，方便访问多个 AWS 账户和云应用程序。

*   **与企业身份目录集成：**  连接到 Active Directory, Azure AD 等，实现用户身份同步和集中管理。

*   **简化用户 onboarding/offboarding：**  集中管理用户访问权限，方便用户加入和离开团队时的权限调整。

*   **提升安全性：**  集中身份管理，减少凭证泄露风险，增强合规性。

*   **访问 AWS 控制台和 AWS CLI：**  通过 SSO 方便地访问 AWS Management Console 和 AWS Command Line Interface。

*   **访问预集成的云应用程序和自定义应用程序。**

### **6. IAM Identity Center 的优势**

*   **提高安全性：**  集中身份管理，减少长期凭证使用，利用 SSO 增强安全性。
*   **简化管理：**  集中管理跨多个账户的用户访问权限，降低管理复杂性。
*   **提升用户体验：**  单点登录，方便用户访问 AWS 资源和云应用程序。
*   **增强合规性：**  集中审计和访问控制，更容易满足合规性要求。
*   **提高效率：**  简化用户 onboarding/offboarding，加速团队协作。

### **7. IAM Identity Center 的最佳实践**

*   **与 AWS Organizations 结合使用：**  充分发挥 IAM Identity Center 在多账户管理方面的优势。
*   **集成企业身份提供商 (IdP)：**  利用现有的身份目录，简化用户管理，实现企业级 SSO。
*   **使用权限集 (Permission Sets) 进行角色管理：**  清晰定义和分配角色权限。
*   **遵循最小权限原则：**  在权限集中只授予必要的权限。
*   **定期审查和更新权限集和账户分配。**
*   **启用多因素身份验证 (MFA) for SSO：**  增强 SSO 登录的安全性。
*   **监控和审计 IAM Identity Center 活动。**

**总结**

AWS IAM Identity Center 是一个强大的服务，用于集中管理多 AWS 账户环境下的身份和访问权限，并提供单点登录体验。 它构建于 IAM 之上，简化了跨账户 IAM 角色的管理，并提供了更便捷的用户访问方式。  对于需要管理多个 AWS 账户和希望实现企业级 SSO 的组织来说，IAM Identity Center 是一个非常有价值的服务。

希望这份 IAM Identity Center 笔记对你有所帮助！ 如果你有任何其他问题，请随时提出。