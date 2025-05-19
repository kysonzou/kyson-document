---
category:
  - Tech
tags:
  - Git
status: Done
---
本文档主要涵盖 Git 的日常核心文件操作，包括查看状态、添加文件到暂存区、提交更改、修改提交、删除文件以及查看更改差异，这些是版本控制中最常用的命令。

Git 的基本工作流程涉及工作区 (Working Directory)、暂存区 (Staging Area/Index) 和本地仓库 (Local Repository)。

## 一、查看与跟踪文件状态

1.  **查看当前状态 (`git status`)**：
    查看工作目录和暂存区的状态，了解哪些文件被修改、暂存或未被跟踪。
    ```bash
    git status
    git status -s # 简短输出 (short format)
    ```

2.  **添加文件到暂存区 (`git add`)**：
    将工作区的更改添加到暂存区，准备进行提交。
    ```bash
    git add <文件名>       # 添加指定文件
    git add <目录名>/      # 添加指定目录下的所有更改
    git add .            # 添加当前目录下的所有更改 (常用)
    git add :/           # 添加项目根目录下所有文件的更改 (无论当前在哪个子目录)
    ```

3.  **交互式暂存 (`git add -p` 或 `git add --patch`)**：
    允许你逐块地选择一个文件中的哪些修改部分要添加到暂存区。非常适合在一次提交中只包含相关的更改。
    ```bash
    git add -p <文件名>
    ```
    Git 会显示文件中的每个修改块，并询问你是否要暂存它 (`y/n/q/a/d/s/e/?`)。

## 二、提交更改

1.  **提交文件 (`git commit`)**：
    将暂存区的内容永久记录到本地仓库。
    ```bash
    git commit -m "简明的提交信息"
    git commit -am "暂存所有已跟踪文件的修改并提交" # 跳过 git add，只对已跟踪文件有效
    ```
    示例：
    ```bash
    git commit -m "修复：用户登录页面的布局问题"
    ```
    编写好的 Commit Message 非常重要，建议遵循一定的规范 (如 Conventional Commits)。

2.  **修改最后一次提交 (`git commit --amend`)**：
    如果你提交后发现有些小错误（比如遗漏文件或提交信息写错），可以使用 `--amend`。
    ```bash
    # 先 git add 遗漏的文件 (如果需要)
    git add forgotten-file.txt
    git commit --amend -m "新的或修正后的提交信息"
    git commit --amend --no-edit # 使用上一次的提交信息，仅合并暂存区的更改
    ```
    **注意**：如果已经将此提交推送到远程仓库，应谨慎使用 `git commit --amend`，因为它会修改提交历史。如果其他人已经基于这个旧的提交进行了工作，修改历史会导致问题。

## 三、删除文件

1.  **从 Git 中删除文件 (`git rm`)**：
    用于从工作目录和暂存区删除文件，并停止 Git 对该文件的追踪。
    ```bash
    git rm <文件名>             # 从工作区和暂存区同时删除文件
    git rm -f <文件名>            # 强制删除 (如果文件在工作区有修改且未暂存)
    git rm --cached <文件名>    # 仅从暂存区删除 (停止跟踪)，但保留在工作区
    git rm -r <目录名>          # 递归删除目录及其内容
    ```
    执行 `git rm` 后，更改会进入暂存区，需要 `git commit` 来确认删除。

2.  **恢复被 `git rm --cached` 的文件追踪**：
    如果文件还在工作区，并且你想重新开始追踪它：
    ```bash
    # 如果 git rm --cached 操作还未提交
    git restore --staged <文件名> # 撤销暂存区的 rm --cached，然后可以重新 add
    # 或者直接重新 add
    git add <文件名>
    git commit -m "Re-track filename" # 如果已提交，则需要新的提交来重新追踪
    ```

## 四、查看差异 (`git diff`)

比较文件在不同状态（工作区、暂存区、提交历史）之间的差异。

1.  **工作区 vs 暂存区**：查看尚未暂存的修改。
    ```bash
    git diff
    git diff <文件名>
    ```

2.  **暂存区 vs 上次提交 (HEAD)**：查看已暂存但尚未提交的修改。
    ```bash
    git diff --staged
    git diff --cached # 同上
    ```

3.  **工作区 vs 上次提交 (HEAD)**：查看所有未提交的修改 (包括已暂存和未暂存的)。
    ```bash
    git diff HEAD
    ```

4.  **两次提交之间**：
    ```bash
    git diff <commit-id1> <commit-id2>
    git diff <branch1>..<branch2>
    ```