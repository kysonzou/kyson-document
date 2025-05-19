---
category:
- Tech
tags:
- Web
status: Done
---



**层叠性（Cascading）**
- CSS全称为Cascading Style Sheets，强调了**层叠性**，即样式表可以叠加应用。

- CSS样式会按照优先级叠加，优先级的高低决定了哪条规则会最终生效。

- 优先级排序：**内联样式**（style属性）> **id选择器** > **class选择器** > **元素选择器**。此外，后定义的样式会覆盖先定义的样式。

```html
<p id="para" class="text">这是一个段落。</p>

<style>
    p { color: blue; }              /* 元素选择器 */
    .text { color: green; }          /* class选择器 */
    #para { color: red; }            /* id选择器 */
</style>
```
最终段落文字颜色为红色，因为id选择器的优先级最高。