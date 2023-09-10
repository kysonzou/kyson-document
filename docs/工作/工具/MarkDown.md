## 基本语法

### 标题语法

要创建标题，请在单词或者词语前面添加（`#`）。`#` 的数量代表了标题的级别。例如，添加三个 `#` 表示创建一个三级标题（`<h3>`）(例如：`### My Header`)

|     Markdown语法      |             HTML             |
| :-------------------: | :--------------------------: |
|  \# Heading Level 1   | `<h1> Heading Level 1 </h1>` |
|  \## Heading level 2  | `<h2> Heading Level 1 </h2>` |
|  ### Heading level 3  | `<h3> Heading Level 1 </h4>` |
| #### Heading level 4  | `<h4> Heading Level 1 </h4>` |
| ##### Heading level 5 | `<h5> Heading Level 1 </h5>` |

### 段落语法

要创建段落，请使用空白行将一行或者多行文本进行分割。

- ***Markdown***

```markdown
I real like using markdown 

I think I will use it to format all of my docments form now. 
```

- ***HTML***

```html
<p>I really like using Markdown.</p>
<p>I think I'll use it to format all of my documents from now on.</p>
```

渲染效果如下

> I real like using markdown 
>
> I think I will use it to format all of my docments form now. 

### 换行语法

在一行的末尾添加两个或者多个空格，然后按回车键，即可创建一个换行（`<br>`）

> **Tip: **好像在Typora编辑器中添加两个或多个空格，然后按回车键的方式没用还是<br>好使

- ***markdown添加空格然后按回车键***



- ***换行符（\<br>）***

```markdown
This is the first line. <br> 
And this the second line
```

- ***HTML***

```html
<p>This is the first line.<br>
  And this is the second line.</p>
```

渲染效果如下

>This is the first line. <br>And this the second line

### 强调语法

通过将文本设置为粗体或者斜体来强调其重要性

#### 粗体（Blod）

要加粗文本，请在单词或者短语的前后个添加两个星号(asterisks)（`**`）或者下划线(underscores)（`__`）。如需加粗一个单词或者短语的中间部分用以表示强调的话，请在要加粗部分的两侧各添加两个星号

- ***Markdown***

```markdown
I just love **blod text**
I just love __blod text__
Love**is**blod
```

- ***HTML***

```html
I just love <strong>blod text</strong> 
I just love <strong>blod text</strong> 
Love<strong>is</strong>blod
```

渲染效果如下

>I just love **blood text**
>
>I just love __blod text__
>
>Love**is**blod

#### 斜体（Italic）

要用斜体文本，请在单词或者短语的前后个添加一个星号(asterisks)（`*`）或者下划线(underscores)（`_`）。要斜体突出单词的中间部分，请在字母前后各添加一个星号，中间不要带空格。

- ***Markdown***

```markdown
Italicized text is the *cat's meow*
Italicized text is the _cat's meow_
A*cat*meow
```

- ***HTML***

```html
Italicized text is the <em>cat's meow</em>
Italicized text is the <em>cat's meow</em>
A<em>cat</em>meow
```

渲染效果如下

>Italicized text is the *cat's meow*
>
>Italicized text is the _cat's meow_
>
>A*cat*meow

#### 粗体（Blod）和斜体（Italic）

要用斜体文本，请在单词或者短语的前后个添加三个星号(asterisks)（`***`）或者下划线(underscores)（`___`）。要斜体突出单词的中间部分，请在字母前后各添加三个星号，中间不要带空格。

- ***markdown***

```markdown
This text is ***really important***
This text is ___really important___
This text is really***very***important
```

- ***HTML***

```html
This text is <strong><em>really important</em></strong>
This text is <strong><em>really important</em></strong>
This text is really<strong><em>very</em></strong>important
```

渲染效果

>This text is ***really important***
>
>This text is ___really important___
>
>This text is really***very***important

### 引用语法

#### 单段落引用

要创建引用，请在段落前添加一个`>`符号。

```markdown
> dorothy followed her through many of the beautiful rooms in her castle
```

渲染效果如下

> dorothy followed her through many of the beautiful rooms in her castle

#### 多个段落的引用

块引用可以包含多个段落。为段落之间的空白添加一个`>`符号

