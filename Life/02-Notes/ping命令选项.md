---
category:
  - Tech
tags:
  - Linux
  - MacOS
status: Done
---

**常见的 Ping 命令选项**

- ping -t [目标地址]：持续发送 ping 请求，直到用户中断。

- ping -n [次数] [目标地址]：指定发送 ping 请求的次数。（Windows）
- ping -c [次数] [目标地址]：指定发送 ping 请求的次数。（Linux/Unix 系统）

- ping -l [数据包大小] [目标地址]：指定 ICMP 数据包的大小，以测试网络对大数据包的处理能力  

- ping -4 [目标地址]：强制使用 IPv4 地址。

- ping -6 [目标地址]：强制使用 IPv6 地址。

**怎么暂停ping**

在终端中执行 ping 命令时，如果需要暂停或终止 ping，可以使用以下方法：

 **1. 暂停 ping**  
 
   - 按下键盘上的 Ctrl + Z 可以将 ping 命令挂起。  
   - 挂起后，ping 会停止运行，回到命令提示符。  
   - 如果想恢复运行，可以使用以下命令：
     ```bash
      fg
     ```

**2. 停止 ping**

- 按下 Ctrl + C 可以终止 ping 命令。
- ping 会立即停止，并显示统计信息（如丢包率、平均延迟等）。

**3. 后台运行 ping**

- 如果不想完全暂停，但希望将 ping 放到后台运行，可以使用以下方法：

-  在执行 ping 时直接加上 &：
    ```bash
    ping example.com &
   ```

- 如果 ping 已经在运行，按下 Ctrl + Z 后输入：
    ```bash
    bg
  ```
  