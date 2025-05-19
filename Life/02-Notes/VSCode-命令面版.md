---
category:
  - Tech
tags:
  - VSCode
status: Done
---
在 VS Code 中启动命令面板，除了可以使用 `>` 符号外，还有以下几种方式，它们各有不同的用途和前缀：

**1. `>` (或直接使用快捷键)：**

   *   **快捷键:**  `Ctrl+Shift+P` (Windows/Linux) 或 `Cmd+Shift+P` (macOS)
   *   **前缀:**  `>`
   *   **功能:**  **执行命令 (Command Palette)**。这是最常用的方式，可以访问 VS Code 的所有命令，包括内置命令和扩展命令。
   *   **示例:**  `>Remote-SSH: Connect to Host...`、`>Git: Clone`、`>Python: Run Python File in Terminal`

**2. 无前缀 (直接输入)：**

   *   **功能:**  **快速打开文件 (Quick Open)**。可以直接输入文件名或文件路径，快速打开项目中的文件。
   *   **示例:**  `app.py`、`src/components/Button.js`

**3. `@`：**

   *   **功能:**  **跳转到文件中的符号 (Go to Symbol in File)**。可以跳转到当前文件中的函数、类、变量等定义。
   *   **示例:**  `@myFunctionName`、`@MyClass`

**4. `#`：**

   *   **功能:**  **跳转到工作区中的符号 (Go to Symbol in Workspace)**。可以跳转到整个工作区中的函数、类、变量等定义。
   *   **示例:**  `#calculateTotal`、`#User`

**5. `:`：**

   *   **功能:**  **跳转到指定行号 (Go to Line)**。
   *   **示例:**  `:123` (跳转到第 123 行)

**6. `?`：**

   *   **功能:**  **显示帮助信息**。列出所有可用的命令面板前缀及其功能。

