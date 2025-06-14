---
category:
  - Tech
tags:
  - AWS
  - GCP
status: Done
---

## 1. 核心原则

- 共同点：GCP IAM 和 AWS IAM 都遵循 最小权限原则（Principle of Least Privilege），确保用户或服务只获得完成任务所需的最小权限。
    
- 差异点：
    
    - GCP IAM：强调通过资源层次结构和角色简化权限管理。
        
    - AWS IAM：注重策略的灵活性和角色的动态使用（如临时凭证和跨账户访问）。
        

---

## 2. 基本概念

### 2.1. GCP IAM

- 成员（Member）：
    
    - 类型：Google账户（个人用户）、服务账户（用于应用）、Google群组（批量管理）、域名（基于Cloud Identity）。
        
    - 特点：身份与Google生态紧密集成。
        
- 角色（Role）：权限的集合，用于定义“能做什么”。
    
- 权限（Permission）：
    
    - 格式：service.resource.verb（如compute.instances.delete）。
        
    - 定义对资源的具体操作能力。
        
- 策略（Policy）：将成员绑定到角色的JSON配置文件。
    
- 资源层次结构：组织 > 文件夹 > 项目 > 具体资源，支持权限继承。
    

### 2.2. AWS IAM

- 用户（User）：代表个人或应用程序，绑定长期凭证。
    
- 组（Group）：用户集合，便于批量授权。
    
- 角色（Role）：权限集合，可被用户、服务或外部身份“担任”。
    
- 策略（Policy）：JSON文档，定义具体权限。
    
- 凭证（Credentials）：
    
    - 类型：密码、访问密钥（Access Key）、多因素认证（MFA）、X.509证书、临时安全凭证（通过STS生成）。
        
    - 特点：支持多种认证方式，强调临时凭证安全性。
        

---

## 3. 权限管理

### 3.1. GCP IAM

- 方式：权限不直接授予成员，而是通过角色分配。
    
- 特点：角色作为权限的抽象层，简化管理，权限粒度由GCP预定义。
    

### 3.2. AWS IAM

- 方式：权限通过策略定义，可附加到用户（不推荐）、组（推荐）或角色。
    
- 特点：策略提供更高的灵活性，支持允许（Allow）和拒绝（Deny）规则。
    

---

## 4. 角色（Role）

### 4.1. GCP IAM

- 定义：权限的集合。
    
- 用途：主要用于将权限授予用户或服务账户。
    
- 类型：基本角色、预定义角色、自定义角色。
    

### 4.2. AWS IAM

- 定义：权限的集合，可动态“担任”。
    
- 用途：
    
    - 服务角色：允许AWS服务（如EC2、Lambda）访问其他资源。
        
    - 跨账户访问：支持账户间权限共享。
        
    - 身份联合：集成外部身份提供者（如SAML、OIDC）。
        
- 特点：强调动态性和临时凭证。
    

---

## 5. 策略（Policy）

### 5.1. GCP IAM

- 功能：将成员绑定到角色，应用于资源层次的某一级别。
    
- 特点：依赖角色，策略本身较简单。
    

### 5.2. AWS IAM

- 功能：JSON文档，定义Effect（Allow/Deny）、Action（操作）、Resource（资源）、Condition（条件）。
    
- 类型：
    
    - AWS托管策略：AWS预定义，易于使用。
        
    - 客户托管策略：用户自定义，可复用。
        
    - 内联策略：嵌入用户、组或角色，不推荐。
        
- 特点：高度灵活，支持复杂条件。
    

---

## 6. 权限粒度

### 6.1. GCP IAM

- 格式：service.resource.verb，较为固定。
    
- 特点：权限由GCP预定义，粒度较统一。
    

### 6.2. AWS IAM

- 格式：service:operation（如s3:GetObject），支持通配符（*）。
    
- 特点：策略定义更灵活，用户可自定义范围。
    

---

## 7. 多账户管理

### 7.1. GCP IAM

- 实现：通过资源层次结构（组织 > 文件夹 > 项目）管理。
    
- 特点：支持权限继承，配合共享VPC实现跨项目资源共享。
    

### 7.2. AWS IAM

- 实现：
    
    - IAM角色：跨账户访问的基础。
        
    - AWS Organizations：集中管理多个账户。
        
    - IAM Identity Center：简化多账户SSO和权限分配。
        
- 特点：强调角色扮演和临时凭证。
    

---

## 8. 单点登录（SSO）

### 8.1. GCP IAM

- 支持：原生不直接提供，需通过Google Workspace或Cloud Identity实现。
    
- 特点：依赖外部身份管理工具。
    

### 8.2. AWS IAM

- 支持：IAM Identity Center提供原生SSO。
    
- 特点：与SAML 2.0、SCIM等外部IdP集成，支持多账户和应用访问。
    

---

## 9. 最佳实践

### 9.1. GCP IAM

- 遵循最小权限原则。
    
- 使用服务账户进行自动化任务。
    
- 优先使用预定义角色，必要时创建自定义角色。
    
- 定期审查权限，使用Cloud Audit Logs监控。
    

### 9.2. AWS IAM

- 遵循最小权限原则。
    
- 使用组管理用户权限，避免直接授权用户。
    
- 借助角色实现服务集成、跨账户访问和身份联合。
    
- 优先使用AWS托管策略，必要时创建客户托管策略。
    
- 定期审查权限，使用IAM Access Analyzer分析潜在风险。
    
- 启用IAM Identity Center优化多账户管理。
    

---
## 10. 主要区别

| 特性    | GCP IAM                  | AWS IAM                   |
| ----- | ------------------------ | ------------------------- |
| 权限管理  | 基于角色，粒度固定                | 基于策略，灵活性高                 |
| 角色用途  | 静态授权给用户或服务账户             | 动态“担任”，支持服务和跨账户场景         |
| 策略灵活性 | 依赖预定义角色，较简单              | JSON定义，支持复杂条件和通配符         |
| 多账户管理 | 资源层次结构（组织>文件夹>项目）        | AWS Organizations + IAM角色 |
| SSO支持 | 需外部工具（如Google Workspace） | 原生支持（IAM Identity Center） |

