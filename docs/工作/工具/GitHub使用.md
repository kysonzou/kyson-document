### .DS_Store

.DS_Store 是Mac os 系统自动创建的，存储「访达」打开文件夹时自动显示方式的首选项，以便文件夹以创建者预期的方式显示。在默认情况下，Git会把 DS_Store 文件带入版本控制的范围内，但是我们并不需要对.DS_Store进行版本控制，所以可以手动将其踏入 Git 的版本管理忽略列表（.gitignorel）即可。

### .gitignorel

`.gitignore` 文件是一个文本文件，它告诉 git 不要跟踪特定的文件、目录或文件类型。

通常，可以通过以下两种方式之一获取 `.gitignore` 文件：

- 您自己创建 `.gitignore` 文件并手动将规则添加到文件中

- 从一个与您使用的语言和框架一致的现有项目中的 `.gitignore` 文件复制过来。


### .gitattributes

处理不同平台之间会出现的文件差异问题

[配置 Git 处理行结束符](https://docs.github.com/zh/get-started/getting-started-with-git/configuring-git-to-handle-line-endings)

[.gitattributes 正确使用姿势](https://juejin.cn/post/7084885453920272398)

[请把 .gitattributes 加入你的项目](https://juejin.cn/post/6844904062987550733)

### GitHub引用单个文件链接

将自己自定义的科学上网的配置文件托管到GitHub上，客户端通过链接引用文件，以后修改就直接修改Github上面的内容，然后客户端更新就可以了，不用和以前一样手动去替换。

一开始以为链接就是简单的仓库链接+文件目录，这样不对，不是有效链接

>https://githubfast.com/kysonzou/Magic-Internet.git/rule/clashX.yaml
>
>Not Found

然后发现Github文件页面有一个permalink（永久链接），这也不对，这是这个页面的链接，不是文件内容的链接

>https://githubfast.com/kysonzou/Magic-Internet/blob/57591bb6c552ebd354299bbf04d42504f1f33590/rule/clashX.yaml
>
>是网页的链接

有个Raw（原始的）表示的是文件原始内容的意思，但是它直接显示的链接也不对

>https://external.githubfast.com/https/raw.githubusercontent.com/kysonzou/Magic-Internet/main/rule/clashX.yaml
>
>在浏览器可以打开，但是在clashX客户端无效

后来通过对比其它github项目的链接依葫芦画瓢拼成了正确的引用链接

>https://usercontent.githubfast.com/raw/kysonzou/Magic-Internet/main/rule/clashX.yaml
>
> https://raw.githubusercontent.com/kysonzou/Magic-Internet/main/rule/clashX.yaml 
>
>和前面的对比其实就是改一下就可以了