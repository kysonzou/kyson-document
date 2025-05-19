---
category:
  - Tech
tags:
  - AWS
status: Done
---
> 将用户和权限配置到aws账户

**核心概念:**
*   **IAM Identity Center (原 AWS SSO):** AWS 的单点登录 (SSO) 服务，用于集中管理用户、组、对 AWS 账户的访问权限以及对云应用程序的访问权限。
*   **用户 (Users):** 在 IAM Identity Center 中创建的个体用户。
*   **组 (Groups):** 用户的集合，用于简化权限管理（强烈推荐使用组）。
*   **权限集 (Permission Sets):** 定义了一组针对 *特定 AWS 账户* 的权限。 它们是 AWS 托管策略、自定义策略或现有工作函数策略的组合。
*   **AWS 账户 (AWS Accounts):** 你的 AWS 资源（EC2、S3、DynamoDB 等）所在的账户。 IAM Identity Center 可以管理对多个 AWS 账户的访问。
*   **应用程序分配 (Application Assignments):** 用于控制用户对 *云应用程序*（如 Salesforce、Microsoft 365、Google Workspace 等）的访问，并提供单点登录 (SSO) 功能。
*   **单点登录 (SSO):** 允许用户使用一套凭据登录到多个应用程序。
*   **SAML 2.0:** 一种用于在身份提供商（如 IAM Identity Center）和服务提供商（如云应用程序）之间交换身份验证和授权数据的开放标准。
*   **OIDC (OpenID Connect):** 另一种身份验证标准, 常用于移动和 Web 应用程序。
*    **AWS 组织 (AWS Organizations):** 可以将多个AWS 账户组织成一个整体进行统一管理的服务。（如果你的账户是通过 AWS Organizations 创建的, 那么通常会建议和 IAM Identity Center 集成)

**主要功能:**

1.  **AWS 账户访问管理:**

    *   **目标:** 控制用户对 *AWS 资源* 的访问权限。
    *   **机制:** 通过 *权限集 (Permission Sets)* 实现。
    *   **步骤:**
        1.  创建用户（或组，并将用户添加到组）。
        2.  创建权限集，定义所需的 AWS 权限。
        3.  在 IAM Identity Center 中，选择 *特定的 AWS 账户*。
        4.  将用户（或组）与权限集 *关联*。  这会在目标 AWS 账户中创建相应的 IAM 角色。
        5.  用户通过 IAM Identity Center 门户登录，选择 AWS 账户和角色，即可获得权限。
    *   **最佳实践:**
        *   使用组管理用户和权限。
        *   遵循最小权限原则。
        *   定期审查权限。
        *  尽可能使用AWS 托管的权限集。
    *    **注意:** 权限集是定义, 必须在 *特定 AWS 账户* 中进行分配。

2.  **云应用程序访问管理 (应用程序分配):**

    *   **目标:** 实现对云应用程序的 *单点登录 (SSO)* 和集中式访问管理。
    *   **机制:** 通过 *应用程序分配 (Application Assignments)* 实现。
    *   **步骤:**
        1.  在 IAM Identity Center 中配置云应用程序（通常使用 SAML 2.0 或 OIDC）。
        2.  将用户或组分配给已配置的应用程序。
        3.  用户通过 IAM Identity Center 用户门户访问应用程序，无需再次输入凭据。
    *   **支持的应用程序:**
        *   AWS 管理的应用程序（如 AWS 管理控制台、AWS CLI）。
        *   支持 SAML 2.0 的应用程序（如 Salesforce、Microsoft 365、Google Workspace 等）。
        *   支持 OIDC 的应用程序。
    *   **优点:**
        *   统一的应用程序访问入口。
        *   简化的用户和权限管理。
        *   提高安全性。

**工作流程示例 (同时使用 AWS 账户访问和应用程序分配):**

1.  **创建用户和组:** 在 IAM Identity Center 中创建用户 "Alice" 和 "Bob"，并将他们添加到 "Developers" 组。
2.  **创建权限集:** 创建一个名为 "EC2-FullAccess" 的权限集，授予对 EC2 实例的完全访问权限。
3.  **分配 AWS 账户权限:**
    *   选择 AWS 账户 "DevAccount"。
    *   将 "Developers" 组与 "EC2-FullAccess" 权限集关联。
4.  **配置云应用程序:** 配置 Salesforce 和 Microsoft 365 的 SAML 集成。
5.  **分配应用程序:**
    *   将 "Developers" 组分配给 Salesforce 和 Microsoft 365 应用程序。
6.  **用户登录:**
    *   Alice 和 Bob 登录到 IAM Identity Center 用户门户。
    *   他们可以看到：
        *   "DevAccount" AWS 账户（具有 EC2-FullAccess 角色）。
        *   Salesforce 应用程序图标。
        *   Microsoft 365 应用程序图标。
    *   他们可以：
        *   点击 "DevAccount" 并选择 "EC2-FullAccess" 角色，访问 AWS 管理控制台并管理 EC2 实例。
        *   点击 Salesforce 或 Microsoft 365 图标，直接登录到这些应用程序，无需再次输入凭据。

**重要提示:**

*   IAM Identity Center 本身不存储用户密码（除非你选择使用 IAM Identity Center 作为身份源）。 它可以与其他身份提供商（如 Active Directory、Okta、Azure AD）集成。
*   强烈建议启用多因素身份验证 (MFA) 以提高安全性。
*   定期审查你的 IAM Identity Center 配置，确保其符合你的安全策略。
*   如果你使用了 AWS Organizations, 通常建议将 IAM Identity Center 的管理账户设置为 Organizations 的管理账户。

这份笔记总结了 IAM Identity Center 的核心概念、主要功能和典型工作流程。希望它能帮助你更好地理解和使用 IAM Identity Center。
