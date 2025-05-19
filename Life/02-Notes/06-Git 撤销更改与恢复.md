---
category:
  - Tech
tags:
  - Git
status: Done
---
本文档主要涵盖如何在 Git 中撤销不同阶段的更改，包括工作区、暂存区的修改，以及已提交的更改。介绍了 `git restore`, `git reset`, `git revert` 等核心命令，并包括了 Git 的“后悔药” `git reflog`。

## 一、撤销工作区和暂存区的更改

1.  **取消添加到暂存区的更改 (Unstage Files - `git restore --staged`)**：
    将文件从暂存区移回工作区，但工作区的修改内容不变（即撤销 `git add`）。
    ```bash
    git restore --staged <文件名>  # Git 2.23+ 版本，推荐使用
    git restore --staged .       # 取消暂存所有文件

    # 旧版 Git (2.23 之前) 完成相同操作的命令：
    # git reset HEAD <文件名>
    # git reset HEAD .
    ```
    示例：
    ```bash
    git add file1.txt
    git restore --staged file1.txt # file1.txt 从暂存区移回，修改仍在工作区
    ```

2.  **放弃工作区的更改 (Discard Changes in Working Directory - `git restore`)**：
    将工作区的文件恢复到最近一次提交或暂存的状态。**此操作会丢失工作区的修改，请谨慎使用！**
    ```bash
    git restore <文件名> # Git 2.23+ 版本，推荐使用
    git restore .        # 放弃当前目录下所有已跟踪文件的更改

    # 传统方式 (git checkout -- <文件名>)，但 restore 更清晰：
    # git checkout -- <文件名>
    ```
    **警告**：这些命令会直接丢弃工作区的更改，且通常无法轻易恢复。

## 二、撤销已提交的更改 (Reset & Revert)

撤销已提交的更改需要非常小心，特别是 `git reset --hard`。

1.  **`git reset` (重置)**:
    主要用于将当前分支的 HEAD 指针指向某个特定的提交，并可选地修改暂存区和工作区。**如果提交已推送到远程共享仓库，应避免使用 `reset` 修改共享历史，考虑使用 `revert`。**
    *   **软重置 (`--soft`)**: 移动 HEAD 指针，但不改变暂存区和工作区。已提交的更改会回到暂存区。
        ```bash
        git reset --soft <commit-id>
        # 例如：git reset --soft HEAD~1  (撤销上一次提交，更改放回暂存区)
        ```
        用途：合并多个小提交，或修改上个提交的内容/信息（之后需重新commit）。

    *   **混合重置 (`--mixed`)**: 默认模式。移动 HEAD 指针，并重置暂存区，但不改变工作区。已提交的更改会回到工作区变为未暂存状态。
        ```bash
        git reset <commit-id>
        git reset --mixed <commit-id> # 与上一条命令效果相同
        # 例如：git reset HEAD~1 (撤销上一次提交，更改放回工作区，变为未暂存)
        ```
        用途：撤销提交并重新组织暂存内容。

    *   **硬重置 (`--hard`)**: 移动 HEAD 指针，并重置暂存区和工作区，使其与目标提交完全一致。**此操作会永久丢失目标提交之后的所有提交和工作区/暂存区的未提交更改，请极度谨慎使用！**
        ```bash
        git reset --hard <commit-id>
        # 例如：git reset --hard HEAD~1 (彻底丢弃上一次提交及其更改)
        # 例如：git reset --hard origin/main (使本地分支与远程分支完全一致，丢弃本地所有未推送的提交和更改)
        ```
        用途：彻底放弃某些提交和更改。

2.  **`git revert` (回滚)**:
    创建一个新的提交，该提交的内容是指定提交的“反向”操作。它不会修改项目历史，而是向前追加一个新的提交来撤销效果。**这是推荐的撤销已推送到远程仓库的提交的方式。**
    ```bash
    git revert <commit-id>
    git revert HEAD # 创建一个新提交，撤销上一次提交的更改
    ```
    *   **优点**: 安全，因为它不改变现有历史，适合已经推送到共享仓库的提交。
    *   **场景**: 当需要撤销公共历史中的某个错误提交时。

3.  **恢复单个文件到某个提交的状态 (`git checkout <commit-id> -- <file>` 或 `git restore --source=<commit-id> <file>`)**:
    ```bash
    # 使用 checkout (传统方式)
    git checkout <commit-id> -- <文件路径>

    # 使用 restore (Git 2.23+，更推荐)
    git restore --source=<commit-id> <文件路径>
    ```
    这会用指定提交中的文件版本覆盖工作区和暂存区中的该文件。**此操作也会丢失该文件当前未提交的修改。**

## 三、引用日志 (`git reflog`) - Git 的后悔药

Git 的“后悔药”。`reflog` 记录了 HEAD 和分支引用在过去几个月内的移动历史（默认90天）。即使你删除了分支或用 `reset --hard` 丢弃了提交，只要它们还在 `reflog` 中，通常就有机会恢复。
```bash
git reflog
# 输出会显示类似 HEAD@{0}, HEAD@{1} 等引用，以及它们指向的提交和操作
```
如果你意外地重置或删除了某些东西，可以：

1. 使用 git reflog 找到操作发生前的提交 SHA-1。
2. 使用 git reset --hard <SHA-1> 恢复到那个状态，或者 git checkout -b new-branch-name <SHA-1> 在新分支上恢复。