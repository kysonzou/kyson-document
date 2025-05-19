---
category:
  - Tech
tags:
  - Application
status: Done
---
[xray Github地址](https://github.com/XTLS/Xray-core)
[xray 官网](https://xtls.github.io)
[xray 配置指南](https://github.com/XTLS/Xray-examples)
### 一、xray的docker部署

```yaml
services:
    xray:
        image: ghcr.io/xtls/xray-core:latest
        container_name: xray
        volumes:
            - ./xray/config.json:/etc/xray/config.json
            # - ./xray/log:/var/log/xray # 创建并映射一个目录给Xray日志
            - /etc/letsencrypt:/etc/letsencrypt
        restart: always
        ports:
            - "1080:1080"
            - "2080:2080"
        networks:
            - proxy-network
        command: ["run", "-config", "/etc/xray/config.json"]

networks:
    proxy-network:
        driver: bridge
```
### 二、xray的配置文件目录

```bash
# 配置文件
sudo nano /etc/xray/config.json

# 日志
sudo nano /var/log/xray/access.log
sudo nano /var/log/xray/error.log
```

### 三、相关常用命令

```bash
sudo systemctl start xray

sudo systemctl restart xray

sudo systemctl status xray

sudo nano /usr/local/etc/xray/config.json

sudo journalctl -u xray --no-pager -n 50 --output cat
```
### 四、配置文件

```json
{
    "log": {
        "loglevel": "warning"
    },
    "inbounds": [
        {
            "listen": "0.0.0.0",
            "port": 1080,
            "protocol": "vless",
            "settings": {
                "clients": [
                    {
                        "id": "E03BE103-DEEF-4261-9A30-ACE196E68C79",
                        "flow": "xtls-rprx-vision"
                    }
                ],
                "decryption": "none"
            },
            "streamSettings": {
                "network": "tcp",
                "security": "tls",
                "tlsSettings": {
                    "rejectUnknownSni": true,
                    "minVersion": "1.2",
                    "certificates": [
                        {
                            "ocspStapling": 3600,
                            "certificateFile": "/etc/letsencrypt/live/kyson.store/fullchain.pem",
                            "keyFile": "/etc/letsencrypt/live/kyson.store/privkey.pem"
                        }
                    ]
                }
            },
            "sniffing": {
                "enabled": true,
                "destOverride": [
                    "http",
                    "tls"
                ]
            }
        },
        {
            "listen": "0.0.0.0",
            "port": 2080,
            "protocol": "vless",
            "settings": {
                "clients": [
                    {
                        "id": "DF57BEA1-2DFB-4422-9779-4AF40825386A",
                        "flow": ""
                    }
                ],
                "decryption": "none"
            },
            "streamSettings": {
                "network": "tcp",
                "security": "tls",
                "tlsSettings": {
                    "certificates": [
                        {
                            "certificateFile": "/etc/letsencrypt/live/kyson.store/fullchain.pem",
                            "keyFile": "/etc/letsencrypt/live/kyson.store/privkey.pem"
                        }
                    ],
                    "serverName": "kyson.store" ,
                    "allowInsecure": false
                }
            }
        }
    ],
    
    "outbounds": [
        {
            "protocol": "freedom",
            "tag": "direct"
        },
        {
            "protocol": "blackhole",
            "tag": "block"
        }
    ],
    "routing": {
        "domainStrategy": "IPIfNonMatch",
        "rules": [
            {
                "type": "field",
                "ip": [
                    "geoip:cn"
                ],
                "outboundTag": "block"
            }
        ]
    },
    "policy": {
        "levels": {
            "0": {
                "handshake": 2,
                "connIdle": 120
            }
        }
    }
}
```