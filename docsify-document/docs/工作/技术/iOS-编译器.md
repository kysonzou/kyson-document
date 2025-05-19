# 1.传统编译器设计

## 1.1 传统编译器设计

![image-3.png](../assets/iOS-编译器-传统编译器.png)

- **编译器前端：**编译器前端的任务是**解析源代码**。它会进行词法分析、语法分析、语义分析、检查代码中是否存在错误，然后构建**抽象语法树**（Abstract Syntax Tree ，缩写为 **AST**），然后成成**中间代码（** Intermediate Representation,缩写为**IR）。**

- **优化器：**优化器负责各种优化，**缩小包的体积**（剥离符号 **）** 、**改善代码的运行时间（** 消除冗余计算、减少指针跳转次数等）。

- **后端、代码生成器：**后端将代码映射到目标指令集，生成**机器语言**，并且进行机器相关的代码优化。

由于传统的编译器(如GCC) 是为**整体的应用程序设计**的，**不支持多种语言**或者**多种硬件架构**，所以他们的用途收到了很大的限制。

## 1.2 GCC

GNU 编译器集合（GCC）是GNU项目产生的优化编译器，支持各种编程语言、硬件体系结构和操作系统。GCC 是GNU 工具链的关键组件，也是大多数与GNU和Linux 内核相关的项目的标准编译器。

GCC 原名为 GNU C 语言编译器，因为它原本只能处理 C语言。GCC 很快地扩展，变得可处理 C++。之后也变得可处理 Fortran、Pascal、Objective-C、Java, 以及 Ada与其他语言。

# 2.LLVM的设计

## 2.1 LLVM

**LLVM** 是编译器的架构系统，**C++** 编写而成的。用于优化以任意语言编写的程序的**编译时间(compile-time)、连接时间(link-time)、运行时间(run-time)、空闲时间 (idle-time)**。

**LLVM**设计中最重要的设计是使用了通用的代码表示形式(**IR)，** 在需要支持一种**新的语言**时 **，** 只需要再编写一个可以**产生IR的** **独立** **前端；** 需要支持一种**新的硬件架构**时 **，**只需要再编写一个**可以接收IR的** **独立后端** **。**

![image-4.png](../assets/iOS-编译器-LLVM.png)

## 2.2 LLVM组件

LLVM组件可以分为以下几类：

- **前端（Frontend）**：负责将源代码编译成 LLVM 中间表示（IR）。LLVM 提供了用于编译 C、C++、Objective-C、Objective-C++、Rust、Swift、Go 等语言的前端。
- **优化器（Optimizer）**：负责对 LLVM IR 进行优化，以提高程序的性能和可移植性。LLVM 提供了一个庞大的优化器流水线，包含了许多不同的优化 pass。
- **后端（Backend）**：负责将 LLVM IR 转换为目标机器代码。LLVM 提供了用于生成 x86、x86-64、ARM、AArch64、PowerPC、RISC-V 等平台的后端。
- **工具（Tools）**：提供用于处理 LLVM 文件和 IR 的工具。LLVM 提供了汇编器、反汇编器、调试器、符号表分析器等工具。

以下是一些主要的 LLVM 组件：

1. **Clang**: Clang 是 LLVM 的前端编译器，它用于将源代码翻译成中间表示（IR）以便后续编译和优化。Clang 支持多种编程语言，如C、C++、Objective-C 和Objective-C++。

2. **LLVM IR**: LLVM 中间表示是一种类似汇编语言的中间语言，用于表示编译后的程序。LLVM IR 是静态单赋值（SSA）形式，这使得进行高效的编译优化成为可能。

3. **LLVM Core Libraries**: LLVM 包括一系列核心库，用于处理和操作 LLVM IR，以及执行各种编译器任务，如词法分析、语法分析、代码生成等。

4. **LLVM Backend**: LLVM 支持多种目标架构，因此它有不同的后端，用于将 LLVM IR 转换为特定目标架构的本地机器代码。这些后端包括X86、ARM、PowerPC等。

5. **Optimization Passes**: LLVM 提供了多种编译优化传递，用于提高生成的机器代码的性能。这些传递包括常见的传递，如死代码消除、内联函数、循环优化等。

