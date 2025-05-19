---
category:
- Knowledge
tags:
- Obsidian
status: Done
---



callout 标注块是 obsidian 新增的格式，也被称为**admonitions警告**表现形式是带颜色的块引用，有标题、背景颜色和icon图标。 他极大的丰富了 obsidian 的排版，增加了美观度。

**语法：**

```
> [!info] 自定义标题
> 包裹的内容
> 可以是多行的内容
```

在标题部分可以使用 `-`和`+`符号，让callout面板折叠或者展开，比如：

可折叠被折叠默认的

```
> [!info]+ 这是一个可折叠的callout
> 包裹的内容，注意上面的+号
```

```
> [!info]- 这是一个被折叠的callout
> 包裹的内容，注意上面的-号
```

```
> [!info] 默认的callout
> 包裹的内
```

- Note

	>[!Note]-  Note
	> This is a note

- Abstract

	>[!Abstract]+ Abstact
	> This is Abstract

- Info

	>[!info] info
	>this is info

- Todo

	>[!Todo] todo
	>this is todo

- Tip

	>[!tip] tip
	>this is tip

- Success

	>[!Success] success
	>this is success

- Question

	>[!question] question
	>this is question

- Warning

	>[!warning] warning
	>this is warning

- Failure

	>[!failure] failure
	>this is failure
	>

- Danger

	>[!danger] danger
	>this is danger 

- Bug

	>[!bug] bug
	>this is bug

- Example

	>[!example] example
	>this is example 

- Quote

	>[!quote] quote
	>this is quote

**使用技巧**

- 在使用callout的时候，注意中间不要有空行，否则会导致空行下面的内容不被包裹。
- 标题中也支持 markdown 语法

参考
[callout标注块 | obsidian文档咖啡豆版](https://obsidian.vip/zh/markdown/callout.html)