<font color = 'red'>有时间可以练习一下shell脚本</font>

- 这里只是简单的记录常用命令和常用使用方式
- 每一个命令就是一个程序，一般放在系统的 /usr/bin 目录下
- 系统根目录 /

### Unix命令介绍

Unix命令的基本格式：

**command [-options] [parameter]**

UNIX命令由一个命令（command）和零到多个参数构成，命令和参数之间，以及参数与参数之间用空格隔开，Unix命令区分大小写

#### 通配符

| 通配符 | 含义                             | 说明              |
| ------ | -------------------------------- | ----------------- |
| *      | 代表任意个数字符                 | 代表0～无限字符   |
| ？     | 代表一个字符                     | 有且只代表1个字符 |
| []     | 表示可以匹配字符数组中的任意一个 |                   |
| [abc]  | 匹配abc中的一个                  |                   |
| [a-f]  | 匹配a-f的任意一个                |                   |

### 文件处理

#### ls

list，查看当前目录的内容

| 选项 | 含义                                                     | 说明        |
| ---- | -------------------------------------------------------- | ----------- |
| -a   | 显示隐藏文件夹，包含（.）和（..）                        | all         |
| -A   | 显示隐藏文件夹，不包含（.）和（..）                      | All         |
| -l   | 长格式显示                                               | Long Format |
| -h   | 以适合人类阅读的方式输出（会把大小从字节转换成KB、M...） | Human       |
| -R   | 递归处理，将指定目录下的所有文件及子目录一并处理         | Recursively |

```bash
kczou@zoukechengdeMacBook-Air desktop % ls -l -A -h -R
total 144616
-rw-r--r--@ 1 kczou  staff   6.0K 10 28 17:25 .DS_Store

kczou@zoukechengdeMacBook-Air desktop % ls -lAhR          #选项可以写在一起
total 144616
-rw-r--r--@ 1 kczou  staff   6.0K 10 28 17:25 .DS_Store
```

#### cd

change directory，切换工作目录

```bash
kczou@zoukechengdeMacBook-Air desktop % cd      #进入用户主目录
kczou@zoukechengdeMacBook-Air ~ % cd ~          #进入用户主目录
kczou@zoukechengdeMacBook-Air desktop % cd .    #当前工作目录
kczou@zoukechengdeMacBook-Air desktop % cd ..   #进入上一级目录
kczou@zoukechengdeMacBook-Air desktop % cd -    #返回进入此目录之前所在的目录
```

#### mkdir

make directory，创建文件目录

| 选项 | 含义                                                       | 说明    |
| ---- | ---------------------------------------------------------- | ------- |
| -p   | 若所要建立目录的上层目录目前尚未建立，则会一并建立上层目录 | parents |
| -v   | 显示指令的详细执行过程                                     | verbose |

```bash
kczou@zoukechengdeMacBook-Air 1 % mkdir -p -v  4/31/32  #建立目录，如果上层目录没有则新建
4
4/31
4/31/32
```

#### rmdir

remove directory，删除空目录，文件中有隐藏文件也会提示不为空，删不了的

| 选项 | 含义                                                         |         |
| ---- | ------------------------------------------------------------ | ------- |
| -p   | 删除指定目录后，若该目录的上层目录已变成空目录，则将其一并删除 | parent  |
| -v   | 显示指令的详细执行过程                                       | verbose |

```bash
kczou@zoukechengdeMacBook-Air desktop % rmdir -p -v  2/21/22/23
2/21/22/23
rmdir: 2/21/22: Directory not empty       #因为22文件夹是非空目录，有内容

kczou@zoukechengdeMacBook-Air 22 % ls -A  #查看22文件夹，有一个.DS_Store的隐藏文件
.DS_Store
```

#### rm

remove，删除文件或目录，$\textcolor{Red}{删除文件或目录不可恢复，三思而后行}$  

| 选项   | 含义                                 | 说明        |
| :----- | ------------------------------------ | ----------- |
| -f     | 强制删除文件或目录，不会提示错误信息 | force       |
| -i     | 删除文件或目录之前先询问用户         | inquiry     |
| -r、-R | 递归删除，删除文件夹必须加上         | recursively |
| -v     | 显示指令的详细执行过程               | verbose     |

```bash
kczou@zoukechengdeMacBook-Air desktop % rm -f -r -v 2  #强制删除文件夹2         
2/21/22/23
2/21/22
2/21
2

kczou@zoukechengdeMacBook-Air desktop % rm -i -r -v 1  #会询问是否删除Y删除，NO不删除
examine files in directory 1? 
```

#### cp

copy，复制文件或目录，将一个或多个源文件或者目录复制到指定的目的文件或目录，它可以将单个源文件复制成一个指定文件名的具体的文件或一个已经存在的目录下。cp命令还支持同时复制多个文件，当一次复制多个文件时，目标文件参数必须是一个已经存在的目录，否则将出现错误。

