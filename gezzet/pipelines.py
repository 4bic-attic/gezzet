# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json

class GezzetPipeline(object):
    def process_item(self, item, spider):
        return item

    def __init__(self):
        self.file = open('items.jl', 'wb') #use jsonlines for better scale purposes

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

    def process_value(value):
        m = re.search("index.php?id=8&amp;tx-filelist-pi1\('(.*?)'", value)
        if m:
            return m.group(1)

# class DuplicatesPipeline(object):
#
#     def __init__(self):
#         self.ids_seen = set()
#
#     def process_item(self, item, spider):
#         if item['desc'] in self.ids_seen:
#             raise DropItem("Duplicate item found: %s" % item)
#         else:
#             self.ids_seen.add(item['desc'])
#             return item
