### .DS_Store

.DS_Store 是Mac os 系统自动创建的，存储「访达」打开文件夹时自动显示方式的首选项，以便文件夹以创建者预期的方式显示。在默认情况下，Git会把 DS_Store 文件带入版本控制的范围内，但是我们并不需要对.DS_Store进行版本控制，所以可以手动将其踏入 Git 的版本管理忽略列表（.gitignorel）即可。

### .gitignorel

`.gitignore` 文件是一个文本文件，它告诉 git 不要跟踪特定的文件、目录或文件类型。

通常，可以通过以下两种方式之一获取 `.gitignore` 文件：

- 您自己创建 `.gitignore` 文件并手动将规则添加到文件中

- 从一个与您使用的语言和框架一致的现有项目中的 `.gitignore` 文件复制过来。


### .gitattributes

`.gitattributes` 文件用于配置 Git 仓库中文件的属性，以影响 Git 在处理这些文件时的行为。这些属性可以用于控制文本文件的换行符处理、二进制文件的处理、合并策略和其他文件处理相关的设置。

1. **换行符处理**：在不同的操作系统中，行结束符可以是不同的。Unix 和 Linux 使用 LF（换行），而 Windows 使用 CRLF（回车换行）。这种差异可能会导致在协作开发中出现问题。通过 `.gitattributes` 文件，您可以指定文本文件的换行符处理方式，以确保一致性。

   ```plaintext
   # 1.在.gitattributes中设置换行符规则，Git 自动将文本文件的行结束符转换为适合当前操作系统的格式。
   * text=auto
   
   # 2.告诉git使用lf作为行结束符（Unix 和 Linux 使用）
   *.js text eol=lf
   
   # 3.告诉git使用crlf作为行结束符（ Windows 使用，回车换行）
   *.json text eol=crlf
   ```

2. **二进制文件标记**：有些文件是二进制文件，如图片、音频、视频等。对于这些文件，Git 不应该尝试进行文本差异比较或合并。通过 `.gitattributes` 文件，您可以标记哪些文件是二进制文件。

   ```plaintext
   # 在.gitattributes中标记文件为二进制
   *.jpg binary
   *.png binary
   ```

3. **合并策略**：有时候，您可能需要为特定类型的文件指定合并策略，以控制 Git 在合并分支时如何处理冲突。

   ```plaintext
   # 在.gitattributes中设置合并策略
   *.xml merge=xmlmerge
   ```

   这将告诉 Git 在合并 XML 文件时使用名为 `xmlmerge` 的自定义合并驱动程序。

   常见的合并策略有：

   - **union**：这是 Git 默认的合并策略，它会尝试将两个分支的更改合并到一个新的合并结果中。如果有冲突，它将会标记出来，需要手动解决。
   - **ours**：这个策略会自动接受当前分支的更改，忽略其他分支的更改。这就意味着，如果有冲突，将会选择当前分支的更改，而不是其他分支的更改。
   - **theirs**：这个策略与ours相反，它会自动接受其他分支的更改，忽略当前分支的更改。如果有冲突，将会选择其他分支的更改。
   - **custom**：您还可以自定义合并策略，为其指定一个自定义的合并驱动程序。这需要额外的配置和脚本，以便 Git 知道如何合并特定类型的文件。

4. **diff属性**：您可以使用 `.gitattributes` 文件指定某些文本文件的diff属性，

   ```plaintext
   # 1.算法 diff，使用指定的自定义 diff 算法合并
   *.cpp diff=cpp
   
   # 2.高亮文件的 diff，使用 Pygments 进行 Python 代码的 diff，以改进差异的可读性
   *.py diff=python
   ```

   常见diff算法有：

   - **默认算法**：如果不明确指定 diff 算法，Git 将使用默认的算法。这通常是一种基于行的 diff 算法，它会比较文件的每一行以检测更改。
   - **patience**：Patience diff 算法试图找到一种较好的方式来对待行的重排，以便更容易理解合并冲突。
   - **minimal**：Minimal diff 算法尝试找到最小的差异集，以便更紧凑地表示文件更改。
   - **histogram**：Histogram diff 算法会尝试平衡差异块的大小，以提高可读性。
   - **自定义算法**：

5. **fitter属性**：用于定义 Git 中的过滤器，这些过滤器可以用于处理文件内容，过滤器通常用于对文件进行自动转换、加密、解密或其他自定义操作。

   ```plaintext
   # 1.使用自定义过滤器进行文件内容转换，也可以使用 smudge 和 clean 过滤器来自动压缩和解压缩文件
   *.gz filter=compress
   # 然后，您可以配置 Git 使用自定义的压缩和解压缩脚本来处理这些文件。
   
   # 2.使用加密和解密过滤器，以保护敏感数据。
   secret.txt filter=encrypt diff=encrypt
   # 在这种情况下，您需要编写自定义加密和解密脚本，并将其配置为 Git 过滤器。
   
   # 3.使用自动格式化过滤器，确保提交到仓库的代码始终保持一致的格式
   *.cpp filter=format-cpp
   # 这将要求您创建自定义的代码格式化脚本，并在提交和检出时应用它。
   
   # 4.根据环境使用不同的配置文件，例如，您可以在开发环境和生产环境之间切换不同的数据库连接字符串。
   config.ini filter=config-env
   # 这需要编写自定义脚本以根据环境进行适当的配置。
   
   # 5.对二进制文件应用自定义过滤器，满足特定需求，例如转换图像格式或解密二进制数据。
   *.bin filter=custom-binary-filter
   #这需要编写适用于您的需求的自定义二进制过滤器脚本。
   ```