| 选项    | 含义                                                         | 说明        |
| ------- | ------------------------------------------------------------ | ----------- |
| -f      | 若目标文件或目录与现有的文件或目录重复，则直接覆盖现有的文件或目录，貌似是默认 | force       |
| -i      | 覆盖既有文件之前先询问用户                                   | inquiry     |
| -r、 -R | 递归处理，将指定目录下的所有文件与子目录一并处理，复制文件夹必须加上 | recursively |
| -v      | 详细显示命令执行的操作                                       | verbose     |

```bash
kczou@zoukechengdeMacBook-Air desktop % cp 1/11/12/1-zkc.text 2 #将文件1-zkc.text复制到文件夹2

kczou@zoukechengdeMacBook-Air desktop % cp -r 1 2 #将文件夹1复制到文件夹2中 
```

#### mv

move，用来对文件或目录重新命名，或者将文件或目录从一个目录移到另一个目录中

| 选项 | 含义                                                         | 说明    |
| ---- | ------------------------------------------------------------ | ------- |
| -f   | 若目标文件或目录与现有的文件或目录重复，则直接覆盖现有的文件或目录 | force   |
| -i   | 覆盖既有文件之前先询问用户                                   | inquiry |
| -v   | 详细显示命令执行的操作                                       | verbose |

```bash
kczou@zoukechengdeMacBook-Air desktop % mv -v name.text newName.text
name.text -> newName.text  #将name.text重命名为newName.text

kczou@zoukechengdeMacBook-Air desktop % mv -v dir newDir
dir -> newDir/dir          #将dir移动到newDir
```

#### pwd

print work directory，获取用户文件夹路径

```bash
kczou@zoukechengdeMacBook-Air ~ % pwd
/Users/kczou
```

#### touch

将指定文件的访问时间和修改时间改变，若指定文件不存在则创建之

```bash
kczou@zoukechengdeMacBook-Air ~ % touch zkc.text
```

#### cat

读取文件内容并输出在当前屏幕终端

```bash
kczou@zoukechengdeMacBook-Air ~ % cat zkc.text
成功读取到文件
```

#### open

用默认方式打开文件或文件夹

```bash
kczou@zoukechengdeMacBook-Air desktop % open zkc.text
```

#### find

find命令用来在指定目录下查找文件，如果使用该命令时，不设置任何参数，则find命令将在当前目录下查找子目录与文件。并且将查找到的子目录和文件全部进行显示。

| 选项      | 含义                                                         | 说明 |
| --------- | ------------------------------------------------------------ | ---- |
| name      | <范本样式>：指定字符串作为寻找文件或目录的范本样式           |      |
| iname     | <范本样式>：此参数的效果和指定“-name”参数类似，但忽略字符大小写的差别； |      |
| -path     | <范本样式>：指定字符串作为寻找目录的范本样式；               |      |
| -maxdepth | <目录层级>：设置最大目录层级；                               |      |
| -mindepth | <目录层级>：设置最小目录层级；                               |      |

```bash
#find . 列出当前目录及子目录的所有文件和文件夹（ls -R -a 也能实现类似的查找功能）
kczou@zoukechengdeMacBook-Air desktop % find .
.
./.DS_Store
./.localized
./node-v18.6.0.pkg
./1
./1/.DS_Store

#通过名字查找 "111" 的文件或文件夹
kczou@zoukechengdeMacBook-Air desktop % find . -name 111 
./1/11/111

#指定目录层级
kczou@zoukechengdeMacBook-Air desktop % find . -maxdepth 2  -name 111 //啥也没有，因为 "111" 在第三层级
kczou@zoukechengdeMacBook-Air desktop % find . -maxdepth 3  -name  111
./1/11/111

#通过path去匹配路径中，只要文件或文件夹的路径中有对应的字符串，都会被查询到
kczou@zoukechengdeMacBook-Air desktop % find . -path  "*22*" //貌似一定要加通配符
./2/22
./2/22/111
./2/22/111/1111
```

#### which

用于查找并显示给定命令的绝对路径

```bash
kczou@zoukechengdeMacBook-Air ~ % which git    
/usr/bin/git
```

#### whereis

根据标准可执行文件路径查看安装路径，找的就是bin目录下的文件路径。

```bash
kczou@zoukechengdeMacBook-Air ~ % whereis git  
git: /usr/bin/git /Applications/Xcode.app/Contents/Developer/usr/share/man/man1/git.1
```

### 其它

#### man

man command，查询命令手册

```bash
kczou@zoukechengdeMacBook-Air ~ % man ls

kczou@zoukechengdeMacBook-Air ~ % man cd
```

#### clear

清除当前屏幕终端上的任何信息。

