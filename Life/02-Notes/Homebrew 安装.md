---
category:
  - Tech
tags:
  - MacOS
status: Done
---
### 一、Homebrew安装

可以在官网直接下载安装包安装，下面介绍的是用命令行安装：

1. 使用官网的安装方法，通过terminal输入以下代码：

    ```bash
    /bin/bash -c "$(curl -fsSL   https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	```

	>[!Tip]- code
	>
	>这条命令是用来安装Homebrew的。让我逐步分析这个命令：
	>
	>1. `/bin/bash`: 这是指定要使用的shell，即Bash shell。
	>
	>2. `-c`: 这个选项告诉Bash从后面的字符串中读取并执行命令，而不是从脚本文件或标准输中读取。
	>
	>3. `"$(...)"`：这是命令替换语法。括号内的命令会被执行，其输出会替换整个 `$()` 表达式。
	>
	>4. `curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh`: 
	> 	  - `curl`: 这是一个用于发送HTTP请求的工具。
	> 	  - `-f`: 静默失败。如果服务器返回错误，curl会静默失败而不是输出错误页面。
	> 	  - `-s`: 静默模式。不显示进度条或错误消息。
	> 	  - `-S`: 与 `-s` 一起使用时，仍然显示错误消息。
	> 	  - `-L`: 如果页面被重定向，跟随重定向。
	> 	  - URL: 指向Homebrew安装脚本的原始GitHub链接。
	>
	>5. 整个命令的作用是：
	>	- 使用curl下载Homebrew的安装脚本。
	>	-将下载的脚本内容通过命令替换传递给Bash。
	>	-Bash执行这个脚本，从而安装Homebrew。
	>
	>简而言之，这个命令会从GitHub下载Homebrew的安装脚本并立即执行它，从而在系统上安装Homebrew包管理器。

    > 若以上安装失败，并提醒：
    > 
    > Failed to connect to raw.githubusercontent.comport 443: Connection refused.
    > 
    > 报错连接不上这个链接
    > 
    > 1. 如果有科学上网，可以在终端配置替换端口后再执行命令，替换成翻墙软件给的端口
    > 
    > 	```bash
    > 	export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890
    > 	```
    > 	后来想想是不是可以直接把这个配置写进～/.zshrc作为终端的全局配置呢？试过了妥妥的ok。
    >
    > 2. 没有科学上网，可以直接配置/etc/hosts文件，将raw.githubusercontent.com直接指向真实IP
    > 	在[ipaddress.com/](https://www.ipaddress.com/)查询 raw.githubusercontent.com 的真实IP 199.232.28.133
    > 	修改hosts，添加如下内容： 199.232.28.133 raw.githubusercontent.com
    > 
    > 3. 用国内的镜像安装源，详情请看[Gitee / CunKai / HomebrewCN](https://link.zhihu.com/?target=https%3A//gitee.com/cunkai/HomebrewCN)

	> [!Note] 安装故事
    Homebrew需要依赖Command Line Tools , 它是Apple提供的一个工具包，里面包含很多系统没有提供的命令程序，比如Git……..，Apple在安装Xcode的时候会默认安装这个工具包的，我的电脑上有两个版本的Xcodel就应该存在两个在对应的Xcode.app/Contents/Developer目录里。在安装Homebrew的时候依然提示需要安装Command Line Tools，貌似它链接不到Xcode自带的工具包，只能在按照它的提示下载，刚好这时候我电脑是Public Bate系统竟然提示系统版本过高安装不了。没办法只能手动下载也是Beta版本的它并安装，默认的目录是 /Library/Developer/CommandLineTools，之后成功安装Homebrew。
    
2. 测试 Homebrew 是否正确安装
    
    ```bash
    brew -v
    ```
    
3. 若上一步输入命令，回车后提示：`brew：command not found`。则需要进行环境配置，若成功则跳过该步骤：
    
    Homebrew基于 ARM 的CLI程序会软链接至 `/opt/homebrew/bin` 目录，这个目录shell不会主动export它，如果是基于inte的CLI 程序会自动软链接至 `/usr/local/bin` 目录，shell会主动export这个目录。
    
    ```bash
    1、在终端通过vim打开～/.zshrc文件，如果没有则新建sudo vim .zshrc
    2、在 .zshrc 文件的末尾添加配置：
    export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"
    3、保存并退出文件
    4、刷新配置文件source ~/.zshrc
    5、再次输入 brew -v 测试
    ```
    
    > 这里看很多资料 export 都是把系统的那几个也加上，其实是不用的，只需要把我们自己需要的路径加上就行
    > 
    > 
    > `PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"`
    > 

### 二、切换Homebrew源

遇到 `brew update` 会卡住的情况，也是因为网络的问题，可以直接切换到国内的源

1. 更换brew.git
    
    ```bash
    git -C "$(brew --repo)" remote set-url origin https://mirrors.ustc.edu.cn/brew.git # 中科大或
    git -C "$(brew --repo)" remote set-url origin https://mirrors.aliyun.com/homebrew/brew.git # 阿里巴巴或
    git -C "$(brew --repo)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git # 清华大学
    ```
	
    ```bash
    //查看源
    git -C "$(brew --repo)" remote get-url origin
    ```
    
2. 更换CLI程序仓库：homebrew-core.git
	
    ```bash
    git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git # 中科大或
    git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.aliyun.com/homebrew/homebrew-core.git # 阿里巴巴或
    git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git # 清华大学
    ```
    
    ```bash
    //查看源
    git -C "$(brew --repo homebrew/core)" remote get-url origin
    ```
    
3. 更换GUI程序仓库：homebrew-cask.git
	
    ```bash
    git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git # 中科大或
    git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.aliyun.com/homebrew/homebrew-cask.git # 阿里巴巴或
    git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask.git # 清华大学
    ```
    
    ```bash
    //查看源
    git -C "$(brew --repo homebrew/cask)" remote get-url origin
    ```
    
4. 配置环境变量：homebrew-bottles
    
    ```bash
    echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.aliyun.com/homebrew/homebrew-bottles' >> ~/.zshrc # 阿里云
    或
    echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles' >> ~/.zshrc # 中科大
    或
    echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/bottles' >> ~/.zshrc # 清华大学
    
    source ~/.zshrc
    ```

	>[!Tip]- code
	>这条命令的目的是将一个环境变量设置添加到 Zsh shell 的配置文件中。让我们逐步分析这个命令：
	>
	>1. `echo`: 这是一个用于在终端输出文本的命令。
	>
	>2. 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.aliyun.com/homebrew/homebrew-bottles': 
	 >	- `export`: 用于设置环境变量。
	 >	- `HOMEBREW_BOTTLE_DOMAIN`: 这是 Homebrew（一个常用的 macOS 包管理器）的一个环境变量。
	 > 	- 等号后面的 URL 是阿里云提供的 Homebrew 镜像源地址。
	 > 	
	>3. `>>`: 这是输出重定向符号，表示将输出追加到指定文件的末尾。
	>
	>4. `~/.zshrc`: 这是 Zsh shell 的用户配置文件路径。
	>	- `~` 表示当前用户的主目录
	>	- `.zshrc` 是 Zsh 的配置文件名
	>
	>整体含义：
	>这个命令将 Homebrew 的瓶装软件（预编译的二进制包）下载源设置为阿里云的镜像。这样做的目的是为了加快 Homebrew 安装软件的速度，特别是对于中国大陆的用户来说，使用国内的镜像源通常会比使用默认的国外源更快。
	>
	>当你运行 Zsh shell 时，它会读取 `.zshrc` 文件并应用其中的设置。这意味着每次你打开新的终端窗口或启动新的 Zsh 会话时，都会使用这个阿里云镜像源来下载 Homebrew 的瓶装软件。

5. 恢复默认源
    
    ```bash
    1. git -C "$(brew --repo)" remote set-url origin https://github.com/Homebrew/brew.git
    2. git -C "$(brew --repo homebrew/core)" remote set-url origin https://github.com/Homebrew/homebrew-core.git
    3. git -C "$(brew --repo homebrew/cask)" remote set-url origin https://github.com/Homebrew/homebrew-cask.git
    4. 删除环境变量 HOMEBREW_BOTTLE_DOMAIN
    5. source ~/.zshrc
    6. brew update
    ```

	>[!Tip]- code
	>这个命令是用来更改 Homebrew 仓库的远程 URL 的。让我们逐步分析这个命令：
	>
	>1. `brew --repo`: 这部分命令会输出 Homebrew 的主仓库路径。
	>
	>2. `"$(brew --repo)"`: 这是命令替换，会将 `brew --repo` 的输出作为一个字符串。
	>
	>3. `git -C "$(brew --repo)"`:  `-C` 选项告诉 git 在执行后面的命令之前，先切换到指定的目录。在这里，它会切换到 Homebrew 的仓库目录。
	>
	>4. `remote set-url origin`: 这是 git 的一个命令，用于设置一个已存在的远程仓库的 URL。
	>	- `remote` 表示我们要操作远程仓库
	>	- `set-url` 表示我们要设置 URL
	>	- `origin` 是远程仓库的默认名称
	>
	>5. `https://github.com/Homebrew/brew.git`:这是新的远程仓库 URL，指向 Homebrew 的官方 GitHub 仓库。
	>
	>综合起来，这个命令的作用是：
	>将 Homebrew 本地仓库的远程 origin 仓库 URL 设置（或重置）为 `https://github.com/Homebrew/brew.git`。
	>
	>这通常用于修复 Homebrew 的更新问题，或者将 Homebrew 重置到官方源。

6. 查看brew源
    
    ```bash
    $ git -C "$(brew --repo)" remote get-url origin
    $ git -C "$(brew --repo homebrew/core)" remote get-url origin
    $ git -C "$(brew --repo homebrew/cask)" remote get-url origin
    ```
