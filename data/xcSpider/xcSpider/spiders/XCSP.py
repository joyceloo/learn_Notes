# coding='utf-8'
import scrapy
from scrapy.spiders import Spider 
from xcSpider.items import XcspiderItem
from scrapy.spiders import CrawlSpider,Rule
from bs4 import BeautifulSoup

class SpiderDeep(CrawlSpider):
	name="DeepSP"
	
	def __init__(self,rule):
		self.rule=rule
		self.name=rule.name
		self.allowed_domains=rule.allowed_domains.split(',')
		self.start_urls=rule.start_urls.split(',')
		rule_list=[]
		

