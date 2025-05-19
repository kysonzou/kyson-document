---
category:
- Tech
tags:
- Python
status: Done
---



### 1. 使用 venv 创建私有虚拟环境
1. 在 Python 3 中，venv 是一个内置模块，可以直接使用：
   ```bash
   python3 -m venv .venv
   ```
   - python3: 调用你的 Python 3 版本。   
   
   - -m venv：告诉 Python 运行 venv 模块。-m 是 “module” 的缩写，作用是指示 Python 运行某个模块而不是一个脚本文件。venv 是 Python 标准库中的一个模块，用于创建虚拟环境。这个命令相当于让 Python 执行 venv 模块中的代码，创建一个新的虚拟环境。  
   
   - .venv: 这是虚拟环境的目录名。你可以随意命名这个目录，比如 .env 或 .myenv，但常见的是 venv。

2. 激活虚拟环境
   ```bash
   source .venv/bin/activate
   ```

3. 退出虚拟环境
   ```bash
   deactivate
   ```

4. 删除虚拟环境
   ```bash
   rm -rf venv
   ```

### 2. 使用 virtualenv 创建私有虚拟环境
1. 安装virtualenv：
   ```bash
   pip install virtualenv
   ```

2. 创建虚拟环境：
   ```bash
   virtualenv .venv
   ```

3. 激活、退出、删除虚拟环境和venn一样
   啊算法的说法


[[python使用虚拟环境|使用方法]]

