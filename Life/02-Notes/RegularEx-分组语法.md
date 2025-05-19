---
category:
- Tech
tags:
- RegularE
status: Done
---
#### 1. 分组 ()

分组是通过圆括号 () 来将正则表达式的部分内容组合成一个整体，这样可以更灵活地定义模式结构，并允许我们对捕获的内容进行引用。

- **基本语法**：(pattern)

- **用途**：可以将匹配到的内容存储在一个分组中，方便后续使用。分组按从左至右的顺序编号，编号从 1 开始。

**示例**：匹配重复的单词，如 “hello hello”。
```regex
(\b\w+\b) \1
```
解释：

- `(\b\w+\b)`：匹配一个单词，使用 \b 限制单词边界，并将其存储为第一个分组。

- \1：引用第一个分组内容，确保匹配的下一个单词和第一个单词相同。

**Python示例**：
```python
import re

text = "hello hello world"
result = re.search(r"(\b\w+\b) \1", text)
print(result.group())  # 输出：hello hello
```
  
#### 2. 非捕获分组 (?: )

非捕获分组 (?: pattern ) 用于分组而不存储匹配的内容，适合在不需要引用分组内容时使用。

**示例**：匹配 “apple” 或 “orange” 字符串。
```regex
(?:apple|orange)
```
解释：
- `(?: ... )`：将 apple 和 orange 组合成一个模式，表示匹配其中一个即可，但不存储匹配内容。

**Python示例**：

```python
import re
text = "I like apple and orange."
result = re.findall(r"(?:apple|orange)", text)
print(result)  # 输出：['apple', 'orange']

# 非常经典的网址匹配
(?:https?:\/\/)?(?:www\.)?\w+\.\w+    
✅ google.com
✅ www.google.com
✅ http://google.com
✅ http://www.google.com
✅ https://google.com
✅ https://www.google.com
❌ google
❌ .com
```
  
#### 3. 反向引用 \n

反向引用 \n 用于在表达式中引用之前捕获的分组内容，适合在匹配中确保一致性。

**示例**：匹配成对的 HTML 标签。
```regex
<(\w+)>.*?</\1>
```
解释：

- <(\w+)>：匹配开头的 HTML 标签并捕获标签名为第一个分组。

- </\1>：引用第一个分组，确保匹配的结束标签与开头标签一致。