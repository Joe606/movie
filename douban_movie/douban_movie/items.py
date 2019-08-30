# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    pic = scrapy.Field()
    link = scrapy.Field()
    _name = scrapy.Field()
    _year = scrapy.Field()
    _pic = scrapy.Field()
    _director = scrapy.Field()
    _writer = scrapy.Field()
    _cast = scrapy.Field()
    _type = scrapy.Field()
    _country = scrapy.Field()
    _language = scrapy.Field()
    _premiere = scrapy.Field()
    _episode = scrapy.Field()
    _runningtime = scrapy.Field()
    _plot = scrapy.Field()
    
    pass
