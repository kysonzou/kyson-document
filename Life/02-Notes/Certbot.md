---
category:
  - Tech
tags:
  - Linux
status: Done
---
[[Certbot 原理]]  

Certbot 是一个开源工具，用于申请、安装和管理 Let’s Encrypt SSL/TLS 证书，支持自动化处理，让网站快速启用 HTTPS 加密。

---

## 1. 安装 Certbot

### 1.1 **Debian/Ubuntu**

```bash
sudo apt install certbot

# 安装 Web 服务器插件（自动化处理）
sudo apt install python3-certbot-nginx
sudo apt install python3-certbot-apache

# 安装 DNS 插件（用于自动 DNS 验证）
sudo apt install python3-certbot-dns-cloudflare # Cloudflare
sudo apt install python3-certbot-dns-google     # Google Cloud
sudo apt install python3-certbot-dns-route53   # AWS Route 53
```
> 根据所用的 Web 服务器，选择适合的插件，例如 python3-certbot-nginx 或 python3-certbot-apache。

### 1.2 **CentOS/RHEL**

```bash
sudo yum install certbot
```
> 其它插件的安装方式与 Debian/Ubuntu 类似。

### 1.3 **macOS** (通过 Homebrew):

```bash
brew install certbot
```

### 1.4 **Windows**

Certbot 没有直接支持 Windows，但可以通过 WSL（Windows Subsystem for Linux）使用。

### 1.5 **Docker**

Certbot 提供官方 Docker 镜像：`certbot/certbot`。

---

## 2. 申请证书（HTTP 验证）

Certbot 根据 Web 服务器类型提供自动化或手动模式。

### 2.1 **自动模式（推荐）**

适用于 Nginx 或 Apache，Certbot 可自动完成证书申请和配置。

#### Nginx:
```bash
sudo certbot --nginx -d your-domain.com
```

#### Apache:
```bash
sudo certbot --apache -d your-domain.com
```
> Certbot 会自动调整服务器配置，完成证书申请、配置和服务重启。

### 2.2 **手动模式**

#### 自动路径配置:
使用 Nginx 的默认路径，自动申请和续期证书，但不会主动将证书配置到服务器。
```bash
sudo certbot certonly --nginx -d your-domain.com
```

#### 指定路径:
指定 Web 根路径并手动配置服务器
```bash
sudo certbot certonly --webroot -w /var/www/html -d example.com
```

#### 全手动验证:
1. 运行以下命令：
   ```bash
   sudo certbot certonly --manual
   ```
2. 按提示验证域名所有权（HTTP 文件上传或 DNS TXT 记录）。
3. 验证完成后，Certbot 会生成证书，但不会自动续期。

### 2.3 **独立模式**

适用于没有运行 Web 服务器的环境。Certbot 会启动一个临时 HTTP 服务器验证域名所有权。
```bash
sudo certbot certonly --standalone -d example.com
```
确保 TCP 80 端口未被占用。

### 2.4 **证书存储路径**

- **证书文件**: `/etc/letsencrypt/live/<domain>/fullchain.pem`
- **私钥文件**: `/etc/letsencrypt/live/<domain>/privkey.pem`
- 查看证书
    ```bash
    sudo certbot certificates 
    ```

---

## 3. 申请证书（DNS 验证）

DNS 验证通常用于无法通过 HTTP 验证的场景。需要配置 DNS 插件或手动添加 TXT 记录。

### 示例:
使用 Cloudflare 插件：
```bash
sudo certbot -d your-domain.com --dns-cloudflare --dns-cloudflare-credentials /path/to/credentials
```

> 更多详情可参见具体插件文档。

---

## 4. 测试模式

Let’s Encrypt 提供测试环境，避免因重复请求受到限制：
```bash
sudo certbot --staging
```
> 测试模式不会生成有效证书。

---

## 5. 续期证书

Let’s Encrypt 证书有效期为 **90 天**，Certbot 提供自动续期功能。

### 手动续期:
```bash
sudo certbot renew
```

### 测试续期:
```bash
sudo certbot renew --dry-run
```

### 自动续期（推荐）:
Certbot 安装后通常会自动配置定时任务。检查是否已设置：
```bash
systemctl list-timers | grep certbot
```

---

## 6. 删除证书

如果不再需要某个域名的证书，可删除：
```bash
sudo certbot delete -d example.com
```

---

## 7. 调试和日志

Certbot 的操作日志路径：
```
/var/log/letsencrypt/letsencrypt.log
```
检查日志可了解详细错误信息。


