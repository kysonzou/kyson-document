---
category:
- Tech
tags: null
status: Done
---



RESTFUL API（全称Representational State Transfer API）是一种基于HTTP协议的Web API设计架构，允许不同的应用程序通过网络进行数据交换和通信。RESTFUL API的设计遵循REST（Representational State Transfer）的原则，是一种轻量级、无状态的架构风格，特别适合于分布式系统中的服务交互。

**RESTFUL API的主要特点：**

1. **资源（Resource）**  
   RESTFUL API将一切可以访问的对象（如用户、商品、订单等）抽象为资源。每个资源通过URI（Uniform Resource Identifier）唯一标识，如`https://api.example.com/users`可以表示一个用户资源。

2. **无状态（Stateless）**  
   RESTFUL API是无状态的，即服务器不存储客户端的状态信息。每次请求都是独立的，客户端需要在每次请求中提供必要的状态信息（如认证信息），以便服务器正确处理请求。

3. **使用标准的HTTP方法**  
   RESTFUL API使用HTTP协议的标准方法来操作资源：

      - GET：用于获取资源
      - POST：用于创建资源
      - PUT：用于更新资源
      - DELETE：用于删除资源

4. **数据格式**  
   通常使用JSON格式来传输数据，也支持XML等其他格式。JSON格式的轻量级特点使得它更适合网络传输。

5. **统一接口**  
   RESTFUL API设计需要保持接口的统一性，包括资源路径的命名规则、请求方法的使用等，使API易于理解和使用。

**例子**  
假设有一个提供用户信息的API：

- 获取用户列表：GET https://api.example.com/users

- 获取指定用户信息：GET https://api.example.com/users/{id}

- 创建新用户：POST https://api.example.com/users

- 更新用户信息：PUT https://api.example.com/users/{id}

- 删除用户：DELETE https://api.example.com/users/{id}

这种结构简洁明了，遵循HTTP方法和REST原则，是RESTFUL API的典型设计方式。