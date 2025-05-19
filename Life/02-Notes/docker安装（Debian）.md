---
category:
  - Tech
tags: 
status: Done
---
在 Debian 上安装 Docker 有几种方法，最常用和推荐的方法是使用 Docker 的官方仓库。以下是详细步骤：

**1. 更新软件包索引并安装必要的依赖：**

```bash
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release
```

**2. 添加 Docker 的官方 GPG 密钥：**

```bash
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

**3. 设置稳定版仓库：**

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

**4. 更新软件包索引并安装 Docker Engine、containerd 和 Docker Compose：**

```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

**5. 验证 Docker 是否安装成功：**

```bash
sudo docker run hello-world
```

如果看到 "Hello from Docker!" 的输出，则表示安装成功。

**6.  (可选) 将当前用户添加到 docker 用户组，以便无需 sudo 即可运行 docker 命令：**

```bash
sudo usermod -aG docker $USER
```

**重要提示：** 执行此命令后，你需要**注销并重新登录**才能使更改生效。或者，你可以运行 `newgrp docker` 来立即应用更改，但这只会影响当前 shell 会话。

**7. (可选) 启动 Docker 服务并设置为开机自启：**

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

**解释一下各个步骤：**

*   **步骤 1：** 更新软件包索引以获取最新的软件包列表，并安装一些必要的软件包，以便能够通过 HTTPS 使用仓库。
*   **步骤 2：** 添加 Docker 的官方 GPG 密钥，以验证软件包的完整性和真实性。
*   **步骤 3：** 设置 Docker 的稳定版仓库。  `$(lsb_release -cs)` 会自动获取你的 Debian 版本代号 (例如 bullseye, buster 等)。
*   **步骤 4：** 再次更新软件包索引，然后安装 Docker Engine (docker-ce), Docker CLI (docker-ce-cli), containerd (containerd.io) 和 Docker Compose 插件 (docker-compose-plugin)。
*   **步骤 5：** 运行一个简单的 "hello-world" 容器来验证 Docker 是否正常工作。
*   **步骤 6：**  将用户添加到 `docker` 用户组，这样就可以不使用 `sudo` 来运行 Docker 命令。  这是一个可选步骤，但强烈推荐，因为它更方便，也更安全（避免过度使用 root 权限）。
* **步骤 7**: 启动Docker服务并设置成开机自动运行。

**8.把它整理成一个脚本的形式：install_docker.sh**

```sh
#!/bin/bash

# 安装 Docker 脚本

# 检查是否为 root 用户
if [ "$EUID" -ne 0 ]; then
   echo "此脚本必须以 root 用户身份运行"
   exit 1
fi

# 更新 apt 包索引
echo "更新 apt 包索引..."
apt update

# 安装必要的软件包
echo "安装必要的软件包..."
apt install -y apt-transport-https ca-certificates curl gnupg lsb-release

# 添加 Docker 的官方 GPG 密钥
echo "添加 Docker 的官方 GPG 密钥..."
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 设置 stable 存储库
#这里做了点修改，以防万一lsb_release -cs命令出错，加了判断和处理
echo "设置 stable 存储库..."
distro=$(lsb_release -cs 2>/dev/null)
if [ -z "$distro" ]; then
    echo "无法自动检测您的 Debian 版本. 请手动设置docker源"
    exit 1
fi
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $distro stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# 再次更新 apt 包索引
echo "再次更新 apt 包索引..."
apt update

# 安装 Docker Engine、containerd 和 Docker Compose
echo "安装 Docker Engine、containerd 和 Docker Compose..."
apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
#如果安装失败了，就提示用户并且退出
if [ $? -ne 0 ];then
    echo "安装Docker失败，请检查网络和源配置!"
    exit 1
fi
# 运行 hello-world 镜像进行测试
echo "运行 hello-world 镜像进行测试..."
docker run hello-world

# 启动 Docker 服务并设置为开机自启
echo "启动 Docker 服务并设置为开机自启..."
systemctl start docker
systemctl enable docker

echo "Docker 安装完成！"

exit 0
```

```bash
#执行步骤
sudo chmod +x install_docker.sh
sudo ./install_docker.sh
```

**9.卸载docker的脚本：uninstall_docker.sh**

```sh
#!/bin/bash

# 卸载 Docker 脚本

# 检查是否为 root 用户
if [ "$EUID" -ne 0 ]; then
   echo "此脚本必须以 root 用户身份运行"
   exit 1
fi

# 停止 Docker 服务
echo "停止 Docker 服务..."
systemctl stop docker
systemctl disable docker

# 卸载 Docker 软件包
echo "卸载 Docker 软件包..."
apt purge -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
if [ $? -ne 0 ]; then
    echo "卸载Docker软件包失败。"
    exit 1
fi

# 删除 Docker 相关的资源
echo "删除 Docker 相关的资源..."
rm -rf /var/lib/docker
rm -rf /var/lib/containerd

# 删除 Docker 的 apt 源列表文件
echo "删除 Docker 的 apt 源列表文件..."
rm /etc/apt/sources.list.d/docker.list

#删除gpg key
echo "删除 Docker 的 GPG 密钥"
sudo rm /usr/share/keyrings/docker-archive-keyring.gpg

# 再次更新 apt 索引
echo "更新 apt 索引..."
apt update

echo "Docker 卸载完成！"

exit 0
```

```bash
#执行步骤
sudo chmod +x ininstall_docker.sh
sudo ./uninstall_docker.sh
```
