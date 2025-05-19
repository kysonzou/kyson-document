---
category:
  - Tech
tags:
  - Linux
  - Application
status: Done
---
### 一、Nginx的docker部署

```yaml
services:
    nginx:
        image: nginx:alpine # 使用轻量级的 Alpine 版本
        container_name: nginx
        volumes:
            - ./nginx/conf.d:/etc/nginx/conf.d # http配置文件
            - ./nginx/data/www:/data/www:ro # 将宿主机的 /data/www 映射到容器内的 /data/www，只读模式
            - /etc/letsencrypt:/etc/letsencrypt # 证书
            # - ./nginx/log:/var/log/nginx # 日志
        ports:
            - "80:80"
            - "443:443"
        restart: always
        networks:
            - proxy-network

networks:
    proxy-network:
        driver: bridge
```

### 二、Nginx的配置文件

```bash
# 主配置文件
sudo nano /etc/nginx/nginx.conf

# http默认的配置文件，更好的写法是写到/etc/nginx/conf.d文件夹中去
sudo nano /etc/nginx/sites-available/default

# 默认的http服务配置文件夹，这里面的http配置都会被主配置文件引用
sudo nano /etc/nginx/conf.d

# 日志
sudo nano /var/log/nginx/access.log
sudo nano /var/log/nginx/error.log 
```

### 三、相关常用命令

```bash
# 检查配置是否正确
sudo nginx -t 

# 开始服务
sudo systemctl start nginx  

# 立即停止服务
sudo systemctl stop nginx  

# 重新开始服务
sudo systemctl restart nginx

# 查看 Nginx 状态
sudo systemctl status nginx 

# 查看端口状态
sudo lsof -i :80
sudo lsof -i :443
sudo ss -tuln | grep 8443

# 结束进程
sudo kill -9 1234 5678
```

### 四、配置文件
#### 4.1、HTTP模块配置文件
```c
http {
    # 默认服务器块（放在最前面）
    server {
        listen 443 ssl default_server;
        server_name _;# 无需指定 server_name

        ssl_certificate /etc/letsencrypt/live/kyson.store/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/kyson.store/privkey.pem;

        location / {
            return 404;
        }
    }
    
    # kyson.store            
    server {
        listen 443 ssl;
        server_name kyson.store;

        ssl_certificate /etc/letsencrypt/live/kyson.store/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/kyson.store/privkey.pem;
        
        root /var/www/html;
        index index.html;
    }
    
    # V2Ray 服务配置 websocket
    server {
        listen 443 ssl;
        server_name v2ray.kyson.store v2ray-cdn.kyson.store;

        ssl_certificate /etc/letsencrypt/live/kyson.store/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/kyson.store/privkey.pem;

        location / {
            proxy_redirect off;
            proxy_pass http://127.0.0.1:10000;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
    
    # HTTP 到 HTTPS 的重定向
    server {
        listen 80;
        server_name kyson.store  v2ray.kyson.store v2ray-cdn.kyson.store;
        return 301 https://$host$request_uri;
    }
}
# 常见的还有 API 服务配置、静态资源服务配置
```
#### 4.2、Streaming模块

```c
# Stream 模块配置，用于 TCP 代理 V2Ray
stream {
    upstream v2ray_backend {
        server 127.0.0.1:10001;  # V2Ray 的后端服务监听地址和端口
    }

    upstream web_backend {
        server 127.0.0.1:20001;  
    }

    # 默认是监听全部server_name的
    map $ssl_preread_server_name $allowed {
        v2ray.kyson.store  1;  # 仅允许 v2ray.kyson.store
        v2ray-cdn.kyson.store  1;  
        kyson.store        0;
        default            0;
    }

    map $ssl_preread_server_name $backend_name {
        v2ray.kyson.store   v2ray_backend;
        v2ray-cdn.kyson.store   v2ray_backend;
        kyson.store         web_backend;
        default             web_backend;
    }
    server {
        listen 8443 ssl;  # 使用 8443 端口处理 TCP+TLS 流量

        ssl_certificate /etc/letsencrypt/live/kyson.store/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/kyson.store/privkey.pem;

        # 启用 SNI 以便区分流量（可选）
        ssl_preread on;
        # 转发流量到上游 
        proxy_pass $backend_name;
        # 超时设置
        proxy_timeout 10m;
        proxy_connect_timeout 1s;
        
        # 过滤域名，非 v2ray.kyson.store 拒绝访问
        preread_by_lua_block {
            if ngx.var.allowed == "0" then
                return ngx.exit(444);  # 返回状态码 444 直接关闭连接
            end
        }
    }
}
```