#!/usr/bin/python
# -*- coding:utf-8 -*-
import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    m = f.read()
    connection.executescript(m)

cur = connection.cursor()

cur.execute("INSERT INTO twitter (batch,conversation_id, date_created,username,name,place,tweet,language,mentions,urls,photos,replies_count,retweets_count,likes_count,hashtags,link,thumbnail) VALUES (?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?)",
            (1,'1', '2020-01-01 00:00:00', 'username', 'name', 'place', 'tweet', 'language', 'mentions', 'urls', 'photos', 'replies_count', 'retweets_count', 'likes_count', 'hashtags', 'link', 'thumbnail'))

connection.commit()
connection.close()