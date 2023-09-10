- Terminal的可访问程序系统默认放在 */bin 文件夹中，启动Terminal的时候会 export   */bin文件 ，如果程序没在 */bin 中则可以通过 ./zshrc 配置文件将程序软链接到 */bin 中以便Terminal可以export到
- 如果程序没在 */bin 中也可以直接通过 ./zshrc 配置文件将程序路径直接添加到 export 中
- export的作用是设置环境变量

自己暂时没遇到，这是引用别人的写的我觉得很不错所以就记录一下

"`zsh: command not found:`"这个错误相信大家都不陌生，以前每次遇到这个问题都是Google一下，然后告诉你在`xxx`文件添加`xxx`文字，或者在Terminal运行`xxx`命令即可，有些work，有些不行。

> 万事皆有因，今天我们就来说一下这个问题发生的时最常见的原因和解决办法，让你下次再遇到这种问题时自己就可以解决不需要在去Google`xxx Gems command not found`。

问题通常发生在局部安装了某个Terminal程序之后，此时程序可能在某个ruby gem的bin目录下，或者Application下（如：sublime），需要我们创建一个指向这个地址软链接，可以方便的访问它。

### Terminal访问程序原理

Linux环境下通常我们将Terminal可访问的程序放在/bin、/sbin、/usr/bin、/usr/sbin、/usr/local/bin有时也会放在 ~/bin 目录下。

那么在Terminal页面打开（其实是shell login）的时候，程序是如何Load进来的呢？过程大致如下：

1. Terminal打开时当前user默认的shell会去读取自己的配置文件和系统默认配置文件，一般自己的配置文件在`~`目录下；
2. 这个配置文件会去`export`路径，读取`*/bin`下的可执行文件；
3. `*/bin`下的可执行文件通常情况下是指向某个路径下的软链接（可以使用`ln -s`创建）；

### 问题原因

基于上面的过程，我们在Terminal中访问得到`command not found`的具体原因可能如下：

1. 当前调用的命令确实没有安装，如："lorem spear"；

2. 当前命令安装了，但是没有创建软链接到`*/bin`；

3. 当前命令已创建软链接到`*/bin`，但是所在`*/bin`路径没有被export；

   > export的作用是设置环境变量

### 解决办法

接下来以Mac下的zsh为例给出解决办法：

> Linux系统或者其他Shell（如：bash、sh等）只需要换一些shell的配置文件即可。
>
> 如果是bash，配置文件是~/.bash_profile

1. 命令已安装，但是没有创建软链接到系统默认的`*/bin`，这种情路我们需要把目标程序软链接到系统默认的`*/bin` 中

   - 首先使用任何编辑器（vim、atom）打开[zsh](https://link.jianshu.com/?t=http://402v.com/oh-my-zsh/)的的当前用户配置文件`~/.zshrc`（没有则创建）

   - 找到`not found`的这个程序在什么位置，例如

     ```bash
     $ whereis xxx
     # OR
     $ gem which xxx
     ```

   - 创建从程序所在位置到`*/bin`的软链接。创建软链接的命令是`ln -s $source $target`，`-s`参数表明创建的链接类型，`source`表示程序所在位置，`target`表示软链接的所在路径，例如

     >ln -s /Users/kczou/*    /usr/local/bin

   - 运行`source`命令使软链接生效。新创建的软链接在当前的Terminal页面（即没有再次运行shell login）不会生效，需要对当前Shell（在本例中即`zsh`）的配置文件（在本例中即`~/.zshrc`）手动执行`source`来加载。例如：

     ```bash
     source ~/.zshrc
     ```

   - 此时再次运行命令已经不会报错了。

2. 当面命令已经被放到非系统默认的 */bin 中，这时候我们可以直接将`*/bin`添加到`export`中，让系统去链接程序，

   - 首先使用任何编辑器（vim、atom）打开[zsh](https://link.jianshu.com/?t=http://402v.com/oh-my-zsh/)的的当前用户配置文件`~/.zshrc`（没有则创建）

   - 找到`not found`的这个程序在什么位置，例如

     ```bash
     $ whereis brew
     $ brew: /opt/homebrew/bin/brew 
     ```

   - 将brew所在的 /opt/homebrew/bin 添加到 export 中

     >export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"

   - 运行`source`命令使软链接生效

   - 此时再次运行命令已经不会报错了。

### 参考

["command not found"问题的解决办法](https://www.jianshu.com/p/bba968ca3957)

[已解决 zsh command not found (macOS)](https://juejin.cn/post/7118571181539590174)
