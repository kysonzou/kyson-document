---
category:
- Knowledge
tags:
- Obsidian
status: Done
---
Markdown 本身没有内建的高亮语法，但是Obsidian通过html扩展来支持了高亮样式
```html
这是 <mark>高亮文本</mark> ！
```

Obsidian中使用下面语法展示高亮
```markdown
这是 ==高亮文本== ！
```

显示效果
这是 ==高亮文本== ！


如果你想修改高亮的颜色，还可以通过 Obsidian 的 **样式片段 (CSS snippets)** 来自定义样式：

1. **创建样式片段**：
    - 在 Obsidian 的主目录中，找到 .obsidian/snippets 文件夹。如果没有该文件夹，可以手动创建一个。
    - 在该文件夹中创建一个新的 .css 文件（例如 highlight.css）。

2. **编写 CSS**：  
   打开新建的 .css 文件，添加以下内容来自定义高亮颜色：
    ```css
    .markdown-preview-view mark {
    
        background-color: yellow; /* 修改为你想要的高亮颜色 */
    
        color: black; /* 字体颜色 */
    
        padding: 0.1em;
    
        border-radius: 3px;
    
    }
    ```

3. **启用样式片段**：
      - 打开 Obsidian，进入 **设置 > 外观 > 样式片段**。
      - 在样式片段列表中找到 highlight.css 并启用它。

这样，你可以通过修改 CSS 来调整 ==文本== 的高亮效果，使其更符合自己的需求。