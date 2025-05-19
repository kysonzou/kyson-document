---
category:
- Tech
tags:
- Compiler
status: Done
---



### 1. make 是什么
make 是一个自动化构建工具，用于管理和编译程序项目。它使用一个叫 Makefile 的配置文件，定义如何生成项目中的目标文件。make 工具通过读取 Makefile 中的规则，自动判断哪些文件需要重新编译，并根据依赖关系执行相应的命令。这样可以节省时间和减少错误，因为只会重新编译那些发生变化的文件，而不是整个项目。

- **依赖管理**：make 会检查每个文件的修改时间，仅重新编译发生变化的文件，避免不必要的重复工作。
-  **规则与目标**：Makefile 中定义的规则（如“文件A依赖于文件B”）让 make 可以清晰地知道构建流程。这些规则类似于脚本中的命令序列，但 make 会自动解析依赖关系和构建顺序。
- **跨平台适应**：Makefile 提供了一种跨平台的项目构建方式，尤其在 Unix/Linux 系统中非常通用。

### 2. 典型的Make file文件

#### 2.1 makefile文件
```makefile
# 编译器和选项
CC = gcc
CFLAGS = -Wall -O2 -g
LDFLAGS = -lm

# 文件设置
SRC = $(wildcard *.c)
OBJ = $(SRC:.c=.o)
TARGET = main

# 默认目标
all: $(TARGET)

# 链接目标文件
$(TARGET): $(OBJ)
    $(CC) $(LDFLAGS) -o $@ $(OBJ)

# 编译每个源文件
%.o: %.c
    $(CC) $(CFLAGS) -c $< -o $@

# 清理命令
clean:
    rm -f $(OBJ) $(TARGET)
```

#### 2.2 运行流程

假设项目目录中有 main.c 和 utils.c 两个源文件，执行 make 的完整流程如下：

1. **运行** make：make 执行默认目标 all，all 依赖于 main。

2. **检查** main：make 发现 main 依赖 main.o 和 utils.o，并且这些 .o 文件需要生成。

3. **编译** .c **文件**：

   • 执行 $(CC) $(CFLAGS) -c main.c -o main.o 生成 main.o。  
   • 执行 $(CC) $(CFLAGS) -c utils.c -o utils.o 生成 utils.o。

4. **链接**：

   • 执行 $(CC) $(LDFLAGS) -o main main.o utils.o 生成最终的可执行文件 main。

5. **清理**：运行 make clean 时会删除 main.o、utils.o 和 main 文件。

#### 2.3 **参数说明**
1.  **编译器和选项**
    ```makefile
    CC = gcc
    # CC：指定编译器，这里使用的是 gcc（GNU Compiler Collection）。
    # 这样设置后，后续使用 $(CC) 就等同于 gcc，方便更改编译器（例如 clang），只需修改这一  行。
    ```

    ```makefile
    CFLAGS = -Wall -O2 -g
    # CFLAGS：传递给编译器的参数，通常用于控制编译行为。
    # -O2：开启二级优化，生成更高效的代码，通常在性能和编译时间之间取得平衡。
    # -Wall：开启所有常见的编译警告，帮助检测潜在问题。
    # -g：添加调试信息，使调试器能关联代码行和机器代码。
    ```

    ```makefile
    LDFLAGS = -lm
    # LDFLAGS：传递给链接器的参数。
    # -lm：表示链接数学库 libm，一般用于程序中包含数学函数（如 sin()、cos()）时。
    ```

2. **文件设置**
   ```makefile
    SRC = $(wildcard *.c)
    # SRC：定义源文件列表。$(wildcard *.c) 使用 Makefile 内建的 wildcard 函数，自动找到当前目录下所有 .c 文件。
    # 例如，如果目录中有 main.c 和 utils.c，那么 SRC 将被设置为 main.c utils.c。
    ```

    ```makefile
    OBJ = $(SRC:.c=.o)
    # OBJ：定义目标文件列表，将所有 .c 文件名替换为 .o。
    # $(SRC:.c=.o) 表示将 SRC 中每个文件的 .c 后缀替换为 .o。
    # 例如，main.c utils.c 将变成 main.o utils.o。
    ```

    ```makefile
    TARGET = main
    # TARGET：定义最终生成的可执行文件名称，这里设为 main。可以随意命名，也可以通过调整 Makefile 来生成不同的目标文件。
    ```

