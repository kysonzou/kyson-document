---
category:
  - Tech
tags:
  - Application
status: Done
---
要在 AWS 服务器上搭建一个 Shadowsocks (SS) 节点，你可以按照以下步骤操作：

### 1、连接到 AWS EC2 服务器
1. 通过 SSH 连接到你的 AWS 服务器：
   ```bash
   ssh -i /path/to/your-key.pem ec2-user@your-aws-public-ip
   ```

### 2、安装 Shadowsocks 服务
1. 更新服务器的包管理器：
   ```bash
   sudo apt update
   ```

2. 安装 Shadowsocks：
   ```bash
   sudo apt install shadowsocks-libev
   ```

### 3、配置 Shadowsocks
1. 创建 Shadowsocks 的配置文件：
   ```bash
   sudo nano /etc/shadowsocks-libev/config.json
   ```

2. 编辑文件内容，例如：
   ```json
   {
       "server": ["::0","0.0.0.0"],
       "mode":"tcp_and_udp",
       "server_port": 8388,
       "local_port": 1080,
       "password": "kETQBio807K7",
       "timeout": 600,
       "method": "chacha20-ietf-poly1305"
   }
   ```
   - `server`：设置为`"0.0.0.0", "::0"`表示服务器将监听所有 IP 地址（IPV4、IPV6）。
   - `server_port`：指定 Shadowsocks 服务器的端口，可以自行设置。
   - `password`：设置你的 Shadowsocks 密码。
   - `method`：指定[[shadowsocks搭建服务#^d2fdb4|加密方法]]（这里选择 `aes-256-gcm`，你也可以根据需要更改）。

### 4、配置防火墙
1. 确保你在 AWS 控制台的安全组中打开了服务器的端口（如`8388`），以允许外部连接。

2. 检查本地防火墙（如果存在）并确保端口开放：

###  5、启动 Shadowsocks 服务
1. 启动 Shadowsocks 服务：
   ```bash
   sudo systemctl start shadowsocks-libev
   ```

2. 设置为开机启动：
   ```bash
   sudo systemctl enable shadowsocks-libev
   ```

3. 查看服务器是否在预期的端口监听
   ```bash
   sudo ss -tuln | grep 8388
   ```
   如果看到类似 `0.0.0.0:8388` 或 `:::8388` 的输出，说明端口正在监听。

4. 重启服务
   ```bash
   sudo systemctl restart shadowsocks-libev
   ```

5. 检查服务状态
   ```bash
   sudo systemctl status shadowsocks-libev
   ```
   你应该看到 `active (running)`，表示 Shadowsocks 正在运行。

### 6、安装 BBR 加速
为了提高连接质量，你可以安装并启用 Google 的 BBR 拥塞控制算法来加速网络：

1. 开启 BBR：
   ```bash
 sudo sysctl -w net.ipv4.tcp_congestion_control=bbr
   ```

2. 验证是否已成功启用：
   ```bash
 sudo sysctl net.ipv4.tcp_congestion_control
   ```
   你应该会看到 `bbr` 作为当前使用的拥塞控制算法

3. 查看支持的TCP 拥塞控制算法
   ```bash
 sudo sysctl net.ipv4.tcp_available_congestion_control
   ```


>[!Note]- Shadowsocks 支持多种加密算法 
>Shadowsocks 支持多种加密算法。选择加密算法时需要权衡安全性和性能。以下是一些 Shadowsocks 支持的加密算法分类及其特点：
>
>1. **推荐的 AEAD (Authenticated Encryption with Associated Data) 加密算法**
 >   这些算法提供了更好的安全性和性能，被推荐用于现代 Shadowsocks 设置。
>    - **`aes-256-gcm`**：安全性高，性能较好，广泛使用。
>    - **`aes-192-gcm`**：类似于 `aes-256-gcm`，但密钥长度稍短。
>    - **`aes-128-gcm`**：与 `aes-256-gcm` 相比，安全性稍差，但速度更快，适用于资源受限的设备。
>    - **`chacha20-ietf-poly1305`**：基于 ChaCha20 流密码和 Poly1305 MAC，适合低性能设备（如移动设备），同时保持较高的安全性。
>    - **`xchacha20-ietf-poly1305`**：`chacha20-ietf-poly1305` 的扩展版本，密钥长度更长，安全性更高。
>
>2. **传统的加密算法**
>    这些算法较旧，一些已经被认为不再安全，推荐尽量使用 AEAD 加密算法替代。
>    - **`aes-256-cfb`**：曾经非常流行，但逐渐被 AEAD 算法取代。
>    - **`aes-192-cfb`**：类似于 `aes-256-cfb`，但密钥长度稍短。
>    - **`aes-128-cfb`**：与 `aes-256-cfb` 相比，速度更快，安全性稍弱。
>    - **`aes-256-ctr`**：较 CFB 模式更快，适合对延迟敏感的场景。
>    - **`aes-192-ctr`**：与 `aes-256-ctr` 类似，但密钥长度稍短。
>    - **`aes-128-ctr`**：与 `aes-256-ctr` 相比更快，安全性稍低。
>
>3. **其他流密码**
>    - **`chacha20`**：适合低性能设备，速度快，安全性较高，但 AEAD 算法提供了更好的保护
>    - **`salsa20`**：`chacha20` 的前身，较少使用。
>    - **`rc4-md5`**：不推荐，已经被认为不再安全。
>
>如何选择合适的加密算法
>- **高安全性与现代算法**：`aes-256-gcm`, `chacha20-ietf-poly1305`, `xchacha20-ietf-poly1305`
>- **较低计算能力设备**：`chacha20-ietf-poly1305`, `aes-128-gcm`
>- **过时但可用的算法**：`aes-256-cfb`, `aes-128-cfb`（不推荐用于新配置）
>
>你可以根据自己的网络条件、设备性能和对安全性的需求来选择最合适的加密算法。如果希望更高的安全性，建议优先使用 AEAD 系列的加密算法。

^d2fdb4


