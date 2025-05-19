---
category:
  - Tech
tags:
  - Git
status: Done
---
Git 的分支功能非常强大且轻量，是其核心特性之一。本笔记介绍分支的创建、切换、查看、重命名、删除等本地操作，以及与远程分支相关的跟踪设置和删除远程分支操作，并简要介绍常见的分支使用策略。

## 一、理解分支

*   **什么是分支**：分支是指向某个提交对象的可变指针。Git 的默认分支名通常是 `main` 或 `master`。
*   **HEAD 指针**：一个特殊的指针，通常指向当前工作的本地分支。

## 二、本地分支操作

1.  **查看分支**：
    ```bash
    git branch             # 查看本地分支，当前分支前有 * 号
    git branch -v          # 查看本地分支及其最后一次提交
    git branch -vv         # 查看本地分支及其跟踪的远程分支信息
    git branch --merged    # 查看已合并到当前分支的分支
    git branch --no-merged # 查看尚未合并到当前分支的分支
    ```

2.  **创建新分支**：
    只是创建分支，HEAD 仍然指向当前分支。
    ```bash
    git branch <新分支名>
    git branch <新分支名> <基于某次提交或某分支创建>
    # 例如: git branch feature-x main (基于 main 分支创建 feature-x)
    # 例如: git branch release-v1.0 abc123d (基于 commit abc123d 创建)
    ```

3.  **切换分支**：
    移动 HEAD 指针到指定分支，并更新工作区文件。
    ```bash
    git switch <分支名>     # Git 2.23+ 版本，推荐用于切换分支
    
    # 旧版命令
    # git checkout <分支名>
    ```
    > 在 Git 的早期版本中，`git checkout` 被用来切换分支和恢复文件。从 Git 2.23 版本开始，引入了 `git switch` (切换分支) 和 `git restore` (恢复文件) 以分离这两类操作，使命令语义更清晰。

4.  **创建并切换到新分支**：
    ```bash
    git switch -c <新分支名>        # Git 2.23+ 版本，推荐使用
    git switch -c <基于某次提交或某分支创建>
    
    # 旧版命令
    # git checkout -b <新分支名>
    # git checkout -b <新分支名> <基于某分支创建>
    ```
    示例：
    ```bash
    git switch -c feature/user-login main # 从 main 分支创建并切换到 feature/user-login
    ```

5.  **重命名分支**：
    ```bash
    # 重命名当前分支
    git branch -m <新分支名>
    # 重命名其他本地分支
    git branch -m <旧分支名> <新分支名>
    ```

6.  **删除本地分支**：
    ```bash
    git branch -d <分支名>  # 删除已合并到当前分支或其他上游分支的分支
                           # 如果分支有未合并的提交，此命令会失败

    git branch -D <分支名>  # 强制删除分支，无论是否已合并 (会丢失未合并的提交)
    ```
    **注意**：不能删除当前所在的分支。需要先切换到其他分支。

## 三、与远程分支的关联 (跟踪分支)

1.  **设置上游分支 (Upstream Branch) / 跟踪远程分支**：
    当第一次推送一个新创建的本地分支时，或想将本地分支与特定的远程分支关联起来时，使用 `-u` 或 `--set-upstream` 选项。
    ```bash
    git push -u <远程名> <本地分支名> # 推送并设置上游分支
    # 例如: git push -u origin feature/new-login
    ```
    一旦设置了上游分支，之后在该分支上执行 `git push` 和 `git pull` 就不再需要指定远程名和分支名。

2.  **查看上游分支**：
    ```bash
    git branch -vv
    ```

3.  **更改上游分支**：
    ```bash
    git branch <分支名> --set-upstream-to=<远程名>/<新远程分支名>
    ```

4.  **删除上游关联**：
    ```bash
    git branch <分支名> --unset-upstream
    ```

## 四、删除远程分支

将本地的删除操作同步到远程仓库。
```bash
git push <远程名> --delete <远程分支名>
# 或者使用更晦涩的语法:
git push <远程名> :<远程分支名> # 本地分支名留空
```
示例：
```bash
git push origin --delete feature/old-feature
```

## 五、分支使用策略 (Workflow 例子)

- **Git Flow**: 一个较复杂的模型，包含 master, develop, feature/*, release/*, hotfix/* 等分支。适合大型、有明确发布周期的项目。
- **GitHub Flow**: 简单模型。main 分支始终是可部署的。新工作在特性分支上进行，通过 Pull Request (PR) 讨论和审查，然后合并到 main。
- **GitLab Flow**: 对 GitHub Flow 的扩展，增加了环境分支或发布分支。

选择适合团队规模和项目特点的分支策略很重要。