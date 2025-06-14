---
category:
  - Tech
tags:
  - TCPIP
status: Done
---
### 前言

SSL（Secure Socket Layer 安全套接层）是基于HTTPS下的一个协议加密层，由于HTTPS的推出受到了很多人的欢迎，在SSL更新到3.0时，IETF对SSL3.0进行了标准化，并添加了少数机制（但是几乎和SSL3.0无差异），标准化后的IETF更名为TLS1.0（Transport Layer Security 安全传输层协议），可以说TLS就是SSL的新版本3.1。

> TLS（Transport Layer Security）是更为安全的升级版 SSL（Secure Socket Layer ）  
> TLS（Transport Layer Security）是Secure Socket Layer ）的标准化后的产物

SSL协议位于TCP/IP协议与各种应用层协议之间，为数据通讯提供安全支持。SSL协议可分为两层： 
- SSL记录协议（SSL Record Protocol）：它建立在可靠的传输协议（如TCP）之上，为高层协议提供数据封装、压缩、加密等基本功能的支持。 
- SSL握手协议（SSL Handshake Protocol）：它建立在SSL记录协议之上，用于在实际的数据传输开始前，通讯双方进行身份认证、协商加密算法、交换加密密钥等。

### 1、SSL/TLS的工作原理

SSL/TLS协议主要分为两个部分：**握手过程**和**数据传输过程**。

### 2、握手过程

握手是客户端（如浏览器）和服务器建立安全连接的初始过程，主要步骤包括：

1. **客户端问候**：客户端发送支持的TLS版本、加密算法列表以及随机数。

2. **服务器回应**：服务器选择加密算法、生成随机数并将其证书发送给客户端。

3. **密钥交换**：客户端使用服务器证书中的公钥加密生成的会话密钥，并将其发送给服务器。

4. **完成握手**：双方使用会话密钥加密通信，握手完成。


**握手过程演示：**

![https握手过程](../assets/network-HTTPS-https握手过程.jpg)

在第一次请求时，客户端先去请求服务端的数字证书，并且生成一个随机数R1，将随机数和自己支持的加密算法告诉服务端。

服务端收到客户端的请求后，选择双方共同支持的加密算法，并且生成新的随机数R2，将服务器的数字证书及加密算法、随机数一并返回给客户端。

客户端收到服务端的数字证书，然后判断数字证书的完整性和合法性，从而确保通信安全。然后生成新的随机数R3，使用服务端的公钥对随机数R3进行加密后返回给服务端并将随机数R1、R2、R3组合成一串密钥用作对称加密用。

服务端收到客户端加密后的随机数R3，使用自己的私钥对密文进行解密获取到随机数R3，组合R1、R2、R3获取到一串密钥(和客户端一致)；然后开始使用对称加密进行通信。

上述就是HTTPS对密钥协商的过程，由于非对称加密一方密匙加密后只能使用另一方密匙解密，所以在前两次数据传输中即使被窃听也不怕，因为在第三次传递随机数R3时是使用公钥加密的，只有服务端的私钥才能解密，从而确保密钥的安全性。

合法性：通过数字证书来确定

完整性、安全性：因为通过非对称加密协商对称加密密钥，所以对称加密密钥是没有在互联网中暴漏过的，所以第三方是很难破解数据和篡改数据的

### 3、数据传输过程

完成握手后，客户端和服务器使用会话密钥进行加密数据传输。数据传输分为两步：

1. **数据加密**：使用对称加密算法（如AES、ChaCha20）加密要传输的数据。

2. **完整性校验**：传输的数据附带哈希校验值，以便接收方校验数据完整性。（这一步加入会话密钥，确保数据的完整性，确保即使数据被篡改也不可能生成合法的哈希校验值，因为没有会话密钥）
  
### 4、SSL/TLS加密技术

SSL/TLS使用两种主要的加密技术来保护数据：

1. **对称加密**：在通信双方之间使用相同的密钥加密和解密数据。它速度快，适合大量数据传输。

2. **非对称加密**：使用公钥和私钥加密和解密数据。非对称加密主要在握手过程中使用，确保密钥交换的安全。

### 5、SSL/TLS证书

[[TSLSSL证书]]由受信任的证书颁发机构（CA）颁发，用于验证服务器身份。证书包括服务器的公钥、签名和一些信息（如域名、有效期等）。在浏览器和服务器通信中，证书确保客户端信任该服务器，防止中间人攻击。

