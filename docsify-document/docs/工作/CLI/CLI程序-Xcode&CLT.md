### 一、什么是Command Line Tools

简单来讲 Command Line Tools 就是一个小型工具包，为mac终端用户提供了许多常用的工具，实用程序和编译器。包括git，GCC，clang以及其他很多能够在Linux默认安装中找到的有用的命令。

Command Line Tool是Xcode的对应底层，Xcode的所有运行都依赖于Command Line Tool提供的命令程序。

### 二、如何安装Command Line Tools

安装Command Line Tools有以下几种方法

1. 安装完整的Xcode包

   安装Xcode，系统会自动安装Command Line Tools工具包，如果不是需要用Xcode开发不建议，包太大没必要，安装路径为：

   > /Applications/Xcode.app/Contents/Developer/usr/bin

2. 当 Command Line Tools 相关的命令被触发时会请求安装

   - 没有安装git的时候使用git命令会请求安装，我猜其它包含的命令被触发应该也行

   - 通过 xcode-select 命令安装

     ```bash
     $ xcode-select --install 
     ```

   安装路径为：

   > /Library/Developer/CommandLineTools/

3. 通过安装Homebrew触发安装

   Homebrew是依赖Command Line Tools，所以当安装Homebrew时如果没有Command Line Tools会提示安装，安装路径为：

   >/Library/Developer/CommandLineTools/

4. 离线下载安装

   下载安装包，直接点击安装即可，非常的简单，使用效果和在线安装是一样的。下载地址：https://developer.apple.com/download/more/  安装路径为：

   > /Library/Developer/CommandLineTools/

### 三、什么是xcode-select

输出或者改变活跃的开发者目录的路径，这个目录控制着哪个工具会被用于Xcode命令行工具（Xcode command line tools）（例如xcodebuild）以及BSD开发命令（例如cc、make）。

```bash
$ xcode-select --install # 安装 Command Line Tools ，默认路径/Library/Developer/CommandLineTools/
$ xcode-select -h  #查看帮助文档。
$ xcode-select -p    #输出活跃的开发者路径（说通俗点，就是输出Xcode是路径）。
$ xcode-select -s <path> #为活跃的开发者目录设置路径。（实际上就是设置默认使用的Xcode。这个参数多用于电脑里安装了多个Xcode的时候，对Xcode的设置。）
$ xcode-select -v  #输出xcode-select的版本。
$ xcode-select -r #恢复默认设置。
```

### 四、Xcode 相关终端工具使用

以后有时间在了解学习，收藏一篇文章：[Xcode 相关终端工具使用](https://hanleylee.com/articles/usage-of-xcode-terminal-tools/)
