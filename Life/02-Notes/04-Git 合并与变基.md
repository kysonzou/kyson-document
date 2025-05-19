---
category:
  - Tech
tags:
  - Git
status: Done
---
本笔记聚焦于 Git 中两种主要的分支集成策略：合并 (`git merge`) 和变基 (`git rebase`)。同时，也介绍了 `git cherry-pick` 这一有用的提交复制代码的工具。理解它们的区别和适用场景对于维护清晰、高效的版本历史至关重要。

## 一、合并分支 (Merge)

将一个分支的更改集成到另一个分支。通常是将特性分支合并回主开发分支 (如 `main`)。

1.  **执行合并**：
    首先，切换到接收更改的分支（目标分支）。
    ```bash
    git switch main             # 切换到 main 分支
    git merge <要合并的分支名>  # 例如：git merge feature/user-login
    ```

2.  **合并类型**：
    *   **Fast-forward (快进合并)**：如果目标分支是待合并分支的直接祖先（即目标分支没有任何新的提交），Git 会直接将目标分支指针向前移动到待合并分支的最新提交。不会创建新的合并提交。
        ```bash
        # 可以用 --no-ff 来禁用快进合并，强制创建一个合并提交
        git merge --no-ff <要合并的分支名>
        ```
    *   **Three-way Merge (三方合并)**：如果两个分支自共同祖先以来都有各自的提交，Git 会执行三方合并。它会找到共同祖先、目标分支的最新提交、待合并分支的最新提交，然后将这两方的更改合并起来，并自动创建一个新的**合并提交 (merge commit)**。

3.  **解决合并冲突 (Merge Conflicts)**：
    如果在不同分支上修改了同一个文件的同一部分，Git 无法自动决定如何合并，就会发生合并冲突。此时，Git 会暂停合并过程，并在冲突文件中标记出冲突区域。
    *   **识别冲突文件**：`git status` 会列出未合并 (unmerged) 的路径。
    *   **手动解决冲突**：打开冲突文件，查找类似如下的标记：
        ```
        <<<<<<< HEAD (当前分支的更改)
        // code from current branch (e.g., main)
        =======
        // code from the branch being merged (e.g., feature/user-login)
        >>>>>>> feature/user-login (被合并分支的更改)
        ```
        你需要手动编辑文件，删除这些标记，并决定保留哪些内容或如何组合它们。
    *   **标记为已解决**：解决完所有冲突后，使用 `git add <冲突文件名>` 将文件标记为已解决。
    *   **完成合并**：当所有冲突都解决并 `git add` 之后，执行 `git commit` 来完成合并。Git 通常会自动生成一个合并提交信息。
        ```bash
        # 如果在合并过程中想中止合并，恢复到合并前的状态：
        git merge --abort
        ```

## 二、变基 (Rebase)

变基是另一种将一个分支的更改集成到另一个分支的方法。它会将当前分支的提交逐个“重新播放”到目标分支的最新提交之上，形成一条更线性的提交历史。

1.  **执行变基**：

    1.  **场景一：在特性分支上与远程主分支保持同步 (推荐的日常操作)**
    
        当你正在 `feature-branch` 上开发，希望定期将远程 `main` (或 `develop` 等) 分支的最新更改集成到你的特性分支，以确保你的工作基于最新的主线代码，并保持提交历史线性。
    
        ```bash
        # 确保你在你的特性分支上
        git switch feature-branch
    
        # 从远程仓库获取最新的数据，包括远程 main 分支的更新
        git fetch origin  # 假设你的远程仓库名为 origin
    
        # 将当前特性分支 (feature-branch) 的提交变基到最新的远程 main 分支 (origin/main) 之上
        git rebase origin/main
        ```
        *   **效果**：`feature-branch` 的提交历史会基于 `origin/main` 的最新状态重新构建。
        *   **优点**：这是与远程主线保持同步最直接、最不容易出错的方式。
    
    2.  **场景二：准备将特性分支合并回主分支 (本地整理流程)**
    
        在计划将本地的 `feature-branch` 合并回本地的 `main` 分支之前，你可能希望先确保 `feature-branch` 包含了 `main` 分支的所有最新提交，并且其历史是线性的，以便后续能进行“快进合并”。
    
        **步骤：**
        *   **a. 更新本地 `main` 分支：**
            ```bash
            git switch main
            git pull origin main # 或者 git fetch origin; git merge origin/main
            ```
        *   **b. 在特性分支上同步更新后的本地 `main`：**
            ```bash
            git switch feature-branch
            git rebase main # 将 feature-branch 变基到更新后的本地 main 分支
            ```
        *   **c. 合并到主分支：**
            完成变基后，如果特性分支之前被推送过并且历史被改变，可能需要强制推送 (`git push --force-with-lease origin feature-branch`)。
            然后可以将整理好的特性分支合并回 `main`：
            ```bash
            git switch main
            git merge feature-branch # 此时通常会是快进合并 (fast-forward)
            ```

2.  **变基与合并的区别**：
    *   **历史记录**：
        *   `merge`：保留原始的分支历史，通过合并提交连接分支。历史是分叉的，但更“真实”。
        *   `rebase`：重写提交历史，将一系列提交应用到新的基点上，形成线性的历史记录。历史更“整洁”，但与原始提交不同 (SHA-1 值会改变)。
    *   **冲突解决**：
        *   `merge`：所有冲突在一次合并操作中解决，然后创建一个合并提交。
        *   `rebase`：可能会在“重放”每个提交时多次遇到冲突，需要逐个解决。

3.  **交互式变基 (`rebase -i`)**：
    一个非常强大的工具，允许你在变基过程中修改、合并、编辑、删除或重新排序提交。
    ```bash
    git rebase -i <基提交或分支>
    # 例如，整理当前分支最近的3个提交：
    git rebase -i HEAD~3
    ```
    执行后会打开一个编辑器，列出相关的提交，你可以修改每行前面的命令 (如 `pick`, `reword`, `edit`, `squash`, `fixup`, `drop`)。

4.  **变基的黄金法则**：
    **永远不要对已经推送到公共仓库并可能被他人使用的分支执行 `rebase` 操作（尤其是修改已共享的提交）。**
    因为变基会重写历史，如果其他人基于旧的历史进行了工作，这会导致严重的协作问题。只在本地私有分支上或在推送到远程之前进行历史清理时使用变基是安全的。

## 三、拣选提交 (`git cherry-pick`)

选取其他分支上的一个或多个提交，并将它们的副本应用到当前分支上。
```bash
git cherry-pick <commit-id1> [<commit-id2> ...]
```
- 用途：例如，将一个在特性分支上修复的 Bug 提交，也应用到主发布分支上，而不需要合并整个特性分支。
- 可能会产生冲突，需要像解决合并冲突一样处理。