1. .a是一个纯二进制文件，.framework中除了有二进制文件之外还有资源文件。
2. .a文件不能直接使用，至少要有.h文件配合，.framework文件可以直接使用。

### 什么是库

库是共享程序代码的方式，一把有"library" 和 "framework" 是两种不同的方式来共享和重用代码。

1. **Library（库）**:
   - 就是纯二进制代码文件
   - 通常分为静态库（Static Library）和动态库（Dynamic Library），静态库通常使用`.a`文件扩展名，而动态库通常使用`.dylib`文件扩展名。
2. **Framework（框架）**:
   - 是一个包含二进制代码、头文件、资源文件和其他必要文件的目录结构。
   - 框架通常有一个特定的扩展名，如`.framework`。

#### 静态库与动态库的区别

- 静态库：在编译链接时完整地拷贝至可执行文件中，会增加最终可执行文件的大小。静态库的代码在应用程序中是独立的，被多次使用就有多份冗余拷贝。
-  动态库：在运行时链接文件加载库，不会增加应用程序的大小。程序运行时由系统动态加载到内存，供程序调用，系统只加载一次，多个程序共用，节省内存。

#### iOS库形式

- 静态库：.a、自己构建的.framework
-  动态库：.dylib、系统的构建.framework

> iOS8之前个人打包动态库无法通过上架审核，但是在iOS8以后可以支持“Embedded content”功能，也可以把你的动态库嵌入到APP中使用。在 Target>General>Frameworks,Library,and Embedded content可见

#### a与.framework有什么区别

1. .a是一个纯二进制文件，.framework中除了有二进制文件之外还有资源文件。
2. .a文件不能直接使用，至少要有.h文件配合，.framework文件可以直接使用。
3. .a + .h + sourceFile = .framework。



### 构建Library库

主要是构建路径和真机、模拟器

### 构建Framework

主要是构建路径和真机、模拟器

**白嫖**

[Xcode创建自己的库](https://juejin.cn/post/6844904130939453453)



