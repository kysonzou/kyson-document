### docsify介绍

docsify 是一个动态将.md文件生成文档网站的工具。它不会生成将 .md 转成 .html 的文件，所有转换工作都是在运行时进行，不会产生一些额外的文件，并且学习成本很低，很容易上手。当然，docsify 并不只是轻量，还包含以下特性（官方说法）：

- 无需构建，写完文档直接发布
- 容易使用并且轻量 (压缩后 ~21kB)
- 智能的全文搜索
- 提供多套主题
- 丰富的 API
- 支持 Emoji
- 兼容 IE11
- 支持服务端渲染 SSR

在我看来，docsify 的特点如下：

- 界面简洁大方，把重点留给了「内容」，也是 Wiki 最重要的部分。
- 支持全文搜索，自定义侧栏，让查询和导航变得更容易。
- 丰富的插件，让各种自定义功能触手可及。
- 使用 Markdown 编写文档，符合我平时写文章的习惯。
- 天生的轻量级让我感觉它就是 Wiki 的不二选择。

### docsify安装

docsify的运行需要基于node.js，所以需要先安装node.js，然后通过node的包管理工具npm安装docsify程序

```bash
 npm i docsify-cli -g
```

### 项目初始化

如果想在项目的 `./docs` 目录里写文档，直接通过 `init` 初始化项目

```bash
$ docsify init ./docs
```

### 开始写文档

初始化成功后，可以看到 `./docs` 目录下创建的几个文件

- `index.html` 入口文件
- `README.md` 会做为主页内容渲染
- `.nojekyll` 用于阻止 GitHub Pages 忽略掉下划线开头的文件

直接编辑 `docs/README.md` 就能更新文档内容。

### 本地预览

通过运行 `docsify serve` 启动一个本地服务器，可以方便地实时预览效果。默认访问地址 [http://localhost:3000](http://localhost:3000/)。

```bash
$ docsify serve docs    
```

然后......

官网的文档已尽写的非常详细了，直接看官网文档就OK https://docsify.js.org/#/zh-cn/ 