```bash
kczou@zoukechengdeMacBook-Air ~ % clear 
```

#### sudo

superuser do，以其他身份来执行命令，预设的身份为root，可以解决权限的问题

```bash
kczou@zoukechengdeMacBook-Air ~ % sudo gem install
```

#### curl

client url，是用于在本地计算机与远程服务器之间传输数据的命令行工具。使用curl时您可以使用HTTP，HTTPS， SCP ，SFTP和FTP等协议下载或上传数据。 

| 选项 | 含义                                                     | 说明     |
| ---- | -------------------------------------------------------- | -------- |
| -X   | 指定什么命令                                             |          |
| -H   | 自定义的请求头信息                                       | Header   |
| -d   | http post 传送的数据                                     | data     |
| -s   | 静默模式。不输出任何东西                                 | Silent   |
| -o   | 指定文件下载路径保存下载内容（貌似 > 重定向也可以实现）  | output   |
| -O   | 在当前目录下以远程文件名保存下载内容                     | output   |
| -L   | 指示curl跟随301重定向，直到服务器不返回状态码301才会终止 | location |

##### 发送JSON Body

在发送JSON Body到服务器时，你需要设置header的`Content-Type`为`application/json`，表示指示curl以JSON的形式发送Body的数据。

除了设置header的`Content-Type`之外，还需要使用curl的`-d`/`--data`指定要发送的JSON字符串，注意JSON需要使用单引号（有些操作系统也使用双引号）转义。

```bash
#发送JSON字符串{"email":"web@myfreax.com","website":"myfreax.com"}到服务器

curl -X POST -H "Content-Type: application/json"  
-d '{"email":"web@myfreax.com","website":"myfreax.com"}' http://127.0.0.1:3000/site
```

##### 发送Header

如果要发送Header到服务器，可以使用curl的`-H`/`--header`选项，它允许指定header的Key和value值。

header的Key和value之间必须要空格并且并且这个header使用双引号转义，避免shell的解释。你可以同时使用多个`-H`/`--header`选项来指定多个header的key和value。你可以看到下面的示例将会发送多个Header。

```bash
#第一个header设置内容类型Content-Type: application/json，第二个header发送website: myfreax.com

curl -X POST -H "Content-Type: application/json" -H "website: myfreax.com"  
-d '{"email":"web@myfreax.com","website":"myfreax.com"}' http://127.0.0.1:3000/site
```

##### 下载文件

默认情况下`curl`将下载url的资源并重定向标准输出。如果要保存下载的文件，可以使用`-o`或`-O`选项，貌似用重定向也可以实现

```bash
#下载单个文件
curl -o /home/myfreax/work/vue.js https://cdn.jsdelivr.net/npm/vue/dist/vue.js

curl -O https://cdn.jsdelivr.net/npm/vue/dist/vue.js

#下载多个文件
curl -o /home/myfreax/work/vue.js https://cdn.jsdelivr.net/npm/vue/dist/vue.js 
-O https://cdn.jsdelivr.net/npm/vue/dist/vue.js
```

##### 301重定向

某些网址会被重定向到其它的网址，这个时候使用curl需要加上`-L`/`--location`选项，指示curl跟随301重定向，直到服务器不返回状态码301才会终止，才能正确的获取到数据，不然有可能返回Document Has Moved类似的内容

```bash
curl -L apple.com
```



### Vim命令

Vim是一个类似于Vi的著名的功能强大、高度可定制的文本编辑器，在Vi的基础上改进和增加了很多特性。

在Mac OS中系统自带了命令行页面（CLI）版本的Vim

Vim简单命令

#### vim -v

查看Vim程序的版本号

```bash
kczou@zoukechengdeMacBook-Air ~ % vim -v  //version
```

#### vim

打开或者新建文件

```bash
kczou@zoukechengdeMacBook-Air ~ % vim markdown.text #打开或者新建markdown.text文件
```

#### 普通模式

打开或者新建文件之后进入普通模式，普通模式没有光标

| 命令 | 说明             |
| :--- | ---------------- |
| i    | 进入输入模式     |
| :    | 进入底部命令模式 |
| :w   | 保存             |
| :q   | 退出             |
| :wq  | 保存并退出       |

#### 输入模式

普通模式输入 i 进入输入模式，光标会在文档内容某处

| 命令       | 说明                         |
| ---------- | ---------------------------- |
| esc        | 退出输入模式，切换到普通模式 |
| back space | 退格键，删除光标前一个字符   |

#### 底部命令模式

普通模式输入 : 进入底部命令模式，光标在底部

| 命令 | 说明                             |
| ---- | -------------------------------- |
| esc  | 退出底部命令模式，切换到普通模式 |
| w    | 保存                             |
| q    | 退出                             |
| wq   | 保存并退出                       |

### 参考 

[Linux命令大全](https://man.niaoge.com)
