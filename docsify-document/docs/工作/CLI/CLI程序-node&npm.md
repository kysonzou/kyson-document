- Node.js 不是 JavaScript 框架，不是一种编程语言，不是 JavaScript 库，不是一组技术的总称，也不是 JavaScript 的别名。
- Node.js 是一个可以在浏览器外理解和执行 JavaScript 代码的软件程序。更准确地说，Node.js 是一个 开源、跨平台的JavaScript 运行环境，或者说是一个 JS 语言解释器。

### Node.js

1. Node.js介绍

   Node.js 是基于 Chrome 的 V8 引擎开发的一个 C++ 程序，目的是提供一个 JS 的运行环境。最早 Node.js 主要是安装在服务器上，辅助大家用 JS 开发高性能服务器代码，但是后来 Node.js 在前端也大放异彩，带来了 Web 前端开发的革命。Node.js 下运行 JS 代码有两种方式，一种是在 Node.js 的交互环境下运行，另外一种是把代码写入文件中，然后用 node 命令执行文件代码.

2. 如何安装node.js

   官网下载安装文件，官网地址：https://nodejs.org/zh-cn/download

   通过Homebrew安装

   ```bash
   $ brew install node
   ```

3. Node.js的常用命令行

   1. 更新node.js

      ```bash
      $ brew upgrade node
      
      # 查看node版本号
      $ node -v
      ```
   
   2. 运行js
   
      ```bash
      $ node XXX.js
      ```
   
   3. 以后用到了在了解学习

### npm

1. 什么是npm

   npm 是 Node Package Manager 的缩写，用于管理Node.js应用程序中的依赖项和执行各种任务的命令行工具，开发者可以通过它来管理自己的包和使用别人的包。

   - 允许用户从NPM服务器下载别人编写的第三方包到本地使用。
   - 允许用户从NPM服务器下载并安装别人编写的命令行程序到本地使用。
   - 允许用户将自己编写的包或命令行程序上传到NPM服务器供别人使用。

2. npm安装

   安装新版的node.js在安装的时候会同步安装npm程序

3. npm常用命令行

   1. 查看npm源
   
      ```bash
      $ npm config get registry
      ```
   
   2. 查看npm版本号
   
      ```bash
      $ npm -v              #查看npm版本号
      $ npm config list -l  #查看 npm 的配置
      $ npm -l              #查看各个命令的简单用法
      ```
   
   3. 更新npm程序
   
      更新node.js就可以更新npm
   
   4. 搜索软件
   
      ```bash
      $ npm search <搜索词> 
      ```
   
   5. 下载软件
   
      ```bash
      $ npm install <name> -g         # 默认安装指定模块的最新(@latest)版本
      $ npm install <name>@<version> -g  # 安装指定模块的指定版本
      $ npm install <tarball url> -g     # 通过Github代码库地址安装
      
      #配置选项
      #全局安装
      -g | -global 
      ```
   
      本地安装：
   
      1. 将安装包放在 ./node_modules 下（运行 npm 命令时所在的目录），如果没有 node_modules 目录，会在当前执行 npm 命令的目录下生成 node_modules 目录。
      2. 可以通过 require() 来引入本地安装的包。
   
      全局安装：
   
      1. 将安装包放在 /usr/local 下或者你 node 的安装目录。
      2. 可以直接在命令行里使用。
   
   6. 更新软件
   
      ```bash
      $ npm update <name> [-g]   #升级当前项目或全局的指定模块
      ```
   
   7. 卸载软件
   
      ```bash
      $ npm uninstall <name> [-g]  #卸载当前项目或全局模块 
      
      ```
   
      卸载后，你可以到. /node_modules/ 目录或全局安装下查看包是否还存在，或者使用以下命令查看：
   
      ```bash
      $ npm ls [-g]  #好像和 $ npm list [-g] 是类似的命令
      ```
   
   8. 列出已安装的软件
   
      ```bash
      $ npm list [-g]    #查看所有本地或全局安装的模块
      $ npm list <name> [-g]  #如果要查看某个模块的版本号
      ```
   

### 参考

[Node.js 究竟是什么？初学者指南](https://zhuanlan.zhihu.com/p/633216265)

[什么是 Nodejs ?](https://zhuanlan.zhihu.com/p/47822968)