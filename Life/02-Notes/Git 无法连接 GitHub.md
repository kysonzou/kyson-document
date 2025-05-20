---
category:
  - Tech
tags:
  - Git
status: Done
---
这是一份关于解决 Git 因代理软件（如 V2RayN）导致无法连接 GitHub 问题的笔记：

**问题描述：**

当执行 git clone, git push, git pull 等命令时，出现类似以下错误：

fatal: unable to access 'https://github.com/...': Failed to connect to github.com port 443 after <...> ms: Couldn't connect to server

尽管浏览器可以通过代理正常访问 GitHub。

**核心原因：**

Git 命令行工具没有配置为通过代理软件（如 V2RayN）建立的网络连接，导致无法直接访问 GitHub。

**解决方案步骤：**

**1. 确认代理软件的本地监听端口**：

- 打开你的代理软件 (如 V2RayN) 的设置界面。
- 查找其提供的本地 HTTP 代理端口和/或 SOCKS5 代理端口。
    - **HTTP 代理端口示例**：`127.0.0.1:10809` (IP 通常是 `127.0.0.1`，端口号需根据你的软件实际设置填写)。
    - **SOCKS5 代理端口示例**：`127.0.0.1:10808` (IP 通常是 `127.0.0.1`，端口号需根据你的软件实际设置填写)。

**2. 配置 Git 使用代理：**

打开命令行/终端 (Git Bash, PowerShell, CMD, Terminal等)，根据你的代理类型执行相应命令：

- **如果使用 HTTP 代理：**
    ```Bash
    git config --global http.proxy http://127.0.0.1:10809
    git config --global https.proxy http://127.0.0.1:10809
    ```
    
    _(将 `端口号` 替换为你在步骤1中找到的 HTTP 代理端口)_
    
- **如果使用 SOCKS5 代理 (推荐使用 `socks5h` 以便代理服务器解析DNS)：**
    ```Bash
    git config --global http.proxy socks5h://127.0.0.1:10808
    git config --global https.proxy socks5h://127.0.0.1:10808
    ```
    
    _(将 `端口号` 替换为你在步骤1中找到的 SOCKS5 代理端口)_
    
- **说明：**
    
    - `--global` 使配置对当前用户的所有 Git 仓库生效。若只想对当前仓库生效，去掉 `--global` 并在仓库目录下执行。

**3. 测试 Git 连接：**

重新尝试执行之前失败的 Git 命令，例如：
```Bash
git clone https://github.com/kysonzou/kyson-document.git
```

**4. 恢复 Git 默认网络设置 (不再使用代理时)：**

如果之后不需要 Git 通过代理，执行以下命令清除代理配置：
```Bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

**核心思路总结：** Git 本身不直接识别系统级的代理设置（除非是通过环境变量间接影响），需要显式为其配置代理服务器地址和端口。确保 Git 使用的代理端口与代理软件提供的本地监听端口一致，并注意代理软件本身的运行模式和路由规则。
