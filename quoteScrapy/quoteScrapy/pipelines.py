# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# import sqlite3
import mysql.connector

class QuotescrapyPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        # self.connection = sqlite3.connect('myquotes.db')
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = '',
            database = 'myquotes'
        )
        self.current_connection = self.connection.cursor()

    def create_table(self):
        self.current_connection.execute("""DROP TABLE IF EXISTS quotes_tbl""")
        self.current_connection.execute("""create table quotes_tbl(
                                            title text,
                                            author text,
                                            tags text
                                            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        # insert into quotes_tbl values(?, ?, ?)
        self.current_connection.execute("""insert into quotes_tbl values(%s, %s, %s)""",(
            item['title'],
            item['author'],
            item['tags'][0]
        ))
        self.connection.commit()