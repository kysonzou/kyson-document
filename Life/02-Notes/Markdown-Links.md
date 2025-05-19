---
category:
  - Knowledge
tags:
  - Markdown
status: Done
---
Markdown 中需要避免多余的缩进，因为缩进会导致 Markdown 渲染为代码块格式（尤其是 4 个空格的缩进），这可能会破坏代码显示，特别是在 Markdown 编辑器中直接复制时。下面是调整过的内容，去掉了缩进，以便你可以直接复制并在 Markdown 编辑器中渲染：

标准 Markdown 语法中有以下三种主要的链接和引用格式：

**1. 标准链接（内联链接）**

使用 \[链接文本](URL) 语法：

```markdown
[链接文本](https://example.com)
```

**2. 引用式链接**

通过定义标签，在正文和引用部分分开写法：

正文部分：
```markdown
[链接文本][标签]
```
  
在文档底部定义标签和 URL：
```markdown
[标签]: https://example.com
```

**3. 可选标题（title）属性**

在链接中可以添加可选的标题（title）属性，鼠标悬停时会显示该标题内容：
```markdown
[链接文本](https://example.com "可选标题")
```

或在引用式链接中：
```markdown
[链接文本][标签]

[标签]: https://example.com "可选标题"
```

**4. 图片引用**

使用 !\[替代文本](图片URL) 语法可以内嵌图图片：

```markdown
![替代文本](https://example.com/image.png)
```

对一其它类型的资源的内嵌，markdown语法是不支持的，但是很多Markdown解析器都会支持HTML语法

图片
```html
<p align="center">
  <img src="./Assets/Obsidian-Embed-1.png" alt="替代文本" width="300">
</p>
```

网页
```html
<iframe src="https://example.com"></iframe>
```

视频
```markdown
<video controls>
  <source src="路径/视频文件.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
```

音频
```markdown
<audio controls>
  <source src="路径/音频文件.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
