---
category:
- Tech
tags:
- Compiler
status: Done
---



clang 是 LLVM 项目下的 C、C++ 及 Objective-C 编译器，它支持 GCC 大部分的参数，同时也提供一些独有的功能。下面列出了一些 clang 的常用命令和参数：

**基本用法**

```bash
1. clang <file>：编译源文件，但不生成可执行文件。仅检查语法。

2. clang <file> -o <output>：将源文件编译成指定的可执行文件。

3. clang <file> -c：仅编译生成目标文件（.o 文件），不链接。

4. clang <file1> <file2> -o <output>：编译多个源文件并链接成一个可执行文件。
```
  
**编译与优化选项**

```bash
1. -O0, -O1, -O2, -O3, -Ofast：优化等级，-O0 是无优化，-O3 是最高等级优化，-Ofast 是极致优化（不保证完全符合标准）。

2. -Os：优化编译输出文件的大小。

3. -Oz：进一步减小可执行文件的大小。

4. -g：生成调试信息，用于调试程序。

5. -march=<arch>：针对特定架构（如 x86-64）优化。

6. -mtune=<cpu>：为指定 CPU 调整性能（如 -mtune=native 为本地 CPU 优化）。
```

**代码检查与警告控制**

```bash
1. -Wall：启用大多数常见的警告信息。

2. -Wextra：启用更多的警告信息。

3. -Werror：将所有警告视为错误。

4. -pedantic：严格遵循标准，报告任何与标准不一致的代码。

5. -Weverything：启用所有警告，适合调试和严格检查代码质量。
```

**语言与标准控制**

```bash
1. -std=<standard>：指定语言标准，如 -std=c11、-std=c++17。

2. -stdlib=<libc++ or libstdc++>：指定 C++ 标准库，如 libc++ 或 libstdc++。

3. -fsyntax-only：仅进行语法检查，不生成目标文件。
```
  
**预处理选项**

```bash
1. -D<macro>：定义宏，在代码中相当于 #define。

2. -U<macro>：取消定义宏。

3. -E：仅运行预处理器，生成预处理后的输出。

4. -I<dir>：指定头文件路径。

5. -include <file>：编译时强制包含一个头文件。
```
  
**链接选项**

```bash
1. -L<directory>：指定链接库的路径。

2. -l<library>：链接指定的库，如 -lm 表示链接数学库 libm。

3. -static：生成静态链接的可执行文件。

4. -shared：生成共享库（如 .so 文件）。

5. -fPIC：为共享库生成位置无关代码。
```
  
**生成目标代码和汇编代码**

```bash
1. -S：生成汇编代码，不生成目标文件。

2. -emit-llvm：生成 LLVM IR 中间代码。

3. -emit-llvm -S：生成 LLVM 汇编代码（.ll 文件）。

4. -emit-llvm -c：生成 LLVM 位代码（.bc 文件）。
```
  
**调试与性能分析**

```bash
1. -g：生成调试信息。

2. -fsanitize=<type>：启用运行时检测，常用类型包括 address（地址错误）、undefined（未定义行为）、memory（内存错误）等。

3. -ftime-report：显示编译时各阶段的耗时。
```
  
**其他选项**

```bash
1. -v：显示编译器执行的详细信息。

2. --version：显示 clang 版本信息。

3. --help：显示所有选项的帮助信息。

4. -fno-rtti：禁用运行时类型信息（仅适用于 C++）。

5. -fexceptions：启用 C++ 异常处理。
```
  

这些命令和参数让 clang 灵活适应不同编译需求，如优化、调试、检查等。