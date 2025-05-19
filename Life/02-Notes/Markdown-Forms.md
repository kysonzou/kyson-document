---
category:
- Knowledge
tags:
- Markdown
status: Done
---



要添加表，请使用三个或多个连字符（`---`）创建每列的标题，并使用管道（`｜`）分割每列。您可以选择在表的任何一端添加管道。

```markdown
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
```

渲染效果

|Syntax|Description|
|---|---|
|Header|Title|
|Paragraph|Text|


您可以通过在标题行中的连字符的左侧，右侧或两侧添加冒号（`:`），将列中的文本对齐到左侧，右侧或中心。

```markdown
| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
```

渲染效果如下

| Syntax    | Description |   Test Text |
| :-------- | :---------: | ----------: |
| Header    |    Title    | Here's this |
| Paragraph |    Text     |    And more |


参考
[高级格式语法 - Obsidian 中文帮助 - Obsidian Publish](https://publish.obsidian.md/help-zh/编辑与格式化/高级格式语法#表格)