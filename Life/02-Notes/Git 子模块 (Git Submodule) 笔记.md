---
category:
  - Tech
tags:
  - Git
status: Done
---
**一、核心概念与原理**

1. **定义**：Git 子模块允许你将一个外部的 Git 仓库作为你主仓库（父仓库）的一个子目录来引用和管理。子模块本身是一个完整且独立的 Git 仓库。
2. **目的**：
    - 在主项目中包含并使用外部库、依赖项或共享组件，同时保持这些组件的独立版本控制。
    - 实现代码/配置的模块化和重用。
3. **工作机制**：
    - **父仓库存储引用**：父仓库不直接存储子模块的所有文件内容或完整历史。相反，它只存储：
        - 子模块在其远程源的 URL。
        - 子模块应该检出到的**特定提交哈希 (commit SHA-1)**。
    - **`.gitmodules` 文件**：当添加第一个子模块时，父仓库根目录下会创建（或更新）此文件。它记录了所有子模块的配置信息（路径、URL、有时还有分支）。此文件会被提交到父仓库的版本历史中。
    - **独立性**：子模块保持其独立的提交历史、分支和标签。你可以在子模块目录内执行标准的 Git 操作（`commit`, `push`, `pull`, `checkout` 等），这些操作只影响子模块自身。

**二、常用操作命令**

1. **添加子模块到父仓库：**
    ```Bash
    git submodule add <repository_url> [path_to_submodule_directory]
    ```
    
    - `<repository_url>`：子模块的远程 Git 仓库地址。
    - `[path_to_submodule_directory]`：子模块在父仓库中检出的路径（如果省略，通常使用仓库名作为目录名）。
    - **操作结果**：
        - 克隆子模块仓库到指定路径。
        - 创建或更新 `.gitmodules` 文件。
        - 在父仓库的暂存区添加子模块的引用（路径和初始提交哈希）以及 `.gitmodules` 文件。你需要 `git commit` 来保存这些更改到父仓库。
2. **克隆包含子模块的父仓库：**
    
    - **选项一（推荐，一步到位）：**

        ```Bash
        git clone --recurse-submodules <parent_repository_url>
        ```
        
    - **选项二（分步）：**
        
        ```Bash
        git clone <parent_repository_url>
        cd <parent_repository_directory>
        git submodule init     # 初始化本地配置文件中定义的子模块
        git submodule update   # 根据父仓库记录的提交哈希检出子模块内容
        # 或者合并为一步：
        # git submodule update --init --recursive # --recursive 用于处理嵌套子模块
        ```
        
3. **更新子模块：**
    
    - **场景A：父仓库切换到记录了不同子模块版本的提交后，更新本地子模块内容：**
        
        ```Bash
        # (在父仓库根目录)
        git pull # 拉取父仓库的更新，这可能改变了父仓库对子模块的提交引用
        git submodule update --init --recursive
        ```
        
    - **场景B：让子模块更新到其远程仓库的最新提交 (例如其 `main` 分支的最新版)：**
        1. **方法一（推荐，直接更新并准备提交父仓库）：**
                
            ```Bash
            # (在父仓库根目录)
            git submodule update --remote [submodule_path]
            # 示例: git submodule update --remote path/to/your/submodule
            ```
            
            这会自动拉取子模块远程分支的最新提交，并更新子模块的工作目录。之后，父仓库会检测到子模块引用已更改，你需要 `git add [submodule_path]` 和 `git commit` 来记录这个更新。
        2. **方法二（手动进入子模块操作）：**
            
            ```Bash
            # (在父仓库根目录)
            cd [submodule_path]
            git checkout main # 或子模块的主分支
            git pull          # 拉取子模块自身的最新更改
            cd ..             # 返回父仓库根目录
            git add [submodule_path] # 父仓库暂存子模块的新提交引用
            git commit -m "Updated submodule [submodule_path] to latest"
            ```
            
4. **查看子模块状态：**

    ```Bash
    git status # 会显示子模块是否有新的提交引用或未提交的更改
    git submodule status # 显示已注册子模块及其当前检出的提交哈希
    ```
    
5. **在子模块内工作和推送更改：**
    
    1. `cd [submodule_path]`
    2. 进行修改，执行 `git add .`, `git commit -m "Changes in submodule"`。
    3. `git push origin <submodule_branch_name>` (推送到子模块自己的远程仓库)。
    4. `cd ..` (返回父仓库)。
    5. `git add [submodule_path]` (父仓库记录子模块的新提交引用)。
    6. `git commit -m "Updated submodule [submodule_path] pointer"`。
    7. `git push` (推送父仓库的更改)。
6. 移除子模块 (较复杂，需谨慎)：
    
    Git 没有一个简单的 git submodule rm 命令能完美处理所有情况，通常步骤如下：
    
    1. `git submodule deinit -f -- [submodule_path]`
    2. `git rm -f [submodule_path]` (这会从工作树和索引中移除，但 `.gitmodules` 中的条目还在)
    3. `git rm --cached [submodule_path]` (如果上一步没有完全移除索引)
    4. 编辑 `.gitmodules` 文件，手动删除对应子模块的配置段落。
    5. `git add .gitmodules`
    6. 删除 `.git/modules/[submodule_path]` 目录 (可能需要手动)。
    7. `git commit -m "Removed submodule [submodule_path]"`
    8. (可选) 清理不再需要的子模块对象：`git gc --prune=now`

**三、工作流程逻辑**

1. **添加依赖**：当项目A（父）需要项目B（子）时，将项目B作为子模块添加到项目A中。项目A的某次提交会记录它依赖于项目B的某个特定版本（提交X）。
2. **更新依赖源**：项目B独立发展，产生了新的版本（提交Y）。
3. **父项目更新依赖**：
    - 项目A的维护者决定采纳项目B的提交Y。
    - 他们会更新项目A中的子模块引用，使其指向项目B的提交Y。
    - 然后提交项目A，记录这个依赖关系的变更。
4. **协作者获取更新**：
    - 其他协作者拉取项目A的最新代码。
    - 他们会发现项目A记录的子模块版本已更新。
    - 他们执行 `git submodule update` 来使本地子模块检出到项目A指定的那个新版本（提交Y）。

**四、注意事项**

- **子模块不是分支的替代品**：子模块用于管理外部依赖，而不是项目内部的特性分支。
- **分离的 HEAD 状态**：当 `git submodule update` 检出子模块时，子模块通常会处于“分离 HEAD (detached HEAD)”状态，即直接指向一个提交哈希而不是一个本地分支。如果你想在子模块内做修改并提交，最好先在子模块内切换到一个分支 (`git switch main` 或 `git switch -c new-feature-in-submodule`)。
- **`--remote` 选项**：使用 `git submodule update --remote [submodule_path]` 可以方便地让子模块更新到其跟踪分支的最新提交，而不是父仓库记录的那个固定提交。这对于希望子模块总是使用最新版本的场景很有用，但需要父仓库随后提交这个新的引用。
- **协作**：团队成员都需要理解子模块的工作方式，并正确执行 `submodule update` 等命令来保持同步。
