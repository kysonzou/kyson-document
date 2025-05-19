---
category:
  - Tech
tags:
  - Application
status: Done
---
### 一、常见命令

```bash
sudo nano /etc/v2ray/config.json

sudo systemctl daemon-reload

sudo systemctl enable v2ray

sudo systemctl start v2ray

sudo systemctl restart v2ray

sudo systemctl status v2ray

sudo nano /var/log/v2ray/access.log

sudo nano /var/log/v2ray/error.log

journalctl -u v2ray.service -b # 查看日志

#通过 openssl s_client 验证服务器是否正确加载了证书
openssl s_client -connect v2ray.kyson.store:8443 -servername v2ray.kyson.store 

#运行以下命令检查证书的内容，确保域名 v2ray.kyson.store 在证书中。
openssl x509 -in /etc/letsencrypt/live/kyson.store/fullchain.pem -text -noout | grep -E "Subject|DNS"

#在服务器上使用 curl 测试 V2Ray 是否在本地响应：
curl -vk https://127.0.0.1:8443

ps aux | grep v2ray
```

### 二、配置文件

```bash
# 配置文件
sudo nano /etc/v2ray/config.json

# 日志
sudo nano /var/log/v2ray/access.log
sudo nano /var/log/v2ray/error.log
```
