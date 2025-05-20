---
category:
  - Tech
tags:
  - Git
status: Done
---
本部分涵盖如何查看提交历史、使用标签进行版本标记。

## 一、查看提交历史 (`git log`)

`git log` 命令用于显示提交历史记录。

1.  **基本用法**：
    ```bash
    git log
    ```
    默认按时间倒序显示提交，包括提交的 SHA-1 哈希值、作者、日期和提交信息。按 `q` 退出日志查看。

2.  **常用选项**：
    * **格式化输出**:
        ```bash
        git log --oneline             # 每个提交显示为一行 (精简哈希 + 提交信息)
        git log --graph               # 图形化显示分支合并历史 (通常与 --oneline, --decorate 一起使用)
        git log --decorate            # 显示指向提交的指针 (如分支名、标签名)
        git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short
        # 自定义格式: %h (短哈希), %H (完整哈希), %ad (作者日期), %ar (作者相对日期),
        # %cd (提交者日期), %cr (提交者相对日期), %s (主题/提交信息),
        # %d (修饰, 如分支/标签), %an (作者名), %ae (作者邮箱), %cn, %ce
        ```
    * **限制输出数量**:
        ```bash
        git log -n <数量>             # 例如: git log -3 (显示最近3条)
        git log -<数量>               # 同上
        ```
    * **按时间过滤**:
        ```bash
        git log --since="2 weeks ago"
        git log --until="2024-12-31"
        git log --after="2024-01-01" --before="2024-06-30"
        ```
    * **按作者/提交者过滤**:
        ```bash
        git log --author="作者名或邮箱的部分匹配"
        git log --committer="提交者名或邮箱的部分匹配"
        ```
    * **按提交信息过滤**:
        ```bash
        git log --grep="关键词"       # 搜索提交信息中包含关键词的提交 (区分大小写)
        git log --grep="关键词" -i    # 忽略大小写
        ```
    * **按文件/路径过滤**:
        显示影响了特定文件或路径的提交。
        ```bash
        git log -- <文件路径>
        git log -- <目录路径>/
        # 例如: git log -- src/main/java/
        ```
        注意 `--` 的使用，它用来分隔修订参数和路径参数。

    * **查看文件更改详情**:
        ```bash
        git log -p                    # 显示每个提交的详细差异 (diff)
        git log -p <文件路径>         # 显示特定文件的详细更改历史
        git log --stat                # 显示每个提交中文件的增删统计信息
        ```
    * **按范围显示**:
        ```bash
        git log <分支1>..<分支2>      # 显示在分支2但不在分支1中的提交
        git log <分支1>...<分支2>     # 显示两个分支各自独有的提交 (对称差)
        git log ^<分支1> <分支2>       # 同 <分支1>..<分支2>
        ```

## 二、标签 (Tagging)

标签用于标记项目历史中的特定重要点，通常用于版本发布 (如 `v1.0`, `v2.0-beta`)。

1.  **标签类型**：
    * **轻量标签 (Lightweight Tag)**：像一个不会改变的分支，只是一个特定提交的引用（指针）。
    * **附注标签 (Annotated Tag)**：存储在 Git 数据库中的一个完整对象。它包含打标签者的名字、电子邮件、日期、标签信息，并且通常会进行 GPG 签名和校验。**推荐使用附注标签**，因为它们包含更多信息。

2.  **创建标签**：
    * **创建附注标签**:
        ```bash
        git tag -a <标签名> -m "标签的描述信息"
        git tag -a v1.0.0 -m "Version 1.0.0 release"
        # 给过去的某次提交打标签
        git tag -a v0.9.0 <commit-id> -m "Version 0.9.0 for old commit"
        ```
    * **创建轻量标签**:
        ```bash
        git tag <标签名>
        # 例如: git tag v1.0.0-lw
        ```

3.  **列出标签**：
    ```bash
    git tag                   # 列出所有标签
    git tag -l "v1.*"         # 列出匹配模式的标签 (如 v1 开头的所有标签)
    ```

4.  **查看特定标签信息**：
    ```bash
    git show <标签名>
    ```
    对于附注标签，会显示标签对象信息和该标签指向的提交信息。对于轻量标签，只显示提交信息。

5.  **推送标签到远程仓库**：
    `git push` 命令默认不会传送标签到远程仓库。
    ```bash
    git push <远程名> <标签名>        # 推送单个标签
    # 例如: git push origin v1.0.0

    git push <远程名> --tags         # 推送所有本地尚未在远程的标签
    ```

6.  **删除标签**：
    * **删除本地标签**:
        ```bash
        git tag -d <标签名>
        # 例如: git tag -d v1.0.0-alpha
        ```
    * **删除远程标签**:
        需要先删除本地标签 (如果需要)，然后从远程删除。
        ```bash
        git push <远程名> --delete <标签名>
        # 或者使用旧语法:
        git push <远程名> :refs/tags/<标签名>
        # 例如: git push origin --delete v1.0.0
        ```

7.  **检出标签 (Checkout Tag)**：
    可以将仓库恢复到某个标签指向的状态。这会将你置于“分离 HEAD” (detached HEAD) 状态。
    ```bash
    git switch <标签名>
    # 例如: git checkout v1.0.0
    ```
    如果你想在这个状态上进行修改和新的提交，最好基于这个标签创建一个新的分支：
    ```bash
    git switch -c branch-from-tag-<标签名> <标签名>
    # 例如: git checkout -b hotfix-for-v1.0.0 v1.0.0
    ```
