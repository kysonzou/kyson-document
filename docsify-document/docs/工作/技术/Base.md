- zsh：系统Sell
- /etc：系统配置目录
- /bin、/sbin、/usr/bin、/usr/sbin、/usr/local/bin、~/bin：Binary程序文件目录
- ~/.gitconfig、/etc/.gitconfig：git的配置文件

### 硬链接&符号链接&拷贝

硬链接：硬链接的文件内容与创建时指向的源文件一模一样，把源文件删除，不会影响硬链接文件。类似于两个文件指向了相同的磁盘空间。

符号链接（软链接）：它的文件内容应该是指向源文件的路径， 如果把源文件删除，那么符号链接就找不到源文件了，也就访问不了了，而硬链接和源文件相等，删除源文件不会影响到硬链接文件，这也是和硬链接的本质区别。

拷贝：拷贝就是把源文件的内容在磁盘上复制一份，并将拷贝文件指向新的磁盘内容，这样磁盘空间占用就会翻倍，两个文件之间也没什么关系。



### 图形用户界面（GUI）

>图形用户界面（Graphical User Interface，简称 GUI，又称图形用户接口）是指采用图形方式显示的计算机操作用户界面。

图形用户界面是一种人与计算机通信的界面显示格式，允许用户使用鼠标等输入设备操纵屏幕上的图标或菜单选项，以选择命令、调用文件、启动程序或执行其它一些日常任务

- 图形界面程序可以向下兼容命令行界面程序，就是命令行界面程序功能都可以图形化，用图形的方式的实现（比如git是个命令行程序，通过命令行操作，但是也可以把这些命令行集成到图形程序中去，比如Xcode、github desktop就集成了git功能）

### 命令行界面（CLI）

> 命令行界面（英语：Command-line Interface，缩写：CLI）是在图形用户界面得到普及之前使用最为广泛的用户界面，它通常不支持鼠标，用户通过键盘输入指令，计算机接收到指令后，予以执行。

相信大家对于影视作品中出现的那种，某黑客/程序员/安全专家坐在电脑前猛敲键盘、屏幕上放眼望去全是滚动的字符的场景不会感到陌生。这种靠一行行命令的输入输出进行交互的用户界面，就叫做命令行界面

- 一般每一个命令行程序都会提供命令行，以便用户去使用这程序（比如安装了Git，Git就会提供各种命令行`git name` ；安装了cocoapods，cocoapods就会提供各种命令行`cocoapods name`）

### 文件路径

#### 绝对路径

目标文件在硬盘上的真实路径（最精确路径）

>/Users/kczou/Library/Mobile Documents/com~apple~CloudDocs/Markdown/日记.md

#### 相对路径

相对于当前文件位置的路径

/：表示根路径（用户路径之上的层级）

./：表示当前路径

../：表示父路径

**举例**

- 文件在当前目录

  >"./1.png" 或 "1.png"

- 文件在上层目录

  1. 在上层目录

     >"../1.png"
  
  2. 在上层目录下的一个Image文件夹下

     > "../Image/1.jpg"

  3. 在上上层目录下
  
     >"../../1.jpg"

- 文件在下一层目录(Image1文件夹)

  >  "./Image1/1.jpg"
  
- 根目录表示法,任何页面访问Image下的Image.jpg图片

  ~~这个没搞懂，以后遇到了在学习~~  /就是系统的根目录

  >"C:/Image/1.jpg"




### zsh

zsh、sh、bash、csh、tcsh等它们都是Shell，用作接收终端的命令行指令，并且让计算机执行指令并把结果返回给终端。通常它们都会以「sh」结尾，一个系统可以安装多个Sell，在Mac OS 中是默认是zsh，但是ssh、bash、csh都有，默认的Sell是可以更改的。

```bash
kczou@zoukechengdeMacBook-Air ~ % cat /etc/shells

\# List of acceptable shells for chpass(1).

\# Ftpd will not allow users to connect who are not using

\# one of these shells.

/bin/bash

/bin/csh

/bin/dash

/bin/ksh

/bin/sh

/bin/tcsh

/bin/zsh
```



### /etc 目录

标准unix系统配置文件存放目录，是系统下的一个文件夹，各种个样的系统配置文件都会放在这里，此目录实际为指向 /private/etc 的链接。如

/etc/sells      //系统支持的sell

/etc/hosts    //本地域名解析文件

/etc/network   //IP、掩码、网关、主机名配置

/etc/passwd   //用户名和密码



###  Binary 程序目录

Binary二进制程序一般都是Sell程序，比如：cd、ls、vim....，在系统中有多个文件夹存储它们，

- /bin ：传统unix命令的存放目录（cat、cp、ls）

- /sbin：传统unix管理类命令存放目录（fdisk，ifconfig）

- /usr：第三方Binary程序安装目录

  - /usr/bin
  - /usr/sbin
  - /usr/local/bin

- ～/bin：用户的程序目录

  

### Mac OS 常见目录的了解

/ 是系统的根目录，在这个目录下常见的有

- /bin：传统unix命令的存放目录，如cat、cp、ls、......
- /sbin：传统unix管理类命令存放目录，如fdisk、ifconfig、......
- /usr：第三方Binary程序安装目录
  - /usr/bin
  - /usr/sbin
  - /usr/local/bin
- /etc：标准unix系统配置文件存放目录，passwd、zshrc、shells、hosts、networks、......，此目录实际为指向/private/etc的链接

- /dev：设备文件存放目录，如何代表硬盘的/dev/disk0。
- /tmp：临时文件存放目录，其权限为所有人任意读写。此目录实际为指向/private/tmp的链接。
- /var：存放经常变化的文件，如日志文件。此目录实际为指向/private/var的链接。
- /Applications：程序文件夹，用户安装的GUI应用都会在这里

- /Library： 数据文件、帮助文件、文档等等
- /System： 系统配置和文件
  - /System/Applications：系统自带程序的安装目录
  - /System/Library：数据文件、帮助文件、文档等等
  - /System/iOSSupport：iOS支持文件

- /Users：用户文件夹，系统所有的用户都会被存储在这里
  - /Users/kczou 用户名为kczou的用户目录，在这个目录下常见的有
    - Applications：用户私有程序的安装目录
    - Desktop：桌面文件夹，桌面的东西都存储在这里	
    - Documents：文档文件夹
    - Downloads：网络下载默认文件夹
    - Library：用户的数据文件、帮助文件、文档等等
    - Movies：iMove.app 默认文件夹
    - Music：Music.app默认文件夹
    - Pictures：Photos.app默认文件夹
    - Public：需要和其他用户的共享文件夹
    - iCloud Drive (Archive)：iCloud云文件夹
    - .*：各种隐藏文件、文件夹，.gitconfig、.config、.zsh_history、.vim、......

- /Network： 网络节点存放目录
- /Volumes ：文件系统挂载点存放目录。
- /cores： 内核转储文件存放目录。当一个进程崩溃时，如果系统允许则会产生转储文件。
- /private：里面的子目录存放了/tmp、/var、 /etc等链接目录的目标目录

