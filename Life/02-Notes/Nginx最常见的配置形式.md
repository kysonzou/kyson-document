---
category:
  - Tech
tags:
  - Linux
status: Done
---
Nginx 是一个高性能的 Web 服务器，广泛应用于反向代理、负载均衡、静态资源服务等场景。以下是实际应用中最常见的配置形式：

---

## 1. 反向代理和负载均衡
### 用途
将客户端的请求转发到后端服务器，并支持多台服务器的负载均衡。

### 配置示例
```nginx
http {
    upstream backend_servers {
        server 192.168.1.10;  # 后端服务器 1
        server 192.168.1.11;  # 后端服务器 2
    }

    server {
        listen 80;
        server_name example.com;

        location / {
            proxy_pass http://backend_servers;  # 转发到后端服务器
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
}
```

### **特点**
- **反向代理：** 前端 Nginx 接收请求并转发给后端服务器。
- **负载均衡：** 自动分发流量到多台服务器。

---

## 2. 静态文件服务器
### 用途
直接提供 HTML、CSS、JS、图片等静态文件的访问。

### 配置示例
```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        root /var/www/html;   # 静态文件目录
        index index.html;     # 默认文件
    }

    location /images/ {
        root /var/www/images; # 单独的图片目录
    }
}
```

### 特点
- **高效：** 直接处理静态文件请求，性能优异。
- **灵活：** 支持不同路径绑定不同目录。

---

## 3. HTTPS 和 TLS 配置
### 用途
为站点启用 HTTPS，提供安全加密通信。

### 配置示例
```nginx
server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    location / {
        root /var/www/html;
        index index.html;
    }
}

server {
    listen 80;
    server_name example.com;

    # 强制跳转 HTTPS
    return 301 https://$host$request_uri;
}
```

### 特点
- **安全：** 提供 HTTPS 支持，保护通信数据。
- **自动跳转：** 从 HTTP 自动跳转到 HTTPS。
- **免费证书：** 可使用 Let’s Encrypt 提供的免费证书。

---

## 4. 动态与静态资源分离
### 用途
将静态资源和动态请求分开处理，减少后端服务器压力。

### 配置示例
```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://127.0.0.1:8080;  # 动态请求转发到后端应用
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        root /var/www/html;  # 静态文件目录
    }
}
```

### 特点
- **动态资源：** 转发到后端处理（如 Python、Node.js）。
- **静态资源：** 直接由 Nginx 提供，减少后端服务器压力。

---

## 5. CDN 和缓存
### 用途
将 Nginx 配置为缓存服务器，提高文件加载速度。

### 配置示例
```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=cache_zone:10m max_size=1g;
server {
    listen 80;
    server_name cdn.example.com;

    location / {
        proxy_cache cache_zone;      # 启用缓存
        proxy_cache_valid 200 1h;   # 缓存时间
        proxy_pass http://backend_servers;
        add_header X-Cache-Status $upstream_cache_status;
    }
}
```

### 特点
- **快速：** 减少请求延迟，提高访问速度。
- **节省：** 缓存内容减少后端服务器负载。

---

## 6. WebSocket 代理
### **用途**
支持 WebSocket 协议，用于代理双向通信服务。

### 配置示例
```nginx
server {
    listen 80;
    server_name example.com;

    location /websocket/ {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

### 特点
- **支持双向通信：** 满足 WebSocket 应用需求。
- **协议切换：** 通过 `Upgrade` 头实现 WebSocket 协议切换。

---

## 7. 多站点支持
### 用途
在同一台服务器上运行多个站点，通过域名或端口区分。

### 配置示例
```nginx
server {
    listen 80;
    server_name site1.example.com;

    location / {
        root /var/www/site1;
        index index.html;
    }
}

server {
    listen 80;
    server_name site2.example.com;

    location / {
        root /var/www/site2;
        index index.html;
    }
}
```

### 特点
- **灵活：** 一个 Nginx 实例可服务多个站点。
- **易管理：** 通过域名和路径区分不同站点。

---

## 8. 流量限制和防御
### **用途**
限制每秒请求数、连接数，防止恶意攻击（如 DDOS）。

### 配置示例
```nginx
http {
    limit_req_zone $binary_remote_addr zone=req_zone:10m rate=5r/s;

    server {
        listen 80;
        server_name example.com;

        location / {
            limit_req zone=req_zone burst=10 nodelay;  # 限制每秒请求数
            proxy_pass http://127.0.0.1:8080;
        }
    }
}
```

### 特点
- **保护服务器：** 防止恶意请求导致服务中断。
- **灵活控制：** 自定义请求速率、突发限制等参数。

---
## 9. 重定向

### 用途
用于将客户端请求从一个 URL 转发到另一个 URL。
### 配置示例
#### 1. HTTP 到 HTTPS 的普通重定向
- **需求**：将所有流量从 HTTP 重定向到 HTTPS，业务逻辑不依赖 POST 数据。
- **推荐方式**：使用 `301`（永久）、302（临时）。
- **配置示例**：
  ```nginx
  server {
      listen 80;
      server_name example.com www.example.com;
      return 301 https://$host$request_uri;
  }
  ```

#### 2. 表单提交或 API 请求需要保留 POST 数据
- **需求**：需要保留 POST 请求方法和数据，用于处理表单或 API 请求。
- **推荐方式**：使用 `307`（临时） 或 `308`（永久）。
- **配置示例**：
  ```nginx
  server {
      listen 80;
      server_name example.com www.example.com;
      return 308 https://$host$request_uri;
  }
  ```