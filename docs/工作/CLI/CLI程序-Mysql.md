### 数据库、数据库管理系统、数据库语句的关系

数据库（Database）、数据库管理系统（DBMS）和数据库语句（Database Statements）是在数据存储和管理领域中密切相关的概念，它们之间的关系如下：

1. **数据库（Database）**：数据库是一个结构化的数据集合，用于存储和组织数据。数据库中的数据按照某种数据模型（如关系模型、文档模型、键-值模型等）组织，可以包含表格、文档、键-值对或其他数据结构。数据库是一种持久性存储，可以长期保存数据。

2. **数据库管理系统（DBMS）**：数据库管理系统是一个软件系统，用于管理和操作数据库。它允许用户创建、访问、更新和删除数据库中的数据，并提供数据完整性、安全性、并发控制和数据备份等功能。DBMS负责管理数据库的物理存储、查询优化和数据访问，以及维护数据库的结构。

3. **数据库语句（Database Statements）**：数据库语句是指用于与数据库进行交互的命令或查询。这些语句用于创建表、插入、更新、删除和查询数据。常见的数据库语句包括SQL（Structured Query Language）语句，用于操作关系型数据库，以及各种NoSQL数据库的查询语句和命令。

- DBMS提供了一个接口，允许用户使用数据库语句来与数据库交互。用户可以使用SQL或其他查询语言向DBMS发送请求，以执行数据操作。
- DBMS负责解释和执行这些数据库语句，确保数据的完整性、安全性和一致性。
- DBMS还负责管理数据库的物理存储、索引、缓存、事务处理和查询优化等任务。

综而言之，数据库是数据的集合，DBMS是用于管理和操作数据库的软件，而数据库语句是用于与数据库进行交互的命令或查询。这三者共同协作，使得数据可以有效地存储、检索和管理。不同类型的数据库可能使用不同的数据模型和语言，但基本的概念和关系通常是类似的。

### 数据库分为哪些类型

数据库可以分为不同类型，主要根据其结构和用途来分类。以下是一些常见的数据库类型：

- **关系型数据库（RDBMS）**：这种数据库使用表格形式来存储数据，具有预定义的模式和关系。例如，MySQL、Oracle和SQL Server属于关系型数据库。(RDBMS - Relational Database Management System)
   - MySQL
   - Oracle Database
   - Microsoft SQL Server
   - PostgreSQL
   - SQLite
   - IBM Db2、MariaDB、Amazon RDS（Relational Database Service）、Google Cloud SQL、SAP HANA
- **非关系型数据库（NoSQL）**：这些数据库不使用表格形式，而是采用其他数据存储方式，如文档、键-值对、列族、图等。MongoDB、Cassandra和Redis是一些NoSQL数据库的例子。
  1. **文档数据库**：这种数据库用于存储半结构化数据，通常以JSON或类似格式存储。
     - MongoDB
  2. **键-值存储数据库**：这些数据库使用简单的键值对来存储数据，适合快速存储和检索数据。
     - Redis
     - Amazon DynamoDB
  3. **列族数据库**：这类数据库以列族的形式存储数据，通常用于大规模分布式存储。
     - HBase
  4. **图数据库**：图数据库用于存储和查询具有复杂关系的数据，如社交网络和网络拓扑。
     - Neo4
  5. **内存数据库**：这些数据库将数据存储在内存中，以加快数据访问速度。
     - Redis
  6. **时间序列数据库**：用于处理时间相关数据，如传感器数据和日志。
     - InfluxDB
     - Prometheus
  7. **空间数据库**：这种数据库专门用于存储地理信息和空间数据，如地图和地理位置。
     - PostGIS

请注意，每种数据库类型都有其自己的优势和适用场景。关联数据库通常用于需要强调数据一致性和结构的应用程序，而非关联数据库更适合需要处理大量非结构化或半结构化数据的应用程序，或者需要高度可伸缩性和性能的情况。选择数据库类型应根据您的具体需求和项目的特性来决定。

### MYSQL

1. 安装mysql

   ```bash
    $ brew install mysql
   ```

2. 启动mysql服务

   ```bash
   $ brew services start mysql
   
   $ mysql.server start
   ```

3. 暂停mysql服务

   ```bash
   $ brew services stop mysql
   ```

4. 链接mysql

   ```bash
   $ mysql -u root -p
   ```

5. 显示数据库

   ```bash
   $ show databases;
   ```

### mysql使用问题

1. **Mac下解决mysql ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)**

   在Mac上使用Homebrew安装MySQL时出现"ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)"错误通常是由于密码验证问题导致的。以下是一些可能的解决方法：

   1. 重置MySQL密码：
      如果你忘记了MySQL的root用户密码，可以尝试重置密码。请打开终端，并按以下步骤操作：

      a. 停止MySQL服务：
      ```bash
      $ brew services stop mysql
      ```

      b. 启动MySQL并跳过授权表：
      ```bash
      $ sudo mysqld_safe --skip-grant-tables
      # 如果提示已经有MySQL进程则使用
      $ sudo mysqld --skip-grant-tables
      ```
      
      c. 打开另一个终端窗口，登录到MySQL：
      ```bash
      $ mysql -u root
      ```
      
      d. 使用以下命令来更改密码：
      ```bash
      $ FLUSH PRIVILEGES;
      $ ALTER USER 'root'@'localhost' IDENTIFIED BY '新密码';
      ```

      请将 `'新密码'` 替换为你想要的新密码。
      
      e. 退出MySQL并停止mysqld_safe：
      ```bash
      $ quit
      $ sudo mysqladmin shutdown
      ```
      
      f. 重新启动MySQL服务：
      ```bash
      $ brew services start mysql
      ```
      
   1. 通过vscode一直连不上数据库，最后的问题应该是端口没有开放绑定的问题
      
      >ERROR (ext): ERROR: Error opening connection connect ECONNREFUSED 127.0.0.1:3306, {"code":-1,"data":{"driver":"MySQL","driverOptions":{"mysqlOptions":{"authProtocol":"default","enableSsl":"Disabled"}}}}
      
      这个问题搞了好久，通过终端启动mysql也是错误的，为什么这样不知道，最后直接用brew卸载了再重装解决这个问题

