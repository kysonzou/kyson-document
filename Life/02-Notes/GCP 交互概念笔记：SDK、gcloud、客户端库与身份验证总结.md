---
category:
  - Knowledge
tags:
  - GCP
status: Done
---
与 Google Cloud Platform (GCP) 交互主要有几种方式，理解它们之间的关系和认证机制非常重要。

### 1. 核心交互基础：Google Cloud APIs

- 所有 GCP 服务都通过 **API (应用程序编程接口)**（主要是 RESTful API 或 gRPC API）暴露其功能。
- 这是最底层、最通用的交互方式。所有更高级的工具（SDK/CLI、客户端库）最终都是通过调用这些 API 来工作的。

### 2. 主要交互工具

- **Google Cloud SDK (软件开发工具包)**
    
    - 一个可下载安装的**工具包**，主要为了提供**命令行交互**能力。
    - 它本身**主要用 Python 编写**。
    - 包含核心的命令行工具 `gcloud`，以及其运行所需的内部库和其他辅助工具（历史上如 `gsutil`, `bq`）。
    - **`gcloud` CLI**:
        - SDK 中主要的**命令行界面 (CLI)** 工具。
        - 用于通过**终端命令**管理 GCP 资源、配置、认证等。
        - 适合**手动操作、脚本自动化**。
        - 运行机制：用户输入 `gcloud ...` -> Shell 找到 `gcloud` 包装器脚本 -> 包装器调用 SDK 内的 Python 解释器执行核心 Python 代码 -> Python 代码解析参数、调用 GCP API、格式化输出。
- **Google Cloud Client Libraries (客户端库)**
    
    - **针对特定编程语言**（如 Python, Node.js, Java, Go 等）提供的库。
    - 通常需要通过该语言的包管理器**单独安装**（如 `pip install google-cloud-storage`, `npm install @google-cloud/storage`）。
    - 目的是让开发者能以**符合该语言习惯的方式（编程方式）**在自己的应用程序代码中与 GCP 服务交互。
    - 提供了比直接调用 API 更方便的接口，封装了认证、重试等细节。
    - 适合**构建应用程序、实现复杂逻辑**。

### 3. 工具之间的关系

- `gcloud` CLI 和 客户端库 都是 GCP API 的**不同类型的客户端 (Client)**。
- 它们提供了**不同的交互接口**（命令行 vs. 编程接口），服务于不同的场景和用户。
- 它们**通常不直接互相调用或封装**（从用户角度看）。选择哪个取决于您的需求。

### 4. 核心概念：身份验证 (Authentication)

如何证明“您是谁”或“您的应用是谁”，以便 GCP 授权访问？

- **Application Default Credentials (ADC)**
    
    - 是 Google Cloud 推荐的、**自动查找和使用凭证**的标准策略。
    - 客户端库（以及 `gcloud` 等工具）默认使用 ADC 来寻找有效的凭证。
    - **ADC 查找顺序**（通常）：
        1. **`GOOGLE_APPLICATION_CREDENTIALS` 环境变量**: 是否指向一个服务账号密钥文件？
        2. **`gcloud` 设置的用户凭证**: 是否存在由 `gcloud auth application-default login` 命令创建的本地凭证文件？(常见于本地开发)
        3. **GCP 环境的附加服务账号**: 代码是否运行在 GCE, GKE, Cloud Run, App Engine, Cloud Functions 等环境中？如果是，则通过**元数据服务器 (Metadata Server)** 自动获取该环境关联的服务账号凭证。
- **本地开发认证 (使用 `gcloud`)**:
    
    - 运行 `gcloud auth application-default login` 命令，用您的 Google 用户账户登录。
    - `gcloud` 会将您的用户凭证保存在本地一个特定文件中。
    - 当您在本地运行使用客户端库的 Python (或其他语言) 代码时，ADC 会找到这个文件，使您的代码能以您的用户身份进行认证，**无需在代码中处理密钥**。
- **GCP 环境认证 (元数据服务器)**:
    
    - 在 GCE, Cloud Run 等环境中，每个资源通常关联一个**服务账号 (Service Account)**。
    - 这些环境提供一个特殊的**元数据服务器**（地址通常是 `169.254.169.254` 或 `metadata.google.internal`），只能从环境内部访问。
    - 客户端库通过 ADC 检测到在此类环境中运行时，会自动向元数据服务器请求**附加服务账号**的**访问令牌 (Access Token)**。
    - 这样就实现了**无密钥文件的无缝认证**，只需为服务账号配置好 IAM 权限即可。

### 5. 回顾最初的例子

- `from google.cloud import storage`: 这是在 Python 代码中导入**适用于 Python 的 Google Cloud Storage 客户端库**，以便通过编程方式操作 GCS。
- `from google.colab import auth`: 这是导入 Google Colaboratory 环境**特有的库**中的认证模块，用于在 Colab 笔记本内进行用户身份验证，以便授权访问 Drive 或 GCP 等。
