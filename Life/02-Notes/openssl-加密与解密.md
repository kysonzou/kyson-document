---
category:
  - Tech
tags:
  - Network
status: Done
---



### 1、对称加密

#### 1.1 AES 加密与解密

**AES (Advanced Encryption Standard)** 是一种对称加密算法，支持多种密钥长度（128, 192, 256 位）。
  
**加密**
```bash
openssl enc -aes-256-cbc -salt -in plaintext.txt -out encrypted.txt
```
- aes-256-cbc: 使用 AES 256 位加密，CBC 模式
- salt: 增加盐值提高安全性
- in: 输入文件
- out: 输出加密文件

**解密**
```bash
openssl enc -aes-256-cbc -d -in encrypted.txt -out decrypted.txt
```
- d: 表示解密


#### 1.2 DES 加密与解密

  **DES**（Data Encryption Standard）也是一种对称加密算法，但现在由于安全性原因通常推荐使用 AES。

  **加密**
```bash
openssl enc -des-cbc -salt -in plaintext.txt -out encrypted_des.txt
```
- -des-cbc: 使用 DES 加密，CBC 模式

**解密**
```bash
openssl enc -des-cbc -d -in encrypted_des.txt -out decrypted_des.txt
```
- -d: 表示解密

### 2、非对称加密

#### 2.1 RSA 加密与解密

  **RSA** 是一种非对称加密算法，适合用来加密小数据或者用于加密对称密钥。

1. **生成 RSA 密钥对：**
   ```bash
   # 生成私钥
   openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048 

   # 从私钥中导出公钥
   openssl rsa -pubout -in private_key.pem -out public_key.pem 
   ```
   - 2048: 密钥长度（位数），通常为 2048 或 4096

2. **使用公钥加密：**
   ```bash
   openssl rsautl -encrypt -inkey public_key.pem -pubin -in plaintext.txt -out encrypted_rsa.bin
   ```
   - -pubin：表示使用公钥加密。
   
3. **使用私钥解密：**
   ```bash
   openssl rsautl -decrypt -inkey private_key.pem -in encrypted_rsa.bin -out decrypted_rsa.txt
   ```

#### 2.2 ECC 加密与解密

  **ECC (Elliptic Curve Cryptography)** 是一种基于椭圆曲线的非对称加密算法，密钥长度比 RSA 短，但提供相同级别的安全性。

1. **生成 ECC 密钥对：**
   ```bash
   # 生成私钥
   openssl ecparam -genkey -name prime256v1 -out ecc_private.pem 

   # 从私钥导出公钥
   openssl ec -in ecc_private.pem -pubout -out ecc_public.pem 
   ```
   - prime256v1：指定椭圆曲线的名称。

2. **ECC 加密与解密**  
   OpenSSL 默认不提供 ECC 加密命令，可以通过其他库或手动实现 ECC 加密解密。
