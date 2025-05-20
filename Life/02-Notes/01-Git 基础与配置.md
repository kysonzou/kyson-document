---
category:
  - Tech
tags:
  - Git
status: Done
---
本笔记主要涵盖 Git 的基础设置、仓库的初始化与克隆，以及 `.gitignore` 文件的使用，这些是开始使用 Git 进行版本控制的最初步骤。

## 一、Git 基本设置

在开始使用 Git 前，需要配置个人信息，这些信息会嵌入到你的每一次提交中。

1.  **设置用户名和邮箱**：
    ```bash
    git config --global user.name "你的用户名"
    git config --global user.email "你的邮箱"
    ```
    示例：
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "youremail@example.com"
    ```
    * `--global`: 表示这个配置应用于当前用户的所有 Git 仓库
    * `--local` (仅当前仓库) 
    - `--system` (系统所有用户) 级别
    - 优先级为 `local > global > system`。

2.  **查看 Git 配置**：
    ```bash
    git config --list
    git config user.name # 查看具体某项配置
    ```

3.  **设置默认分支名 (可选, 推荐为 `main`)**:
    从 Git 2.28 版本开始，`init.defaultBranch` 可以用来指定新仓库的默认分支名。很多社区已从 `master` 迁移到 `main`。
    ```bash
    git config --global init.defaultBranch main
    ```

4.  **配置文件位置**:
    * `--global` 配置通常在用户主目录下的 `.gitconfig` 文件中 (例如 `~/.gitconfig` 或 `~/.config/git/config`)。
    * `--local` 配置在当前仓库的 `.git/config` 文件中。

## 二、仓库操作

1.  **初始化仓库**：在当前目录创建一个新的 Git 仓库。
    ```bash
    git init
    ```
    这会在当前目录下创建一个 `.git` 子目录，其中包含了初始的 Git 仓库骨架。

2.  **克隆仓库**：从远程仓库复制一个完整的仓库到本地。
    ```bash
    git clone <仓库URL>
    git clone <仓库URL> <本地目录名> # 克隆到指定目录
    ```
    示例：
    ```bash
    git clone https://github.com/example/repo.git my-project
    ```

## 三、`.gitignore` 文件

指定项目中不需要被 Git跟踪的文件和目录模式。这些文件不会出现在 `git status` 的未跟踪列表里，`git add .` 也不会添加它们。

*   创建一个名为 `.gitignore` 的纯文本文件，通常放在项目根目录。
*   每一行指定一个忽略模式。
*   示例：
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
*   `.gitignore` 文件本身也应该被添加到 Git 仓库中并提交。