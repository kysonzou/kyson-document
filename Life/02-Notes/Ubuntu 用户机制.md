在 Ubuntu 系统中，用户机制和权限体系基于多用户设计，旨在提供安全性和资源管理。以下是系统化的用户机制、权限模型以及常见操作的详细介绍。

---

## 1. 用户机制

### 1.1 用户分类
1. **超级用户（root）**：
   - 拥有系统最高权限，可以执行所有操作，包括管理文件、安装软件、修改系统配置。
   - 一般不直接登录 root，而是通过 `sudo` 提升权限执行命令。

2. **普通用户**：
   - 用户权限受限，通常用于运行日常应用程序和管理用户自身文件。
   - 无法访问系统关键目录（如 `/root`、`/etc`）或操作其他用户的文件。

3. **系统用户**：
   - 专用于运行服务或守护进程（如 `nobody`、`www-data`）。
   - 无登录权限，权限最低，仅访问运行服务所需的特定文件。

### 1.2 用户和组
1. **用户（User）**：
   - 每个用户都有唯一的用户名和用户 ID（UID）。
   - 系统中的用户信息存储在 `/etc/passwd` 文件中。

2. **组（Group）**：
   - 用于管理一组用户的权限，共享访问某些文件或目录。
   - 每个用户可以属于一个主组和多个附加组。

### 1.3 用户信息文件
- **`/etc/passwd`**：存储用户信息。
  示例：
  ```
  ubuntu:x:1000:1000:Ubuntu,,,:/home/ubuntu:/bin/bash
  ```
  各字段含义：
  - 用户名：`ubuntu`
  - 密码占位符：`x`（实际密码存储在 `/etc/shadow` 中）
  - 用户 ID（UID）：`1000`
  - 组 ID（GID）：`1000`
  - 用户描述：`Ubuntu`
  - 主目录：`/home/ubuntu`
  - 登录 Shell：`/bin/bash`

- **`/etc/group`**：存储组信息。
  示例：
  ```
  sudo:x:27:ubuntu
  ```


---

## 2. 用户管理常见操作

### 2.1 用户操作
1. 添加用户：
   ```bash
   sudo adduser username
   ```
2. 删除用户：
   ```bash
   sudo deluser username
   ```
3. 修改用户信息：
   ```bash
   sudo usermod -l newname oldname      # 修改用户名
   sudo usermod -G groupname username  # 添加用户到组
   ```
4. 锁定用户：
   ```bash
   sudo passwd -l username
   ```

### 2.2 组操作
1. 添加组：
   ```bash
   sudo groupadd groupname
   ```
2. 删除组：
   ```bash
   sudo groupdel groupname
   ```
3. 将用户添加到组：
   ```bash
   sudo usermod -aG groupname username
   ```


