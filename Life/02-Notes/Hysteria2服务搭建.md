---
category:
  - Tech
tags:
  - Application
status: Done
---
[Hysteria2官方文档](https://v2.hysteria.network/zh/docs/getting-started/Installation/)
### 一、Hysteria2的docker部署

```yaml
services:
    hysteria:
        image: tobyxdd/hysteria:latest
        container_name: hysteria
        volumes:
            - ./hysteria/config.yaml:/etc/hysteria/config.yaml
            # - ./hysteria/log:/var/log/hysteria # 映射日志目录
            - /etc/letsencrypt:/etc/letsencrypt
        restart: always
        ports:
            - "8443:8443/udp"
        networks:
            - proxy-network
        command: ["server", "-c", "/etc/hysteria/config.yaml"]

networks:
    proxy-network:
        driver: bridge
```

### 二、Hysteria2的配置文件目录

```bash
# 配置文件
sudo nano /etc/hysteria/config.yaml

# 日志
sudo nano /var/log/hysteria/hysteria.log

# 启动日志
sudo journalctl -u hysteria-server --no-pager -n 50 --output cat
```

### 三、相关常用命令

### 四、配置文件

```yaml
# 监听地址和端口
listen: :8443

# 认证配置 (单用户)
auth:
    type: password
    password: "kydby-t3kuhs-agegRop"

# TLS 配置
tls:
    cert: "/etc/letsencrypt/live/kyson.store/fullchain.pem"
    key: "/etc/letsencrypt/live/kyson.store/privkey.pem"

quic:
    initStreamReceiveWindow: 8388608
    maxStreamReceiveWindow: 8388608
    initConnReceiveWindow: 20971520
    maxConnReceiveWindow: 20971520
    maxIdleTimeout: 30s
    maxIncomingStreams: 1024
    disablePathMTUDiscovery: false

# 日志配置
log:
    level: debug
    format: text
    output: "/var/log/hysteria/hysteria.log"
```