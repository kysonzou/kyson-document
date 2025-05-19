---
category:
  - Tech
tags:
  - TCPIP
status: Done
---
DHCP（Dynamic Host Configuration Protocol，动态主机配置协议）是一种网络协议，用于自动为网络设备（如计算机、手机等）分配 IP 地址以及其他网络配置信息。它简化了网络设备的管理，避免了手动配置每台设备的网络参数。具体来说，DHCP可以动态地分配：

1. **IP 地址**：为设备分配一个有效的 IP 地址，使其能够与网络中的其他设备通信。
2. **子网掩码**：用于确定网络部分和主机部分的界限。
3. **网关地址**：指定默认网关（通常是路由器的 IP 地址），使设备可以访问外部网络。
4. **[[DNS|DNS 服务器]]**：为设备提供解析域名到 IP 地址的 DNS 服务器。

##### DHCP 工作过程
DHCP 使用客户端-服务器模式工作，主要有以下几个步骤：

1. **DHCP Discover**：当一台设备连接到网络时，它会发送一个广播消息（DHCP Discover），请求一个 IP 地址。
2. **DHCP Offer**：DHCP 服务器收到请求后，预留一个 IP 地址，并通过 DHCP Offer 报文提供给设备。
3. **DHCP Request**：设备收到多个 DHCP Offer 后，选择一个，发送 DHCP Request 确认使用该 IP 地址。
4. **DHCP Acknowledgment**：DHCP 服务器确认设备选择的 IP 地址，并通过 DHCP Acknowledgment 将最终配置发送给设备。

这一过程使得设备可以动态获取网络配置，而无需人工干预。