```markdown
> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
```

渲染效果如下

> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

#### 嵌套块引用

块引用可以嵌套。在要嵌套的段落前添加一个 `>>` 符号。

```markdown
> Dorothy followed her through many of the beautiful rooms in her castle.
>
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
```

渲染效果如下

> Dorothy followed her through many of the beautiful rooms in her castle.
>
> > The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

#### 带其它元素的引用

块引用可以包含其他 Markdown 格式的元素。并非所有元素都可以使用，你需要进行实验以查看哪些元素有效。

```markdown
> ### The quarterly result look great 
> 
> - Revenue was off the chart 
> - profits were higher than ever 
>
> *Everythings* is going according to **plan** 
```

渲染效果如下

> ### The quarterly result look great <!-- {docsify-ignore} -->
>
> - Revenue was off the chart 
> - profits were higher than ever 
>
> *Everythings* is going according to **plan** 



### 列表语法

可以将多个条目组织成有序或者无需的列表

#### 有序列表

要创建有序列表，请在每个列表项前添加数字并紧跟一个英文句点。数字不必按数学顺序排列，但是列表应当以数字 `1` 起始。

- ***markdown***

```markdown
1. first item
2. second item
3. third item 
4. forth item 
```

- ***HTML***

```html
<ol>
<li>First item</li>
<li>Second item</li>
<li>Third item</li>
<li>Fourth item</li>
</ol>
```

预览效果

1. first item
2. second item
3. third item 
4. forth item 

#### 无序列表

要创建无序列表，请在每个列表项前面添加破折号（`-`）、星号（`*`）或加号（`+`）。缩进一个或多个列表项可创建嵌套列表

* ***markdown***

| 破折号（-）   | 星号（*）     | 加号（+）     |
| :------------ | :------------ | ------------- |
| - first item  | * first item  | + first item  |
| - second item | * second item | + second item |
| - third item  | * third item  | + third item  |
| - fourth item | * fourth item | + fourth item |

* ***HTML***

```html
<ul>
<li>First item</li>
<li>Second item</li>
<li>Third item</li>
<li>Fourth item</li>
</ul>
```

渲染效果

+ first item 
+ Second item
+ Third item
+ Fourth item

#### 在列表中嵌套其它元素

要在保留列表连续性的同时在列表中添加一种元素，请将该元素缩进四个空格或一个制表符

- ***markdown***

  嵌套代码块

  ~~~markdown
  - This is the first list item
  
  - Here is the second list item 
  	```
  	I need to add another paragraph below the second list item
    ```
  
  - And here is the third list item
  ~~~

  嵌套链接

  ```markdown
  1. This is the first list item
  
  2. Here is the second list item 
  
    [markdown中文官方教程](https://markdown.com.cn)
  
  3. And here is the third list item
  ```

渲染效果

嵌套代码块

- This is the first list item

- Here is the second list item 
	```text
	I need to add another paragraph below the second list item
  ```

- And here is the third list item

嵌套链接

1. This is the first list item

