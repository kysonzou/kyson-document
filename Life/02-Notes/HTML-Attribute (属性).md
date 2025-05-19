---
category:
- Tech
tags:
- Web
status: Done
---



这些玩意不用死记硬背，看看文档，多写写就熟悉了
- [HTML（超文本标记语言） | MDN](https://developer.mozilla.org/zh-CN/docs/Web/HTML)
- [The W3C Markup Validation Service](https://validator.w3.org/#validate_by_input)（**HTML 验证工具**）

#### **1. 全局属性**

这些属性几乎可以用于所有HTML元素。

• **id**：元素的唯一标识符，用于JavaScript或CSS中的选择。
```html
<div id="header">Header Content</div>
```
  
• **class**：用于指定元素的类名称，可在CSS和JavaScript中使用，允许多个元素共享一个类。
```html
<p class="text-primary">Some Text</p>
```
  
• **style**：内联样式，用于直接指定元素的CSS样式。
```html
<h1 style="color:blue;">Hello World</h1>
```
  
• **title**：鼠标悬停时显示的提示信息。
```html
<img src="image.jpg" title="A beautiful image">
```
  
• **lang**：定义元素内容的语言。
```html
<p lang="en">This is English text.</p>
```
  
• _data- 属性_*：自定义数据属性，用于存储页面或应用程序的私有数据。
```html
<div data-user-id="12345">User Info</div>
```
  
#### **2. 特定元素的属性**

这些属性在特定HTML标签中使用，例如\<a>, \<img>, \<input>等。

• **href** (用于 \<a>)：指定链接的目标URL。
```html
<a href="https://example.com">Visit Example</a>
```

• **src** (用于 \<img> 和 \<script>)：指定资源的URL，例如图片、脚本。
```html
<img src="picture.jpg" alt="A picture">
```
  
• **alt** (用于 \<img>)：图像的替代文本，在图像无法显示时可见。
```html
<img src="image.jpg" alt="Description of image">
```
  
• **type** (用于 \<button>, \<input>, \<script> 等)：定义元素的类型，如按钮的类型、输入类型或脚本类型。
```html
<button type="submit">Submit</button>
```
  
• **value** (用于 \<input>, \<button>)：定义输入字段的默认值。
```html
<input type="text" value="Default Text">
```
  
• **placeholder** (用于 \<input>)：输入字段中的提示信息。
```html
<input type="text" placeholder="Enter your name">
```
  
• **disabled** (用于 \<button>, \<input> 等)：禁用元素，使其无法与用户交互。
```html
<button disabled>Disabled Button</button>
```
  
• **checked** (用于 \<input type="checkbox"> 或 \<input type="radio">)：指定是否默认选中。
```html
<input type="checkbox" checked>
```
  
• **readonly** (用于 \<input>, \<textarea>)：只读属性，用户无法修改内容。
```html
<input type="text" value="Read-only text" readonly>
```
  
• **required** (用于 \<input>, \<textarea>)：表单字段的必填项。
```html
<input type="text" required>
```
  
• **multiple** (用于 \<input type="file">, \<select>)：允许选择多个值。
```html
<input type="file" multiple>
```
  
• **maxlength** (用于 \<input>, \<textarea>)：指定输入的最大字符数。
```html
<input type="text" maxlength="10">
```
  