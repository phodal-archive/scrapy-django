# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class GuokrJsonWithEncodingPipeline(object):
    def __init__(self):
        self.encode_file = codecs.open('spider/json/guokr_items_encode.json', 'wr', encoding='utf-8')
        self.encode_file.write("[")
        self.file = codecs.open('spider/json/guokr_items.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.encode_file.write(line.encode('utf-8').decode("unicode_escape"))
        self.encode_file.write(",")
        return item

    def spider_closed(self, spider):
        self.encode_file.write("]")
        self.file.close()
        self.encode_file.close()