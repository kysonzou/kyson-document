---
category:
  - Tech
tags:
  - MacOS
status: Done
---
1. 更新Homebrew
    
    更新Homebrew，从 Git 仓库中获取最新版本的 Homebrew
    
    ```bash
    $ brew update
    $ brew doctor    #诊断brew，并给出修复命令
    $ brew -version        #查看Homeview的版本号
    $ brew config    #查看brew配置
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
    $ brew list --formulae  # 所有已安装的 Formulae，CLI命令行软件包
    $ brew list --cask      # 所有已安装的 Casks，GUI图行界面软件包
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
    
13. 卸载homebrew
    
	```bash
    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall.sh)"
    $ rm -rf /opt/homebrew/*
    $ sudo rm -rf /opt/homebrew
	```