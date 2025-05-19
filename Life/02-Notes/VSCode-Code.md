---
category:
- Tech
tags:
- VSCode
status: Done
---
code 是 Visual Studio Code (VS Code) 自带的命令行工具。通过这个命令，你可以在终端中打开 VS Code 并执行一些特定的操作。
### 一、常用命令

1. **打开当前目录**：
   ```bash
   code .    # 在当前目录中打开 VS Code。
   ```

2. **打开特定文件**：
   ```bash
   code filename   # 打开指定的文件，如果没有会新建
   ```

3. **打开特定目录**：
   ```bash
   code path/to/directory  # 打开指定的目录。
   ```
  
4. **打开新窗口**：
   ```bash
   code -n   # 在新窗口中打开 VS Code。
   ```
  
5. 查看code的版本信息
   ```bash
   code --version
   ```
### 二、code的安装

1. 添加 code 命令到 PATH
   - 打开 VS Code，按 Ctrl + Shift + P 打开命令面板。
   - 输入并选择 Shell Command: Install 'code' command in PATH。
   
   VSCode 会在 /usr/local/bin 目录下创建一个名为 code 的**符号链接**（symlink），指向 VS Code 的实际可执行文件所在路径。这样一来，终端可以直接使用 code 命令，而无需知道 VS Code 的真实安装路径。

