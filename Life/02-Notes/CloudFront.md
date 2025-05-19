---
category:
  - Tech
tags:
  - Cybersecurity
status: Done
---
**CloudFront 的工作逻辑**

1. **与源服务器的通信：**

    - CloudFront 需要您在配置中明确指定源服务器（源域名或 IP 地址）。如果您提供的是域名，CloudFront 会在需要时通过 DNS 系统解析这个域名得到对应的 IP 地址，然后与源服务器建立连接。
    - 这种逻辑是“**被动使用 DNS**”：CloudFront 并不接管 DNS 系统，只是通过常规 DNS 解析获取源服务器的 IP。

2. **独立于 DNS 设置：**

    - 您不需要修改域名的 DNS 设置。CloudFront 的分配域名（例如 xxxxxx.cloudfront.net）直接由 AWS 提供并解析到最近的边缘节点。
    - 如果您有自己的自定义域名（如 example.com），只需要将您的域名 CNAME 解析到 xxxxxx.cloudfront.net 即可。

3. **与源服务器的独立性：**

    - 源服务器的地址或 IP 不依赖于 CloudFront，它可以是任何支持 HTTP/HTTPS 的服务器（包括 AWS S3、Lightsail 实例、第三方服务器等）。

> [!note]- CloudFront和CloudFlare工作逻辑对比
> 
> **Cloudflare 的工作逻辑**
>
> 1. **DNS 托管：**
>
>    - Cloudflare 要求用户将域名的 DNS 服务器设置为 Cloudflare 提供的服务器（例如 ns1.cloudflare.com 和 ns2.cloudflare.com）。这样，所有针对该域名的请求都会先经过 Cloudflare 的网络。
>
>    - Cloudflare 在其网络中决定如何处理请求（缓存、转发、拦截等）。
>
>2. **完全接管 DNS：**
>
>    - 因为 DNS 已经完全托管在 Cloudflare，因此它可以精确地控制流量的路由逻辑，例如：是否直接命中缓存、 是否转发请求到源服务器、 是否应用 DDoS 防护或其他规则。
>
>3. **DNS 解析和通信整合：**
>
>    - Cloudflare 同时充当 DNS 服务和 CDN，这意味着请求在进入 Cloudflare 时，DNS 解析和内容分发都由它控制。

> CloudFront在创建的时候已经通过提供的源服务器域名解析得到了源服务器IP，以后通过CloudFront像源服务器的请求是不会再做DNS解析的，所以在得到分配的域名以后，就可以在主域名的DNS服务器中将原来主域名指向源服务器IP的A记录删除，把主域名直接用CNAME记录指向CloudFront分配的域名就可以了，然后正常使用主域名，只是这样所有的请求就都要通过CloudFront了