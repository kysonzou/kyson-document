---
category:
  - Tech
tags:
  - MacOS
status: Done
---



在命令行中，可以通过**环境变量**来传递敏感信息（如密码、API 令牌），避免直接在命令中暴露这些信息。这不仅提高了安全性，也更便于脚本的复用。以下是使用环境变量的常见方法：

#### 1. 在命令行中设置环境变量

可以在命令前设置环境变量，然后在命令中引用它们。例如：
```bash
API_TOKEN="your_api_token_here"

curl -H "Authorization: Bearer $API_TOKEN" https://api.example.com/data
```
在这里，API_TOKEN 是一个环境变量，它包含了 API 令牌的值，$API_TOKEN 表示引用这个变量的值。

#### 2. 使用 export 命令设置环境变量

使用 export 命令可以使环境变量在当前终端会话中生效，适合多个命令共享同一个变量：
```bash
export API_TOKEN="your_api_token_here"

curl -H "Authorization: Bearer $API_TOKEN" https://api.example.com/data

curl -H "Authorization: Bearer $API_TOKEN" https://api.example.com/other-endpoint
```
在此会话中，API_TOKEN 将在所有命令中都可用，直到关闭终端或手动取消（unset API_TOKEN）。

**让终端走代理**
```bash
export http_proxy="http://127.0.0.1:7890" 

export https_proxy="http://127.0.0.1:7890"
```
#### 3. 将环境变量写入文件并读取

可以将环境变量写入文件（例如 .env 文件），然后使用 source 命令加载：

**创建** .env **文件：**

```bash
API_TOKEN=your_api_token_here

USERNAME=your_username_here
```

**加载环境变量：**

```bash
source .env

curl -u "$USERNAME:$API_TOKEN" https://api.example.com/data
```
  
#### 4. 在脚本中引用环境变量

在 Bash 脚本中，可以直接使用环境变量，通过 $变量名 来引用。例如：
```bash
#!/bin/bash

API_TOKEN="your_api_token_here"

curl -H "Authorization: Bearer $API_TOKEN" https://api.example.com/data
```
  
#### 5. 读取用户输入并存入环境变量

如果敏感信息不希望硬编码，可以使用 read 命令从用户输入读取：
```bash
read -sp "Enter API token: " API_TOKEN

curl -H "Authorization: Bearer $API_TOKEN" https://api.example.com/data
```

#### 6. 永久设置环境变量

在 Linux/macOS 上，可以将环境变量添加到 ~/.bashrc、~/.bash_profile 或 ~/.zshrc 文件中，以便每次登录时自动加载。

例如，在 ~/.zshrc中添加：
```bash
export MY_VAR="Hello"

source ~/.zshrc
```

>这里有个很好的例子就是把homebrew二进制程序的路径添加到$Path中
>
>export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"


#### 小结

通过使用环境变量，可以在命令行、脚本、或配置文件中更安全、灵活地处理敏感信息，并简化代码的管理。