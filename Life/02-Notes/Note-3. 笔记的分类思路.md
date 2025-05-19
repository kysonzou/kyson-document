---
category:
  - Life
tags:
  - Note
status: Done
---
# 2024-12-03

旧：前面的设计有主题入口和标签，但是标签设计为单主题标签，这样的标签使用不灵活

新：标签不再是单标签，而是改为多标签表示不同的主题，解决笔记属于多个主题的问题，然后后期可以引入MOC（Map Of Content）来直观的现实主题的层级，而不应该执着于只用Graph View来，为了用Graph View去妥协很多设计


# **2024-11-06** 

旧：前面那样的设计让metadata的数据变得更复杂了，同时因为笔记间的层级关系没有理想的那个清晰，所以再次更改

新：把原来的catetory、subtags、tags标签改为category、tags，tags标签作为主题标签来使用，这样在Graph图谱中就可以以主题来显示，但是这样笔记的层级是不存在的，所以再设计一个index.md文件作为所有主题的入口文件，如果笔记内容需要还可以建立assistant笔记作为子主题来让Graph脑图实现清晰的知识结构，虽然这样会新增很多assistant和index文件，但是目前就这样吧

---

# 2024-11-05

原来的方式很好的满足了文件的分类，现在随着笔记的增多和全面系统性的学习内容的时候会非常需要一个类似于脑图（思维导图）的知识结构，这个需求可以通过手动整理、通过canvas整理、或者通过插件实现，但是没有一个是完全满意的。obsidian是有关系图谱的，现在的笔记方式生成的关系图谱完全没有任何价值，所以就想着利用关系图谱来满足脑图的知识结构的需求。

旧：tags作为大类标签，这样进入Graph的时候，所有的文件都是关联到tags的，笔记之间的知识结构（层级关系）是不存在的，比如所有的Tech大类笔记全部关联在Tech标签上，很不合理。

新：把原来的tags、category的方式改为tags、subtags、category的方式，tags作为完整知识的一个入口就行，不需要每篇笔记都设置tags，只有第一层笔记关联tags作为入口，新增的subtags来做主题标签，category来做大类的细分，这样应该有效利用关系图谱这个特性

---

# 2024-10-05

通过大标签的形式去做大类的分类，然后通过category属性做具体模块的细分，这样通过dataview可以很方便的按需显示笔记看板（标签作为一级文件夹，category作为二级文件夹）
- Technology
   - Networking
   - Security
   - VSCode
   - Python
   - GFW
   - CLI
   - Other
- Life
   - 世林
- Knowledge
   - Earth
   - Laws
   - Obsidian
   - Markdown
   - Other
- Finance
   - Stocks
   - Crypto
   - Other
- Learning