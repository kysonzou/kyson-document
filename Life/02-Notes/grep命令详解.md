---
category:
  - Tech
tags:
  - Linux
  - MacOS
status: Done
---
`grep` 是 Linux/Unix 系统中用于文本搜索的强大工具，其名称来源于“**global regular expression print**”，意为“全局正则表达式搜索并打印匹配的行”。`grep` 支持简单字符串匹配和复杂的正则表达式匹配，是系统管理员和开发者的常用工具。

---

## **基本语法**
```bash
grep [选项] [匹配模式] [文件]
```
- **选项**：用于修改 `grep` 的行为。
- **匹配模式**：要搜索的文本或正则表达式。
- **文件**：指定要搜索的文件。

如果省略文件，`grep` 会从标准输入（stdin）读取数据。

---

## **常用选项**
| **选项**    | **作用**                 | **示例**                             |
| --------- | ---------------------- | ---------------------------------- |
| `-i`      | 忽略大小写匹配                | `grep -i error file.txt`           |
| `-v`      | 反向匹配（显示不符合模式的行）        | `grep -v error file.txt`           |
| `-c`      | 仅统计匹配行的数量              | `grep -c error file.txt`           |
| `-n`      | 显示匹配行的行号               | `grep -n error file.txt`           |
| `-o`      | 仅显示匹配的部分，而不是整行         | `grep -o error file.txt`           |
| `-E`      | 支持扩展正则表达式（等同于 `egrep`） | `grep -E 'error warning' file.txt` |
| `-r`      | 递归搜索目录中的文件             | `grep -r error /path/to/directory` |
| `--color` | 高亮显示匹配的部分              | `grep --color error file.txt`      |

---

## **典型用法**

### **1. 搜索文件中的关键词**
搜索文件 `file.txt` 中包含 `error` 的行：
```bash
grep error file.txt
```

### **2. 忽略大小写**
搜索时忽略大小写：
```bash
grep -i error file.txt
```

### **3. 递归搜索目录**
搜索目录 `/var/log` 中所有文件包含 `error` 的行：
```bash
grep -r error /var/log
```

### **4. 显示匹配行的行号**
在文件中搜索并显示行号：
```bash
grep -n error file.txt
```

### **5. 反向匹配**
显示不包含 `error` 的行：
```bash
grep -v error file.txt
```

### **6. 匹配多个模式**
使用扩展正则匹配 `error` 或 `warning`：
```bash
grep -E 'error|warning' file.txt
```

### **7. 高亮显示匹配部分**
使输出更直观：
```bash
grep --color error file.txt
```


