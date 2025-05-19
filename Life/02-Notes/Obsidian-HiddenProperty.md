---
category:
- Knowledge
tags:
- Obsidian
status: Done
---




 Obsidian 有一些隐藏的默认属性，这些属性可以通过内置的 Dataview 插件或者其他方式访问。这些属性包括文件的创建时间、修改时间、文件路径等。

### 1. 常用

1. `file` 是 Dataview 中表示当前文件的对象。
2. `ctime` 是这个文件对象的一个属性，代表文件的创建时间（creation time）。
3. `file.mtime` 表示文件的最后修改时间（modification time）。
4. `file.name`: 文件名（不包括扩展名）
5. `file.path`: 文件的完整路径
6. `file.folder`: 包含该文件的文件夹路径
7. `file.ext`: 文件扩展名
8. `file.size`: 文件大小（以字节为单位）

使用这些属性，你可以在 Dataview 查询中展示和排序文件的各种信息。例如，你可以按创建时间排序，或者显示文件的大小等。

### 2. file.文件隐式字段

- `file.name`: 文件标题（一个字符串）.
- `file.folder`: 这个文件所属的文件夹的路径.
- `file.path`: 完整的文件路径（一个字符串）.
- `file.ext`: 文件类型的扩展名；一般为'.md'（字符串）.
- `file.link`: 通往该文件的链接（一个链接）
- `file.size`: 文件的大小（以字节为单位）（一个数字）.
- `file.ctime`: 该文件的创建日期（一个日期+时间）
- `file.cday`: 文件创建的日期（只是一个日期）.
- `file.mtime`: 文件最后被修改的日期（一个日期+时间）。.
- `file.mday`: 文件最后被修改的日期（只是一个日期）。.
- `file.tags`: 笔记中所有独特标签的一个数组. 小标签按每个级别进行细分, so `#Tag/1/A` 将被存储在数组中，作为 `[#Tag, #Tag/1, #Tag/1/A]`.
- `file.etags`: 注释中所有显式标签的数组; unlike `file.tags`, 不包括子标签.
- `file.inlinks`: 该文件的所有传入链接的数组.
- `file.outlinks`: 该文件中所有外链的数组.
- `file.aliases`: 笔记中所有别名的一个数组.
- `file.tasks`: 一个包含所有任务的数组 (I.e., `- [ ] blah blah blah`) 在这个文件中。
- `file.lists`: 文件中所有列表元素的数组（包括任务）；这些元素是有效的任务，可以在任务视图中呈现。.
- `file.frontmatter`: 包含所有frontmatter的原始值；主要用于检查frontmatter的原始值或动态地列出前题的 keys 键值(字段)。

如果文件的标题内有一个日期（形式为 `yyyy-mm-dd` 或 `yyyymmdd`），或有一个Date字段/inline字段，它也有以下属性。

- `file.day`: 与文件标题相关的明确日期. 如果你使用obsidian核心插件 "Starred Files"，以下元数据也是可用的。
- `file.starred`: 如果这个文件已经被 "stars " obsidian插件加了星号。

### 3. 待办隐式字段
 
- `status`: 该任务的完成状态，由`[]`括号内的字符决定。一般来说，空格`" "`表示未完成的任务，X`"X"`表示完成的任务，但允许支持其他任务状态的插件。
- `checked`: 该任务是否以任何方式被检查过（即它的状态不是未完成/空的）。.
- `completed`: 这个_具体的_任务是否已经完成；这不考虑任何子任务的完成/未完成情况。如果一项任务被标记为 "X"，则明确视为 "完成"。.
- `fullyCompleted`: Whether or not this task and **all** of its subtasks are completed.
- `text`: 这项任务的文本.
- `line`: 该任务显示的行.
- `lineCount`: 这项任务所占的 markdown 行数.
- `path`: 该任务所在文件的完整路径.
- `section`: 该任务包含的章节链接.
- `tags`: 文本任务内的任何标签。
- `outlinks`: 本任务中定义的任何链接.
- `link`: 通往该任务附近最近的可链接区块的链接；对于建立通往该任务的链接很有用。.
- `children`: 该任务的任何子任务或子清单.
- `task`: 如果为真，这是一个任务；否则，它是一个普通的列表元素.
- `completion`: 一项任务完成的日期; 
- `annotated`: 如果任务有任何自定义注解，则为真，否则为假.
- `parent`: 这个任务上面的任务的行号，如果存在的话；如果这是一个根级任务，则为空。.
- `blockId`: 该任务/列表元素的块ID, if one has been defined with the `^blockId` syntax; otherwise null.

参考
[Dataview进阶(4)隐式字段 | obsidian文档咖啡豆版](https://obsidian.vip/zh/dataview/dataview-advanced-d.html#_3-2-file-文件隐式字段)
