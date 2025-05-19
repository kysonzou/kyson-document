---
category:
  - Tech
tags:
  - Git
status: Done
---
 **问题描述**
 
在使用 git 时，中文文件名显示为编码形式（如 `\346\234\252\345\221\275\345\220\215.md`），影响正常阅读和操作。

**环境检查**

1. 系统编码检查：
    ```bash
    echo $LANG
    # 输出: en_US.UTF-8，系统是支持中文编码的
   ```

2. 中文显示测试：
    ```bash
    echo "未命名"
    # 输出: 未命名，正常显示中文，说明终端支持中文
    ```

3. 文件系统检查：
    ```bash
    ls 02-Notes
    # 正常显示文件夹中的中文文件名，说明文件系统支持中文
    ```

**解决方案**

通过设置 git 配置解决中文显示问题：

1. 核心设置（最重要）：
    ```bash
    git config --global core.quotepath false
    # 禁止 git 对中文文件名进行转义，直接显示中文
    ```

2. 完整中文支持配置：
    ```bash
    git config --global gui.encoding utf-8        # 设置图形界面编码
    git config --global i18n.commit.encoding utf-8    # 设置提交信息编码
    git config --global i18n.logoutputencoding utf-8  # 设置输出日志编码
    ```

配置说明

- `core.quotepath false`: 关闭路径转义，允许直接显示中文字符
- `gui.encoding`: 配置图形界面的编码方式
- `i18n.commit.encoding`: 配置提交信息的编码
- `i18n.logoutputencoding`: 配置日志输出的编码

注：所有配置使用 `--global` 参数，将对当前用户的所有仓库生效。如需针对单个仓库配置，去除 `--global` 参数即可。