6. **LLD (LLVM Linker)**: LLD 是 LLVM 的链接器，用于将生成的目标代码文件链接成可执行文件。LLD 支持多种不同格式的目标文件，如ELF、COFF、Mach-O等。
   1. **LLDB (LLVM Debugger)**: LLDB 是 LLVM 的调试器，用于调试生成的程序，广泛使用 LLVM 的现有库，例如Clang表达式解析器和 LLVM反汇编器。它可以与多种编程语言和平台一起使用。

7. **CMake**: LLVM 使用CMake作为构建系统，用于跨平台的构建和安装。

8. **TableGen**: TableGen 是 LLVM 中的一个工具，用于生成各种代码和数据表，包括目标描述、指令描述等。

9. **Clang Static Analyzer**: Clang Static Analyzer 是用于分析源代码以查找潜在的缺陷和错误的工具，如内存泄漏、空指针解引用等。

# 3.Clang

Clang是LLVM编译器工具集的前端，由 Apple 主动编写，是LLVM项目中的一个子项目。基于 LLVM 的轻量级编译器，之初是为了替代GCC（GCC也可以作为LLVM的前端），提供更快的编译速度。他是负责编译C、C++、Objective-C、CUDA、OpenCL...的编译器 。

> iOS在XCode编译代码码过程中，有时会遇到clang: error: linker command failed with exit code 1 (use -v to see invocation) 错误，这就是一个编译错误。

## 3.1 编译流程

可以通过下面的命令打印源码的编译过程：

```
clang -ccc-print-phases main.m
```

打印结果如下：

![image-5.png](../assets/iOS-编译器-编译流程.png)

**整个过程中，没有明确指出优化器，是因为优化已经分布在前后端里面了。**

![image-6.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14ce972a137e4621b6fd85dcd2e454aa~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp)

接下来对每个步骤，详细分析：

### 0：输入源文件：

找到源文件

### 1：预处理阶段：

执行预处理指令，包括进行宏替换、头文件的导入、条件编译，产生新的源码给到编译器.可以通过命令`clang -E main.m`，看到执行预处理指令后的代码。

### 2：编译阶段->生成IR(.ll) 或者 bitcode(.bc)文件

**进行词法分析、语法分析、语义分析、检测语法是否正确、生成AST、生成IR(.ll) 或者 bitcode(.bc)文件：**

#### 2.1 词法分析: 

预处理完成后，进行**词法分析**，将代码分隔成一个个的**Token**及标明其所在的**行数和列数**，包括关键字、类名、方法名、变量名、括号、运算符等

使用下面的命令，可以看到词法分析后的结果：

```
clang -fmodules -fsyntax-only -Xclang -dump-tokens main.m
```

![image-7.png](../assets/iOS-编译器-词法分析.png)

#### 2.2 语法分析

词法分析后，是**语法分析**，它的任务是**验证源程序的语法结构的正确性**，在词法分析的基础上，将单词组合成各类语法短语，如语句、表达式等。然后将所有节点组成抽象语法树（**AST**）。

通过下面的命令，可以查看语法分析后的结果：

```
clang -fmodules -fsyntax-only -Xclang -ast-dump main.m

// 如果导入头文件找不到，可以指定SDK
clang -isysroot sdk路径 -fmodules -fsyntax-only -Xclang -ast-dump main.m
```

![image-8.png](../assets/iOS-编译器-语法分析.png)

#### 2.3 生成IR

将**语法树**自顶向下遍历逐步**翻译成LLVM IR**。OC 代码在这一步会进行**运行时**的处理，比如 **分类属性的合成、ARC处理等**

通过下面的命令可以生成 **.ll** **的文本文件**，查看**IR代码：**

```
clang -S -fobjc-arc -emit-llvm main.m
```

![image-9.png](../assets/iOS-编译器-生成IR.png)

**上面IR代码的意思是**：

1. test 方法，输入两个参数 %0， %1
2. 创建两个变量 %3，%4

1. 将%0的数据写入到%3中，将%1的数据写入到%4中
2. 读取%3的数据并赋值给%5，读取%4的数据并赋值给%6

