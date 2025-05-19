### 截屏

>Shirft+Command+5

### 显示文件夹中的隐藏文件

使用快捷键Command+Shirft+.可以显示文件夹中的隐藏文件 

>Shirft+Command+.

### 查看文件夹的路径

1. 直接复制路径

   Option+Command+c 为复制路径

   >Option+Command+C 
   
2. 使用【终端】Terminal获取文件完整路径。

   将文件或文件夹拖入终端命令行中，即可显示完整路径

3. 使用【访达】的【显示】设置显示完整路径。

   打开【访达】，找到菜单栏中的【显示】->【显示路径栏】，或者使用快捷键【Option+Command+p】显示路径栏，会显示在【访达】的底部

   >Option+Command+P
   
4. 使用终端命令行

   【defaults write com.apple.finder _FXShowPosixPathInTitle -bool TRUE;killall Finder】显示完整路径

   【defaults delete com.apple.finder _FXShowPosixPathInTitle;killall Finder】，即可恢复默认显示

   会显示在【访达】的顶部

5. 使用【显示简介】查看文件完整路径

   右键文件选择【显示简介】，或者选中文件并按下快捷【Command+i】，即可调出简介菜单查看路径和文件名

   >Command+i
   
   


### 更该文件的默认打开方式

右键文件选择【显示简介】，或者选中文件并按下快捷【Command+i】，然后在`打开方式`选项中更该

