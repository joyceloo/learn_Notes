# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from mafengwo.items import MafengwoItem


class ScrapyMefengwoSpider(Spider):
    name = "scrapy_mefengwo"
    allowed_domains = ["mafengwo.cn"]
    start_urls = (
        'http://www.mafengwo.cn/',
    )

    def parse(self, response):
    	sel=response.xpath("//a[@href]").extract()
    	for i in sel:
    		item=MafengwoItem()
    		item['link']=i 
    		yield item
 
