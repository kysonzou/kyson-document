---
category:
- Knowledge
tags:
- Markdown
status: Done
---



### 1. 行内代码

你可以使用一对反引号在句子插入代码，比如：

```md
`反引号`中的文本将被格式化为代码。
```

`反引号`中的文本将被格式化为代码。

如果要在行内代码中使用反引号，请用双反引号将其包围，比如：

```
``这是一句内部带有`反引号`的代码``。
```

``这是一句内部带有`反引号`的代码。``

### 2. 代码块

要创建一个代码块，请用三个反引号括住代码。

````
```
cd ~/Desktop
```
````

```md
cd ~/Desktop
```

你也可以通过使用 `Tab` 键或4个空格缩进文本来创建代码块。

```md
    cd ~/Desktop
```

你可以在开头的三个反引号后添加语言名称来为代码块添加语法高亮。

````md
```js
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```
````

```js
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```

### 3. 小技巧

>[!tips] 小技巧
>在markdown语法里，想要包括``` 我们可以将3个点改成4个点，就能包裹markdown的语法了

**演示：**

````markdown
```javascript
代码正文，这里就是用了四个`实现的
```
````

参考
[Markdown基本格式语法 - Obsidian 中文帮助 - Obsidian Publish](https://publish.obsidian.md/help-zh/%E7%BC%96%E8%BE%91%E4%B8%8E%E6%A0%BC%E5%BC%8F%E5%8C%96/%E5%9F%BA%E6%9C%AC%E6%A0%BC%E5%BC%8F%E8%AF%AD%E6%B3%95)