3. **默认目标**
    ```makefile
    all: $(TARGET)
    # all：这是默认的目标，即 make 执行时首先会找到 all 并执行。
    # $(TARGET)：all 的依赖项是 $(TARGET)，因此在执行 all 时会先尝试生成目标文件 main。
    # 可以通过 make all 或仅 make 来触发此规则。
    ```
4. **链接目标文件**
   ```makefile
    $(TARGET): $(OBJ)
       $(CC) $(LDFLAGS) -o $@ $(OBJ)
    # $(TARGET): $(OBJ)：定义生成可执行文件 main 的规则，依赖于 $(OBJ) 列表中的所有 .o 文件。
    
    # $(CC) $(LDFLAGS) -o $@ $(OBJ)：这行命令将所有目标文件链接成最终的可执行文件。
    # $(CC)：使用定义的编译器（即 gcc）。
    # $(LDFLAGS)：传递给链接器的参数。
    # -o $@：指定生成文件的名称，$@ 表示目标名称，即 main。
    # $(OBJ)：包含所有 .o 文件，用于链接成可执行文件。
    ```
5. **编译每个源文件**
   ```makefile
    %.o: %.c
       $(CC) $(CFLAGS) -c $< -o $@
    # %.o: %.c：表示一个通用规则，将每个 .c 文件编译为相应的 .o 文件。
    # %.o 和 %.c 中的 % 表示通配符，比如 main.c 会匹配 main.o。

    # $(CC) $(CFLAGS) -c $< -o $@：这是编译命令，将 .c 文件编译为 .o 文件。
    # $(CC)：编译器。
    # $(CFLAGS)：编译参数。
    # -c：表示仅编译，不进行链接，生成 .o 文件。
    # $<：表示第一个依赖文件，即当前要编译的 .c 文件。
    # -o $@：指定输出文件名，这里是对应的 .o 文件。
    ```

6. **清理命令**
   ```makefile
    clean:
       rm -f $(OBJ) $(TARGET)
    # clean：清理规则，通常用于删除生成的中间文件和可执行文件。
    
    # rm -f $(OBJ) $(TARGET)：删除所有 .o 文件和最终的可执行文件 main。
    # -f：表示强制删除，不提示确认。
    # 可以通过 make clean 执行清理命令。
    ```

### 3. 用gcc或者[[Compiler-clang|clang]]实现编译和链接

```bash
# 编译每个源文件
gcc -Wall -g -O2 -c main.c -o main.o
gcc -Wall -g -O2 -c utils.c -o utils.o

# 链接生成可执行文件
gcc main.o utils.o -o main -lm

# 清理中间文件（可选）
rm -f *.o 
```

  也可以编译、链接一起，它们在命令行上的区别就是有没有 `-c` 参数 , `-c` 表示只编译不链接

```bash 
gcc -Wall -g -O2 main.c utils.c -o main
```

### 4. 为什么要先编译在链接

#### 4.1. 增量编译，提升编译效率

当项目包含多个源文件时，分开编译 .c 文件为 .o 文件能显著加快编译过程：  

• 如果修改了 main.c，只需要重新编译 main.c 为 main.o，无需重新编译其他文件如 utils.c。  

• 然后，链接阶段只需使用已编译好的 .o 文件生成可执行文件。  

这种方式避免了每次修改都从头编译整个项目，提高了效率。

#### 4.2. 简化调试与模块化

分开编译使代码更模块化，每个 .o 文件独立对应一个 .c 文件的功能模块：

• 这便于调试，某个模块有问题时只需修改对应的 .c 文件并重新编译，而不必影响其他模块。

• 如果需要重用某些模块，只需保留其 .o 文件，链接时直接使用。

#### 4.3. 便于依赖管理

编译和链接分开更有利于管理复杂项目的依赖关系：

• Makefile 通过设置依赖项，能自动追踪哪些 .o 文件需要重新编译，哪些可以复用，简化管理。

#### 4.4. 灵活的链接控制

有时会需要将一些 .o 文件与不同的库或配置进行组合：

• 例如，可以针对不同版本的程序，只需链接不同的 .o 文件和库，而不用重新编译整个项目。

因此，分开编译和链接能带来更高的编译效率和灵活性，尤其在项目规模较大、模块较多的情况下。