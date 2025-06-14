---
category:
  - Tech
tags:
  - TCPIP
status: Done
---
### TCP/IP模型

>[!Note]- 定义
>TCP/IP模型（Transmission Control Protocol/Internet Protocol Model）是现代互联网通信的基础。它为网络设备之间的通信提供了一个标准化的框架，包含了从物理传输到应用交互的所有层级。该模型通常被划分为四层：**网络接口层**、**互联网层**、**传输层**和**应用层**。它与OSI七层模型类似，但更简化。
>
>1. 网络接口层（Link Layer）
>	- **功能**：负责在本地网络中将数据从一台设备传输到另一台设备。这一层主要处理物理网络连接的细节，如以太网、Wi-Fi等。
>	- **核心任务**：定义如何通过物理媒介发送数据帧，处理硬件的物理地址（如MAC地址）以及错误检测与校正。
>	- **典型协议**：以太网（Ethernet）、Wi-Fi、PPP（点对点协议）。
>
>2. 互联网层（Internet Layer）
>	- **功能**：负责实现跨网络的数据传输，定义如何将数据包从源地址路由到目的地址。其核心协议是IP（Internet Protocol），也是该层名称的来源。
>	- **核心任务**：提供逻辑地址（IP地址），进行分组路由选择，确保数据包可以通过不同的网络传输。
>	- **协议**：
>		- **IP（Internet Protocol）**：最核心的协议，提供不可靠、无连接的数据传输服务。数据包可以独立传输且无顺序保证，因此可能发生丢包。
>		- **ICMP（Internet Control Message Protocol）**：用于网络设备之间的错误报告和诊断。例如，`ping`命令通过ICMP来测试连接的可达性。
>		- **ARP（Address Resolution Protocol）**：将IP地址转换为物理地址（MAC地址）。
>		- **RARP（Reverse ARP）**：将物理地址转换为IP地址（现已过时）。
>
>3. 传输层（Transport Layer）
>	- **功能**：为应用层提供端到端的数据传输服务，确保数据在两台设备间可靠地传输。
>	- **核心任务**：提供端口地址（区分不同的应用），并提供传输的可靠性和流量控制。
>	- **协议**：
>		- **TCP（Transmission Control Protocol）**：提供可靠的、面向连接的服务。TCP确保数据包按顺序到达且无丢失，通过建立连接、数据传输和关闭连接来实现这一点。TCP还提供错误检测和流量控制。
>		- **UDP（User Datagram Protocol）**：提供无连接的、不可靠的传输服务。它不保证数据包的顺序或到达，适用于需要快速传输且对可靠性要求不高的场景，如视频流或在线游戏。
>
>4. 应用层（Application Layer）
>	- **功能**：直接面向用户，提供各种网络应用程序的接口。应用层协议为用户与应用程序提供通信服务。
>	- **核心任务**：支持各种互联网服务，如电子邮件、文件传输、网页浏览等。
>	- **协议**：
>		- **HTTP（Hypertext Transfer Protocol）**：用于网页浏览。
>		- **FTP（File Transfer Protocol）**：用于文件传输。
>		- **SMTP（Simple Mail Transfer Protocol）**：用于电子邮件发送。
>		- **DNS（Domain Name System）**：将域名解析为IP地址。
>
>TCP/IP模型的工作流程
>1. **数据封装**：应用层生成的数据会先被传输层（TCP/UDP）封装为段（segment），然后在互联网层进一步封装为数据包（packet），最后在网络接口层封装为帧（frame）进行物理传输。
>2. **路由与传输**：数据帧通过网络接口层在本地传输，互联网层负责将数据包跨网络传输并找到合适的路径。传输层确保数据完整性和正确顺序。
>3. **解封装**：接收方的每一层依次解封装收到的数据，直到应用层可以处理最终数据并展示给用户。
>
>TCP/IP模型是互联网通信的基石，负责从低层次的物理传输到高层次的应用交互。每一层都有明确的功能和协议，层层封装和解封装数据，确保数据能够可靠地从一台设备传输到另一台设备。

OSI模型注重通信协议必要的功能，TCP/IP更强调在计算机上实现协议应该开发哪种程序。

应用层：OSI模型的应用成+表示层+会话层（Application Layer ）

传输层：OSI模型的传输层（Transport Layer）

网络层：OSI模型的网络层（Network Layer）

网络接口层：OSI模型的数据链路层+物理层（Network Port Layer）

####  应用层

最上层的，也是我们能直接接触到的就是**应用层**（*Application Layer*），我们电脑或手机使用的应用软件都是在应用层实现。那么，当两个不同设备的应用需要通信的时候，应用就把应用数据传给下一层，也就是传输层。

所以，应用层只需要专注于为用户提供应用功能，比如：文件传输协议（FTP）、网页浏览协议（HTTP、HTTPS）、远程登录（SSH、Telnet）、域名系统（DNS）、电子邮件传输协议（SMTP），电子邮件接收协议（POP3和IMAP）等。

应用层是不用去关心数据是如何传输的，就类似于，我们寄快递的时候，只需要把包裹交给快递员，由他负责运输快递，我们不需要关心快递是如何被运输的。

而且应用层是工作在操作系统中的用户态，传输层及以下则工作在内核态。

####  传输层

应用层的数据包会传给传输层，**传输层**（*Transport Layer*）是为应用层提供网络支持的。
![[TCPIP模型-传输层.png]]


在传输层会有两个传输协议，分别是 TCP 和 UDP。

