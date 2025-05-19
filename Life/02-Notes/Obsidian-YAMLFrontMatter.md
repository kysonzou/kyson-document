---
category:
- Knowledge
tags:
- Obsidian
status: Done
---

>[!tips] 名词解释
>- YAML是一种轻量级的数据序列化格式，通常用于表示配置文件和数据传输。
>- Frontmatter（前置内容）指的是位于文件顶部的一段元数据。可以是YAML、JSON格式
>- YAML Frontmatter 是使用YAML添加前置元数据

在Obsidian中添加文档属性的最合理方法是使用YAML前置元数据（YAML Front Matte）。这种方法既简单又灵活，而且与Obsidian的其他功能和插件兼容性很好。

1. 添加方法：
   在每个Markdown文件的开头添加YAML格式的元数据。例如：

    ```ymal
    ---
	title: "示例文档"
	date: 2024-07-14
	tags: [笔记, 示例]
	category: 工作
	status: 进行中
	---
    ```

    >这些信息需要放在文档最开始，并用 `---` 包裹。

2. 注意事项：
   - 确保YAML语法正确，错误的语法可能导致整个前置元数据块被忽略。
   - 对于日期和时间，使用标准格式（如YYYY-MM-DD）以确保兼容性。
   - 对于多值属性（如标签），可以使用数组格式 `[tag1, tag2, tag3]` 或列表格式。

通过这种方法，你可以为文档添加丰富的元数据，这些元数据可以被Dataview等插件用来创建强大的查询和视图，实现类似Notion的表格视图功能。

参考
[YAML和属性语法 | obsidian文档咖啡豆版](https://obsidian.vip/zh/markdown/yaml.html)
 