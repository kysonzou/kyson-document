---
category:
  - Tech
tags:
  - GCP
status: ToDo
---
本笔记总结了 `gcloud` 命令行工具中管理 **身份认证** 与 **环境配置** 的核心命令，适用于本地开发、自动化部署、多项目管理等场景。

>gcloud 配置管理核心：用“配置”管理“环境”。一个配置 = 账号 + 项目 + 区域等设置。切换配置 (activate) 就是切换完整的、包含身份和上下文的工作环境。不能用简单的账号去理解，**账号只是配置里面的一个属性**

## 一、身份认证管理（`gcloud auth`）
用于管理 `gcloud` 与 Google Cloud 通信所需的凭据。
###  1. 用户账号认证（适用于人工交互）

```bash
gcloud auth login [ACCOUNT]
```
- 启动浏览器授权流程，登录 Google 账号。
- 可选参数：
    - `--no-launch-browser`：不自动打开浏览器，适合 CLI-only 环境。
    - `--update-adc`：登录后更新应用默认凭据（ADC）。

### 2. 服务账号认证（适用于脚本和自动化）

```bash
gcloud auth activate-service-account [ACCOUNT] --key-file=<KEY_FILE>
```
- 使用服务账号 JSON 密钥文件认证。
- `ACCOUNT` 可省略，通常已包含在密钥中。
- 推荐用于 CI/CD、服务器等非交互式环境。
###  3. 查看当前认证状态

```bash
gcloud auth list
```
- 列出已登录的所有账号。
- 使用 `*` 标注当前**活动账号**。
###  4. 移除认证凭据

```bash
gcloud auth revoke [ACCOUNT]
```
- 撤销指定账号的认证信息。
- 省略 `ACCOUNT` 时撤销当前活动账号。
##  二、环境配置管理（`gcloud config`）
Google Cloud 使用“配置（Configuration）”管理不同项目、区域、账号等上下文环境。
###  1. 配置概念

|概念|说明|
|---|---|
|**Configuration**|一组命名设置集合，例如 `default`、`prod-config`|
|**Active Configuration**|当前生效的配置，所有命令默认引用该配置|
|**Property**|具体配置项，如 `core/project`, `compute/zone`|
###  2. 配置管理命令

#### 2.1 查看已有配置

```bash
gcloud config configurations list
```

####  2.2 创建新配置

```bash
gcloud config configurations create <CONFIG_NAME>
```

- 通常会引导进行账号登录和项目设置。

#### 2.3 激活配置

```bash
gcloud config configurations activate <CONFIG_NAME>
```

#### 2.4 删除配置

```bash
gcloud config configurations delete <CONFIG_NAME>
```

- 无法删除当前激活的配置。

#### 2.5 查看配置详情

```bash
gcloud config configurations describe <CONFIG_NAME>
```

### 3. 配置属性管理

#### 3.1 查看当前配置的属性

```bash
gcloud config list
```
- 显示当前活动配置中设置的所有属性。
- 常用标志：
    - `--all`：包含默认或继承的属性。
    - `--configuration=<CONFIG_NAME>`：查看指定配置。
#### 3.2 设置属性值

```bash
gcloud config set <SECTION/PROPERTY> <VALUE>
```

**常见示例：**
```bash
gcloud config set project my-project-id
gcloud config set compute/region us-central1
gcloud config set core/account user@example.com
```

#### 3.3 移除属性

```bash
gcloud config unset <SECTION/PROPERTY>
```

###  4. 常见属性说明

|属性|说明|
|---|---|
|`core/project`|默认项目 ID|
|`core/account`|默认账号|
|`compute/region`|默认区域|
|`compute/zone`|默认可用区|
##  三、认证与配置之间的交互关系

| 概念       | 说明                                                                       |
| -------- | ------------------------------------------------------------------------ |
| **关联**   | `core/account` 对应 `auth list` 中的一个账号                                     |
| **上下文**  | 配置中设置了项目、区域等默认值                                                          |
| **切换**   | 使用 `activate` 命令快速切换身份与环境                                                |
| **临时覆盖** | 所有命令均可使用标志 `--project`、`--account`、`--configuration` 等临时指定配置，**不会更改原配置** |