1. 将%5 加上 %6的结果赋值给%7
2. 将%7 加上 3 的结果赋值给%8

1. 返回%8

#### IR 优化

在上面的IR代码中，可以看到，通过一点一点翻译语法树，生成的IR代码，看起来有点蠢，其实是可以优化的。

**IR优化等级从低到高分别是：** **-O0 -O1 -O2 -O3 -Os -Ofast -Oz**

可以使用**命令**进行**优化**:

```
clang -Os -S -fobjc-arc -emit-llvm main.m -o main.ll
```

也可以在 **xcode** 中**设置**：target -> build Setting -> **Optimization Level**

![iOS-编译器-Xcode设置优化级别](../assets/iOS-编译器-Xcode设置优化级别.png)

我们看一下**Os级别**优化后的代码：

![image-11.png](../assets/iOS-编译器-IR优化后.png)

**上面IR代码的意思是**：

1. 将%0 加上 3 结果赋值给%3
2. 将%3加上%1的结果赋值给%4

1. 返回%4

**优化后的IR代码，更加的简洁明了了！**

#### bitcode

xcode7之后，如果开启了bitcode, 苹果会**对IR文件**做进一步的**优化** **生成.bc 文件**的中间代码。

命令如下：

```
clang -emit-llvm -c main.ll -o main.bc
```

### 3：后端阶段->汇编文件(.s)：

后端将接收到的 IR 结构化成不同的处理对象，并将其处理过程实现为一个个的Pass类型。通过处理 Pass ，来完成对IR的转换、分析和优化。然后生成汇编代码。

命令如下：

```bash
// bitcode -> .s  
clang -S -fobjc-arc main.bc -o main.s
// IR -> .s  
clang -S -fobjc-arc main.ll -o main.s
// 也可以对汇编代码进行优化
clang -Os -S -fobjc-arc main.ll -o main.s
```

![image-12.png](../assets/iOS-编译器-生成汇编文件.png)

### 4：汇编阶段->生成目标文件(.o)：

汇编器将汇编代码转换成机器码，生成一个个的目标文件的Mach-O文件

命令如下：

```
clang -fmodules -c main.s -o main.o
```

通过 nm 的命令，查看main.o的mach-O文件的符号

```
xcrun nm -nm main.o
```

打印结果如下：

![image-13.png](../assets/iOS-编译器-生成目标文件.png)

可以看到执行命令时，报了一个错：**没找到外部的 _printf 的符号。** 因为这个函数是在外部引入的，这里需要把**使用到的其他的库也** **链接过来**，才能不报错。

### 5：链接阶段->可执行的Mach-O文件：

将一个个的目标文件链接到一起，并且**链接需要的动态库(.dylib)和静态库(.a)** ，生成**可执行文件 -（Mach-O）文件。**

命令如下：

```
clang main.o -o main
```

![image-14.png](../assets/iOS-编译器-生成可执行文件.png)

可以看到打印结果中依然显示没有找到外部符号 printf , 但是后面多了（from libsystem）。**指明_printf 所在的库是** **libsystem。** 这是因为**libsystem动态库，** 需要在**运行时动态绑定** **。** 目前这个文件已经是一个**正确的可执行文件**了。

使用如下命令执行：

```
./main
```

执行结果：

![image-15.png](../assets/iOS-编译器-执行结果.png)

### 6：绑定硬件架构：

**根据x86_64硬件架构生成对应的可执行文件** **（Mach-O）**

## 3.2 总结编译流程

### 1. 各阶段使用的命令

```
//// ====== 前端 开始=====
// 1. 词法分析
clang -fmodules -fsyntax-only -Xclang -dump-tokens main.m

// 2. 语法分析
clang -fmodules -fsyntax-only -Xclang -ast-dump main.m

// 3. 生成IR文件
clang -S -fobjc-arc -emit-llvm main.m

// 3.1 指定优化级别生成IR文件
clang -Os -S -fobjc-arc -emit-llvm main.m -o main.ll

// 3.2 （根据编译器设置） 生成bitcode 文件
clang -emit-llvm -c main.ll -o main.bc


//// ====== 后端 开始=====

// 1. 生成汇编文件
// bitcode -> .s  
clang -S -fobjc-arc main.bc -o main.s
// IR -> .s  
clang -S -fobjc-arc main.ll -o main.s
// 指定优化级别生成汇编文件
clang -Os -S -fobjc-arc main.ll -o main.s


// 2. 生成目标Mach-O文件
clang -fmodules -c main.s -o main.o
// 2.1 查看Mach-O文件
xcrun nm -nm main.o

// 3. 生成可执行Mach-O文件
clang main.o -o main


//// ====== 执行 开始=====
// 4. 执行可执行Mach-O文件
./main
```

