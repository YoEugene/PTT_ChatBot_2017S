### 創造 Table

code: [sqlite_create_table.py](https://github.com/YoEugene/PTT_ChatBot_2017S/blob/master/sqlite_create_table.py)

執行指令：

```python
c.execute("CREATE TABLE [Gossiping] (articleId text, category text, ... , push real, boo real)")
```

若成功會顯示：

```
Table created successfully.
```

否則顯示：

```
Gossiping already existed.
```

***

### 讀取 Table 中的 Record

code: [sqlite_read_record.py](https://github.com/YoEugene/PTT_ChatBot_2017S/blob/master/sqlite_read_record.py)

1. 方法一：把 table_cursor 當作 iterator 一行一行讀出來

```python
conn = sqlite3.connect('ptt.db')
print("Opened database successfully")
table_cursor = conn.cursor()

table_cursor = conn.execute("SELECT * from Gossiping")

for row in table_cursor:
    print("articleId = " + str(row[0]))
    print("category = " + str(row[1]))
    print("title = " + str(row[2]))
    print("author = " + str(row[3]))
    print("date = " + str(row[4]))
    print("content = " + str(row[5]))
    print("ip = " + str(row[6]))
    print("push = " + str(row[7]))
    print("neutral = " + str(row[8]))
    print("boo = " + str(row[9]))
```

2. 方法二：使用 table_cursor 的 fetchone() method 一次讀取一行

```python
conn = sqlite3.connect('ptt.db')
print("Opened database successfully")
table_cursor = conn.cursor()

table_cursor = conn.execute("SELECT * from Gossiping")

print(table_cursor.fetchone())
print(table_cursor.fetchone())
print(table_cursor.fetchone())
```

3. 方法三：讀取 Table 中含有特定值的 record

```python
conn = sqlite3.connect('ptt.db')
print("Opened database successfully")
table_cursor = conn.cursor()

# 從 Gossiping 版搜尋 push 大於 100 的 record，顯示 title, push, boo 並以 push 數降序排列
table_cursor = conn.execute("SELECT title, push, boo FROM Gossiping where push > 100 ORDER BY push DESC" )

for row in table_cursor:
    print(row)
```

***

### 插入 Record 至 Table 中

code: [sqlite_read_record.py 最後一段](https://github.com/YoEugene/PTT_ChatBot_2017S/blob/master/sqlite_read_record.py)

```python
conn = sqlite3.connect('ptt.db')
print("Opened database successfully")
table_cursor = conn.cursor()

# put values you want to insert here
params = [, , , , , , , ... ]
table_cursor.execute("INSERT INTO Gossiping VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)

# 一定要下面這行才能完成插入
conn.commit()
```