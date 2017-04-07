#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sqlite3
import time

board_list = ["AllTogether", "Baseball", "Beauty", "Boy-Girl", "C_Chat", "car", "Gossiping", "joke", "Japan_Travel", "KR_Entertain",
              "LoL", "marvel", "movie", "MakeUp", "MobileComm", "NBA", "PlayStation", "sex", "Stock", "StupidClown", "Tennis", "ToS", "WomenTalk"]
json_file_list = ["data/AllTogether-2812-3312.json", "data/Baseball-4530-5030.json",
                  "data/Beauty-1626-2126.json", "data/Boy-Girl-2871-3371.json",
                  "data/C_Chat-9960-10460.json", "data/car-3000-3500.json",
                  "data/Gossiping-21927-22427.json", "data/joke-4288-4788.json",
                  "data/Japan_Travel-4316-4816.json", "data/KR_Entertain-628-1128.json",
                  "data/LoL-6618-7118.json", "data/marvel-1402-1902.json",
                  "data/movie-4797-5297.json", "data/MakeUp-2025-2525.json",
                  "data/MobileComm-4500-5000.json", "data/NBA-4145-4645.json",
                  "data/PlayStation-1863-2363.json", "data/sex-2613-3113.json",
                  "data/Stock-2997-3497.json", "data/StupidClown-2835-3335.json",
                  "data/Tennis-770-1270.json", "data/ToS-2710-3210.json", "data/WomenTalk-4495-4995.json"]

conn = sqlite3.connect('ptt.db')
print("Opened database successfully")
c = conn.cursor()

for i in range(len(board_list)):
    board = board_list[i]
    json_path = json_file_list[i]

    # Read JSON file
    try:
        json_file = open(json_path)
        json_str = json_file.read()
        json_data = json.loads(json_str)
        articles = json_data['articles']
    except Exception as e:
        print("Error while open json: " + board + " for " + str(e))
        continue

    pt = False

    try:
        c.execute("DELETE FROM " + board)

        # Insert a row of data
        for article in articles:
            # Found error record
            if "error" in article:
                continue

            articleId = article["article_id"] if "article_id" in article else "NULL"
            start = -1
            end = -1
            if "article_title" in article:
                start = article["article_title"].find('[') if article["article_title"] is not None else -1
                end = article["article_title"].find(']') if article["article_title"] is not None else -1
            category = article["article_title"][start + 1:end] if start != -1 and end != -1 else "NULL"
            title = article["article_title"] if "article_title" in article else "NULL"
            author = article["author"] if "author" in article else "NULL"
            date = article["date"] if "date" in article else "NULL"
            content = article["content"] if "content" in article else "NULL"
            ip = article["ip"] if "ip" in article else "NULL"
            push = article["message_conut"]["push"] if "message_conut" in article else "NULL"
            neutral = article["message_conut"]["neutral"] if "message_conut" in article else "NULL"
            boo = article["message_conut"]["boo"] if "message_conut" in article else "NULL"

            params = (articleId, category, title, author, date, content, ip, push, neutral, boo)

            c.execute("INSERT INTO " + board + "  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)

        conn.commit()
        print("Successful. " + board)
    except Exception as e:
        print("Failed. " + board + ' for ' + str(e))

    time.sleep(3)

conn.close()