### 2. 各个阶段生成的文件类型

![image-16.png](../assets/iOS-编译器-Clang各流程生成的文件.png)

### 3. 编译流程图示

![image-17.png](../assets/iOS-编译器-Clang流程示意图.png)

## 3.3 OC 生成C++文件

- **功能：** 可以把 `OC` 文件编译成 `C++`文件。 例如 `main.m` 编译成 `main.cpp` 文件，用来更好的查看代码的底层结构及实现逻辑，便于了解底层原理。

- **编译方式：** 在终端中进入需要编译的文件所在目录，执行文件编译命令：

  ```
  //1、将 main.m 编译成 main.cpp
  clang -rewrite-objc main.m -o main.cpp
  
  //2、将 ViewController.m 编译成  ViewController.cpp
  clang -rewrite-objc -fobjc-arc -fobjc-runtime=ios-13.0.0 -isysroot / /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator13.7.sdk ViewController.m
  
  //以下两种方式是通过指定架构模式的命令行，使用xcode工具 xcrun
  //3、模拟器文件编译
  - xcrun -sdk iphonesimulator clang -arch arm64 -rewrite-objc main.m -o main-arm64.cpp 
  
  //4、真机文件编译
  - xcrun -sdk iphoneos clang -arch arm64 -rewrite-objc main.m -o main- arm64.cpp 
  ```

举个🌰：

```
- (instancetype)init {
    self = [super init];
    if (self) {
        NSLog(@"%@-----%@", [self class], [super class]);
    }
    return self;
}
```

编译后：

```
static instancetype _I_LGPerson_init(LGPerson * self, SEL _cmd) {
    self = ((LGPerson *(*)(__rw_objc_super *, SEL))(void *)objc_msgSendSuper)((__rw_objc_super){(id)self, (id)class_getSuperclass(objc_getClass("LGPerson"))}, sel_registerName("init"));
    if (self) {
        NSLog((NSString *)&__NSConstantStringImpl__var_folders_86_0y_j3bzj65z6vw6hy1chw_4m0000gp_T_LGPerson_1615a9_mi_0, ((Class (*)(id, SEL))(void *)objc_msgSend)((id)self, sel_registerName("class")), ((Class (*)(__rw_objc_super *, SEL))(void *)objc_msgSendSuper)((__rw_objc_super){(id)self, (id)class_getSuperclass(objc_getClass("LGPerson"))}, sel_registerName("class")));
    }
    return self;
}
```

以上参考[iOS编译原理篇“LLVM & Clang”](https://juejin.cn/post/7041112216287838238)



# 4.Swiftc

**Swift** 的编译过程中使用 **Swiftc** ，与 **Clang** 一样，**Swiftc** 是**LLVM**编译架构的一个**前端。**

## 4.1 swift 的编译流程

![image.png](../assets/iOS-编译器-Swift流程示意图.png)

**与 Clang 相比， LLVM前端的流程中，在AST 和 IR之间，多了一层中间语言SIL** **(Swift Intermediate Language )** **，** 这么做的目的是希望弥补一些 Clang 编译器的缺陷，如无法执行一些**高级分析，可靠的诊断和优化**，而 AST 和LLVM IR 都不是合适的选择。因此，SIL应运而生，用来解决现有的缺陷。

以上参考[Swift高级进阶-Swift编译过程，”SIL代码“，“IR语法”](https://juejin.cn/post/7041105468852273166)



# 5.Xcode编译器的变化历史

1. GCC编译器时代
2. LLVM-GCC编译器时代
3. LLVM-Clang、LLVM-Swiftc编译器时代

