---
category:
  - Tech
tags:
  - Git
status: Done
---

“分离 HEAD” (Detached HEAD) 状态是 Git 中的一个特殊状态，理解它对于灵活使用 Git 非常重要。

**首先，理解什么是 `HEAD`：**

在 Git 中，`HEAD` 是一个特殊的指针，它通常指向你**当前所在本地分支的最新提交**。当你提交新的更改时，你所在的分支指针会向前移动，而 `HEAD` 也会跟着这个分支指针移动。所以，`HEAD` 通常是一个指向分支的符号引用（例如，`HEAD -> refs/heads/main`）。

**什么是“分离 HEAD”状态？**

当 `HEAD` 指针**不指向一个本地分支名，而是直接指向一个特定的提交哈希 (commit SHA-1) 或一个标签 (tag)** 时，你就进入了“分离 HEAD”状态。

你可以把这种情况想象成：你直接跳到了 Git 历史长河中的某一个特定的时间点（某一个提交），而不是站在某条河流（分支）的尽头。

**如何进入“分离 HEAD”状态？**

最常见的几种方式是：

1. **`git checkout <commit-hash>`**：当你检出某一个具体的提交哈希时。

    ```Bash
    git switch a1b2c3d4
    ```

2. **`git checkout <tag-name>`**：当你检出某一个标签时（因为标签也是指向特定提交的）。

    ```Bash
    git switch v1.0.0
    ```

3. **`git switch <remote-branch-name>`**：当你直接检出远程跟踪分支时（例如 `git checkout origin/main`）。这种情况下，你实际上是检出了远程分支所指向的那个提交，而不是创建了一个本地分支来跟踪它。

**处于“分离 HEAD”状态时会发生什么？**

1. **工作目录更新**：你的工作目录中的文件会更新，以匹配 `HEAD` 当前指向的那个特定提交的内容。
    
2. **警告信息**：Git 通常会给出一个提示信息，告诉你正处于“分离 HEAD”状态，并解释这意味着什么，例如：
    
    ```
    You are in 'detached HEAD' state. You can look around, make experimental
    changes and commit them, and you can discard any commits you make in this
    state without impacting any branches by switching back to a branch.
    
    If you want to create a new branch to retain commits you create, you may
    do so (now or later) by using -c with the switch command. Example:
    
      git switch -c <new-branch-name>
    
    Or undo this operation with:
    
      git switch -
    
    Turn off this advice by setting config variable advice.detachedHead to false
    ```
    
3. **进行修改和提交**：
    
    - 你**可以**在这个状态下进行修改和创建新的提交。
    - 这些新的提交会直接附加到 `HEAD` 当前指向的那个提交之后，形成一条匿名的、不属于任何分支的提交链。
    - `HEAD` 指针会随着你的新提交向前移动。
4. **潜在的“丢失”提交**：
    
    - **这是分离 HEAD 状态最需要注意的一点！** 如果你在分离 HEAD 状态下创建了一些新的提交，然后你切换回了某个已存在的分支 (例如 `git checkout main` 或 `git switch main`)，而**没有为这些新提交创建一个新的分支来指向它们**，那么这些在分离 HEAD 状态下创建的提交就会变得“悬空”（unreachable）。
    - 虽然这些提交仍然存在于 Git 的对象数据库中一段时间，但没有任何分支或标签指向它们，它们最终会被 Git 的垃圾回收机制 (`git gc`) 清理掉，从而导致这些工作丢失。

**如何处理“分离 HEAD”状态下的工作？**

如果你在分离 HEAD 状态下做了一些有用的修改并创建了提交，并且希望保留这些工作，你有以下选择：

1. **基于当前 `HEAD` 创建一个新的分支**：这是最推荐的做法。
    
    ```Bash
    # 假设你已经在分离 HEAD 状态并做了一些提交
    git switch -c new-feature-branch  # 或者 git checkout -b new-feature-branch
    ```
    
    这条命令会创建一个名为 `new-feature-branch` 的新分支，让它指向你当前 `HEAD`（即你在分离 HEAD 状态下创建的最新提交），然后将 `HEAD` 切换到这个新分支上。现在你的工作就在一个正式的分支上了，不会丢失。
    
2. **基于当前 `HEAD` 创建一个标签**：
    
    ```Bash
    git tag my-experimental-tag
    ```
    
    这会为当前 `HEAD` 指向的提交创建一个标签，这样即使你切换到其他分支，也可以通过这个标签找回这些提交。但通常，为了继续开发，还是会创建一个分支。

**什么时候使用“分离 HEAD”状态？**

- **查看历史版本**：当你只想快速查看项目过去的某个特定状态（某个旧的提交或某个发布的标签版本）时，而不需要立即在其基础上进行修改。
- **进行临时实验**：如果你想在一个旧版本的基础上做一些快速的、不确定是否要保留的实验性修改，可以在分离 HEAD 状态下进行。如果实验成功，再创建一个分支来保存。
- **代码审查**：有时，CI/CD 系统或代码审查工具可能会检出特定的提交（例如 Pull Request 中的某个提交）进行检查，这时就会处于分离 HEAD 状态。
- **创建补丁或进行 bisect**：在进行某些高级 Git 操作时，可能会临时进入分离 HEAD。

**总结：**

“分离 HEAD”状态意味着你的 `HEAD` 指针直接指向了一个具体的提交，而不是一个分支。这对于查看历史和进行临时实验很有用，但如果你在这个状态下创建了新的提交，并且希望保留它们，**务必记得在切换回其他分支之前，为这些提交创建一个新的分支。** 否则，这些提交就有丢失的风险。