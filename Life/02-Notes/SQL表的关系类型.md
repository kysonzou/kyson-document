---
category:
- Tech
tags:
- SQL
status: Done
---



在数据库设计中，关系类型是决定表与表之间如何关联的关键。常见的关系有**一对多**、**多对一**、**多对多**。设计表时，关系类型直接影响表结构及其外键的设置。

### 1.  一对多/多对一关系

在“一对多”或“多对一”关系中，通常是一张表中的一个记录可以关联另一张表的多个记录，或者反过来，一张表中的多个记录只能关联另一张表的一个记录。

**示例**：一个用户可以拥有多个订单（用户表和订单表为一对多的关系）。
-   用户表（User）：
    ```sql
   CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    username VARCHAR(100)
   );
    ```

-  订单表（Orders）：
   ```sql
   CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
   );
   ```

>这个写法是通过订单点来关联订单是属于那个用户的，其实我还思考另外一个设计就是这种一对多关系的时候用户表来关联订单表，虽然看着可以，但是在`增删`的时候就是灾难性的：
>- 现在这中设计在增删的时候是只需要操作订单表，用户表不会变更； 
>- 如果是我的思考那种，那增删还得去操作用户表里面的订单字段做更新
>- 如果需要增加新的关系表时，还需要让用户表新增字段去关联，怎么想怎么不对

### 2. 多对多关系

“多对多”关系是指一张表的多条记录可以与另一张表的多条记录相关联。在这种情况下，需要引入一张**中间表**（或称关联表）来管理两张表的关系。

**示例**：电影和电影类型（Movie 与 Genre 表）之间的多对多关系。
- 电影表（Movie）：
   ```sql
   CREATE TABLE Movies (
       movie_id INT PRIMARY KEY,
       title VARCHAR(100)
   );
   ```
- 类型表（Genre）：
   ```sql
   CREATE TABLE Genres (
       genre_id INT PRIMARY KEY,
       genre_name VARCHAR(50)
   );
   ```
- 中间表（Movie_Genres）：
   ```sql
   CREATE TABLE Movie_Genres (
       movie_id INT,
       genre_id INT,
       PRIMARY KEY (movie_id, genre_id),
       FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
       FOREIGN KEY (genre_id) REFERENCES Genres(genre_id)
   );
   ```

>还有一种设计是让类型表直接关联电影点，这样貌似不对，比如两部电影都有 '喜剧'这个类型，那么类型表就会有两条'喜剧'的的记录，不是个好的设计，好的设计是应该只有一个类型，而不能重复的出现



>[!question] 关于电商评论的两种设计方式
>1. **直接在评价表中存储商品ID和评价人ID**
>    **优点：**  
>     - **简单直观**：设计清晰，评价表直接关联商品和用户，查询简单。
>     - **性能较好**：读取评价时只需查询一张表，无需进行额外的JOIN操作，尤其在评价数据量大的情况下能提高查询速度。
>     - **适用于单一场景**：如果一个评价只属于一个商品且一个用户，且评价和商品、用户之间的关系不会太复杂，这种设计足够简洁。
>
>   **缺点**
>     - **灵活性不足**：评价表结构是固定的，评价只能属于一个商品和一个用户。如果以后业务需求变更，比如允许一条评价关联多个商品或多个用户，修改会比较困难。
>     - **表扩展性较差**：如果以后需要对评价关联更多的信息（比如评价类型、评价标签等），这种设计不利于扩展。
>
>2. **使用中间表关联评价ID、商品ID和评价人ID**
>    **优点：**  
>     - **灵活性高**：可以支持复杂的关系，例如一条评价可以同时关联多个商品，或一个用户对同一个商品写了多条评价，业务变化时修改更灵活。
>     - **扩展性好**：如果将来需要引入更多关联信息（如评价的类别、来源等），可以通过中间表轻松实现，不需要改动评价表的结构。
>     - **解耦关系**：中间表将商品、用户与评价的关系解耦，未来修改某个关系时不会影响其他部分的数据结构。  
>
>   **缺点**
>     - **性能影响**：在查询评价时，需要进行JOIN操作，通过中间表查询商品和用户，查询复杂度增加，性能会有所下降，尤其是在评价表和中间表数据量大的情况下。
>     - **设计稍复杂**：表结构更复杂，维护和理解难度增加，尤其在涉及到多个中间表时，需要考虑如何高效地进行数据操作。
>
>3. **怎么选**
>    - **如果场景较为简单**：每个评价只针对一个商品，且由一个用户提交，评价表不会频繁扩展，直接在评价表中存储 product_id 和 user_id 会更加简单且性能更好。
>    - **如果场景较为复杂或未来扩展性需求较高**：比如允许一个评价关联多个商品、多个用户，或者需要管理更多的复杂关联，中间表的设计会更加灵活，便于未来的扩展和维护。
>    - 对于大多数普通电商或评价系统，**直接在评价表中关联商品和用户** 的方案通常已经足够，并且具有较好的性能表现。


