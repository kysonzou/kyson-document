---
category:
  - Tech
tags:
  - Linux
  - MacOS
status: Done
---
`tar` 是 **Linux** 和 **类 Unix (Unix-like)** 系统中常用的命令，用于创建和解压归档文件。它的名称来自 "tape archive"，最初是为磁带备份设计的。

`tar` 通常内置于操作系统中，一般不需要额外下载

### 格式

```bash
tar [选项] [归档文件] [文件或目录]
```

### 常用选项

1. **创建归档文件**
   - `-c`：创建新的归档文件
   - `-f`：指定归档文件的名称

   ```bash
   tar -cf archive.tar file1 file2 directory/
   ```

2. **解压归档文件**
   - `-x`：解压归档文件
   - `-f`：指定归档文件的名称

   ```bash
   tar -xf archive.tar
   ```

3. **查看归档内容**
   - `-t`：列出归档文件的内容
   - `-f`：指定归档文件的名称

   ```bash
   tar -tf archive.tar
   ```

4. **压缩归档文件**
   - `-z`：使用 gzip 压缩
   - `-j`：使用 bzip2 压缩
   - `-J`：使用 xz 压缩

   ```bash
   tar -czf archive.tar.gz file1 file2 directory/  # 使用 gzip 压缩
   tar -cjf archive.tar.bz2 file1 file2 directory/  # 使用 bzip2 压缩
   tar -cJf archive.tar.xz file1 file2 directory/  # 使用 xz 压缩
   ```

5. **解压缩归档文件**
   - `-z`：解压 gzip 压缩的归档文件
   - `-j`：解压 bzip2 压缩的归档文件
   - `-J`：解压 xz 压缩的归档文件

   ```bash
   tar -xzf archive.tar.gz  # 解压 gzip 压缩的归档文件
   tar -xjf archive.tar.bz2  # 解压 bzip2 压缩的归档文件
   tar -xJf archive.tar.xz  # 解压 xz 压缩的归档文件
   ```

### 常用组合命令示例

1. **创建 gzip 压缩的归档文件**
   ```bash
   tar -czvf archive.tar.gz file1 file2 directory/
   ```

2. **解压 gzip 压缩的归档文件**
   ```bash
   tar -xzvf archive.tar.gz
   ```

3. **创建 bzip2 压缩的归档文件**
   ```bash
   tar -cjvf archive.tar.bz2 file1 file2 directory/
   ```

4. **解压 bzip2 压缩的归档文件**
   ```bash
   tar -xjvf archive.tar.bz2
   ```

5. **创建 xz 压缩的归档文件**
   ```bash
   tar -cJvf archive.tar.xz file1 file2 directory/
   ```

6. **解压 xz 压缩的归档文件**
   ```bash
   tar -xJvf archive.tar.xz
   ```

### 其他有用的选项

- `-v`：显示详细的处理信息（verbose）
- `-C`：切换到指定目录

```bash
tar -xzf archive.tar.gz -C /path/to/directory  # 将归档文件解压到指定目录
```

这些是 `tar` 命令的一些基本用法，可以满足大多数归档和解压的需求。根据实际情况选择适合的选项和参数组合，可以更灵活地使用 `tar` 命令。