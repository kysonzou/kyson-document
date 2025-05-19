---
category:
  - Tech
tags:
  - Linux
  - MacOS
status: Done
---
```bash

ping www.baidu.com

PING www.a.shifen.com (153.3.238.110): 56 data bytes

  

64 bytes from 153.3.238.110: icmp_seq=0 ttl=53 time=14.676 ms

  

64 bytes from 153.3.238.110: icmp_seq=1 ttl=53 time=14.399 ms

  

64 bytes from 153.3.238.110: icmp_seq=2 ttl=53 time=14.192 ms

```

- **PING www.a.shifen.com (153.3.238.110)**：ping 命令显示了目标域名 www.baidu.com 被解析为 IP 地址 153.3.238.110，并显示其实际指向的域名 www.a.shifen.com （百度的一个 CDN 或负载均衡域）。

- **56 data bytes**：表示发送的数据包大小是 56 字节（不包括 IP 和 ICMP 头部的总大小为 64 字节）。

- **64 bytes**：从目标服务器收到的数据包大小是 64 字节。

- **from 153.3.238.110**：表示收到的 ICMP 回显应答是从 IP 地址 153.3.238.110 返回的。

- **icmp_seq**：表示 ICMP 数据包的序列号，从 0 开始递增，帮助检测数据包的顺序和丢失情况。

- **ttl（Time to Live）= 53**：表示该数据包的生存时间。TTL 起始值由源设备设定，每经过一个路由器减一。TTL 数字较大表明数据包经过的路由器较少。

- **time**：数据包的往返时间（RTT，Round Trip Time），以毫秒为单位。time=14.676 ms 表示从发送 ICMP 请求到收到应答所用的时间为 14.676 毫秒，显示网络的延迟。
  
