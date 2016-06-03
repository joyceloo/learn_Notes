#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from scrapy.spiders import Spider
from scrapy.http import Request
from weixin.items import WeixinItem
from bs4 import BeautifulSoup

class wxSP(Spider):
	name="weixin_sp"
	start_urls=["http://weixin.sogou.com/weixin?type=1&query=北京&page=1"]
	
	# # http_headers = {"X-Requested-With":"XMLHttpRequest"}
	# for i in range(6,7):
	# 	start_urls.append("http://weixin.sogou.com/weixin?type=%d&query=%s&page=%d" % (tp, q, i))

	def parse(self,response):
		base="http://weixin.sogou.com/weixin?type=1"
		sites=response.xpath("//div[@class='results mt7']/div/div[@class='txt-box']")
		for site in sites:
			item=WeixinItem()
			item['title']=site.xpath("h3/text()").extract()[0]
			item['name']=site.xpath("h4/span/text()").extract()[0]
			item['authority']=site.xpath("p[2]/span[@class='sp-txt']").extract()[0]
			item['detail']=site.xpath("p[1]/span[@class='sp-txt']").extract()[0]
			yield item
		next=response.xpath("//a[@id='sogou_next']/@href")
		if next:
			next_url=base+next.extract()[0]
			yield Request(next_url,callback=self.parse)






