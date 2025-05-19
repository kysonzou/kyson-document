---
category:
  - Tech
tags:
  - Linux
status: Done
---
APT (Advanced Package Tool) 是 Debian 系和基于 Debian 的 Linux 发行版（如 Ubuntu）用来管理软件包的工具。它提供了一系列用于安装、更新、移除软件包的命令行工具。

APT 通常是内建在基于 Debian 的 Linux 发行版中的，比如 Debian 和 Ubuntu。也就是说，当你安装了这些发行版后，APT 工具已经包含在系统中，无需额外安装。

### 1. 更新包列表和升级系统

1. **更新软件包列表** 
   ```bash
   sudo apt update
   ```
   作用：从配置的源中获取最新的软件包信息。

2. **升级所有已安装的软件包**
   ```bash
   sudo apt upgrade
   ```
   作用：将所有已安装的软件包升级到最新版本。

3. **完整升级**
   ```bash
   sudo apt full-upgrade
   ```
   作用：类似于 `apt upgrade`，但会删除有冲突的包以进行完整升级。

### 2. 安装和移除软件包

1. **安装软件包**
   ```bash
   sudo apt install [package_name]
   ```
   作用：安装指定的软件包。

2. **移除软件包**
   ```bash
   sudo apt remove [package_name]
   ```
   作用：移除指定的软件包，但保留配置文件。

3. **彻底移除软件包**
   ```bash
   sudo apt purge [package_name]
   ```
   作用：移除指定的软件包及其所有配置文件。

### 3. 搜索软件包

1. **搜索软件包**
   ```bash
   apt search [keyword]
   ```
   作用：搜索与关键词相关的软件包。

2. **显示软件包详细信息**
   ```bash
   apt show [package_name]
   ```
   作用：显示指定软件包的详细信息。

### 4. 清理系统

1. **移除不再需要的依赖包**
   ```bash
   sudo apt autoremove
   ```
   作用：移除系统中不再需要的依赖包。

2. **清理下载的软件包缓存**
   ```bash
   sudo apt clean
   ```
   作用：清理下载的软件包缓存。

3. **清理已过期的软件包缓存**
   ```bash
   sudo apt autoclean
   ```
   作用：清理已过期的软件包缓存。

### 5. 检查和修复系统

1. **检查系统中是否有损坏的依赖关系**
   ```bash
   sudo apt check
   ```
   作用：检查系统中是否有损坏的依赖关系。

2. **修复损坏的依赖关系**
   ```bash
   sudo apt install -f
   ```
   作用：修复损坏的依赖关系。
