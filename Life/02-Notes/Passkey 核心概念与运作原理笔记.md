---
category:
  - Knowledge
tags: 
status: Done
---
好的，这是我们关于 Passkey 及相关话题的聊天记录总结笔记，重点梳理 Passkey 的内容，方便你日后回顾（基于截至 2025年4月10日的讨论）：

**Passkey 核心概念与运作原理笔记**

**1. Passkey 是什么？**

- **目标：** 取代密码，提供更安全、更便捷、防钓鱼的登录方式。
- **技术基础：** 基于公钥加密技术 (Public-key Cryptography) 和 FIDO/WebAuthn 标准。
- **组成：** 每个 Passkey 包含一个**私钥 (Private Key)** 和一个**公钥 (Public Key)**。
    - 私钥：极其机密，安全地存储在你的设备硬件中。
    - 公钥：存储在网站或服务的服务器上，用于验证你的身份。
- **与传统方式区别：**
    - 通常能同时取代密码和传统的两步验证（如短信、TOTP 验证码）。
    - 登录时无需输入密码，更抗网络钓鱼。

**2. Passkey 如何工作？**

- **硬件依赖：** 强依赖设备内置的**安全硬件**（如苹果的 Secure Enclave、Windows 的 TPM、Google Pixel 的 Titan 芯片）来安全地生成、存储和使用私钥。私钥本身**不会离开**这个安全硬件（指其明文形式）。
- **登录流程：**
    1. 网站发送“挑战”（随机数据）到你的设备。
    2. 设备找到对应网站的 Passkey。
    3. 系统提示进行**本地用户验证**（User Verification）。
    4. 你使用**生物识别**（指纹/面容）或**设备密码**完成验证。
    5. 验证成功后，安全硬件**授权使用**私钥对“挑战”进行**加密签名**。
    6. 设备将签名结果发送回网站。
    7. 网站使用预存的公钥验证签名，成功则登录。
- **用户验证（如指纹）：**
    - 指纹/面容信息本身**不存储**在 Passkey 私钥中，而是由设备的安全生物识别系统独立管理（同样在安全硬件内）。
    - 指纹验证仅用于**授权**安全硬件使用私钥，验证过程和数据都在本地安全硬件内完成，网站无法获取。
    - Passkey 系统只接收到“验证成功/失败”的结果。

**3. 谁来管理 Passkey？—— Passkey 提供商 (Passkey Provider)**

- **为何需要提供商：** 解决私钥的安全存储、跨设备使用（同步）和恢复问题。
- **主要提供商：**
    - **Apple:** 通过 iCloud Keychain (iCloud 钥匙串) 管理，与 Apple ID 绑定，在苹果设备间同步。
    - **Google:** 通过 Google Password Manager (Google 密码管理器) 管理，与 Google Account 绑定，主要在 Chrome 和 Android 设备间同步。
    - **第三方密码管理器:** 如 1Password, Dashlane 等也正成为提供商，提供跨平台方案。
    - **硬件安全密钥:** 如 YubiKey，密钥存储在物理设备上，不依赖云同步。
- **选择提供商：** 通常在创建 Passkey 时根据使用的设备、浏览器和登录的账号（Apple ID / Google Account）来决定保存在哪里。

**4. Passkey 的存储与同步**

- **iCloud Keychain vs. Google Password Manager (在 Mac/iOS 上):**
    - **iCloud Keychain:** 与 macOS/iOS 系统和 Safari 深度集成，在苹果生态内同步无缝。
    - **Google Password Manager:** 主要与 Chrome 浏览器和 Google Account 集成，跨平台（如 Windows/Android）同步性更好。在 iOS 上可通过 Chrome App 集成系统自动填充功能。
- **私钥的云同步：**
    - 为了实现跨设备使用和备份，提供商（Apple/Google）**确实会同步**与私钥相关的数据。
    - **关键：** 同步的是**高度加密和安全封装**的数据，并非明文私钥。私钥在离开源设备前加密，在云端加密存储，下载到新设备后，只有在用户通过本地验证后，才会在新设备的安全硬件内解密使用。
    - **结论：** “私钥（明文）不离开安全硬件”的核心原则依然成立，但其加密副本会为了同步而传输。这强调了保护好主账户（Apple ID/Google Account）安全的重要性。

**5. 使用 Passkey 的注意事项**

- **本地设备验证：** 使用 Passkey 时**必须**通过本地验证（指纹、面容、设备密码），证明是授权用户在操作当前设备。这与你是否已登录 iCloud 或 Google 账户是两回事。
- **共享设备的生物识别信息：** 如果你在设备上（如 iPhone）同时录入了自己和他人的指纹/面容，那么**任何一个**录入信息的人**都能**通过生物识别验证，从而授权使用存储在该设备上的**所有** Passkey。因此，请仅添加完全信任的人的生物识别信息。
- **Chrome 与 iCloud Keychain 密码填充：** 在 macOS 上，Chrome 默认使用 Google Password Manager 填充**密码**，一般不直接填充 iCloud Keychain 中的**密码**。但对于 **Passkey**，由于依赖系统级 API (WebAuthn)，Chrome 可以触发系统提示，从而可能使用 iCloud Keychain 中的 Passkey。

**6. （附带说明）关于 2FA (TOTP) 验证码迁移**

- 从 iCloud Keychain 迁移到 Google Password Manager 或 Google Authenticator 时，无法直接迁移 2FA 的 TOTP 密钥。
- 需要为每个服务**手动**在网站端禁用旧的 2FA 设置，然后重新启用，并用**新的**工具（如 Google Authenticator）扫描**新的**二维码/密钥。

**核心总结:** Passkey 通过公私钥和安全硬件提供了取代密码的安全便捷方案。Passkey 提供商（如 Apple、Google）负责安全存储和加密同步密钥。使用时需通过本地设备验证（生物识别/设备密码）。理解提供商、同步机制和本地验证是掌握 Passkey 的关键。