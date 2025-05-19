---
category:
  - Tech
tags:
  - MacOS
status: Done
---
在 macOS 中，有几个主要的环境变量文件可以用来设置和管理用户的环境变量。不同的文件适用于不同的 shell 和场景，以下是一些常见的环境变量文件及其用途：

#### **1. /etc/profile**

- **系统级别的配置文件**，适用于所有用户。

- 在登录时加载，通常包含系统范围的环境变量。

- 文件路径：/etc/profile

#### **2. /etc/paths**

- 也是一个系统级文件，专门用于定义 PATH 环境变量（可执行文件的搜索路径）。

- 每行包含一个目录路径，macOS 会将这些目录添加到所有用户的 PATH 中。

- 文件路径：/etc/paths

#### **3. 用户级别的环境变量文件**

##### 3.1 ~/.bash_profile

- 在用户登录 Bash shell 时执行，适用于当前用户。

- 常用于设置用户的自定义环境变量或配置 PATH。

- 如果文件不存在，可以手动创建。

- 文件路径：~/.bash_profile

##### 3.2 ~/.bashrc

- 每次启动新的 Bash shell（非登录 shell）时都会执行，比如打开新的终端窗口。

- 通常将别名和函数等配置放在 ~/.bashrc 中，以便每次启动新的 shell 时都加载这些设置。

- 在 ~/.bash_profile 中可以添加一行 source ~/.bashrc，确保每次登录 shell 时也加载 ~/.bashrc 的内容。

- 文件路径：~/.bashrc

  
##### 3.3 ~/.zshrc

- macOS Catalina 及以后的版本默认使用 zsh（而不是 bash）作为默认 shell。

- ~/.zshrc 是 Zsh shell 的配置文件，会在每次启动新的 Zsh shell 时执行。

- 可以在这里添加环境变量、自定义 PATH 和其他配置。

- 文件路径：~/.zshrc

##### 3.4 ~/.zprofile

- 适用于 Zsh 的登录 shell 配置文件，只在用户登录时加载一次。

- 类似于 Bash 的 ~/.bash_profile。

- 可以在这里配置只需在登录时加载的变量。

- 文件路径：~/.zprofile

##### 3.5 ~/.profile

- 是一个更通用的配置文件，支持多种 shell（包括 sh、bash 和 zsh）。

- 通常用于定义环境变量。~/.profile 会在登录时加载，适用于兼容性需求。

- 如果系统检测到 ~/.bash_profile 存在，~/.profile 不会自动加载。

- 文件路径：~/.profile

##### 3.6 临时设置环境变量

- 临时环境变量可以在当前终端会话中通过 export 命令设置，退出会话后会自动失效：
   ```bash
   export MY_VAR="value"
   ```

##### 3.7 按需创建 .env 文件

- 对于需要存储敏感信息（如 API 密钥、数据库密码）的项目，可以在项目目录中创建 .env 文件。

- 在开发环境中加载 .env 文件以配置应用程序的运行环境。
   ```bash
   source .env
   ```

#### 4 总结

在 macOS 上，~/.bash_profile、~/.bashrc（适用于 Bash 用户）、~/.zshrc（适用于 Zsh 用户）是最常用的环境变量文件。对于全局设置，可以使用 /etc/profile 或 /etc/paths。根据所用的 shell 和设置需求选择合适的文件，可以灵活配置和管理环境变量。