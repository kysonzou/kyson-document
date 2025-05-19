---
category:
  - Tech
tags:
  - Git
status: Done
---
重要前提：

在进行任何这些操作之前，强烈建议您备份所有相关的 Git 仓库，或者始终在原始仓库的全新克隆副本上进行操作。 这些操作，特别是涉及历史重写的，如果操作不当可能会导致数据丢失。

---

### 第一部分：将多个 Git 仓库合并为一个（保留提交历史）

**目标：** 将两个或多个独立的 Git 仓库（例如 `RepoA` 和 `RepoB`）合并成一个单一的仓库，并保留它们各自完整的提交历史。

**方法一：直接合并（适用于文件结构不冲突，或一个仓库内容直接并入另一个仓库根目录）**

1. **准备主仓库：**
    
    - 克隆你希望作为基础的主仓库（例如 `RepoA`）：
        ```Bash
        git clone <url_to_RepoA> CombinedRepo
        cd CombinedRepo
        ```
        
2. **添加其他仓库为远程仓库：**
    
    - 将需要合并进来的仓库（例如 `RepoB`）添加为一个临时的远程源：
        ```Bash
        git remote add repoB_remote <url_to_RepoB>
        ```
        
3. **获取其他仓库的数据：**
    
    - 拉取 `RepoB` 的所有分支和提交历史：
        ```Bash
        git fetch repoB_remote
        ```
        
4. **合并历史：**
    
    - 将 `RepoB` 的主分支（例如 `main` 或 `master`）合并到当前 `CombinedRepo` 的主分支：  
        ```Bash
        git merge repoB_remote/main --allow-unrelated-histories
        ```
        
        - `--allow-unrelated-histories`：因为两个仓库通常没有共同的祖先，所以此参数是必需的。
    - **解决冲突：** 如果两个仓库有相同路径和名称的文件，Git 会提示冲突。你需要手动解决这些冲突，然后 `git add .` 并 `git commit`。
5. **（可选）将合并内容放入子目录：**
    
    - 如果在合并后，你希望 `RepoB` 的内容位于 `CombinedRepo` 的一个子目录下（例如 `sub_repoB/`）：
    
        ```Bash
        mkdir sub_repoB
        # 将原RepoB的文件（现在位于根目录）移动到 sub_repoB/
        # 例如: git mv file_from_repoB.txt folder_from_repoB/ sub_repoB/
        git commit -m "Moved RepoB content to sub_repoB subdirectory"
        ```
        
6. **推送：**
    
    - 将合并后的 `CombinedRepo` 推送到一个新的远程仓库，或者（谨慎地）推送到原 `RepoA` 的远程仓库。
        
        ```Bash
        # git remote set-url origin <url_of_new_combined_remote_repo> # (如果推送到全新仓库)
        git push origin main # (或你的主分支名)
        ```
        
7. **清理：**
    
    - 可以移除临时的远程仓库：
        
        ```Bash
        git remote remove repoB_remote
        ```
        

**方法二：使用 `git filter-repo` 将一个仓库重写到子目录后再合并（推荐用于清晰的子目录结构）**

1. **准备待合并仓库 (`RepoB`)：**
    
    - 克隆 `RepoB` 到一个临时位置：
        ```bash
        git clone <url_to_RepoB> RepoB_temp
        ```

    - 进入 `RepoB_temp`：
        ```bash
        cd RepoB_temp
        ```

    - 使用 `git filter-repo` 将 `RepoB_temp` 的所有内容和历史重写到一个目标子目录（例如 `sub_repoB/`）下：
        
        ```Bash
        # 首先确保已安装 git filter-repo
        git filter-repo --to-subdirectory-filter sub_repoB
        ```
        
    - 返回上一级目录：`cd ..`
2. **准备主仓库 (`RepoA`) 并合并：**
    
    - 克隆 `RepoA`：
        ```bash
        git clone <url_to_RepoA> CombinedRepo
        ```
    
    - 进入 `CombinedRepo`：
        ```bash
        cd CombinedRepo
        ```
    
    - 将处理过的 `RepoB_temp` 添加为远程仓库：
        ```Bash
        git remote add repoB_filtered ../RepoB_temp # 使用本地路径
        ```
        
    - 获取数据：
        ```bash
        git fetch repoB_filtered
        ```
    
    - 合并（此时 `RepoB_temp` 的内容已在 `sub_repoB/` 下，冲突可能性降低）：
        ```Bash
        git merge repoB_filtered/main --allow-unrelated-histories
        ```
        
    - 解决可能发生的任何冲突。
3. **推送和清理：** 同方法一的步骤 6 和 7。

**合并仓库的关键点：**

- `--allow-unrelated-histories` 参数是核心。
- 合并后，两个仓库的提交历史会按时间顺序交织在一起。
- 注意处理文件名和路径冲突。

---

### 第二部分：将仓库的子目录分离为新的独立仓库（保留相关历史）

**目标：** 从一个现有的 Git 仓库 (`OriginalRepo`) 中提取一个子目录 (`path/to/your/subdirectory`)，使其成为一个全新的、独立的 Git 仓库 (`NewRepo`)，并且只包含与该子目录相关的提交历史。

**推荐工具：`git filter-repo`** (确保已安装)

**步骤：**

1. **克隆原始仓库（重要！）：**
    
    - 在一个新的、安全的位置克隆你的原始仓库，以进行操作：
        
        ```Bash
        git clone <url_to_OriginalRepo> NewRepo_from_subdir
        cd NewRepo_from_subdir
        ```
        
2. **执行历史过滤：**
    
    - 使用 `git filter-repo` 来提取子目录，并将其作为新仓库的根：
        
        ```Bash
        git filter-repo --subdirectory-filter path/to/your/subdirectory
        ```
        
        - 将 `path/to/your/subdirectory` 替换为实际子目录的路径。
        - 此命令会重写历史，只保留与该子目录相关的提交和文件，并将该子目录设为项目根目录。
3. **检查结果：**
    
    - 使用 `git log` 和查看文件结构，确认新仓库只包含子目录的内容和其相关历史。
4. **创建新的远程仓库：**
    
    - 在你的 Git托管平台（如 GitHub, GitLab）上创建一个全新的**空仓库**，用于存放这个分离出来的子项目。获取其 URL。
5. **更新本地仓库的远程链接：**
    
    - （可选）移除旧的远程链接（如果存在）：`
        ```bash
        git remote remove origin
        ```

    - 添加新的远程仓库链接：
        
        ```Bash
        git remote add origin <url_of_your_new_empty_repo>
        ```
        
6. **推送至新仓库：**
    
    - 推送所有分支和标签到新的远程仓库：
        
        ```Bash
        git push -u origin --all
        git push -u origin --tags
        ```
        

**分离子目录的关键点：**

- 始终在原始仓库的克隆副本上操作。
- `git filter-repo` 是现代化且推荐的工具。
- 新仓库的历史将只包含那些修改过指定子目录内文件的提交。
- 原始仓库保持不变。

---

**通用最佳实践：**

- **备份！备份！备份！**
- 在执行命令前，理解每个命令的作用，尤其是历史重写命令。
- 如果操作涉及到共享仓库，请务必与团队成员沟通协调。对于合并操作，通常推送到一个全新的远程仓库是更安全的选择。对于分离子目录，原始仓库不受影响。
