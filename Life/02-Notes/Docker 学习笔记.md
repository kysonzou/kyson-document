---
category:
  - Tech
tags:
  - Docker
status: Done
---
好的，我把构建镜像的方法添加到之前的笔记中，并做一些排版上的优化：

**Docker 学习笔记**

### 一、Docker 核心概念

1.  **镜像 (Image):**
    *   Docker 镜像类似于一个只读的模板，包含了运行应用程序所需的所有内容：代码、运行时环境、库、环境变量和配置文件。
    *   常用命令：
        *   `docker search`: 搜索 Docker Hub 上的镜像。
        *   `docker pull`: 下载镜像。
        *   `docker images`: 列出本地镜像。
        *   `docker rmi`: 删除本地镜像。

2.  **容器 (Container):**
    *   容器是镜像的可运行实例。每个容器都是隔离的、安全的应用程序平台。可以把容器看作是一个简易版的 Linux 环境。
    *   常用命令：
        *   `docker run`: 创建并运行一个容器。
        *   `docker ps`: 列出正在运行的容器（`-a` 参数可以列出所有容器，包括已停止的）。
        *   `docker stop`: 停止一个正在运行的容器。
        *   `docker start`: 启动一个已停止的容器。
        *   `docker restart`: 重启一个容器。
        *   `docker stats`: 查看容器的资源使用情况（CPU、内存等）。
        *   `docker logs`: 查看容器的日志输出。
        *   `docker exec`: 在运行的容器中执行命令。
        *   `docker rm`: 删除一个容器。
        *   `docker run` 常用参数
            *   `-d`: 后台启动
            *   `-p`: 端口映射
            *   `--name`: 容器名

3.  **仓库 (Repository):**
    *   仓库是集中存放镜像文件的地方。
    *   最大的公开仓库是 Docker Hub，国内也有很多云服务商提供镜像仓库服务（如阿里云、腾讯云等）。

4.  **分享**
    *   常用命令
        *   `docker commit`: 提交
        *   `docker save`: 保存
        *   `docker load`: 加载
        *   `docker login`: 登录
        *   `docker tag`: 命名
        *   `docker push`: 推送

### 二、构建 Docker 镜像

1.  **使用 `docker commit` 命令（不推荐，但方便快速实验）:**

    *   基于已有的容器进行修改，然后提交为一个新的镜像。
    *   步骤：
        1.  运行一个基础镜像的容器。
        2.  在容器内进行修改。
        3.  退出容器。
        4.  使用 `docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]` 命令提交。
    *   缺点：不透明、难追溯、不方便重复构建和版本控制、容易产生臃肿的镜像。

2.  **使用 Dockerfile（推荐）:**

    *   这是构建 Docker 镜像的标准方式。
    *   步骤：
        1.  **创建 Dockerfile:** 在一个空目录下创建一个名为 `Dockerfile` 的文本文件。
        2.  **编写 Dockerfile:** 使用一系列的指令来定义镜像的构建过程。
        3.  **构建镜像:** 在 Dockerfile 所在目录下执行 `docker build -t <image_name>:<tag> .` 命令。
        4.  **查看镜像:** 使用 `docker images` 命令查看新构建的镜像。

### 三、Dockerfile

Dockerfile 是一个文本文件，其中包含了一系列的指令，用于自动构建 Docker 镜像。

*   **常用指令:**

    *   `FROM`: 指定基础镜像。
    *   `RUN`: 执行命令，并在新的镜像层中添加结果。
    *   `CMD`: 设置容器启动后默认执行的命令及其参数（只能有一条 CMD 指令，如果有多条，则最后一条生效）。
    *   `ENTRYPOINT`: 类似于 `CMD`，但其指定的命令不会被 `docker run` 的命令行参数覆盖（除非使用 `--entrypoint` 选项）。
    *   `LABEL`: 为镜像添加元数据（键值对）。
    *   `EXPOSE`: 声明容器运行时监听的端口（仅是声明，并不会自动进行端口映射）。
    *   `ENV`: 设置环境变量。
    *   `ADD`: 将文件或目录复制到镜像中（可以自动解压缩）。
    *   `COPY`: 将文件或目录复制到镜像中（不解压缩）。
    *   `VOLUME`: 创建一个挂载点，用于持久化数据或共享数据。
    *   `USER`: 指定运行容器时的用户名或 UID。
    *   `WORKDIR`: 设置工作目录。
    *   `ARG`: 定义构建时的变量。

#### 四、Docker Compose

Docker Compose 是一个用于定义和运行多容器 Docker 应用程序的工具。通过一个 YAML 文件（`compose.yaml` 或 `docker-compose.yml`）来配置应用程序的服务、网络和卷。

*   **常用命令:**

    *   `docker compose up`: 构建、创建并启动服务（`-d` 参数表示在后台运行）。
    *   `docker compose down`: 停止并移除由 `docker compose up` 创建的容器、网络、卷等。
    *   `docker compose start`: 启动已存在的服务。
    *   `docker compose stop`: 停止已存在的服务。
    *   `docker compose scale`: 扩展服务的容器数量。
    *   `docker compose ps`: 列出 Compose 项目中的容器。
    *   `docker compose logs`: 查看服务的日志输出。
    *   `docker compose exec`: 在运行的服务容器中执行命令。
    *   `docker compose config`: 验证并查看 Compose 配置文件。

### 五、补充内容

1.  **Docker 网络:**

    *   Docker 提供了多种网络模式。
    *   常见网络模式：`bridge`、`host`、`none`、`container`、自定义网络。

2.  **Docker 数据卷:**

    *   数据卷用于持久化数据，其生命周期独立于容器。
    *   可以在容器之间共享和重用。
    *   可以使用 `docker volume create` 命令创建数据卷。

3.  **Docker 与持续集成/持续部署 (CI/CD):**

    *   Docker 可以与各种 CI/CD 工具集成，实现自动化构建、测试和部署。
