# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3


class MagnatilesPipeline:
    def __init__(self):
        self.connection = sqlite3.connect('mtiles.db')
        self.current_connection = self.connection.cursor()
        self.create_table()
    
    def create_table(self):
        self.current_connection.execute('''CREATE TABLE IF NOT EXISTS products(
            sku REAL PRIMARY KEY,
            name TEXT,
            price REAL
        )''')

    def process_item(self, item, spider):
        self.current_connection.execute('''INSERT OR IGNORE INTO products VALUES(?, ?, ?)''',(
            item['sku'],
            item['name'],
            item['price']
        ))
        self.connection.commit()
        return item
