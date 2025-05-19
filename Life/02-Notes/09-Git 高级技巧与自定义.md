---
category:
  - Tech
tags:
  - Git
status: Done
---
1.  **`.gitignore` 文件**：
    指定项目中不需要被 Git跟踪的文件和目录模式。这些文件不会出现在 `git status` 的未跟踪列表里，`git add .` 也不会添加它们。
    * 创建一个名为 `.gitignore` 的纯文本文件，通常放在项目根目录。
    * 每一行指定一个忽略模式。
    * 示例：
        ```gitignore
        # 忽略 .env 文件
        .env

        # 忽略所有 .log 文件
        *.log

        # 忽略 node_modules 目录
        node_modules/

        # 忽略 build 输出目录
        build/
        dist/

        # 但不忽略 build/important.txt
        !build/important.txt
        ```
    * `.gitignore` 文件本身也应该被添加到 Git 仓库中并提交。

2.  **`git reflog` (引用日志)**：
    Git 的“后悔药”。`reflog` 记录了 HEAD 和分支引用在过去几个月内的移动历史（默认90天）。即使你删除了分支或用 `reset --hard` 丢弃了提交，只要它们还在 `reflog` 中，通常就有机会恢复。
    ```bash
    git reflog
    # 输出会显示类似 HEAD@{0}, HEAD@{1} 等引用，以及它们指向的提交和操作
    ```
    如果你意外地重置或删除了某些东西，可以：
    1.  使用 `git reflog` 找到操作发生前的提交 SHA-1。
    2.  使用 `git reset --hard <SHA-1>` 恢复到那个状态，或者 `git checkout -b new-branch-name <SHA-1>` 在新分支上恢复。

3.  **`git cherry-pick` (拣选)**：
    选取其他分支上的一个或多个提交，并将它们的副本应用到当前分支上。
    ```bash
    git cherry-pick <commit-id1> [<commit-id2> ...]
    ```
    * 用途：例如，将一个在特性分支上修复的 Bug 提交，也应用到主发布分支上，而不需要合并整个特性分支。
    * 可能会产生冲突，需要像解决合并冲突一样处理。

4.  **交互式暂存 (`git add -p` 或 `git add --patch`)**：
    允许你逐块地选择一个文件中的哪些修改部分要添加到暂存区。非常适合在一次提交中只包含相关的更改。
    ```bash
    git add -p <文件名>
    ```
    Git 会显示文件中的每个修改块，并询问你是否要暂存它 (`y/n/q/a/d/s/e/?`)。

5.  **别名 (Aliases)**：
    为常用的复杂 Git 命令设置简短的别名，提高效率。
    在你的 `.gitconfig` 文件中设置，或通过命令行：
    ```bash
    git config --global alias.co checkout
    git config --global alias.br branch
    git config --global alias.ci commit
    git config --global alias.st status
    git config --global alias.unstage 'reset HEAD --'
    git config --global alias.last 'log -1 HEAD'
    git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
    ```
    之后就可以使用 `git co`, `git br`, `git lg` 等。
