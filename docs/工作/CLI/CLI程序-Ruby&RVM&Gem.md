### Ruby

1. 什么是Ruby

   Ruby 是一种面向对象的编程语言，它具有简洁、易读、灵活的语法，广泛用于开发各种类型的应用程序，特别是Web应用程序。

2. 如何安装Ruby

   1. 通过RVM安装，需要先安装RVM

      ```bash
      $ rvm install ruby_version
      ```

   2. 通过brew（MacOS）

      ```bash
      $ brew install ruby	
      ```

      通过brew安装ruby会同步安装gem

      > macOS provides gem as part of Ruby. To install a newer version:

   3. macOS 系统会自带ruby和gem

   4. [ruby的官网](https://www.ruby-lang.org/en/documentation/installation/)介绍的安装方法，windows可以下载安装包安装

      

3. ruby的常用命令

   1. 查看当前使用的Ruby版本号

      ```bash
      $ ruby -v
      ```

   2. 运行Ruby程序

      ```bash
      $ ruby my_script.r
      ```

   3. 打开Ruby交互式控制台，可以在其中实时执行 Ruby 代码。

      ```bash
      $ irb
      
      ```

   4. 更新Ruby

      通过RVM安装的，则通过RVM更新

      ```bash
      # 1. 安装新版本
      $ rvm install ruby_version
      # 2. 卸载就版本
      $ rvm remove ruby_version
      ```

      通过brew安装的，则通过brew更新

      ```bash
      $ brew upgrade ruby
      ```

      


### RVM

1. RVM是什么

   RVM 是一个用于管理 Ruby 版本的工具。它允许开发者在同一系统上安装和管理多个不同版本的 Ruby。这对于在不同项目中使用不同的 Ruby 版本或在同一项目中跟踪 Ruby 的更新非常有用。RVM 还允许您创建独立的 gemsets，以便在不同的项目中管理 gem（Ruby 包管理工具）依赖关系。通过 RVM，您可以轻松地在需要时切换 Ruby 版本和 gemsets。

2. 如何安装RVM

   貌似RVM只能使用官网的方法安装，[官网地址](https://rvm.io)

   Install GPG keys:

   ```bash
   # 通过官方的方法
   $ gpg2 --keyserver keyserver.ubuntu.com --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
   
   #也可以使用brew安装
   $ brew install gpg
   ```

   Install RVM:

   ```bash
   $ \curl -sSL https://get.rvm.io | bash -s stable
   ```

3. RVM的常用命令

   1. 更新RVM自己

      ```bash
      $ rvm update
      ```

      

   2. 查看当前使用的ruby版本和gemset信息

      ```bash
      $ rvm info
      ```

      

   3. 查看已安装的ruby列表

      ```bash
      $ rvm list
      ```

      

   4. 查看可安装的所有版本的ruby

      ```bash
      $ rvm list know
      ```

      

   5. 安装某个版本的ruby

      ```bash
      $ rvm install ruby_version
      ```

      

   6. 卸载某个版本的ruby

      ```bash
      $ rvm remove ruby_version
      ```

      

   7. 选择使用某个版本的ruby，并且设置为默认

      ```bash
      $ rvm use ruby_version --default
      ```

      

   8. 将默认 Ruby 版本设置为系统中的默认版本

      ```bash
      $ rvm use --default
      ```

      

   9. 切换到系统安装的 Ruby 版本

      ```bash
      $ rvm use sysytem
      ```

         
   
   10. 创建一个新的 gemset，用于隔离不同项目的 gem 依赖。
   
       ```bash
       $ rvm gemset create gemset_name
       ```
   
       
   
   11. 选择要使用的 gemset。
   
       ```bash
       $ rvm gemset use gemset_name
       ```
   
   12. 创建一个别名以便于切换 Ruby 版本，切换的时候就可以使用别名
   
       ```bash
       $ rvm alias create alias_name ruby_version
       ```
   
   13. 删除一个 Ruby 版本别名
   
       ```bash
       $ rvm alias delete alias_name
       ```



**白嫖**

[RVM玩法总结](http://homeway.github.io/tutorial/rvm.html)

### Gem

1. 什么是Gem

   Gem 是 Ruby 的包管理工具，用于管理和分发 Ruby 应用程序和库。Gem 允许开发者轻松地安装、更新和卸载 Ruby 库和应用程序。许多 Ruby 库和框架都以 gem 的形式提供，开发者可以使用 gem 命令来管理它们。通过 Gem，您可以方便地共享自己的 Ruby 代码或使用其他人创建的 gem，这极大地促进了 Ruby 社区中的代码共享和复用

2. 如何安装Gem

   1. macos系统自带ruby和gem，通过brew安装ruby也会自动安装gem

      

1. Gem常用命令

   1. gemset源
   
      ```bash
      # 查看
      $ gem sources -l
      # 添加
      $ gem sources -a url地址
      # 更新
      $ gem sources -u
      # 删除
      $ gem sources -r url地址
      ```
   
      自带的为：https://rubygems.org/   因为网络原因可以替换为： [https://ruby.taobao.org](https://ruby.taobao.org/)
   
   2. 更新gemset
   
      ```bash
      # 更新RubyGems软件 
      $ gem update --system 
      ```
   
      
   
   3. 列出已安装的gem
   
      ```bash
      $ gem list
      ```
   
      
   
   4. 搜索 gem 库以查找与关键字匹配的 gem
   
      ```bash
      $ gem search keyword
      ```
   
      
   
   5. 安装一个 gem
   
      ```bash
      $ gem install gem_name
      ```
   
      
   
   6. 卸载一个 gem
   
      ```bash
      $ gem uninstall gem_name
      ```
   
      
   
   7. 更新一个 gem 到其最新版本
   
      ```bash
      $ gem update gem_name
      
      # 更新所有的gem软件
      $ gem update
      ```
   
      
   
   8. 清理不再使用的旧 gem 版本
   
      ```bash
      $ gem cleanup
      ```
   
      
   
   9. 显示关于 RubyGems 环境的信息，包括 gem 存储路径等
   
      ```bash
      $ gem environmen
      ```
   
      
   
   10. 获取有关特定 gem 的详细信息，包括版本、作者和描述。
   
       ```bash
       $ gem info gem_name
       ```
   
       
   
   11. 查找特定 gem 的安装路径。
   
       ```bash
       $ gem which gem_name
       ```
   
       
   
   12. 从 gem 规范文件构建一个 gem 文件
   
       ```bash
       $ gem build gemspec_file
       ```
   
       
   
   13. 将自己创建的 gem 发布到 RubyGems.org 或其他 gem 仓库
   
       ```bash
       $ gem push gem_file
       ```
   
       
