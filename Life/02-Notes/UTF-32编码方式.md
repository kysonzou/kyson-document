---
category:
- Tech
tags:
- Coding
status: Done
---



**UTF-32**是32位[Unicode](https://zh.wikipedia.org/wiki/Unicode "Unicode")转换格式（Unicode Transformation Formats， 或UTF）的缩写。**UTF-32**是一种用于编码[Unicode](https://zh.wikipedia.org/wiki/Unicode "Unicode")的协定，该协定使用32位比特对每个Unicode[码位](https://zh.wikipedia.org/wiki/%E7%A0%81%E4%BD%8D "码位")进行编码（但前导比特数必须为零，故仅能表示231个Unicode[码位](https://zh.wikipedia.org/wiki/%E7%A0%81%E4%BD%8D "码位")）。与其他可变长度的Unicode转换格式（UTF）相比，UTF-32编码长度是固定的，UTF-32中的每个32位值代表一个Unicode码位，并且与该码位的数值完全一致。

UTF-32的主要优点是可以直接由Unicode码位来索引。在编码序列中查找第N个编码是一个[常数时间](https://zh.wikipedia.org/wiki/%E5%B8%B8%E6%95%B8%E6%99%82%E9%96%93 "常數時間")操作。相比之下，其他可变长度编码需要进行[循序存取](https://zh.wikipedia.org/wiki/%E5%BE%AA%E5%BA%8F%E5%AD%98%E5%8F%96 "循序存取")操作才能在编码序列中找到第N个编码。这使得在计算机程序设计中，编码序列中的字符位置可以用一个整数来表示，整数加一即可得到下一个字符的位置，就和ASCII字符串一样简单。

UTF-32的主要缺点是每个码位使用四个字节，空间浪费较多。在大多数文本中，非[基本多文種平面](https://zh.wikipedia.org/wiki/%E5%9F%BA%E6%9C%AC%E5%A4%9A%E6%96%87%E7%A8%AE%E5%B9%B3%E9%9D%A2 "基本多文種平面")的字符非常罕见，这使得UTF-32所需空间接近[UTF-16](https://zh.wikipedia.org/wiki/UTF-16 "UTF-16")的两倍和[UTF-8](https://zh.wikipedia.org/wiki/UTF-8 "UTF-8")的四倍（具体取决于文本中ASCII字符的比例）。

尽管每一個碼位使用固定長度的位元組看似方便，但UTF-32並不如其它Unicode編碼使用廣泛。與[UTF-8](https://zh.wikipedia.org/wiki/UTF-8 "UTF-8")及[UTF-16](https://zh.wikipedia.org/wiki/UTF-16 "UTF-16")相比，UTF-32更容易遭到截斷。即使使用了"定寬"字型，在大多数情况下用UTF-32計算顯示字串的寬度也并不比其他编码更加容易。主要原因是，存在著一個字符位置會有多於一種可能的碼點（[結合字符](https://zh.wikipedia.org/w/index.php?title=%E7%B5%90%E5%90%88%E5%AD%97%E7%AC%A6&action=edit&redlink=1 "結合字符（页面不存在）")）或一個碼點用多於一個字符位置（如[CJK](https://zh.wikipedia.org/wiki/CJK "CJK")表意字符）。結合符號也意味著，文書編輯者不能將一個码位視同一個編輯上的單位。