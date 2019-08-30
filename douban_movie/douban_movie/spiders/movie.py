# -*- coding: utf-8 -*-
import scrapy
from douban_movie.items import DoubanMovieItem
import time

class Toscrapemovie(scrapy.Spider):
    name = 'scrape_movie'
    
    def start_requests(self):
        urls = ['https://movie.douban.com/tag/#/',]
        for url in urls:     
            yield scrapy.Request(url=url,callback=self.parse,meta={'depth':0}) #用meta标记
    
    def parse(self,response):
        print(response.text)
        item = DoubanMovieItem()
        selector = response.xpath('//div[@class="list-wp"]/a')
        
        item['name'] = selector.xpath('p/span[@class="title"]/text()').getall()
        item['score'] = selector.xpath('p/span[@class="rate"]/text()').getall()
        item['pic'] = selector.xpath('div/span/img/@src').getall()
        item['link'] = selector.xpath('@href').getall()
        
        yield item
        
        print(type(item['link']),len(item['link']))
        for link in item['link']:
            yield response.follow(link,callback=self.next_parse,meta={'depth':1})
        '''
        for url_next in selector.xpath('@href'):
            yield response.follow(url_next,callback=self.next_parse)
        print('next page')
        '''
        
        
    def next_parse(self,response):
        item2 = DoubanMovieItem()
        print(item2)
        item2['_name'] = response.xpath('//div[@id="content"]/h1/span[@property="v:itemreviewed"]/text()').getall()    
        item2['_year'] = response.xpath('//div[@id="content"]/h1/span[@class="year"]/text()').getall()    
        item2['_pic'] = response.xpath('//div[@id="mainpic"]/a/img/@src').getall()    
        print(item2)
        
        selector_next = response.xpath('//div[@id="info"]')
        item2['_director'] = selector_next.xpath('//span[@class="attrs"]/a/text()').getall()[:2]
        item2['_writer'] = selector_next.xpath('//span[@class="attrs"]/a/text()').getall()[2:]
        item2['_cast'] = selector_next.xpath('//span[@class="actor"]/span[@class="attrs"]/span/a/text()').getall()
        item2['_type'] = selector_next.xpath('span[@property="v:genre"]/text()').getall()
        item2['_country'] = selector_next.xpath('text()').getall()[7]
        item2['_language'] = selector_next.xpath('text()').getall()[9]
        item2['_premiere'] = selector_next.xpath('span[@property="v:initialReleaseDate"]/text()').getall()
        item2['_episode'] = selector_next.xpath('text()').getall()[13]
        item2['_runningtime'] = selector_next.xpath('text()').getall()[15]
        
        item2['_plot'] = response.xpath('//span[@property="v:summary"]/text()').getall()
        
        return item2
