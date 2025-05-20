---
category:
  - Tech
tags:
  - Git
status: Done
---
**GitHub Flow** 和 **[[Git-GitLab Flow|GitLab Flow]]** 这两种 Git 工作流程的设计逻辑、核心原则和具体步骤。它们都强调使用特性分支和合并请求（Pull/Merge Requests），并且都非常注重代码审查和自动化。GitLab Flow 通常被看作是 GitHub Flow 的一种扩展或一组更灵活的变体，以适应更复杂的部署需求。

### 一、设计逻辑与核心原则

GitHub Flow 以其极致的简洁性而闻名，特别适合那些实践持续交付（Continuous Delivery）或持续部署（Continuous Deployment）的团队。

1. **`main` 分支始终是可部署的 (main is always deployable):** 这是 GitHub Flow 最核心的基石。`main` 分支（在 Git 的早期版本中通常是 `master` 分支）必须时刻保持稳定，并且可以随时部署到生产环境。所有在 `main` 分支上的提交都应该通过了所有测试。
2. **从 `main` 创建描述性的分支 (Create descriptive branches off `main`):** 所有新的工作，无论是新功能、Bug 修复还是实验性尝试，都应该在一个从 `main` 分支当前状态创建出来的、具有清晰描述性名称的分支上进行。这样可以隔离各个工作单元。
    - 例如：`feature/user-login` (功能/用户登录), `fix/payment-gateway-error` (修复/支付网关错误), `experiment/new-homepage-layout` (实验/新首页布局)。
3. **定期推送到命名分支 (Push to named branches regularly):** 在本地进行提交，并定期将你的工作推送到远程服务器上对应的命名分支。这样做的好处是：
    - 方便团队成员之间的协作和代码共享。
    - 让其他人了解你的工作进展。
    - 作为一种备份，防止本地数据丢失。
4. **准备好后发起合并请求 (Open a Pull Request when ready):** 当你认为一个功能开发完成，或者即使工作仍在进行中但希望获得反馈时，从你的特性分支向 `main` 分支发起一个合并请求（Pull Request,简称 PR）。
5. **通过 PR 进行协作、审查和测试 (Collaborate, review, and test via the PR):** PR 是团队讨论、代码审查（Code Review）和自动化检查（如持续集成构建、自动化测试、代码风格检查等）的中心。如果在审查或测试中发现问题，开发者应该在自己的特性分支上进行修改并推送新的提交，PR 会自动更新这些新的更改。
6. **在合并前回滚特性分支进行最终测试 (Deploy from the branch for final testing - 可选但推荐):** 在将特性分支合并到 `main` 之前，可以将该特性分支部署到一个预生产环境（staging）或测试环境中，以验证其在集成环境中的行为是否符合预期。
7. **仅在审查通过且 CI 成功后合并到 `main` (Merge to `main` only after review and CI passes):** 一旦 PR 获得批准，所有讨论的问题都已解决，并且所有的自动化检查都成功通过，就可以将特性分支合并到 `main` 分支。
8. **立即部署 `main` 分支 (Deploy `main` immediately):** 因为 `main` 分支始终是可部署的，所以一旦有新的代码合并进来，就应该立即将其部署到生产环境。
9. **合并后删除特性分支 (Delete the feature branch after merge):** 这有助于保持仓库的提交历史整洁，移除不再需要的特性分支。

### 二、工作流程步骤 (简化版)

1. **创建分支:** `git checkout -b new-feature main`
2. **添加提交:** 进行代码修改, `git add .`, `git commit -m "描述信息"`
3. **推送分支:** `git push -u origin new-feature`
4. **发起合并请求:** 访问 GitHub 网站, 从 `new-feature` 分支向 `main` 分支发起一个 PR。
5. **讨论与审查:** 团队成员审查代码，进行评论。CI (持续集成) 系统运行自动化检查。
6. **根据反馈修改 (如果需要):** 根据审查意见在 `new-feature` 分支上添加更多提交, `git push`。
7. **合并:** 一旦 PR 被批准且所有检查通过，在 GitHub 上合并 PR。
8. **部署:** 合并后的 `main` 分支被自动或手动部署到生产环境。
9. **删除分支:** 在本地删除 `new-feature` 分支 (`git branch -d new-feature`) 并在远程删除 (可以通过 GitHub 界面或 `git push origin --delete new-feature`)。

### 三、最适合的场景

- Web 应用和服务。
- 实践持续交付或持续部署的团队。
- 生产环境中始终维护一个单一、稳定版本的项目。
- 开源项目也经常采用类似的工作模式。

