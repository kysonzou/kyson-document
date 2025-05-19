---
category:
  - Tech
tags:
  - Linux
status: Done
---



UFW（Uncomplicated Firewall）是Ubuntu和其他基于Debian的Linux系统中常用的防火墙管理工具，旨在简化复杂的iptables配置。通过UFW，用户可以方便地设置和管理主机的防火墙规则，控制网络访问。下面是UFW的基本操作和常见命令：

### 1. **启用/禁用UFW**
   - 启用防火墙：
     ```bash
     sudo ufw enable
     ```
   - 禁用防火墙：
     ```bash
     sudo ufw disable
     ```

### 2. **查看UFW状态**
   - 检查防火墙状态和规则：
     ```bash
     sudo ufw status
     ```
   - 查看详细的规则列表：
     ```bash
     sudo ufw status verbose
     ```

### 3. **允许/拒绝特定端口或服务**
   - 允许特定端口的入站流量：
     ```bash
     sudo ufw allow 22/tcp   # 允许SSH
     sudo ufw allow 80/tcp   # 允许HTTP
     ```
   - 拒绝特定端口的入站流量：
     ```bash
     sudo ufw deny 22/tcp
     ```
   - 允许服务名（如SSH、HTTP等）的流量：
     ```bash
     sudo ufw allow ssh
     sudo ufw allow http
     ```

### 4. **删除规则**
   - 删除一条规则：
     ```bash
     sudo ufw delete allow 22/tcp
     ```

### 5. **设置默认策略**
   - 默认拒绝所有入站连接：
     ```bash
     sudo ufw default deny incoming
     ```
   - 默认允许所有出站连接：
     ```bash
     sudo ufw default allow outgoing
     ```

### 6. **允许特定IP访问**
   - 允许某个IP的流量：
     ```bash
     sudo ufw allow from 192.168.1.100
     ```
   - 限制到某个端口：
     ```bash
     sudo ufw allow from 192.168.1.100 to any port 22
     ```

### 7. **日志记录**
   - 开启日志记录以监控防火墙活动：
     ```bash
     sudo ufw logging on
     ```

UFW适合个人服务器或小型网络中的防火墙管理。如果需要更精细的控制和功能，可以结合[[iptables防火墙|iptables]]进行高级配置。