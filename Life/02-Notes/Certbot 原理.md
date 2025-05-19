---
category:
  - Tech
tags:
  - Linux
status: Done
---
**Certbot 证书更新原理与方式**

Certbot 是一个用于申请和更新 SSL/TLS 证书的自动化工具，依赖于 **ACME (自动证书管理环境)** 协议。Certbot 更新证书的核心是完成域名的所有权验证。常用的验证方式包括 **HTTP-01 验证** 和 **DNS-01 验证**。

---

### **1. HTTP-01 验证原理**

**HTTP-01 验证** 是 Certbot 的默认验证方式，其原理如下：

1. Certbot 生成一个随机字符串 (**Token**)，用于验证。

2. Certbot 将该 Token 放在域名对应服务器的特定路径上：
   ```
   http://<your-domain>/.well-known/acme-challenge/<Token>
   ```

3. 证书管理机构 Let’s Encrypt 通过 DNS 查询获得域名对应的 IP 地址，然后向该服务器发送 HTTP 请求，查看路径上是否有正确的验证文件。

4. Let’s Encrypt 验证 Token 与您的 ACME 账户签名匹配，如果正确，认为您控制该域名。

5. 验证通过后，Certbot 将继续证书申请或更新。

**适用场景：**适合于能访问 HTTP 服务器的公网域名。

---

### **2. DNS-01 验证原理**

**DNS-01 验证** 是另一种常用的验证方式，通常用于以下场景：
- 申请泛域名证书（如 `*.example.com`）。
- 域名没有 HTTP 公网访问权限。
- 需要为内网域名或私有域名证书。

**验证过程：**

1. Certbot 生成一个挑战字符串 (**Token**)，请您在 DNS 配置中添加一条 `_acme-challenge.<domain>` 的 `TXT` 记录。

2. Let’s Encrypt 通过 DNS 查询验证该 `TXT` 记录是否存在，并确认记录值与记录要求一致。

3. 如果 DNS 配置正确，验证通过，Certbot 将继续处理证书申请或更新。

**适用场景：**
- 需要申请泛域名证书。
- 域名访问带有限制，无法运行 HTTP 服务器。


