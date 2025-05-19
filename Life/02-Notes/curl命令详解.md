---
category:
  - Tech
tags:
  - Linux
  - MacOS
status: Done
---
curl 是一种强大且灵活的命令行工具，用于在命令行环境下与网络进行交互。它可以通过多种协议（如 HTTP、HTTPS、FTP、SMTP、IMAP 等）传输数据，是网络请求和自动化脚本中的常用工具。以下是对 curl 的详细介绍，包括它的基本用法、高级选项、常见应用场景以及一些最佳实践。

### 一、curl 的基本用法

1. **基本语法**：
   ```bash
   curl [options] [URL]
   ```

   • URL：指定访问的目标 URL，curl 会默认使用 HTTP 协议。
   
   • options：用于指定请求类型、头信息、数据格式等内容，控制请求的行为。

  
2. **简单请求示例**：
   ```bash
   curl http://example.com
   ```

   上述命令请求 http://example.com 并将服务器返回的数据打印到终端。

   
### 二、curl 的常用选项

#### 2.1. 指定请求类型

• **GET 请求（默认）**：
```bash
curl https://www.google.com
```

• **POST 请求**：发送数据到服务器
```bash
curl -X POST -d "param1=value1&param2=value2" http://example.com
```
-X 指定请求类型为 POST  
-d 指定发送的数据。数据格式可以是 URL 编码、JSON 或其他格式。

• **PUT 请求**：
```bash
curl -X PUT -d "param=value" http://example.com/resource
```
  
• **DELETE 请求**：
```bash
curl -X DELETE http://example.com/resource
```
  
#### 2.2. 指定请求头

**• 使用 -H 选项可以自定义请求头：**
```bash
curl -H "Content-Type: application/json" -H "Authorization: Bearer <token>" http://example.com
```

#### 2.3. 发送数据

• **表单数据**：通过 -d 选项发送表单数据，默认使用 application/x-www-form-urlencoded 编码
```bash
curl -d "name=John&age=30" http://example.com/form
```

• **JSON 数据**：需要手动设置请求头的 Content-Type
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"John","age":30}' http://example.com/api
```

#### 2.4. 保存响应输出

**• 将响应保存到文件中：**
```bash
curl -o output.html http://example.com
```
-o 用于指定保存的文件名。

**• 将响应保存到文件并保留文件名：**
```bash
curl -O http://example.com/file.txt
```
-O 会自动将下载内容保存为 URL 中的文件名（如 file.txt）。

#### 2.5. 显示响应头

• **显示响应头信息**：使用 -I 或 --head
```bash
curl -I http://example.com
```
  
• **包含头部和正文**：使用 -i
```bash
curl -i http://example.com
```

#### 2.6. 跟踪重定向

**• 使用 -L 选项，curl 将自动跟随 HTTP 重定向。**
```bash
curl -L http://example.com
```
  
#### 2.7. 添加超时

• **连接超时**：设置连接的超时时间（单位秒）
```bash
curl --connect-timeout 10 http://example.com
```

• **最大执行时间**：设置请求的总超时时间（单位秒）
```bash
curl -m 30 http://example.com
```
  
#### 2.8. 用户名和密码认证

• **基本认证**：
```bash
curl -u username:password http://example.com

curl -user username:password http://example.com
```

• **令牌认证**：
```bash
curl -H "Authorization: Bearer <token>" http://example.com
```
  
#### 2.9. 代理设置

**• 使用 -x 或 --proxy 选项可以设置代理服务器。**
```bash
curl -x http://proxyserver:port http://example.com
```
  
#### 2.10. SSL/TLS 安全选项

• **忽略 SSL 证书错误**：
```bash
curl -k https://example.com
```
-k 忽略 SSL 证书校验，适用于自签名证书的开发环境。

• **指定 SSL 证书**：
```bash
# 这种配置通常用于双向 TLS/SSL 认证
curl --cert /path/to/cert.pem --key /path/to/key.pem https://example.com
```
**cert.pem**：这个文件包含客户端的证书（包括公钥），通常由认证机构（CA）签发。  
**key.pem**：这个文件包含与证书配对的**私钥**，只能由客户端自己保管，确保不会泄露。

### 三、curl 的常见应用场景

#### 3.1. API 调试

curl 是测试和调试 REST API 请求的常用工具，通过设置请求方法、头部信息和请求数据，可以方便地向 API 服务器发送请求并查看响应。
```bash
curl -X GET http://api.example.com/data
```
  
#### 3.2. 网站性能测试

使用 curl 获取响应时间或下载速度，便于对网站性能进行测试：
```bash
curl -w "Time_Total: %{time_total}\n" -o /dev/null -s http://example.com
```
-w 可以输出不同指标（如总时间 time_total、连接时间 time_connect 等）。

#### 3.3. 批量下载文件

可以将 curl 集成到脚本中，进行批量下载。例如下载文件列表中的所有文件：
```bash
for url in $(cat urls.txt); do

  curl -O $url

done
```
  
#### 3.4. 模拟浏览器行为

通过 -A 选项设置 User-Agent，curl 可以模拟浏览器发送的请求。
```bash
curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" http://example.com
```
  
#### 3.5. 网络故障排查

curl 能帮助用户快速测试是否能访问某个 URL，排查网络连接问题或验证域名解析情况。
  
### 四、curl 的高级功能

#### 4.1. cookie 支持

• **发送 cookie**：可以使用 -b 选项向服务器发送 cookie 信息
```bash
curl -b "name=value" http://example.com
```
  
• **保存和加载 cookie**：curl 可以将 cookie 保存到文件中并在后续请求中加载
```bash
curl -c cookies.txt http://example.com     # 保存

curl -b cookies.txt http://example.com     # 加载
```
  
#### 4.2. 复杂的 POST 请求

**• 支持发送文件数据，模拟文件上传**
```bash
curl -F "file=@/path/to/file" http://example.com/upload
```

#### 4.3. 重试机制

**• 使用 --retry 选项可以设置失败时自动重试的次数**
```bash
curl --retry 5 http://example.com
```
  
#### 4.4. 执行自定义命令

**• 在 curl 请求中执行脚本或命令后输出结果。**
```bash
curl http://example.com -o output.txt && bash output.txt
```

### 五、最佳实践

1. **安全性**：避免在命令行中直接写明敏感信息（如密码或 API 令牌），使用环境变量代替。

2. **超时控制**：设置合理的连接和请求超时时间，避免请求因网络原因无限制地挂起。

3. **日志和调试**：使用 -v 或 -w 来查看详细信息，帮助定位问题。

4. **自动化脚本**：在脚本中使用 curl，特别是 API 调用和下载任务中，简化工作流程并提高效率。

  
### 六、总结

curl 是一个强大且灵活的命令行工具，能够执行各种网络请求和数据传输操作。它的高可配置性、跨平台支持和广泛的应用场景使其在网络调试、自动化脚本、API 调试和测试中发挥着重要作用。