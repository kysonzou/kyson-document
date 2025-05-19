---
category:
  - Tech
tags:
  - Git
status: Done
---
本文档专门介绍 Git 的 `stash` (储藏) 功能。当你需要临时切换分支或处理紧急事务，但当前工作区的修改还不想提交时，`git stash` 是一个非常有用的工具。

## 一、理解 `git stash`

*   **作用**：将工作区的未提交更改 (已跟踪文件) 和暂存区的更改保存到一个临时的“储藏栈”中，并将工作区恢复到干净状态 (即 HEAD 的状态)。
*   **特点**：主要用于临时保存工作区的更改，不涉及提交记录。默认不保存未跟踪 (untracked) 或被忽略 (ignored) 的文件。
*   **使用场景**：开发中途需要切换分支修复 Bug，或拉取最新代码，但当前工作不想立即提交。

## 二、`git stash` 常用命令

1.  **保存当前更改 (Stash)**：
    ```bash
    git stash push -m "可选的储藏描述信息"
    git stash # 简单储藏，不带描述 (git stash push 的简写)
    # git stash save "可选的储藏描述信息" # 旧版命令，与 push 类似，现已不推荐
    git stash -u # 或者 git stash push --include-untracked，储藏时包含未跟踪文件
    git stash -a # 或者 git stash push --all，储藏时包含未跟踪和被忽略文件
    ```

2.  **查看储藏列表**：
    ```bash
    git stash list
    ```
    输出类似于：`stash@{0}: On main: My feature work`

3.  **应用储藏 (Apply Stash)**：
    将储藏的更改应用回工作区，储藏记录仍然保留在栈中。
    ```bash
    git stash apply stash@{N} # 应用指定的储藏，N是编号，如 stash@{0}
    git stash apply # 默认应用最近的储藏 (stash@{0})
    ```

4.  **应用并移除储藏 (Pop Stash)**：
    将储藏的更改应用回工作区，并从储藏栈中移除该储藏记录。
    ```bash
    git stash pop stash@{N}
    git stash pop # 默认应用并移除最近的储藏
    ```
    **注意**：如果在应用储藏时发生冲突，`git stash pop` 不会自动移除储藏，需要手动解决冲突后使用 `git stash drop stash@{N}` 来移除。

5.  **查看储藏内容**：
    ```bash
    git stash show stash@{N} # 查看储藏的概要改动 (文件名列表)
    git stash show -p stash@{N} # 查看储藏的详细改动 (diff)
    ```

6.  **删除储藏**：
    ```bash
    git stash drop stash@{N} # 删除指定的储藏
    git stash clear # 清空所有储藏
    ```

7.  **从储藏创建分支**：
    如果你储藏的更改比较大，想在一个新分支上继续工作：
    ```bash
    git stash branch <新分支名> stash@{N}
    ```
    这会创建一个新分支，检出到该分支，应用指定的储藏，然后如果应用成功，则删除该储藏。