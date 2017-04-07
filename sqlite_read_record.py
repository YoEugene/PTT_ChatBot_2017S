#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sqlite3
import time

target_board = "Gossiping"  # Change to the board you want to search

conn = sqlite3.connect('ptt.db')
print("Opened database successfully")


# # First method of reading records: treat cursor as an iterator.
# cursor = conn.execute("SELECT * from " + target_board)
# for row in cursor:
#     print("articleId = " + str(row[0]))
#     print("category = " + str(row[1]))
#     print("title = " + str(row[2]))
#     print("author = " + str(row[3]))
#     print("date = " + str(row[4]))
#     print("content = " + str(row[5]))
#     print("ip = " + str(row[6]))
#     print("push = " + str(row[7]))
#     print("neutral = " + str(row[8]))
#     print("boo = " + str(row[9]))
#     time.sleep(3)


# # Second method of reaging a single record: call the cursor's fetchone() function
# cursor = conn.execute("SELECT * from " + target_board)
# print(cursor.fetchone())
# time.sleep(3)
# print(cursor.fetchone())
# time.sleep(3)
# print(cursor.fetchone())


# # Find specific row by id (or other attibutes)
# cursor2 = conn.execute("SELECT title, push, boo FROM " + target_board + " where push > 100 ORDER BY push DESC" )
# for row in cursor2:
#     print(row)
#     time.sleep(1)


# # Insert a record into SQLite
# params = [, , , , , , , ... ] # put values you want to insert here
# c.execute("INSERT INTO "+ board +"  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
# conn.commit()

conn.close()
