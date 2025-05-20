---
category:
  - Tech
tags:
  - Git
status: Done
---

>**[[Git-GitHub Flow|GitHub Flow]]** 和 **GitLab Flow** 这两种 Git 工作流程的设计逻辑、核心原则和具体步骤。它们都强调使用特性分支和合并请求（Pull/Merge Requests），并且都非常注重代码审查和自动化。GitLab Flow 通常被看作是 GitHub Flow 的一种扩展或一组更灵活的变体，以适应更复杂的部署需求。

GitLab Flow 借鉴了 GitHub Flow 的简洁性，并通过增加额外的结构来处理在较大型项目或组织中常见的一些场景，例如管理不同的部署环境（如开发、预生产、生产）和明确的发布管理。它更像是一套通用的实践模式，而不是一个僵硬的规定。

### 一、设计逻辑与核心原则

1. **特性分支仍然是核心 (Feature branches are still key):** 所有的开发工作都始于特性分支，通常基于 `main` (或者 `develop`，如果将其作为主要的集成分支) 创建。
2. **合并请求至关重要 (Pull/Merge Requests (MRs) are essential):** 用于代码审查、讨论和在合并到集成分支之前运行 CI。在 GitLab 中通常称为 Merge Request (MR)。
3. **针对特定环境或特定发布的长期分支 (Environment-specific or Release-specific long-lived branches):** 这是 GitLab Flow 对 GitHub Flow 的主要扩展。你可能会有：
    - **环境分支 (Environment branches):** 例如，`main` -> `staging` -> `production`。代码从稳定性较低的环境“向下游”流向稳定性较高的环境。
    - **发布分支 (Release branches):** 例如，`release/1.2.0`, `release/1.3.0`。用于准备和稳定特定版本的发布。
4. **`main` (或 `develop`) 作为集结点 (`main` (or `develop`) as an integration point):** 特性分支首先合并到这里。这个分支通常部署到开发或预生产环境。
5. **使用标签进行发布 (Tags for releases):** 特定的提交（通常在 `production` 分支或 `release` 分支上）会通过打标签（tag）的方式来标记发布的版本 (例如, `v1.0.0`)。
6. **修复优先上游 (Upstream first (for fixes)):** 如果在生产环境中发现 Bug，修复通常在一个从生产/发布分支创建的 `hotfix` 分支上进行，然后合并回生产/发布分支并部署。之后，这个修复**也必须合并回上游**的 `main` (以及 `develop`，如果适用)，以确保修复不会在后续开发中丢失。

### 二、常见的工作流程变体

#### A. 带有环境分支的 GitLab Flow

- **分支结构:**
    - `main`: 主要的开发/集成分支。部署到开发环境或预生产环境 (staging)。
    - `staging` (或 `pre-production`): 代表预生产环境。代码从 `main` 合并到 `staging` 以进行更全面的测试。
    - `production`: 代表线上生产环境的代码。代码从 `staging` (或在 `staging` 测试通过后的 `main`) 合并到 `production`。
- **工作流程步骤:**
    1. 从 `main` 创建 `feature-branch`。
    2. 在 `feature-branch` 上开发、提交、推送。
    3. 从 `feature-branch` 向 `main` 发起 MR。
    4. 代码审查通过，CI 通过，合并到 `main`。
    5. `main` 分支被自动或手动部署到**开发/预生产环境**。
    6. 当 `main` 分支被认为足够稳定可以进行更广泛的测试时，将 `main` 合并到 `staging`：
        - `git checkout staging`
        - `git merge main`
        - `git push origin staging`
    7. `staging` 分支被部署到**预生产环境**。
    8. 在预生产环境测试成功后，将 `staging` 合并到 `production`：
        - `git checkout production`
        - `git merge staging`
        - `git push origin production`
    9. `production` 分支被部署到**线上生产环境**。在 `production` 分支上为该版本打上标签。
    10. **紧急修复 (Hotfixes):** 从 `production` 创建 `hotfix-branch`，修复问题，合并回 `production` 并部署。然后，务必将 `hotfix-branch` 的更改也合并回 `staging` 和 `main`。

#### B. 带有发布分支的 GitLab Flow

- **分支结构:**
    - `main` (或 `develop`): 主要的集成分支，特性分支合并到这里。
    - `release/<version>` (例如, `release/1.2.0`): 当准备新版本发布时，从 `main` 创建。只允许与此版本相关的 Bug 修复进入此分支。
- **工作流程步骤:**
    1. 从 `main` 创建 `feature-branch`。
    2. 在 `feature-branch` 上开发、提交、推送。
    3. 从 `feature-branch` 向 `main` 发起 MR。
    4. 代码审查通过，CI 通过，合并到 `main`。
    5. 当准备开始一个新的发布周期时 (例如, 版本 1.2.0):
        - `git checkout -b release/1.2.0 main`
        - `git push -u origin release/1.2.0`
    6. `release/1.2.0` 分支现在用于该特定版本的最后测试、Bug 修复和文档更新。
        - 针对该版本的 Bug 修复提交到 `release/1.2.0`。
        - **关键：这些修复也必须合并回 `main` 分支**，以确保它们包含在未来的开发中。
    7. 一旦 `release/1.2.0` 稳定，就进行部署。
    8. 在 `release/1.2.0` 分支上为该发布的提交打上标签 (例如, `git tag v1.2.0`)。
    9. 将 `release/1.2.0` 合并回 `main` (如果 release 分支上有任何未先经过 `main` 的直接修复，这种情况应尽量避免)。一些团队如果维护一个长期的 `production` 分支，也会将 release 分支合并到 `production`。
    10. `release` 分支可能会保留一段时间以便为该版本提供后续的补丁更新，或者在不需要时删除。

### 三、最适合的场景

- 需要管理到多个不同环境（开发、预生产、生产）部署的项目。
- 有计划的发布周期，或者需要在生产环境中维护多个版本的项目（发布分支变体对此更有利）。
- 希望在 GitHub Flow 的简洁性基础上增加一些结构，但又觉得 Gitflow 过于繁重的团队。

### 四、总结对比

- **GitHub Flow** 追求极致的简洁和速度，核心是 `main` 分支始终可用于生产部署。
- **GitLab Flow** 借鉴了 GitHub Flow 中特性分支和 MR 的核心思想，并通过可选的环境分支或发布分支增加了灵活性，以更好地控制和管理更复杂的部署和发布流程。
