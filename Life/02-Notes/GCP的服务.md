---
category:
  - Tech
tags:
  - GCP
status: Done
---
好的，我将GCP（Google Cloud Platform）目前所有的服务进行分类总结，并尽量涵盖每个类别下的主要服务。请注意，GCP服务不断更新和增加，以下总结基于当前可用的信息：

**1. 计算 (Compute)**

*   **虚拟机 (Virtual Machines):**
    *   **Compute Engine:** 可自定义的虚拟机，提供各种操作系统、机器类型和全球数据中心部署选项。
    *   **Preemptible VMs (抢占式虚拟机):** 成本较低的虚拟机，适合容错、批处理和短时任务。
    *   **Confidential VMs (机密虚拟机):** 在使用中加密数据，提供更高的数据安全性。
    *   **Bare Metal Solution (裸金属解决方案):** 运行专用硬件，满足特定性能或合规性需求。

*   **容器 (Containers):**
    *   **Kubernetes Engine (GKE):** 托管的Kubernetes服务，用于部署、管理和扩展容器化应用程序。
    *   **GKE Autopilot:** 完全托管的Kubernetes模式, 进一步简化操作。
    *   **Cloud Run:** 完全托管的无服务器容器平台，用于运行可自动扩缩的容器化应用程序。
    *   **Cloud Run for Anthos:** 在GKE集群上运行Cloud Run工作负载。
    *   **Container Registry:** 用于存储和管理Docker容器镜像的私有仓库。
    *   **Artifact Registry:** Container Registry的升级版, 统一管理容器镜像和非容器构件(如Maven和npm包)。

*   **无服务器计算 (Serverless Computing):**
    *   **Cloud Functions:** 事件驱动的无服务器计算平台，用于运行响应事件的代码片段（函数）。
    *   **App Engine:** 完全托管的平台，用于构建和部署Web应用程序和移动后端，支持多种语言和框架。
    *  **Workflows**: 无服务器编排服务, 用于协调多个服务和API。

**2. 存储 (Storage)**

*   **对象存储 (Object Storage):**
    *   **Cloud Storage:** 可扩展且经济高效的对象存储，用于存储各种类型的数据，如图像、视频、备份和归档数据。

*   **块存储 (Block Storage):**
    *   **Persistent Disk:** 为Compute Engine虚拟机提供持久块存储，有多种类型（SSD、HDD）和性能选项。
    *   **Local SSD:** 性能更高的临时块存储，直接连接到虚拟机实例。

*   **文件存储 (File Storage):**
    *   **Filestore:** 完全托管的网络文件系统（NFS），用于共享文件存储。

*   **数据传输 (Data Transfer):**
    *   **Storage Transfer Service:** 用于将大量数据从本地或其他云提供商迁移到Cloud Storage。
    *   **Transfer Appliance:** 物理设备，用于离线传输PB级数据到GCP。
    *   **BigQuery Data Transfer Service:** 自动将数据从各种SaaS应用程序导入BigQuery。

**3. 数据库 (Databases)**

*   **关系型数据库 (Relational Databases):**
    *   **Cloud SQL:** 完全托管的MySQL、PostgreSQL和SQL Server数据库服务。
    *   **Cloud Spanner:** 全球分布式、水平可扩展、强一致性的关系型数据库。
    *   **AlloyDB for PostgreSQL:** 与PostgreSQL完全兼容的、为要求严苛的企业工作负载设计的数据库。
    *   **Bare Metal Solution for Oracle (Oracle裸金属解决方案):** 运行Oracle数据库的专用硬件。

*   **NoSQL数据库:**
    *   **Firestore:** 面向移动、Web和IoT应用程序的文档数据库（NoSQL）。
    *   **Datastore:** 高度可扩展的NoSQL数据库，用于Web和移动应用程序。 (Firestore的早期版本)
    *   **Bigtable:** 宽列NoSQL数据库，用于大规模、低延迟的数据存储和分析。
    *   **Memorystore:** 完全托管的内存数据缓存服务，支持Redis和Memcached。

**4. 数据分析 (Data Analytics)**

*   **数据仓库 (Data Warehousing):**
    *   **BigQuery:** 完全托管、PB级、低成本的企业数据仓库，用于大规模数据分析。

*   **数据处理 (Data Processing):**
    *   **Dataflow:** 完全托管的数据处理服务，用于批处理和流处理（基于Apache Beam）。
    *   **Dataproc:** 完全托管的Apache Hadoop、Spark和Flink服务，用于大数据处理和分析。
    *   **Cloud Data Fusion:** 完全托管、图形化界面的数据集成服务（ETL/ELT）。

*   **数据编排 (Data Orchestration):**
    *   **Cloud Composer:** 完全托管的工作流编排服务（基于Apache Airflow）。

*   **数据探索与可视化 (Data Exploration & Visualization):**
    *   **Looker:** 企业级商业智能和数据可视化平台。
    *   **Data Studio:** 免费的数据可视化和报告工具。

*   **消息队列 (Message Queues):**
    *   **Pub/Sub:** 可扩展且可靠的实时消息传递服务，用于发布和订阅事件流。

**5. 人工智能与机器学习 (AI & Machine Learning)**

*   **预训练模型 (Pre-trained Models):**
    *   **Vision AI:** 图像识别、对象检测、文本提取等。
    *   **Video AI:** 视频内容分析、对象跟踪、场景检测等。
    *   **Natural Language AI:** 文本分析、情感分析、实体识别、翻译等。
    *   **Translation AI:** 机器翻译。
    *   **Speech-to-Text:** 语音转文本。
    *   **Text-to-Speech:** 文本转语音。
    *   **Dialogflow:** 构建对话式AI应用（聊天机器人、语音助手）。
    *   **Recommendations AI:** 个性化推荐。