2. Here is the second list item 

     [markdown中文官方教程](https://markdown.com.cn)

3. And here is the third list item

### 代码语法

要将单词或短语表示为代码，请将其包裹在反引号 (``) 中。

| Markdown语法                              | HTML                                                  | 预览效果                            |
| ----------------------------------------- | ----------------------------------------------------- | ----------------------------------- |
| ```At the command prompt, type `nano`.``` | ```At the command prompt, type <code>nano</code>. ``` | At the command prompt, type `nano`. |

#### 转义反引号

如果你要表示为代码的单词或短语中包含一个或多个反引号，则可以通过将单词或短语包裹在双反引号(````)中。

| Markdown语法                                  | HTML                                                 | 预览效果                              |
| --------------------------------------------- | ---------------------------------------------------- | ------------------------------------- |
| ````` Use `code` in your Markdown file.`` ``` | ```<code>Use `code` in your Markdown file.</code>``` | ``Use `code` in your Markdown file.`` |

>**Tip：**这预览效果在Typora中貌似不太对，我预想的应该是其它字符不会有加代码的效果，但实际上在Typora中加双反引号（````）的预览效果和代码语法的一样，在简书中试过也一样。



#### 代码块

要创建代码块，请将代码块的每一行缩进至少四个空格或一个制表符。			

> **Tip：**在Typora缩进的方式没用，在简书中试过是有用的



## 扩展语法

### 表格

要添加表，请使用三个或多个连字符（`---`）创建每列的标题，并使用管道（`｜`）分割每列。您可以选择在表的任何一端添加管道。

```markdown
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
```

> **Tip：**貌似在typora中不是这么设置的，直接｜----｜----｜然后换行就可以，在简书中不知道怎么添加表格哈哈

渲染效果

| Syntax    | Description |
| --------- | ----------- |
| Header    | Title       |
| Paragraph | Text        |

单元格宽度可以变化，如下所示。呈现的输出将看起来相同。

```markdown
| Syntax | Description |
| --- | ----------- |
| Header | Title |
| Paragraph | Text |
```

#### 对齐

您可以通过在标题行中的连字符的左侧，右侧或两侧添加冒号（`:`），将列中的文本对齐到左侧，右侧或中心。

```markdown
| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
```

渲染效果如下

| Syntax    | Description |   Test Text |
| :-------- | :---------: | ----------: |
| Header    |    Title    | Here's this |
| Paragraph |    Text     |    And more |

#### 格式化表格中的文字

您可以在表格中设置文本格式。例如，您可以添加链接，代码（仅反引号（```）中的单词或短语，而不是代码块）和强调。

您不能添加标题，块引用，列表，水平规则，图像或HTML标签。

#### 在表中转义管道字符

您可以使用表格的HTML字符代码（`|`）在表中显示竖线（`|`）字符。

### 围栏式代码块

Markdown基本语法允许您通过将行缩进四个空格或一个制表符来创建[代码块](https://markdown.com.cn/basic-syntax/code-blocks.html)。如果发现不方便，请尝试使用受保护的代码块。根据Markdown处理器或编辑器的不同，您将在代码块之前和之后的行上使用三个反引号（```）或三个波浪号（~~~）。

~~~markdown
```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
~~~

渲染效果如下

```markdown
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

> **Tip:**要在代码块中显示反引号？请参阅了解如何[转义](https://markdown.com.cn/basic-syntax/escaping-backticks.html)它们。

#### 语法高亮

许多Markdown处理器都支持受围栏代码块的语法突出显示。使用此功能，您可以为编写代码的任何语言添加颜色突出显示。要添加语法突出显示，请在受防护的代码块之前的反引号旁边指定一种语言。

````markdown
```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
````

渲染效果如下

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

> **Tip:** 在Typora中就是在右下角设置代码语言的意思

### 设置颜色

Markdown不支持设置文本的颜色，但是很多markdown编辑器是支持HTML的，你可以使用html中的 <font> 标签。颜色属性可以设置为颜色的名字或者是十六进制#RRGGBB的颜色代码。貌似就是Markdown标签的一种形式。

```markdown
<font color = "red"> this is red </font>
<font color = #FF000000 > this is red </font>
```

渲染效果如下

<font color = "red"> this is red </font>
<font color = #FF000000 > this is red </font>

<font> 标签在技术上是支持的但是官方已经放弃了，这意味着它现在可以使用且你不得不用，因为现在没有什么方式可以替代HTML标签，你可以试着选择用CSS，但是并不是所有的Markdowm编辑器都支持CSS，如果支持的话，应该可以这么实现 <font> 标签的功能

```css
<p style="color:blue">Make this text blue.</p>
```

渲染效果如下

<p style = "color:blue">Make this text blue. </p>

### 删除线

通过在单词中心放置一条水平线来删除单词。结果看起来像这样。此功能使您可以指示某些单词是一个错误，要从文档中删除。若要删除单词，请在单词前后使用两个波浪号`~~`

```markdown
~~需要加删除线的内容~~
```

渲染效果如下

~~需要加删除线的内容~~

### 注释

通过<!---->来添加注释

```markdown
<!--这就是需要注释的内容-->
```

渲染鲜果如下

<!--这就是需要注释的内容-->



### 参考

[Markdown中文官方教程](https://markdown.com.cn)

[Markdown英文官方教程](https://www.markdownguide.org)



