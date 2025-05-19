---
category:
  - Tech
tags:
  - TCPIP
status: Done
---
- HTTP请求报文由 请求行、请求头、空行、请求数据 4个部分组成
- HTTP响应报文由 状态行、响应头、空行、响应正文 4个部分组成
- HTTP协议明文传输，数据容易泄漏，HTTPS则为数据加密传输
- GET的参数写在URL，没有Body；POST的参数不写在URL，写在Body；**这个只是约定，并不是HTTP的协议内容**，实际上GET参数写在Body，POST参数写在URL只要服务器支持也行

### 一、HTTP协议

HTTP协议是Hyper Text Transfer Protocol（超文本传输协议）的缩写,是用于从万维网（WWW:World Wide Web ）服务器传输超文本到本地浏览器的传送协议。

HTTP是一个基于TCPIP协议栈来传递数据（HTML 文件, 图片文件, 查询结果等）。

HTTP（Hypertext Transfer Protocol）本质上就是一个TCP连接，只不过协议规定了使用==80端口==，以及发送命令或数据的格式，而TCP本身是没有加密的功能。致命的是，HTTP在数据传输过程中，数据就是以明文的方式传输的，由于数据没有被加密，所以很容易出现数据窃听、篡改或者是身份伪造的不安全的行为。

### 二、HTTP特点

- HTTP是无连接：无连接的含义是限制每次连接只处理一个请求。服务器处理完客户的请求，并收到客户的应答后，即断开连接。采用这种方式可以节省传输时间。
- HTTP是媒体独立的：这意味着，只要客户端和服务器知道如何处理的数据内容，任何类型的数据都可以通过HTTP发送。客户端以及服务器指定使用适合的MIME-type内容类型。
- HTTP是无状态：HTTP协议是无状态协议。无状态是指协议对于事务处理没有记忆能力。缺少状态意味着如果后续处理需要前面的信息，则它必须重传，这样可能导致每次连接传送的数据量增大。另一方面，在服务器不需要先前信息时它的应答就较快。

### 三、HTTP请求方法

HTTP1.0 定义了三种请求方法： GET, POST 和HEAD 方法

HTTP1.1 新增了六种请求方法：OPTIONS、PUT、PATCH、DELETE、TRACE 和CONNECT 方法

| 方法    | 描述                                                         |
| ------- | ------------------------------------------------------------ |
| GET     | 幂等，用于获取资源，请求指定页面，并返回实体主体             |
| HEAD    | 幂等，类似于GET请求，但是不不返回实体主体                    |
| POST    | 非幂等，用于提交请求，可以更新或者创建资源                   |
| PUT     | 幂等，用于向指定的URL传送更新或者创建资源，前端需提供完整字段 |
| PATCH   | 幂等，请求是一个局部更新，后端仅更新接收到的字段。           |
| DELETE  | 幂等，请求服务器删除指定的页面                               |
| CONNECT | HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器       |
| OPTIONS | 允许客户端直接查看服务器的性能                               |
| TRACE   | 回显服务器收到的请求，主要用于测试或者诊断                   |

> 幂等：在编程中一个幂等操作的特点是其任意多次执行所产生的影响均与一次执行的影响相同。

POST、PUT、PATCH这三者都有更新的功能，区别就是：

PATCH：是局部更新，后端仅更新接收到的字段。<br>PATCH：幂等的，如果每次提交相同的内容，结果是一致的。比如：在某个特别的页面里只能修改userName，就可以使用PATCH做局部更新

PUT：虽然也是更新资源，但要求前端提供的一定是一个完整的资源对象，不然缺了的那些字段应该被清空。  
PUT：幂等的，如果每次提交相同的内容，结果是一致的。比如：一个接口的功能是将当前余额减一个值，每次提交指定该值为100，这个时候如果连续用PUT掉用（提交的内容一样），那结果只会减100.

POST：个人理解好像也是可以局部更新的回想以前使用的API<br>POST：非幂等的，如果每次提交相同的内容，结果可能不一致的。比如：一个接口的功能是将当前余额减一个值，每次提交指定该值为100，这个时候如果连续用POST掉用（提交的内容一样），那每次结果都减100.

> POST和PUT的区别容易被简单地误认为 “POST表示创建资源，PUT表示更新资源“ ，但实际上两者都可以用来创建或是更新数据，单从技术上来说,他们并没有什么区别。他们的区别主要体现在PUT是幂等的，而POST是非幂等的。

### 四、HTTP请求消息

一个HTTP请求报文由请求行（request line）、请求头（header）、空行和请求数据4个部分组成，下图给出了请求报文的一般格式。

![HTTP请求消息](../assets/network-HTTP-HTTP请求消息.png)

#### 4.1 请求行

请求行（Request Line）由请求方法字段、URL字段和HTTP协议版本字段3个字段组成，它们用空格分隔。例如<br>GET  /index.html  HTTP/1.1。

#### 4.2 请求头

