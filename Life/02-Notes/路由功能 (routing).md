---
category:
- Tech
tags:
- Network
status: Done
---



>**[[路由器|路由器]]**：主要功能是路由，即负责在同一类型网络中转发数据，决定数据包的下一跳。

路由是网络中的核心概念，指的是数据从源地址传输到目标地址的路径选择过程。在这一过程中，数据包会经过多个路由器，每个路由器负责决定数据包的下一跳方向。为了确保数据包能够高效传递，路由过程依赖以下关键功能和概念：

1. **路由表**：路由器根据内部的路由表决定数据包的下一跳目标地址。路由表中记录了各种网络目的地的路径信息，帮助路由器找到最优路径。

2. **IP 地址转发**：路由器通过分析数据包中的目标 IP 地址，并根据路由表中的信息，选择合适的路径，将数据包逐步转发到最终目的地。

3. **路由协议**：这是路由过程中的另一重要概念，用于在不同路由器之间交换路由信息，动态更新路由表。路由协议帮助路由器了解网络拓扑的变化，并自动调整路由决策。
	- **路由信息的交换**：通过路由协议，路由器能够共享自己已知的网络路径，保持对整个网络的最新了解。
	- **路径计算和更新**：当网络路径变化时，路由协议自动更新路由表，确保数据包总是通过最佳路径传输。

常见的路由协议分为两类：
- **距离矢量协议**（如 RIP）：基于跳数来计算路径的优劣，适用于小型网络。
- **链路状态协议**（如 OSPF、IS-IS）：每个路由器维护整个网络的拓扑图，基于链路质量选择路径，适合大型网络。

综上所述，路由的核心在于通过路由表进行路径选择和数据包转发，而路由协议则负责动态调整路由表，以适应网络拓扑的变化，确保数据传输的高效和稳定。

>[!Question]- 路由的重点是网络中同一类型网络之间的路径选择和数据包转发。 它的转发也是通过MAC地址的吗?
>**路由器的数据转发**并不是直接通过 **MAC 地址** 来完成的，而是主要通过 **IP 地址** 进行。路由器的工作发生在**网络层**（即 OSI 模型的第三层），而 MAC 地址的使用是在**数据链路层**（第二层）。

>[!question]- 理解了，就是在骨干网络中的路由器是不通过mac地址转发数据的对吧?
>对的，在**骨干网络**中的路由器是不通过 **MAC 地址** 转发数据的。骨干网络的路由器主要是在**网络层（第三层）**工作，**基于 IP 地址**来选择路径并转发数据。
>具体原因：
>
>1. **骨干网络中的路由器处理的是 IP 地址**：路由器根据目标 IP 地址查找其路由表，决定数据包的下一跳位置。IP 地址的作用是在网络层全局唯一标识一台设备或服务器，而路由器根据 IP 地址转发数据包给远程网络中的其他路由器。  
>2. **MAC 地址仅在局域网段（数据链路层）使用**：MAC 地址是一个物理地址，通常仅用于同一个局域网中的通信。当数据包在骨干网络中通过多个路由器转发时，每一跳都不会涉及 MAC 地址。在骨干网络中，数据包是跨多个网络进行传输的，而这些网络可能完全不涉及局域网或链路层的概念。
>
>总结：
>- 在**骨干网络**中，路由器间的通信主要依赖于**IP 地址**来决定下一跳，并进行转发。
>- **MAC 地址只在局域网（如以太网）**的场景中使用，因此在骨干网络中的路由器不依赖 MAC 地址进行数据包的转发。
>
>所以，在大型网络如骨干网中，**MAC 地址没有起到作用**，只有在本地局域网的链路层传输时，MAC 地址才会被使用。

