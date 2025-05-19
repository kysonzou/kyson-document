---
category:
  - Tech
tags:
  - Linux
  - MacOS
status: Done
---
`wget` 是一个用于从网络下载文件的命令行工具。它的名称来自 "web get"，它支持通过 HTTP、HTTPS 和 FTP 协议下载文件，并且可以使用多种选项进行灵活的下载操作。

`wget` 提供了许多功能和选项，以下是一些常用的命令和方法：

1. **下载文件**
   - `wget [URL]`: 下载指定 URL 的文件。
   ```bash
   wget http://example.com/file.zip
   ```

2. **断点续传**
   - `wget -c [URL]`: 断点续传未完成的下载。
   ```bash
   wget -c http://example.com/largefile.zip
   ```

3. **下载到指定目录**
   - `wget -P [目录] [URL]`: 将文件下载到指定目录。
   ```bash
   wget -P /path/to/directory http://example.com/file.zip
   ```

4. **递归下载**
   - `wget -r [URL]`: 递归下载整个目录或网站。
   ```bash
   wget -r http://example.com/directory/
   ```

5. **限制下载速度**
   - `wget --limit-rate=[速度] [URL]`: 限制下载速度。
   ```bash
   wget --limit-rate=100k http://example.com/file.zip
   ```

6. **后台下载**
   - `wget -b [URL]`: 在后台下载文件。
   ```bash
   wget -b http://example.com/file.zip
   ```

7. **指定用户代理**
   - `wget --user-agent="[User-Agent]" [URL]`: 指定用户代理字符串。
   ```bash
   wget --user-agent="Mozilla/5.0" http://example.com/file.zip
   ```

8. **下载所有链接**
   - `wget -i [文件]`: 从一个包含 URL 列表的文件中下载所有链接。
   ```bash
   wget -i urls.txt
   ```