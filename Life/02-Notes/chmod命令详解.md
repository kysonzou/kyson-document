---
category:
  - Tech
tags:
  - Linux
  - MacOS
status: Done
---
`chmod` 是 Unix 和类 Unix 操作系统（如 Linux 和 macOS）中的一个命令，用于改变文件或目录的权限。`chmod` 命令的全称是 “change mode”。文件权限可以用数字（八进制）或符号表示。常见的权限有读取（read）、写入（write）和执行（execute）。

`chmod` 通常内置于操作系统中，一般不需要额外下载

### 使用方法
`chmod` 命令的基本语法如下：
```bash
chmod [选项] 模式 文件
```

### 数字模式
权限通常用一个三位的八进制数字来表示，每一位分别代表用户（owner）、用户组（group）和其他人（others）的权限。每一位的值由读取、写入和执行权限的和组成：

- 读取 (r) = 4
- 写入 (w) = 2
- 执行 (x) = 1

例如：
- `7` 表示读取、写入和执行权限 (4+2+1)
- `6` 表示读取和写入权限 (4+2)
- `5` 表示读取和执行权限 (4+1)
- `4` 表示读取权限 (4)

```bash
chmod 755 file    # 用户：rwx（7），组：rx（5），其他人：rx（5）
chmod 644 file    # 用户：rw（6），组：r（4），其他人：r（4）
chmod 777 file    # 所有人都有读写执行权限
```

### 符号模式
符号模式使用字符来表示权限的改变。

- `u` 表示用户（owner）
- `g` 表示用户组（group）
- `o` 表示其他人（others）
- `a` 表示所有人（all）

操作符：
- `+` 添加权限
- `-` 移除权限
- = 设置精确权限

例如：
```bash
chmod u+x file     # 给用户添加执行权限
chmod g-w file     # 去掉用户组的写权限
chmod o=r file     # 设置其他人只能读权限
chmod a+rw file    # 所有人添加读写权限
```

### 常用选项
- `-R`：递归地更改目录及其内容的权限
- `-v`：详细模式，显示被更改权限的文件

例如：
```bash
chmod -R 755 /path/to/directory   # 递归更改目录及其所有子文件和子目录的权限
chmod -v 644 file                 # 显示更改后的权限
```

### 实际应用
假设有一个脚本 `myscript.sh`，你希望自己可以读写执行，其他人只能读和执行：
```bash
chmod 755 myscript.sh
```

如果你有一个目录 `mydir`，你希望其所有文件和子目录都能被所有人读写执行：
```bash
chmod -R 777 mydir
```

希望这些解释对你有帮助！如果有更多具体的问题，随时告诉我。