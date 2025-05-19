---
category:
  - Tech
tags:
  - Linux
  - MacOS
status: Done
---
- 输入重定向：`<` 把由键盘输入改成由其它方式输入
- 输出重定向：`>`把由终端显示输出改成由其它方式输出
- 重定向：`|` 把左边的输出直接变成右边的输入

### 硬件设备和文件描述符

计算机的硬件设备有很多，常见的输入设备有键盘、鼠标、麦克风、手写板等，输出设备有显示器、投影仪、打印机等。不过，在 Linux 中，标准输入设备指的是键盘，标准输出设备指的是显示器。

为了表示和区分已经打开的文件，Linux 会给每个文件分配一个 ID，这个 ID 就是一个整数，被称为文件描述符（File Descriptor）。

| 文件描述符 | 文件名 | 类型             | 硬件   |
| ---------- | ------ | ---------------- | ------ |
| 0          | stdin  | 标准输入文件     | 键盘   |
| 1          | stdout | 标准输出文件     | 显示器 |
| 2          | stderr | 标准错误输出文件 | 显示器 |

Linux 程序在执行任何形式的 I/O 操作时，都是在读取或者写入一个文件描述符。一个文件描述符只是一个和打开的文件相关联的整数，它的背后可能是一个硬盘上的普通文件、FIFO、管道、终端、键盘、显示器，甚至是一个网络连接。

stdin、stdout、stderr 默认都是打开的，在重定向的过程中，0、1、2 这三个文件描述符可以直接使用。

### 重定向

Linux Shell 重定向分为两种，一种输入重定向，一种是输出重定向；从字面上理解，输入输出重定向就是「改变输入与输出的方向」的意思。

- 输入方向就是数据从哪里流向程序。数据默认从键盘流向程序，如果改变了它的方向，数据就从其它地方流入，这就是输入重定向。
- 输出方向就是数据从程序流向哪里。数据默认从程序流向显示器，如果改变了它的方向，数据就流向其它地方，这就是输出重定向。

#### 输出重定向

输出重定向是指命令的结果不再输出到显示器上，而是输出到其它地方，一般是文件中。

| 类型                     | 符号                      | 作用                                                         |
| ------------------------ | ------------------------- | ------------------------------------------------------------ |
| 标准输出重定向           | command  >file            | 以覆盖的方式，把 command 的正确输出结果输出到 file 文件中    |
|                          | command  >>file           | 以追加的方式，把 command 的正确输出结果输出到 file 文件中    |
| 标准错误输出重定向       | command  2>file           | 以覆盖的方式，把 command 的错误信息输出到 file 文件中        |
|                          | command 2>>file           | 以追加的方式，把 command 的错误信息输出到 file 文件中        |
| 正确和错误信息同时重定向 | command >file 2>&1        | 以覆盖的方式，把正确输出和错误信息同时保存到同一个文件（file）中 |
|                          | command >>file 2>&1       | 以追加的方式，把正确输出和错误信息同时保存到同一个文件（file）中 |
|                          | command >file1  2>file2   | 以覆盖的方式，把正确的输出结果输出到 file1 文件中，把错误信息输出到 file2 文件中 |
|                          | command >>file1  2>>file2 | 以追加的方式，把正确的输出结果输出到 file1 文件中，把错误信息输出到 file2 文件中 |

- 在输出重定向中，`>`代表的是覆盖，`>>`代表的是追加。
- 输出重定向的完整写法其实是`fd>file`或者`fd>>file`，其中 fd 表示文件描述符，如果不写，默认为 1，也就是标准输出文件。当文件描述符为 1 时，一般都省略不写。

```bash
#输出重定向
kczou@zoukechengdeMacBook-Air desktop % ls -lh >file.text
kczou@zoukechengdeMacBook-Air desktop % cat file.text
total 144176
-rw-r--r--  1 kczou  staff    68B Nov  5 01:09 1.text
-rw-r--r--@ 1 kczou  staff   3.7M Jul 17 11:26 Docsify-Guide-main.zip
-rw-r--r--  1 kczou  staff     0B Nov  5 17:48 file.text
-rw-r--r--@ 1 kczou  staff    67M Jul 17 11:30 node-v18.6.0.pkg
kczou@zoukechengdeMacBook-Air desktop % 
```

#### 输入重定向

输入重定向就是改变输入的方向，不再使用键盘作为命令输入的来源，而是使用文件作为命令的输入。

| 符号                  | 说明                                                         |      |
| --------------------- | ------------------------------------------------------------ | ---- |
| command <file         | 将 file 文件中的内容作为 command 的输入                      |      |
| command <<END         | 从标准输入（键盘）中读取数据，直到遇见分界符 END 才停止（分界符可以是任意的字符串，用户自己定义） |      |
| command <file \>file2 | 将 file1 作为 command 的输入，并将 command 的处理结果输出到 file2 |      |

和输出重定向类似，输入重定向的完整写法是`fd<file`，其中 fd 表示文件描述符，如果不写，默认为 0，也就是标准输入文件。

```bash
#从标准键盘读取数据以end结束，并将输入结果输出到file.text文件中
kczou@zoukechengdeMacBook-Air desktop % <<end  >file.text
heredoc> 12
heredoc> 23
heredoc> 45
heredoc> end
kczou@zoukechengdeMacBook-Air desktop % <file.text //有点和读取文件内容相似
12
23
45
```

### 管道

通过前面的学习，我们已经知道了怎样从文件重定向输入，以及重定向输出到文件。Shell 还有一种功能，就是可以将两个或者多个命令（程序或者进程）连接到一起，把一个命令的输出作为下一个命令的输入，以这种方式连接的两个或者多个命令就形成了管道（pipe）。

Linux 管道使用竖线 `|` 连接多个命令，这被称为管道符。Linux 管道的具体语法格式如下：

```bash
$ command1 | command2
$ command1 | command2 [ | commandN... ]
```

当在两个命令之间设置管道时，管道符`|`左边命令的输出就变成了右边命令的输入。只要第一个命令向标准输出写入，而第二个命令是从标准输入读取，那么这两个命令就可以形成一个管道。

#### 重定向和管道的区别

简单地说，重定向操作符 > 将命令与文件连接起来，用文件来接收命令的输出；而管道符 | 将命令与命令连接起来，用第二个命令来接收第一个命令的输出。如下所示：

```bash
$ command > file
$ command1 | command1
```

#### 管道与输入重定向

输入重定向操作符<可以在管道中使用，以用来从文件中获取输入，其语法类似下面这样：

```bash
$ command1 < input.txt | command2
$ command1 < input.txt | command2 -option | command3
```

#### 管道与输出重定向

你也可以使用重定向操作符>或>>将管道中的最后一个命令的标准输出进行重定向，其语法如下所示：

```bash
$ command1 | command2 | ... | commandN > output.txt
$ command1 < input.txt | command2 | ... | commandN > output.txt
```

### 参考

[Shell知识](http://c.biancheng.net/view/3131.html)