>[!question]- 那我家用理由器下面的两台电脑通信是通过mac地址的吗?
>是的，**在家用路由器下的两台电脑通信**，如果它们在**同一个局域网（LAN）**中，数据的转发确实是通过 **MAC 地址** 来完成的。这是因为在局域网内部，设备之间的通信发生在**数据链路层（第二层）**，这时使用的是 **MAC 地址**，而不是 IP 地址。
>详细解释：
>1. **同一局域网内的通信**：
>	- 在局域网中（例如你家用路由器下的网络），如果两台电脑要相互通信，它们会使用**以太网协议**。以太网协议是在**数据链路层**工作的，依赖的是**MAC 地址**来确定数据包的目标。
>	- 假设两台电脑 A 和 B 都连接到同一个家用路由器，如果 A 需要发送数据给 B：
>		- A 会先通过**ARP（地址解析协议）**来查询 B 的 IP 地址对应的 **MAC 地址**。
>		- A 将数据包封装成一个以太网帧，并将目标 **MAC 地址** 设置为 B 的 MAC 地址。
>		- 家用路由器（或者交换机部分）负责在局域网内找到对应的 MAC 地址，并将数据包转发到目标设备 B。
>
>2. **家用路由器的角色**：
>	- 在这个场景下，家用路由器内的**交换功能**起作用，实际上是像一个**交换机**一样工作，负责根据 **MAC 地址** 在同一个局域网内转发数据。
>	- 家用路由器会查看每个设备的 MAC 地址，并建立一个**MAC 地址表**，以确保正确的设备之间的数据流动。
>
>总结：
>在家用路由器下的局域网中，两台设备之间的通信是通过 **MAC 地址** 完成的，因为这是发生在 **数据链路层** 的通信。在局域网内，IP 地址用于识别设备，但实际的转发是基于 MAC 地址。这种通信方式是在**同一个网络段**中通过以太网协议和 MAC 地址进行的，而不需要路由层的 IP 地址选择。

>[!question]- 那我们家用路由器到外网的数据传输是通过MAC地址还是通过IP的呢?
>家用路由器到外网的数据传输是**通过 IP 地址**完成的，而不是通过 MAC 地址。
>详细解释：
>1. **局域网（LAN）内**：
>	- 在你的家用网络（局域网）内，设备之间的通信通常使用 **MAC 地址**。当你的设备（如电脑、手机等）要和家中的另一台设备通信时，数据包在局域网内的传输是基于 MAC 地址的，这种传输是在**数据链路层（第二层）**进行的。
>
>2. **家用路由器到外网（互联网）**：
>	- 当你要访问互联网时，家用路由器的角色是**路由器和网关**，它负责将你设备发出的数据从局域网转发到外部网络（互联网），这部分工作发生在**网络层（第三层）**，使用的是 **IP 地址**。
>   **流程**：
>	- 当你发送一个数据包到外部（比如访问一个网站），你的设备将数据发送到家用路由器。路由器通过 **NAT（网络地址转换）** 将你设备的**私有 IP 地址**转换为 **公共 IP 地址**，然后将数据包发送到互联网。
>	- 在这个过程中，路由器根据**目标 IP 地址**（如某个网站的 IP 地址）来确定数据包的下一跳，转发给 ISP（互联网服务提供商）。
>	- **骨干网络（互联网）**中的数据传输也是基于 IP 地址的，所有路由器之间的通信依赖于 IP 地址进行路径选择和数据包转发。
>
>3. **MAC 地址的作用范围**：
>	- **MAC 地址**只在**局域网内**（如家中的 Wi-Fi 网络或有线网络）使用，用来标识局域网内的设备。
>	- 当数据包离开你的家用网络并进入互联网时，**MAC 地址不再被使用**。在互联网中，路由器之间依赖 **IP 地址** 进行通信，而不是 MAC 地址。
>	- 数据从路由器到外部网络后，目标设备的 MAC 地址不会在广域网中传递，IP 地址成为主要的路由信息。
>
>总结：
>- 在家用路由器到外网的通信过程中，数据是通过 **IP 地址** 进行传输和路由的，路由器和外部网络的设备（如 ISP 和网站服务器）都依赖于 **IP 地址** 来转发数据包。
>- **MAC 地址** 只在局域网内部用于设备之间的通信，一旦数据离开局域网进入广域网（互联网），就不再使用 MAC 地址，而是基于 **IP 地址** 进行路由。
>
>所以，当家用路由器将数据发送到互联网时，传输和路由过程是通过 **IP 地址** 完成的，而不是通过 MAC 地址。