请求头部（Request Header）由关键字/值对组成，每行一对，关键字和值用英文冒号“:”分隔。请求头部通知服务器有关于客户端请求的信息，典型的请求头有：

- User-Agent：产生请求的浏览器类型。
- Host：请求的主机名，允许多个域名同处一个IP地址，即虚拟主机。
- Accept：客户端可识别的内容类型列表。
- Accept-Language：客户端可识别的语言
- Accept-Encoding：客户端可识别的编码（压缩）方式（gzip、deflate...）
- Accept-Charset：客户端可识别的字符集（Unicode(uff-8、utf-16...)、ASCII、GB2312、BIG5、GB18030...）
- Connection：控制网络连接是否保持打开状态（keep-alive、close...）
- Cookie：向服务器发送Cookie
- Content-Type：请求数据的类型（text/html、charset=utf-8、application/json、multipart/form-data、application/x-www-form-urlencoded、boundary=something、[......](https://www.runoob.com/http/http-content-type.html)）
- Content-Length：请求数据的长度
- [Request Header More](https://cloud.tencent.com/developer/section/1189914)

#### 4.3 空行

最后一个请求头之后是一个空行，发送回车符和换行符，通知服务器以下不再有请求头。

#### 4.4 请求数据

请求数据（Request Body）不在GET方法中使用，而是在POST方法中使用

#### 4.5 示例

**GET**
```text
//请求首行，参数放在url中
GET /search?hl=zh-CN&source=hp&q=domety&aq=f&oq= HTTP/1.1

//请求头信息

Host: localhost  //主机名

User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0 //客户端类型

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 //客户端可识别的内容类型
//q被称为相对品质因子，范围 0 =< q <= 1，q 值越大，请求越倾向于获得其“;”之前的类型表示的内容，若没有指定 q 值，则默认为1，若被赋值为0，则用于提醒服务器哪些是浏览器不接受的内容类型
//text/html： 默认q=1
//application/xhtml+xml： 默认q=1
//application/xml： 指定q=0.9
//*/*：任意类型，指定q=0.9
//所以上面的倾向值排序就是：text/html、application/xhtml+xml、application/xml、*/*

Accept-Language: zh-cn,zh;q=0.5 //客户端可识别的语言
//zh-cn：默认q=1
//zh：指定q=0.5

Accept-Encoding: gzip, deflate //客户端可识别的压缩方式

Accept-Charset: GB2312,utf-8;q=0.7,*;q=0.7 //客户端可识别的字符集
//GB2312：默认q=1
//utf-8：指定q=0.7
//*：任意类型，指定q=0.7

Connection: keep-alive //连接状态

Cookie: JSESSIONID=369766FDF6220F7803433C0B2DE36D98 //告诉服务器客户端的Cookie

//空行

//因为GET没有正文，所以下面为空 [可选]
```

**POST**
```text
// 请求首行

POST /hello/index.jsp HTTP/1.1

//请求头信息

Host: localhost //主机名

User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0 //客户端信息

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 //客户端可识别的内容

Accept-Language: zh-cn,zh;q=0.5 //客户端可识别的语言

Accept-Encoding: gzip, deflate //客户端可识别的压缩方式

Accept-Charset: GB2312,utf-8;q=0.7,*;q=0.7 //客户端可识别的字符集

Connection: keep-alive //连接状态

Referer: http://localhost/hello/index.jsp //不知道啥意思

Cookie: JSESSIONID=369766FDF6220F7803433C0B2DE36D98 //告诉服务器客户端的Cookie

Content-Type: application/x-www-form-urlencoded //请求数据的类型为Key=Value形式

Content-Length: 14 //请求数据长度

// 这里是空行

//POST有请求正文

username=hello //正文
```

### 五、HTTP响应消息

HTTP响应也由三个部分组成，分别是：状态行、响应头、空行、响应正文。

![HTTP响应消息](../assets/network-HTTP-HTTP响应消息.jpeg)

#### 5.1 状态行

状态行（Statue Line）格式如下

>HTTP-Version  Status-Code  Reason-Phrase  CRLF 

HTTP-Version：表示服务器HTTP协议的版本，
Status-Code：表示服务器发回的响应状态代码，
Reason-Phrase：表示状态代码的文本描述。

HTTP状态码的英文为HTTP Status Code。状态代码由三位数字组成，第一个数字定义了响应的类别，且有五种可能取值：

- 1xx：指示信息--表示请求已接收，继续处理。
- 2xx：成功--表示请求已被成功接收、理解、接受。
- 3xx：重定向--要完成请求必须进行更进一步的操作。
- 4xx：客户端错误--请求有语法错误或请求无法实现。
- 5xx：服务器端错误--服务器未能实现合法的请求。

常见状态代码、状态描述的说明如下。

- 200 OK：客户端请求成功。
- 400 Bad Request：客户端请求有语法错误，不能被服务器所理解。
- 401 Unauthorized：请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用。
- 403 Forbidden：服务器收到请求，但是拒绝提供服务。
- 404 Not Found：请求资源不存在，举个例子：输入了错误的URL。
- 500 Internal Server Error：服务器发生不可预期的错误。
- 503 Server Unavaiable：服务器当前不能处理客户端的请求，一段时间后可能恢复正常。
- [更多状态码](https://www.runoob.com/http/http-status-codes.html)

#### 5.2 响应头

请求头部（Reponse Header）由关键字/值对组成，每行一对，关键字和值用英文冒号“:”分隔，典型的响应头有：

- Allow：服务器支持哪些请求方法（如GET、POST等）。
- Content-Encoding：文档的编码方法（gzip、deflate...）。只有在解码之后才可以得到Content-Type头指定的内容类型。
- Content-Type：表示后面的文档属于什么MIME类型（text/html、charset=utf-8、application/json、multipart/form-data、application/x-www-form-urlencoded、boundary=something、[......](https://www.runoob.com/http/http-content-type.html)）
- Content-Length：表示内容长度。只有当浏览器使用持久HTTP连接时才需要这个数据。（猜测是设置请求头CONNECTION为keep-alive ）
- Set-Cookie：设置和页面关联的Cookie
- [Response Header More](https://www.runoob.com/http/http-header-fields.html)

#### 5.3 空行

#### 5.4 响应数据

服务器返回的数据，一般都有json、xml等格式

#### 5.5 示例

暂时没有示例

### 六、GET&POST

GET 和 POST，两者是 HTTP 协议中发送请求的方法

`GET`方法请求一个指定资源的表示形式，使用GET的请求应该只被用于获取数据

`POST`方法用于将实体提交到指定的资源，通常导致在服务器上的状态变化或**副作用**

本质上都是 TCP 链接，并无差别

但是由于 HTTP 的规定和浏览器/服务器的限制，导致他们在应用过程中会体现出一些区别

#### 6.1 区别

从`w3schools`得到的标准答案的区别如下：

- GET在浏览器回退时是无害的，而POST会再次提交请求。
- GET产生的URL地址可以被Bookmark，而POST不可以。
- GET请求会被浏览器主动cache，而POST不会，除非手动设置。
- GET请求只能进行url编码，而POST支持多种编码方式。
- GET请求参数会被完整保留在浏览器历史记录里，而POST中的参数不会被保留。
- GET请求在URL中传送的参数是有长度限制的，而POST没有。
- 对参数的数据类型，GET只接受ASCII字符，而POST没有限制。
- GET比POST更不安全，因为参数直接暴露在URL上，所以不能用来传递敏感信息。
- GET参数通过URL传递，POST放在Request body中

##### 6.1.1 参数位置

貌似从上面看到`GET`与`POST`请求区别非常大，但两者实质并没有区别

无论 `GET `还是 `POST`，用的都是同一个传输层协议，所以在传输上没有区别

当不携带参数的时候，两者最大的区别为第一行方法名不同

> POST /uri HTTP/1.1 \r\n
>
> GET /uri HTTP/1.1 \r\n

当携带参数的时候，我们都知道`GET`请求是放在`url`中，`POST`则放在`body`中

`GET` 方法简约版报文是这样的

```text
GET /index.html?name=qiming.c&age=22 HTTP/1.1
Host: localhost
```

`POST `方法简约版报文是这样的

```text
POST /index.html HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded

name=qiming.c&age=22
```

注意：**这里只是约定，并不属于`HTTP`规范**，相反的，我们可以在`POST`请求中`url`中写入参数，或者`GET`请求中的`body`携带参数

##### 6.1.2 参数长度

`HTTP `协议没有`Body`和 `URL` 的长度限制，对 `URL `限制的大多是浏览器和服务器的原因

服务器处理长` URL` 要消耗比较多的资源，为了性能和安全考虑，会给 `URL` 长度加限制

##### 6.1.3 安全

`POST `比` GET` 安全，因为数据在地址栏上不可见

然而，从传输的角度来说，他们都是不安全的，因为` HTTP` 在网络上是明文传输的，只要在网络节点上捉包，就能完整地获取数据报文

只有使用`HTTPS`才能加密安全

##### 6.1.4 数据包

对于`GET`方式的请求，浏览器会把`http header`和`data`一并发送出去，服务器响应200（返回数据）

对于`POST`，浏览器先发送`header`，服务器响应100 `continue`，浏览器再发送`data`，服务器响应200 ok

并不是所有浏览器都会在`POST`中发送两次包，`Firefox`就只发送一次

### 参考

[http请求头和响应头](https://www.cnblogs.com/lauhp/p/8979393.html)

[get和post的区别](https://github.com/febobo/web-interview/issues/145)

[cookie维基百科](https://zh.m.wikipedia.org/zh-hans/Cookie#属性)

[你对cookie了解多少](https://juejin.cn/post/6847902220227182606)