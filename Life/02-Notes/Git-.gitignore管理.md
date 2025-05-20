---
category:
  - Tech
tags:
  - Git
status: Done
---
每次新建项目都手动添加这些通用的忽略规则确实很麻烦。好消息是，Git 提供了解决方案，让你不必为每个项目都重复这些操作。

有两种主要管理 `.gitignore` 的方式，可以结合使用：

1. **项目特定的 `.gitignore` 文件**:
    
    - 这是放在你项目根目录下的 `.gitignore` 文件。
    - 它主要用来忽略那些**与该特定项目相关**的文件和目录，比如编译产物 (`build/`, `dist/`)、依赖包 (`node_modules/`, `venv/`)、日志文件 (`*.log`)、特定框架的缓存 (如 Django 的 `db.sqlite3` 或 Flask 的 `instance/`) 等。
    - 这部分内容确实会根据项目的语言、框架和使用的工具有所不同。例如，一个 Python 项目的 `.gitignore` 会和 Node.js 项目的有所区别。
2. **全局的 `.gitignore` 文件 (Global `.gitignore`)**:
    
    - 你可以配置一个**全局的** `.gitignore` 文件，它会应用到你系统上**所有的 Git 仓库**。
    - 这正是解决你提到的重复添加 `.DS_Store`、`.vscode/` 等通用忽略项的最佳方法。
    - 这个文件通常放在你的用户主目录下 (例如 `~/.gitignore_global`)。

**如何设置全局 `.gitignore` 文件？**

假设你创建了一个名为 `~/.gitignore_global` 的文件，并把通用的忽略规则放进去，比如：

```
# macOS
.DS_Store

# VS Code
.vscode/

# Windows Thumbs.db
Thumbs.db

# Other common editor/OS files
*.swp
*.swo
*~
```

然后，你需要告诉 Git 这个文件的位置。通过命令行执行以下命令：

```Bash
git config --global core.excludesfile ~/.gitignore_global
```

(如果你把文件放在其他位置或命名为其他名称，请相应修改路径。)

**这样配置后：**

- 你就不再需要在每个新项目的 `.gitignore` 文件里都写上 `.DS_Store` 和 `.vscode/` 了。Git 会自动应用全局忽略文件中的规则。
- 你项目中的 `.gitignore` 文件就可以更专注于该项目特有的忽略规则。

**总结：**

- 使用**全局 `.gitignore`** 来处理通用的、与操作系统或编辑器相关的忽略项（如 `.DS_Store`, `.vscode/`）。这样可以避免在每个项目中重复添加。
- 在每个**项目的根目录**下仍然使用 `.gitignore` 文件来处理特定于该项目的忽略项（编译产物、依赖、特定工具的缓存等）。

这种组合方式可以让你既能方便地管理通用忽略，又能灵活地处理项目特定的忽略需求，大大减少了重复工作。