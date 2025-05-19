---
category:
- Knowledge
tags:
- Obsidian
status: Done
---



Dataview 插件： 这是一个强大的插件，可以让你查询和显示笔记中的数据。

1. `TABLE` 查询语法来创建类似表格视图的展示
	````md
	```dataview
	TABLE
		file.ctime as "创建时间", 
		file.mtime as "修改时间", 
		file.folder as "所在文件夹"
	FROM "YourFolder"
	SORT date DESC
	```
	````

2. `LIST` 查询语法来创建列表，和Table的区别是它不能显示更多属性

	````
	```dataview
	List
	FROM #标签
	SORT date DESC
	```
	````

3. `Task`查询语法来创建代办事项，只处理代办事项

4. `From` 筛选条件，如果有多个筛选条件用 `or`、`and` 、`-`，`-`是排除的意思

	```
	FROM #标签1 and #标签2 or #标签3 -#标签4
	FROM 文件 OR 文件夹
	```

5. 时间的格式化 `dateformat`

	```
	TABLE 
		dateformat(file.ctime, "yyyy-MM-dd") as "创建日期", 
		dateformat(file.mtime, "yyyy-MM-dd HH:mm") as "最后修改时间"
	```

6. 设置别名通过 `as`

	```
	TABLE 
		file.filename as "文件名"
		file.ctime as "创建时间"
	```

这里举例中的file.ctime、file.mtime是什么东西呢，详见[[Obsidian-HiddenProperty]]

参考
[Dataview综合文档 | obsidian文档咖啡豆版](https://obsidian.vip/zh/dataview/)