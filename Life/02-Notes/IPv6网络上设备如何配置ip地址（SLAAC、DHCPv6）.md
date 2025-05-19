---
category:
  - Tech
tags:
  - TCPIP
status: Done
---
在IPv6网络中，设备获取IP地址的过程与IPv4有所不同。IPv6提供了几种自动配置IP地址的方法，主要包括**无状态自动配置**（Stateless Address Autoconfiguration, SLAAC）和**有状态配置**（通过DHCPv6，**Dynamic Host Configuration Protocol**）。以下是详细解释：

**1. 无状态地址自动配置（SLAAC）**

这是IPv6中最常见的自动配置方式。设备可以通过以下步骤自动配置IP地址：

- **链接本地地址生成**：当设备首次连接到网络时，会自动生成一个唯一的链路本地地址（Link-Local Address），通常使用fe80::/64前缀和设备的MAC地址（通过EUI-64方法）生成。该地址用于本地网络中的通信。

- **路由器通告**：设备会发送一个路由器请求（Router Solicitation, RS）消息（ICMPv6）来询问网络是否有IPv6路由器存在。连接网络的路由器会通过路由器通告（Router Advertisement, RA）消息进行响应。RA消息中包含网络前缀和其他网络信息。

- **全局唯一地址生成**：设备使用从RA消息中接收到的网络前缀结合自己的接口标识符（例如MAC地址）生成一个全局唯一地址（Global Unicast Address）。

- **重复地址检测（DAD）**：设备在使用生成的IPv6地址之前，会进行重复地址检测，确保该地址在网络中是唯一的。如果发现有地址冲突，设备不会使用该地址。

**2. 有状态配置（DHCPv6）**

与IPv4中的DHCP类似，IPv6网络中也可以使用DHCPv6进行IP地址的有状态分配。这种方法通常用于需要集中管理IP地址分配的网络。步骤如下：

- **Solicit消息**：设备发送Solicit消息来查找网络中的DHCPv6服务器。
    
- **Advertise消息**：DHCPv6服务器接收到Solicit消息后，会发送Advertise消息作为响应，告知设备它可以提供IPv6地址和其他网络配置。
    
- **Request消息**：设备从接收到的Advertise消息中选择一个DHCPv6服务器，并发送Request消息，请求特定的IP地址和配置参数。
    
- **Reply消息**：DHCPv6服务器发送Reply消息，确认分配的IP地址和其他网络配置

**3. 混合模式**

在许多情况下，网络会同时使用SLAAC和DHCPv6。例如，网络中的设备可以使用SLAAC自动获取IP地址，但仍通过DHCPv6获取额外的配置信息（如DNS服务器）。

**区别于IPv4**

- **广播与多播**：IPv6不使用广播来发送网络请求。相反，它使用多播和单播，尤其是路由器通告和请求消息，来减少网络中的不必要流量。

- **链路本地地址**：每个IPv6设备都会自动分配一个链路本地地址，这确保了即使没有全局IP地址，设备也可以在本地网络中通信。

  

