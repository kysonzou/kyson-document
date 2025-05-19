---
category:
- Tech
tags:
- Web
status: Done
---



#### 1. class选择器

- 使用HTML元素的class属性，并通过CSS选择器定义该class的样式。

- 任何带有相同class名称的HTML元素都会应用相同的CSS样式。

- **class选择器**前面用一个点（.）表示，CSS写法为.class-name { ... }。

**示例**：
```html
<!-- HTML -->
<p class="highlight">这是一个带有“highlight”类的段落。</p>
<div class="highlight">这是一个带有“highlight”类的div。</div>

<!-- CSS -->
<style>
    .highlight {
        color: red;
        font-weight: bold;
    }
</style>
```
  
**解释**：
- 上面例子中的\<p>和\<div>标签都带有class="highlight"属性，因此都会应用.highlight的样式，即文本颜色为红色，字体加粗。

- 使用class选择器可以让不同的HTML元素共享相同的样式。

#### 2. id选择器

- 用于为特定的单一元素定义样式，每个id在页面中应该是唯一的。

- **id选择器**前面用井号（#）表示，CSS写法为#id-name { ... }。

**示例**：
```html
<!-- HTML -->
<p id="unique">这是一个带有唯一id的段落。</p>

<!-- CSS -->
<style>
    #unique {
        color: blue;
        font-size: 20px;
    }
</style>
```
  
**解释**：
- id选择器通常用于页面中唯一的元素，它的优先级高于class选择器。

#### 3. 元素选择器

- 针对某一类HTML元素（例如\<p>、\<h1>）定义样式，所有相同标签的元素都会应用该样式。

- **CSS写法**：直接使用元素名称，例如p { ... }。

**示例**：
```html
<!-- HTML -->
<p>所有段落都会使用这个样式。</p>

<!-- CSS -->
<style>
    p {
        font-size: 18px;
        line-height: 1.5;
    }
</style>
```
    
#### 4. 组合选择器

- 可以将**class**、**id**、**元素选择器**组合使用，创建更具体的选择器，应用于特定的场景。

- **CSS写法**：可以是多个选择器组合，如.class-name p { ... }。

**示例**：
```html
<!-- HTML -->
<div class="container">
    <p>这是一个普通的段落。</p>
    <p class="special">这是一个带有class的段落。</p>
</div>

<!-- CSS -->
<style>
    /* 针对.container中的.p标签 */
    .container p.special {
        color: green;
        font-size: 20px;
    }
</style>
```
  