*   **自定义模型 (Custom Models):**
    *   **Vertex AI:** 统一的机器学习平台，用于构建、部署和管理机器学习模型。
        *  **AutoML:** 自动机器学习，无需编写代码即可构建自定义模型。
        * **Training:** 训练自定义模型。
        * **Prediction:** 部署和提供模型预测。
        * **Workbench:** 托管的Jupyter Notebook环境。
        * **Pipelines:** 构建和自动化机器学习工作流程。
        * **Feature Store:** 管理和共享机器学习特征。
        * **Model Monitoring:** 监控模型性能。
        * **Explainable AI:** 解释模型预测。

*   **硬件加速 (Hardware Acceleration):**
    *   **TPUs (Tensor Processing Units):** 谷歌设计的专用硬件，用于加速机器学习工作负载。

**6. 网络 (Networking)**

*   **虚拟网络 (Virtual Networking):**
    *   **Virtual Private Cloud (VPC):** 隔离的私有云网络，用于部署GCP资源。
    *   **Cloud Load Balancing:** 全球负载均衡，支持多种类型（HTTP(S)、TCP、UDP）。
    *   **Cloud DNS:** 高性能、可扩展的DNS服务。
    *   **Cloud NAT:** 网络地址转换，允许私有实例访问互联网。
    *   **Cloud Firewall:** 防火墙规则，控制进出VPC网络的流量。

*   **混合连接 (Hybrid Connectivity):**
    *   **Cloud VPN:** 通过IPsec VPN连接到本地网络。
    *   **Cloud Interconnect:** 通过专用连接或合作伙伴连接到本地网络。
    *  **Network Connectivity Center**: 中心辐射型网络管理模型。

*   **内容分发 (Content Delivery):**
    *   **Cloud CDN:** 内容分发网络，加速Web内容交付。

* **网络安全:**
  * **Cloud Armor:** DDoS防护和WAF(Web应用程序防火墙).

**7. 运维与管理 (Operations & Management)**

*   **监控 (Monitoring):**
    *   **Cloud Monitoring (formerly Stackdriver):** 监控GCP和本地资源的性能、可用性和运行状况。

*   **日志 (Logging):**
    *   **Cloud Logging (formerly Stackdriver Logging):** 集中式日志管理和分析。

*   **调试与跟踪 (Debugging & Tracing):**
    *   **Cloud Debugger:** 调试生产环境中的应用程序。
    *   **Cloud Trace:** 跟踪应用程序中的请求，分析性能瓶颈。
    * **Cloud Profiler:** 持续分析代码性能。

*   **错误报告 (Error Reporting):**
    *   **Error Reporting:** 自动捕获和报告应用程序中的错误。

*   **配置管理 (Configuration Management):**
    *   **Deployment Manager:** 使用模板部署和管理GCP资源（基础设施即代码）。
    *   **Config Connector:** 通过Kubernetes风格的配置管理GCP资源。

* **安全管理**
    * **Security Command Center**: 集中式安全和风险管理平台.
    * **Secret Manager**: 安全存储API密钥, 密码和其他敏感数据。

**8. 开发工具 (Developer Tools)**

*   **Cloud SDK:** 命令行工具，用于管理GCP资源和应用程序。
*   **Cloud Shell:** 基于浏览器的命令行环境，预装了Cloud SDK和其他工具。
*   **Cloud Code:** IDE插件（VS Code、IntelliJ），简化在GCP上开发和部署应用程序。
*   **Container Registry / Artifact Registry:** （见上文“容器”部分）
*   **Cloud Build:** 完全托管的持续集成和持续交付（CI/CD）平台。
*   **Cloud Source Repositories:** 私有Git代码仓库。

**9. 物联网 (Internet of Things, IoT)**

*   **Cloud IoT Core:** 完全托管的IoT设备连接和管理平台。

**10. 游戏开发 (Game Development)**

*   **Game Servers:** 托管的游戏服务器管理。
*   **Open Saves:** 用于游戏进度的云存储。

**11. API 管理 (API Management)**

*   **Apigee API Management:** 全生命周期API管理平台。
*   **Cloud Endpoints:** 用于开发、部署和管理API的代理和工具。
*   **API Gateway:** 完全托管的API网关。

**12. 身份与安全 (Identity & Security)**
* **Identity Platform**: 身份验证和用户管理服务。
* **Cloud Identity**: 企业级用户和设备管理。
* **Identity-Aware Proxy (IAP)**: 基于身份的访问控制, 保护云应用程序和虚拟机。
* **Key Management Service (KMS)**: 管理加密密钥。
* **Cloud HSM**: 硬件安全模块服务。
* **Resource Manager:** 组织和管理GCP资源。

**13. 迁移 (Migration)**
* **Migrate to Virtual Machines:** 迁移虚拟机到GCP。
* **Migrate to Containers:** 迁移应用程序到容器。
* **Database Migration Service:** 数据库迁移服务。

**14. 其他专业领域**
* **Healthcare and Life Sciences**: 专门用于医疗保健和生命科学的解决方案, 如Cloud Healthcare API。
* **Media & Entertainment**: 媒体和娱乐行业的解决方案。
* **Retail**: 零售业解决方案。

这只是GCP服务的详细分类总结。由于GCP服务众多且不断更新，这可能不是一个详尽无遗的列表。如果您有特定的服务或类别感兴趣，可以更具体地提问，我会尽力提供更详细的信息。
