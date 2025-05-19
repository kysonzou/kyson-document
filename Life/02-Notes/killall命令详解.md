---
category:
  - Tech
tags:
  - Linux
  - MacOS
status: Done
---



`killall` 是一个用于在 Unix 和 Linux 系统上终止进程的命令。它通过进程名称来终止所有匹配的进程，而不是通过进程 ID (PID)。这在需要终止多个同名进程时非常有用。

### 基本语法
```
killall [选项] 进程名称
```

### 常用选项
- `-e`：精确匹配进程名称。
- `-I`：忽略进程名称的大小写。
- `-u 用户名`：只终止属于指定用户的进程。
- `-v`：显示被终止的进程信息。
- `-w`：等待所有指定的进程被终止。
- `-s 信号`：发送指定的信号而不是默认的 `SIGTERM`。

### 示例

1. **终止所有名为 `firefox` 的进程**：
   ```shell
   sudo killall firefox
   ```

2. **发送 `SIGKILL` 信号来强制终止所有名为 `firefox` 的进程**：
   ```shell
   sudo killall -s SIGKILL firefox
   ```

3. **终止所有名为 `firefox` 的进程，并显示被终止的进程信息**：
   ```shell
   sudo killall -v firefox
   ```

4. **终止属于用户 `john` 的所有名为 `firefox` 的进程**：
   ```shell
   sudo killall -u john firefox
   ```

5. **忽略大小写终止所有名为 `firefox` 的进程**：
   ```shell
   sudo killall -I firefox
   ```

### 注意事项
- 使用 `killall` 命令时要小心，因为它会终止所有匹配的进程，这可能会导致意外终止重要的系统进程。
- 需要具有适当的权限（通常是超级用户权限）来终止某些进程。
