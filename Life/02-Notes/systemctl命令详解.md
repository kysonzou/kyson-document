---
category:
  - Tech
tags:
  - Linux
status: Done
---
 `systemctl` 是一个用于管理 **systemd** 系统服务的命令行工具。**systemd** 是大多数现代 Linux 发行版（如 CentOS、Ubuntu 和 Fedora）使用的初始化系统和服务管理器，负责管理系统的启动过程、服务的运行状态以及系统资源的分配。

## 主要功能

`systemctl` 提供了对 systemd 单元（Unit）的管理操作，包括启动、停止、重启服务等。

### **1. 服务管理**
- **启动服务**：
  ```bash
  systemctl start 服务名
  ```
- **停止服务**：
  ```bash
  systemctl stop 服务名
  ```
- **重启服务**：
  ```bash
  systemctl restart 服务名
  ```
- **查看服务状态**：
  ```bash
  systemctl status 服务名
  ```

### **2. 开机自动启动管理**
- **启用服务开机自启动**：
  ```bash
  systemctl enable 服务名
  ```
- **禁用服务开机自启动**：
  ```bash
  systemctl disable 服务名
  ```

### **3. 系统状态查看**
- **查看系统整体运行状态**：
  ```bash
  systemctl
  ```
- **列出所有服务**：
  ```bash
  systemctl list-units --type=service
  ```

- 查看系统启动目标：
  ```bash
  systemctl get-default
  ```

- 设置系统启动目标（如图形界面）：
  ```bash
  systemctl set-default graphical.target
  ```

### **4. 控制其他单元类型**
除了服务（`service`），`systemctl` 还能管理其他类型的单元，例如：
- **挂载点（`mount`）**
- **设备（`device`）**
- **目标（`target`）**：如多用户模式（`multi-user.target`）、图形界面（`graphical.target`）




