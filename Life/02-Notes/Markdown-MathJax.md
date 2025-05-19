---
category:
- Knowledge
tags:
- Markdown
status: Done
---
你可以使用 [MathJax](http://docs.mathjax.org/en/latest/basic/mathjax.html) 和 LaTeX 符号在笔记中添加数学公式。

**1. 行间函数用双美元符号（`$$`）**

要在笔记中添加 MathJax 公式，请用双美元符号（`$$`）将其括起来。

```markdown
$$
\begin{vmatrix}a & b\\
c & d
\end{vmatrix}=ad-bc
$$
```

$$
\begin{vmatrix}a & b\\
c & d
\end{vmatrix}=ad-bc
$$

**2. 行内函数用一个美元符号（`$`）**

你也可以用 `$` 符号包裹数学公式来实现行内数学公式。

```markdown
这是一个行内数学表达式 $e^{2i\pi} = 1$。
```

这是一个行内数学表达式 $e^{2i\pi} = 1$。

**参考**

- 想了解更多有关语法的信息，请参阅[MathJax 基础教程](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)。

- 要查看支持的 MathJax 包列表，请参阅[TeX/LaTeX 扩展列表](http://docs.mathjax.org/en/latest/input/tex/extensions/index.html)。

- 参考 [高级格式语法 - Obsidian 中文帮助 - Obsidian Publish](https://publish.obsidian.md/help-zh/编辑与格式化/高级格式语法)