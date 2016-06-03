# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from dataDemo.items import DatademoItem,JDItem,DPItem
import json 
import re


class BaiduspiderSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["lvyou.baidu.com"]
    province="beijing"
    # start_urls=["http://lvyou.baidu.com/destination/ajax/jingdian?format=ajax&cid=0&playid=0&seasonid=5&surl=%s&pn=1&rn=18" % province ,]
    start_urls=["http://lvyou.baidu.com/gugong/remark/?rn=15&pn=15&style=hot#remark-container"]
    def parse(self, response):
    	m=response.xpath("//a[@class='titleheadname']/@href").extract()[0].replace("/","")
    	print m
    	
			



