6. **Git LFS（Large File Storage）配置**：您可以使用 `.gitattributes` 文件来配置 Git LFS，以便管理大文件。这些文件将被存储在 Git LFS 中，而不是直接在 Git 仓库中，以减小仓库大小。

   ```plaintext
   # 配置 Git LFS
   *.jpg filter=lfs diff=lfs merge=lfs -text
   *.mp4 filter=lfs diff=lfs merge=lfs -text
   ```

7. **自定义文件编码**：如果您的项目包含不同的文本文件编码（如 UTF-8 和 ISO-8859-1），您可以在 `.gitattributes` 中指定文件编码。

   ```plaintext
   # 指定编码为 UTF-8
   *.txt encoding=utf-8
   ```

8. **文件清单生成**：您可以使用 `.gitattributes` 文件来生成文件清单，用于自动化任务或生成文档。

   ```plaintext
   # 生成文件清单
   filelist.txt export-subst
   ```

9. **Git属性宏**：您可以在 `.gitattributes` 文件中定义属性宏，以便轻松应用相同的属性规则到多个文件。

   ```plaintext
   # 定义属性宏
   *.html macro
   ```

10. **忽略文件模式**

    ```plaintext
    # 指定要在 .gitignore 中忽略的文件模式
    *.log export-ignore
    ```

通过定制 `.gitattributes` 文件，您可以更好地管理和控制 Git 仓库中的文件，以适应特定的项目需求和开发环境。这有助于确保代码的一致性和可移植性，并减少潜在的合并冲突和问题。

**ChatGPT总结**

```plaintext
# .gitattributes 文件

# 1. 什么是 .gitattributes 文件？
#    - .gitattributes 文件用于配置 Git 仓库中文件的属性，以控制 Git 处理文件时的行为。

# 2. .gitattributes 文件有什么用？
#    - 定义文本文件的换行符处理方式，以确保跨平台协作时的一致性。
#    - 标记二进制文件，防止 Git 尝试对其进行文本差异比较和合并。
#    - 指定合并策略，控制文件合并冲突的处理方式。
#    - 指定文本文件的 diff 算法，影响比较和合并的精确性和性能。

# 3. 如何使用 .gitattributes 文件？
#    - 在 Git 仓库的根目录或子目录中创建一个名为 .gitattributes 的文件。
#    - 在文件中为不同的文件类型或模式定义属性，使用通配符和关键字指定属性。
#    - 提交 .gitattributes 文件到 Git 仓库，以使其生效。

# 4. .gitattributes 文件可以解决什么问题？
#    - 解决跨平台开发中的换行符问题，确保一致的行结束符。
#    - 防止 Git 对二进制文件进行错误的文本差异比较和合并。
#    - 自定义合并策略以处理文件合并冲突。
#    - 控制文本文件比较和合并的精确性和性能。

# 5. 注意事项：
#    - .gitattributes 文件中的规则是按顺序处理的，上面的规则可能会覆盖下面的规则，所以谨慎排序。
#    - 确保您的 .gitattributes 文件符合项目需求和开发环境的要求，以避免潜在的问题。

# 6. 示例：
#    - 下面是一些 .gitattributes 文件的示例：

#    # 设置文本文件的换行符规则
#    * text=auto

#    # 标记文件为二进制
#    *.jpg binary
#    *.png binary

#    # 使用自定义合并策略
#    *.xml merge=xmlmerge

#    # 使用自定义 diff 算法
#    *.cpp diff=cpp
```

**如果你的项目已经存在很久，但是想添加 .gitattributes 文件来统一行尾序列，下面就介绍一下相关方法。**

1. 添加相关的 .gitattributes 文件到项目
2. 运行 `git add .` 添加所有文件
3. 运行 `git commit -m "Saving files before refreshing line endings"` 来保存本次更改
4. 删除所有文件，不包括 .git 目录，`git rm -rf --cached .`
5. 运行 `git reset --hard HEAD`，恢复上一次的提交，这里会得到正确的行尾序列

[.gitattributes 正确使用姿势](https://juejin.cn/post/7084885453920272398)

### GitHub引用单个文件链接

将自己自定义的科学上网的配置文件托管到GitHub上，客户端通过链接引用文件，以后修改就直接修改Github上面的内容，然后客户端更新就可以了，不用和以前一样手动去替换。

一开始以为链接就是简单的仓库链接+文件目录，这样不对，不是有效链接

>https://github.com/kysonzou/Magic-Internet.git/rule/clashX.yaml
>
>Not Found

然后发现Github文件页面有一个permalink（永久链接），这也不对，这是这个页面的链接，不是文件内容的链接

>https://github.com/kysonzou/Magic-Internet/blob/57591bb6c552ebd354299bbf04d42504f1f33590/rule/clashX.yaml
>
>是网页的链接

有个Raw（原始的）表示的是文件原始内容的意思，但是它直接显示的链接也不对

>https://external.github.com/https/raw.githubusercontent.com/kysonzou/Magic-Internet/main/rule/clashX.yaml
>
>在浏览器可以打开，但是在clashX客户端无效，这个地址看着就很奇怪

!< 后来发现不是Raw是错的，而是因为那时候我是通过githubfast去链接的，所以给了一个这么奇怪的地址。Raw的正常链接就是下面的，话说加fast是真的好使 

后来通过对比其它github项目的链接依葫芦画瓢拼成了正确的引用链接

>https://raw.githubusercontent.com/kysonzou/Magic-Internet/main/rule/clashX.yaml 
>
> https://raw.githubusercontent.com/kysonzou/Magic-Internet/main/rule/shadowrocket.conf
>
>和前面的对比其实就是改一下就可以了 