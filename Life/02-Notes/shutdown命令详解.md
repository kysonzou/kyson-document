---
category:
  - Tech
tags:
  - Linux
  - MacOS
status: Done
---

>[!Note] 在macos上面貌似没有定时关机功能的，但是可以用命令行实现。
>```shell
>sudo shutdown +h 60.  # 60分钟后关机
>
>sudo shutdown -c # 取消关机事件
>```


`shutdown` 是用于关闭或重启计算机的命令，通常在 Linux 和 Unix 系统中使用。这个命令有多个参数，可以实现不同的功能，如立即关机、延时关机、重启、注销用户等。

### `shutdown` 命令的基本格式
```bash
shutdown [OPTION] [TIME] [MESSAGE]
```

### 常用选项和方法

1. **立即关机**
   - **Linux:**
     ```bash
     shutdown -h now
     ```
	  其中 `-h` 表示关机，`now` 表示立即执行。
   
2. **定时关机**
   - **Linux:**
     ```bash
     shutdown -h +10
     ```
     这将在 10 分钟后关机。

3. **重启**
   - **Linux:**
     ```bash
     shutdown -r now
     ```
     其中 `-r` 表示重启，`now` 表示立即执行。

4. **取消关机**
   - **Linux:**
     ```bash
     shutdown -c
     ```
     取消之前设置的关机操作。
     在Linux或Unix还可以使用 **killall** 的命令来终止命令

5. **发送消息**
   - **Linux:**
     ```bash
     shutdown -h +5 "系统将在5分钟后关机，请保存工作。"
     ```
     在 5 分钟后关机，并向所有登录的用户发送消息。