TCP 的全称叫传输控制协议（*Transmission Control Protocol*），大部分应用使用的正是 TCP 传输层协议，比如 HTTP 应用层协议。TCP 相比 UDP 多了很多特性，比如流量控制、超时重传、拥塞控制等，这些都是为了保证数据包能可靠地传输给对方。

UDP 相对来说就很简单，简单到只负责发送数据包，不保证数据包是否能抵达对方，但它实时性相对更好，传输效率也高。当然，UDP 也可以实现可靠传输，把 TCP 的特性在应用层上实现就可以，不过要实现一个商用的可靠 UDP 传输协议，也不是一件简单的事情。

应用需要传输的数据可能会非常大，如果直接传输就不好控制，因此当传输层的数据包大小超过 [[TCPIP有几层#^5a80c7|MSS]]（Maximum Segment Size，TCP 最大报文段长度，通常为1460字节） ，就要将数据包分块，这样即使中途有一个分块丢失或损坏了，只需要重新发送这一个分块，而不用重新发送整个数据包。在 TCP 协议中，我们把每个分块称为一个 **TCP 段**（*TCP Segment*）。

![[TCPIP模型-TCP段.png]]

当设备作为接收方时，传输层则要负责把数据包传给应用，但是一台设备上可能会有很多应用在接收或者传输数据，因此需要用一个编号将应用区分开来，这个编号就是**端口**。

比如 80 端口通常是 Web 服务器用的，22 端口通常是远程登录服务器用的。而对于浏览器（客户端）中的每个标签栏都是一个独立的进程，操作系统会为这些进程分配临时的端口号。

由于传输层的报文中会携带端口号，因此接收方可以识别出该报文是发送给哪个应用。

#### 网络层

传输层可能大家刚接触的时候，会认为它负责将数据从一个设备传输到另一个设备，事实上它并不负责。

实际场景中的网络环节是错综复杂的，中间有各种各样的线路和分叉路口，如果一个设备的数据要传输给另一个设备，就需要在各种各样的路径和节点进行选择，而传输层的设计理念是简单、高效、专注，如果传输层还负责这一块功能就有点违背设计原则了。

也就是说，我们不希望传输层协议处理太多的事情，只需要服务好应用即可，让其作为应用间数据传输的媒介，帮助实现应用到应用的通信，而实际的传输功能就交给下一层，也就是**网络层**（*Internet Layer*）。
![[TCPIP模型-网络层.png]]

网络层最常使用的是 IP 协议（Internet Protocol），IP 协议会将传输层的报文作为数据部分，再加上 IP 包头组装成 IP 报文，如果 IP 报文大小超过 [[TCPIP有几层#^5a80c7|MTU]]（Maximum Transmission Unit，最大传输单元，以太网中一般为 1500 字节）就会**再次进行分片**，得到一个即将发送到网络的 IP 报文。

![[TCPIP模型-IP段.png]]


网络层负责将数据从一个设备传输到另一个设备，世界上那么多设备，又该如何找到对方呢？因此，在网络层需要进行IP路由，找到下一跳的IP地址，直到跳到目标IP。

#### 网络接口层

也叫链路层，生成了 IP 头部之后，接下来要交给**网络接口层**（*Link Layer*）在 IP 头部的前面加上 MAC 头部，并封装成数据帧（Data frame）发送到网络上。

![[TCPIP模型-链路层.png]]

接收的网络设备（家庭一般都是路由器）接收到网络接口层的数据后通过[[TCPIP有几层#^c31fb8|IP解析]]处理数据的转发

>下一跳IP解析：
>1. 当目标IP与源IP在同一网段时,设备直接通过ARP寻址获取目标IP的MAC地址，通过物理层(如以太网)发送出去。
>2. 如果不在同一网段,设备会查找路由表确定下一跳的IP（一般都会是默认网关的IP地址）。
>3. 然后通过网关将数据转发到下一跳IP，之后数据就进入公网使用IP协议传输了。
^c31fb8

#### 总结

综上所述，TCP/IP 网络通常是由上到下分成 4 层，分别是**应用层，传输层，网络层和网络接口层**。

![[TCPIP模型-总结.png]]

再给大家贴一下每一层的封装格式：

![[TCPIP模型-封装总结.png]]

网络接口层的传输单位是帧（frame），IP 层的传输单位是包（packet），TCP 层的传输单位是段（segment），HTTP 的传输单位则是消息或报文（message）。但这些名词并没有什么本质的区分，可以统称为数据包。

>[!Note]- MSS、MTU
>MSS（Maximum Segment Size，最大分段大小）和MTU（Maximum Transmission Unit，最大传输单元）是网络通信中的两个重要概念。它们与数据包的大小和传输效率密切相关。以下是对这两个概念的简要解释：
>
>1. MTU（最大传输单元）：
>	- MTU是指在一个网络链路上可以传输的最大数据包大小。
>	- 它通常由网络硬件（如以太网、Wi-Fi等）决定。
>	- 常见的以太网MTU为1500字节。
>
>2. MSS（最大分段大小）：
>	- MSS是TCP协议中的一个参数，表示TCP数据包中可以容纳的最大数据量。
>	- MSS通常比MTU小，因为它需要为IP头和TCP头预留空间。
>	- 典型的MSS值为MTU减去IP头和TCP头的大小（通常为40字节）。
>
>MSS和MTU的关系：
>	- MSS = MTU - (IP头 + TCP头)
>	- 例如，如果MTU为1500字节，那么MSS通常为1460字节（1500 - 40）。
>
>这两个参数的设置对网络性能有重要影响。合适的MTU和MSS可以提高网络传输效率，减少分片和重组的开销。

^5a80c7

