# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class DoubanMoviePipeline(object):
    def __init__(self):
        self.f = open('movie_list.json','w+',encoding='utf-8')
        
    def process_item(self, item, spider):
        
        print(item.keys())
        
        line = json.dumps(dict(item)) + '\n'
        self.f.write(line)
        
        return item
