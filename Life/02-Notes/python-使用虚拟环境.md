---
category:
- Tech
tags:
- Python
status: Done
---



**1. 安装包**

激活虚拟环境后，可以使用 pip 安装项目所需的 Python 包。安装的包会保存在虚拟环境中，而不会影响全局环境。
```bash
pip install 包名
```

例如：
```bash
pip install requests
```
  
**2. 生成 requirements.txt**  

为了记录和共享项目的依赖，可以使用以下命令生成 requirements.txt 文件：
```bash
pip freeze > requirements.txt 
```
这个文件包含了所有安装的包及其版本号
- pip freeze：该命令列出当前环境中已安装的所有 Python 包和版本，格式如下: `包名==版本号`
- \>：这是一个重定向符号，将命令的输出结果保存到指定文件，而不是直接显示在终端。
- requirements.txt：这是文件的名称，通常用来存放项目的依赖信息。这个文件可以被其他开发者或生产环境使用，来安装项目所需的所有包。
  
**3. 从 requirements.txt 安装依赖**

如果有一个 requirements.txt 文件，可以通过以下命令安装所有依赖：
```bash
pip install -r requirements.txt
```
- pip install：pip 是 Python 的包管理工具，用来安装、更新、和卸载 Python 包。install 命令用于安装指定的包。
- -r：这个选项的意思是“requirements file”，表示 pip 将从指定文件（requirements.txt）中读取并安装文件中列出的包。
- requirements.txt：这是包含包和版本信息的文件，通常用于列出项目的所有依赖包以及每个包的特定版本。