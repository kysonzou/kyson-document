---
category:
  - Tech
tags:
  - Git
status: Done
---

本笔记主要介绍 Git 如何与远程仓库进行交互，包括管理远程仓库配置、从远程仓库获取和拉取数据、将本地更改推送到远程仓库，以及推送和删除远程标签。此外，还介绍了如何使用稀疏检出 (Sparse Checkout) 克隆大型仓库的部分内容。

## 一、远程仓库 (Remotes)

远程仓库是托管在网络上（如 GitHub, GitLab, Bitbucket）或另一台服务器上的你的项目的版本。

1.  **查看远程仓库**：
    ```bash
    git remote              # 列出所有远程仓库的简称 (如 origin)
    git remote -v           # 列出远程仓库的简称及其 URL (fetch 和 push)
    git remote show <远程名> # 查看某个远程仓库的详细信息 (如 origin)
                           # 包括跟踪的远程分支，本地分支配置等
    ```

2.  **添加远程仓库**：
    将本地仓库与一个新的远程仓库关联。
    ```bash
    git remote add <远程名> <仓库URL>
    ```
    示例（通常克隆时会自动添加名为 `origin` 的远程）：
    ```bash
    git remote add origin https://github.com/user/repo.git
    git remote add upstream https://github.com/original-owner/repo.git # 常用于 fork 的项目
    ```

3.  **重命名远程仓库**：
    ```bash
    git remote rename <旧远程名> <新远程名>
    ```

4.  **移除远程仓库**：
    ```bash
    git remote remove <远程名>
    git remote rm <远程名> # 同上
    ```

## 二、从远程仓库获取与拉取数据

1.  **`git fetch` (获取)**：
    从远程仓库下载新的分支、标签和数据到本地仓库，但**不会自动合并或修改你当前的工作**。它只是更新你的本地 `.git/objects` 数据库和远程跟踪分支。
    ```bash
    git fetch <远程名>             # 获取指定远程的所有更新
    git fetch <远程名> <分支名>    # 获取指定远程的特定分支的更新
    git fetch --all                # 获取所有已配置远程的更新
    git fetch --prune              # 在获取前，删除本地不存在对应远程分支的远程跟踪分支
    ```
    获取后，你可以使用 `git log origin/main` (假设远程是 `origin`，分支是 `main`) 查看远程分支的提交历史，或使用 `git diff main origin/main` 比较本地与远程的差异。

2.  **`git pull` (拉取)**：
    `git pull` 本质上是 `git fetch` 和 `git merge` (或 `git rebase`，取决于配置) 的组合。它从远程仓库获取最新版本并立即尝试将其合并到你当前的本地分支。
    ```bash
    git pull <远程名> <远程分支名>[:<本地分支名>]
    # 例如: git pull origin main (拉取 origin/main 并合并到当前分支)
    # 例如: git pull origin main:my-main (拉取 origin/main 到本地的 my-main 分支并合并，如果my-main不存在则创建)
    ```
    如果当前本地分支设置了上游跟踪分支，可以直接使用 `git pull`：
    ```bash
    git pull
    ```
    **使用 Rebase 而不是 Merge 进行 Pull**:
    如果你希望在拉取更新时，将本地未推送的提交变基到远程分支的最新提交之上，以保持线性的历史记录：
    ```bash
    git pull --rebase
    # 可以配置为默认行为
    git config --global pull.rebase true # (或者 false, merges)
    ```

## 三、推送到远程仓库 (Push)

将本地仓库的提交分享到远程仓库。

1.  **基本推送**：
    ```bash
    git push <远程名> <本地分支名>[:<远程分支名>]
    # 例如: git push origin main (将本地 main 分支推送到 origin 远程的 main 分支)
    # 如果远程分支名省略，且本地分支名与远程分支名相同，则可以简化
    # git push origin main
    # 如果本地分支已设置上游跟踪分支，可以直接使用
    git push
    ```

2. **设置上游分支 (Upstream Branch) / 跟踪远程分支**：

    当第一次推送一个新创建的本地分支时，或想将本地分支与特定的远程分支关联起来时，使用 `-u` 或 `--set-upstream` 选项。
    ```bash
    git push -u <远程名> <本地分支名> # 推送并设置上游分支
    # 例如: git push -u origin feature/new-login
    ```
    一旦设置了上游分支，之后在该分支上执行 `git push` 和 `git pull` 就不再需要指定远程名和分支名。
    
3.  **强制推送 (`--force` / `--force-with-lease`)**：
    **警告：强制推送会覆盖远程仓库的历史，可能导致其他协作者丢失工作。请极度小心并仅在确切知道后果时使用！**
    ```bash
    git push --force <远程名> <分支名>
    ```

    ```bash
    git push --force-with-lease <远程名> <分支名>
    ```
    *   **`--force-with-lease`**：一个更安全的选择。它只在远程分支的状态与你本地最后一次获取远程信息时的状态一致时才允许强制推送。如果远程分支在你上次获取后有新的提交，推送会失败，防止意外覆盖他人的工作。
    - 通常用于修改了已推送的提交历史（如通过 `rebase` 或 `commit --amend`）后，需要更新远程分支时。

4.  **推送所有本地分支**：
    ```bash
    git push <远程名> --all # 不常用，且可能推送不想共享的分支
    ```

5.  **推送标签到远程仓库**：
    `git push` 命令默认不会传送标签到远程仓库。
    ```bash
    git push <远程名> <标签名>        # 推送单个标签
    # 例如: git push origin v1.0.0

    git push <远程名> --tags         # 推送所有本地尚未在远程的标签
    ```
6. **删除远程分支**：
    ```bash
    git push <远程名> --delete <远程分支名>
    # 或者使用更晦涩的语法:
    git push <远程名> :<远程分支名> # 本地分支名留空
    ```
    示例：
    ```bash
    git push origin --delete feature/old-feature
    ```
7.  **删除远程标签**：
    需要先删除本地标签 (如果需要，参考 `08-Git-History-Tags.md`)，然后从远程删除。
    ```bash
    git push <远程名> --delete <标签名>
    # 或者使用旧语法:
    git push <远程名> :refs/tags/<标签名>
    # 例如: git push origin --delete v1.0.0
    ```
    (删除远程分支，请参考 `03-Git-Branching.md`)
