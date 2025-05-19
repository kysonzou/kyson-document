---
category:
  - Tech
tags:
  - TCPIP
status: Done
---
[[ssh introduce]]：Secure shell

1. **密码登录**

	```bash
	ssh username@hostname
	#  这是最基本的SSH登录命令
	#  执行后会提示输入密码
	#  username是远程服务器上的用户名
	#  hostname是远程服务器的IP地址或域名
	```

2. **密钥登录**
	```bash
	ssh -i /path/to/private_key username@hostname
	# i 选项指定私钥文件的路径
	# /path/to/private_key 是你的私钥文件位置
	# 使用密钥登录无需输入密码
	# 前提是已将对应的公钥添加到远程服务器的authorized_keys文件中
	```

3. 使用 SSH 配置文件 (可选但强烈推荐)

   为了方便管理多个 SSH 连接，可以创建一个 SSH 配置文件 `~/.ssh/config`。
   编辑该文件，添加类似以下内容：

   ```bash
    Host my-ec2-instance # 自定义的别名，方便你记忆和使用。
        HostName your-ec2-public-ip # 服务器公有 IP 地址或公有 DNS 名称。
        User ec2-user # 用户名。
        IdentityFile /path/to/your/key.pem # 私钥文件的路径。
    ```


Host gcp-instance01
        HostName 35.212.169.9
        User kczou 
        IdentityFile ./.ssh/google_compute_engine 