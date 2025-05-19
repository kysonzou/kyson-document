---
category:
  - Tech
tags:
  - Git
status: Done
---
### 1.  克隆仓库
从远程仓库复制一个完整的仓库到本地。

```bash
git clone <仓库URL>
git clone <仓库URL> <本地目录名> # 克隆到指定目录
```
示例：
```bash
git clone https://github.com/example/repo.git my-project
```

### 2. 克隆特定文件夹 (稀疏检出 - Sparse Checkout)

有时候，你可能只需要一个大型仓库中的特定文件夹，而不是整个仓库。Git 2.25.0 及更高版本引入的 `git sparse-checkout` 使得这更容易实现。

这允许你拥有一个完整的 Git 仓库（可以 fetch/pull/push），但工作目录只包含你指定的文件和文件夹。

**步骤：**

1.  **初始化稀疏检出仓库并克隆 (推荐方式)**：
    如果你想在克隆时就指定只检出部分目录，可以这样做：
    ```bash
    # 创建一个目录并进入
    mkdir my-partial-repo
    cd my-partial-repo

    # 初始化 Git 仓库
    git init

    # 添加远程仓库
    git remote add origin <repository-url>

    # 启用稀疏检出模式
    git sparse-checkout init --cone
    # 或者 git config core.sparseCheckout true (旧方式，init --cone 更推荐)

    # 设置要检出的文件夹 (相对于仓库根目录)
    # --cone 模式下，它会自动包含指定目录下的所有文件和子目录
    # 如果是非 --cone 模式，你需要更精确地指定 .git/info/sparse-checkout 文件内容
    git sparse-checkout set "path/to/your/folder1" "another/folder"
    # 例如: git sparse-checkout set "docs" "src/app"

    # 拉取指定分支的内容 (只会填充你指定的文件夹)
    git pull origin <branch-name>
    # 例如: git pull origin main
    ```
    `--cone` 模式是推荐的，因为它更易于管理并且性能更好。它会自动处理父目录和子目录的包含关系。

2.  **在已存在的完整克隆中启用稀疏检出**：
    ```bash
    cd existing-full-clone-repo
    git sparse-checkout init --cone
    git sparse-checkout set "path/to/folder"
    # Git 会自动更新工作目录以匹配新的稀疏检出规则
    ```

3.  **管理稀疏检出模式**：
    *   **查看当前检出模式**：`git sparse-checkout list`
    *   **添加更多目录**：`git sparse-checkout add "new/path"`
    *   **禁用稀疏检出 (检出所有内容)**：`git sparse-checkout disable`
    *   **重新启用并设置**：`git sparse-checkout init --cone` 后接 `git sparse-checkout set ...`

**`sparse-checkout` 与 `pull` 和 `push`：**

*   **`pull`**：`git pull` (或 `git fetch`) 仍然会下载远程仓库对应分支的**所有**元数据和对象。但是，只有那些符合稀疏检出规则的文件和文件夹才会被更新或写入你的工作目录。
*   **`push`**：`git push` 会将你本地分支上**所有**已提交的更改推送到远程仓库，不受稀疏检出配置的影响。稀疏检出主要影响你的本地工作目录，而不是你提交或推送的内容。

**其他只下载部分内容的方式 (非完整 Git 管理)：**

*   **`git archive`**: 下载特定分支/提交下某个文件夹的快照 (zip 或 tar)。
    ```bash
    git archive --remote=<repository-url> <branch> <folder-path> --format=zip -o output.zip
    ```
    这不是一个 Git 仓库，无法进行版本控制。

*   **通过 SVN 客户端检出 GitHub 文件夹**:
    GitHub 支持 SVN 协议访问。
    ```bash
    svn checkout https://github.com/<user>/<repo>/trunk/<folder-path> <local-folder-name>
    ```

选择 `git sparse-checkout` 是当你仍需要 Git 版本控制功能（如 `pull`, `push`, `commit`）但又想限制本地工作目录大小时的最佳方案。