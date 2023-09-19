### 什么是Homebrew？

[Homebrew ](https://brew.sh/index_zh-cn.html)官网有一句话：Homebrew complements macOS. （ Homebrew 使 macOS 更完整。）Homebrew 是 macOS 的套件管理工具，是高效下载软件的一种方法，相当于 Linux 下的 `yum`、`apt-get` 神器，用于下载存在依赖关系的软件包。通俗地说，Homebrew 是类似于 Mac App Store 的一个软件商店。

Homebrew目前支持MacOS和Linux系统

### Homebrew的好处

通过 Homebrew 下载的软件都来自于官网，绝对放心软件的安全性。而且它尽可能地利用系统自带的各种库，使得软件包的编译时间大大缩短，基本上不会造成冗余。

### Homebrew的安装

可以在官网直接下载安装包安装，下面介绍的是用命令行安装：

1. 使用官网的安装方法，通过terminal输入以下代码：

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   >若以上安装失败，并提醒：
   >
   >Failed to connect to raw.githubusercontent.comport 443: Connection refused.
   >
   >报错连接不上这个链接
   >
   >1. 如果有科学上网，可以在终端配置替换端口后再执行命令，替换成翻墙软件给的端口
   >
   >   ```bash
   >   export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890
   >   ```
   >
   >   后来想想是不是可以直接把这个配置写进～/.zshrc作为终端的全局配置呢？试过了妥妥的ok。
   >
   >2. 没有科学上网，可以直接配置/etc/hosts文件，将raw.githubusercontent.com直接指向真实IP
   >
   >  在[ipaddress.com/](https://www.ipaddress.com)查询 raw.githubusercontent.com 的真实IP 199.232.28.133 
   >
   >  修改hosts，添加如下内容： 199.232.28.133  raw.githubusercontent.com
   >
   >3. 用国内的镜像安装源，详情请看[Gitee / CunKai / HomebrewCN](https://link.zhihu.com/?target=https%3A//gitee.com/cunkai/HomebrewCN)

   ⚠️Homebrew需要依赖Command Line Tools , 它是Apple提供的一个工具包，里面包含很多系统没有提供的命令程序，比如Git........，Apple在安装Xcode的时候会默认安装这个工具包的，我的电脑上有两个版本的Xcodel就应该存在两个在对应的Xcode.app/Contents/Developer目录里。在安装Homebrew的时候依然提示需要安装Command Line Tools，貌似它链接不到Xcode自带的工具包，只能在按照它的提示下载，刚好这时候我电脑是Public Bate系统竟然提示系统版本过高安装不了。没办法只能手动下载也是Beta版本的它并安装，默认的目录是 /Library/Developer/CommandLineTools，之后成功安装Homebrew。

2. 测试 Homebrew 是否正确安装

   ```bash
   brew -v
   ```

3. 若上一步输入命令，回车后提示：`brew：command not found`。则需要进行环境配置，若成功则跳过该步骤：

   Homebrew基于 ARM 的CLI程序会软链接至 `/opt/homebrew/bin` 目录，这个目录shell不会主动export它，如果是基于inte的CLI 程序会自动软链接至 `/usr/local/bin` 目录，shell会主动export这个目录。

   ```bash
   1、在终端通过vim打开～/.zshrc文件，如果没有则新建
   sudo vim .zshrc  
   2、在 .zshrc 文件的末尾添加配置：
    export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"
   3、保存并退出文件
   4、刷新配置文件
   source ~/.zshrc
   5、再次输入 brew -v 测试
   
   ```
   
   >这里看很多资料 export 都是把系统的那几个也加上，其实是不用的，只需要把我们自己需要的路径加上就行
   >
   >`PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"`

### 切换Homebrew源

遇到 `brew update` 会卡住的情况，也是因为网络的问题，可以直接切换到国内的源

1. 更换brew.git

   ```bash
   git -C "$(brew --repo)" remote set-url origin https://mirrors.ustc.edu.cn/brew.git # 中科大
   或
   git -C "$(brew --repo)" remote set-url origin https://mirrors.aliyun.com/homebrew/brew.git # 阿里巴巴
   或
   git -C "$(brew --repo)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git # 清华大学
   ```

   ```bash
   //查看源
   git -C "$(brew --repo)" remote get-url origin 
   ```

   

2. 更换homebrew-core.git

   ```bash
   git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git # 中科大
   或
   git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.aliyun.com/homebrew/homebrew-core.git # 阿里巴巴
   或
   git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git # 清华大学
   ```

   ```bash
   //查看源
   git -C "$(brew --repo homebrew/core)" remote get-url origin
   ```

   

3. 更换homebrew-cask.git

   ```bash
   git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git # 中科大
   或
   git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.aliyun.com/homebrew/homebrew-cask.git # 阿里巴巴
   或
   git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask.git # 清华大学
   ```

   ```bash
   //查看源
   git -C "$(brew --repo homebrew/cask)" remote get-url origin
   ```

   

4. 更换homebrew-bottles

   ```text
   echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.aliyun.com/homebrew/homebrew-bottles' >> ~/.zshrc # 阿里云
   或
   echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles' >> ~/.zshrc # 中科大
   或
   echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/bottles' >> ~/.zshrc # 清华大学
   
   source ~/.zshrc
   ```

5. 恢复默认源

   ```bash
   1. git -C "$(brew --repo)" remote set-url origin https://github.com/Homebrew/brew.git
   2. git -C "$(brew --repo homebrew/core)" remote set-url origin https://github.com/Homebrew/homebrew-core.git
   3. git -C "$(brew --repo homebrew/cask)" remote set-url origin https://github.com/Homebrew/homebrew-cask.git
   4. 删除环境变量 HOMEBREW_BOTTLE_DOMAIN
   5. source ~/.zshrc
   6. brew update
   ```

6. 查看brew源

   ```bash
   $ git -C "$(brew --repo)" remote get-url origin
   $ git -C "$(brew --repo homebrew/core)" remote get-url origin 
   $ git -C "$(brew --repo homebrew/cask)" remote get-url origin 
   ```

   

### 常用命令

1. 更新Homebrew

   更新Homebrew，从 Git 仓库中获取最新版本的 Homebrew

   ```bash
   $ brew update 
   $ brew doctor    #诊断brew，并给出修复命令
   $ brew -v        #查看Homeview的版本号
   $ brew config            #查看brew配置
   ```

2. 搜索软件

   ```bash
   $ brew search <keyword>  
   ```

3. 下载软件

   ```bash
   $ brew install <package>        #一般是那些命令行工具、开发库、字体、插件等
   $ brew install --cask <package> #含有 GUI 图形化界面的软件
   ```

4. 更新软件

   ```bash
   $ brew upgrade              # 更新所有
   $ brew upgrade <package>    # 更新指定软件
   $ brew reinstall <package>  # 重装软件
   ```

5. 卸载软件

   ```bash
   $ brew uninstall <package>  # 卸载
   $ brew uninstall --force <package> #强制卸载
   ```

   完整卸载一个brew安装的软件,包括其依赖

   ```bash
   $ brew tap beeftornado/rmtree
   $ brew rmtree git
   $ brew cleanup
   ```

6. 列出已安装的软件

   ```bash
   $ brew list             # 所有的软件，包括 Formulae  和 Cask
   $ brew list --formulae  # 所有已安装的 Formulae
   $ brew list --cask      # 所有已安装的 Casks
   $ brew list <package>   # 列举某个 Formulate 或 Cask 的详细路径
   ```

7. 列出可更新的软件

   ```bash
   $ brew outdated
   ```

8. 清理旧版本软件

   ```bash
   $ brew cleanup            # 清理所有旧版本的包
   $ brew cleanup <package>  # 清理指定的旧版本包
   $ brew cleanup -n         # 查看可清理的旧版本包
   ```

9. 查看已安装软件的依赖

   ```bash
   $ brew deps <package> --installed --tree
   ```

10. 查看软件信息

    ```bash
    $ brew info <package>     # 显示某个包信息
    $ brew info               # 显示安装的软件数量、文件数量以及占用空间
    ```

11. 锁定某个不想更新的软件

    ```bash
    $ brew pin <package>       # 锁定指定包
    $ brew unpin <package>     # 取消锁定指定包
    ```

12. 查看Homebrew的依赖路径

    ```bash
    $ brew --cache    # 下载缓存路径
    $ brew --prefix   # 安装目录，通常是该路径的 Cellar 目录下
    ```



### 参考

[Homebrew 使用详解](https://zhuanlan.zhihu.com/p/30704752)