>[!question]- 服务器和客户端之间的通信会通过证书进行加密，确保第三方无法窃听或篡改数据。 这一点是怎么做到的?
>服务器和客户端之间的通信通过证书进行加密，确保第三方无法窃听或篡改数据的过程，是基于**公钥加密**（Asymmetric Encryption）和**对称加密**（Symmetric Encryption）的结合来实现的。以下是具体的步骤：
>
>**1. 公钥加密的初始握手阶段**
>
>当客户端（例如浏览器）与服务器建立安全连接时，首先通过**公钥加密**来安全地交换加密密钥。
>
>1.1 **服务器发送 SSL/TLS 证书**：
>  - 当客户端请求建立 HTTPS 连接时，服务器会发送它的 SSL/TLS 证书给客户端。
>  - 这个证书中包含了服务器的**公钥**，用于后续的加密操作。
>
>1.2 **验证证书**：
>  - 客户端通过内置的根证书链，验证服务器的证书是否由受信任的证书颁发机构（CA）签发。
>  - 如果验证通过，客户端继续通信；如果证书无效，客户端会提示用户连接不安全。
>
>1.3 **生成对称加密密钥**：
>  - 客户端生成一个**随机的对称加密密钥**（即会话密钥），并使用服务器的公钥对这个密钥进行加密。
>  - 由于服务器拥有对应的**私钥**，只有服务器可以解密这个加密的对称密钥。
>
>1.4 **交换加密密钥**：
>  - 客户端将加密后的对称密钥发送给服务器。
>  - 服务器使用它的私钥解密，获得该对称密钥。
>
>**2. 对称加密的安全通信阶段**
>
>一旦服务器和客户端都拥有相同的对称加密密钥，接下来的通信将使用**对称加密**，这提高了传输效率，并且保证了数据的保密性和完整性。
>
>2.1 **对称加密通信**：
>  - 双方使用相同的对称密钥对数据进行加密和解密。
>  - 例如，客户端发送的每个请求都会使用这个对称密钥加密，服务器接收到加密的数据后，再用同样的密钥解密。
> 
>2.2 **确保数据保密性**：
>  - 对称加密可以确保即使第三方（如中间人）截获了加密的数据包，没有正确的密钥就无法解密，因此通信内容保持保密。
>
>2.3 **确保数据完整性**：
>  - 通信过程中，还会通过**消息认证码（MAC）** 或哈希函数来验证数据的完整性。这样可以确保传输过程中的数据未被篡改。
>
>**3. 防止第三方窃听和篡改**
>
>由于只有服务器和客户端拥有对称密钥，第三方即使截获了加密的通信数据也无法解密。此外，通过对数据包的完整性检查，确保了任何篡改的数据包都会被识别为无效。
>
> - **防止窃听**：
>   - 第三方无法获得对称密钥，也无法通过暴力破解获得加密的数据内容，因此实现了防窃听。
>
> - **防止篡改**：
>   - 数据传输时，每个数据包都会带有哈希值，确保数据未被修改。篡改的数据包在解密或哈希验证时会被检测到，从而被拒绝处理。
>
>总结
>
>SSL/TLS 协议的整个过程利用了**公钥加密**来安全地交换对称加密密钥，再利用**对称加密**进行高效、安全的数据传输。正是这种结合，确保了通信的保密性和数据的完整性，防止了第三方窃听和篡改。

### 6、SSL/TLS的优势

1. **加密通信**：防止第三方窃听传输内容，保护用户隐私。

2. **身份验证**：通过证书验证服务器身份，避免用户访问伪造网站。

3. **数据完整性**：传输的数据附带完整性校验，防止数据被篡改。（哈希值计算的时候加入会话密钥）

### 7、SSL/TLS的应用

SSL/TLS主要用于以下领域：

1. **HTTPS**：保护网站的HTTP传输，确保用户浏览网页的安全性。

2. **电子邮件**：用于保护SMTP、POP3、IMAP等协议下的电子邮件通信。

3. **VPN**：用于保护VPN的通信内容，增强企业或个人的网络安全性。

总之，SSL和TLS是网络安全的重要组成部分，确保了在不安全网络上的安全数据传输。目前，TLS已经成为主要的加密协议，随着版本的升级不断增强网络安全性。