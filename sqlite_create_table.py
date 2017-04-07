#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sqlite3

board_list = ["AllTogether", "Baseball", "Beauty", "Boy-Girl", "C_Chat", "car", "Gossiping", "joke", "Japan_Travel", "KR_Entertain", "LoL", "marvel", "movie", "MakeUp", "MobileComm", "NBA", "PlayStation", "sex", "Stock", "StupidClown", "Tennis", "ToS", "WomenTalk"]

conn = sqlite3.connect('ptt.db')
print("Opened database successfully")
c = conn.cursor()

for board in board_list:
    try:
        # Create table
        c.execute("CREATE TABLE '%s' (articleId text, category text, title text, author text, date text, content text, ip text, push real, neutral real, boo real)" % board)
        print("Table created successfully")
    except:
        print(board + " already existed.")