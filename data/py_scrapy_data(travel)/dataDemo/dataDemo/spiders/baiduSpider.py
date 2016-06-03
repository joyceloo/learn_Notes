# coding="utf-8"
import scrapy
from scrapy.spiders import Spider 
from dataDemo.items import DatademoItem,DPItem
from scrapy.loader import ItemLoader
from scrapy.http import Request
from scrapy.loader.processors import Join,MapCompose,TakeFirst
import json
import re

class baidu_sp(Spider):
	name="bdSP"
	province="beijing"
	start_urls=["http://lvyou.baidu.com/destination/ajax/jingdian?format=ajax&cid=0&playid=0&seasonid=5&surl=%s&pn=1&rn=18" % province ,]

	def parse(self,response):
		base="http://lvyou.baidu.com/destination/ajax/jingdian?format=ajax&cid=0&playid=0&seasonid=5&surl=%s&pn=%s&rn=18"
		dp="http://lvyou.baidu.com/%s/remark/?rn=15&pn=0&style=hot#remark-container"
		js=json.loads(response.body)
		data=js['data']
		dp_province=data['surl']
		now_page=data['current_page']
		total=int(data['scene_total'])
		All=int(total/18)+1
		s_list=data['scene_list']
		if All >= now_page :
			for s in s_list:
				link=dp % str(s['surl'])
				yield Request(link,callback=self.parse_dp)
			now_page=now_page+1
			tup=tuple(str(dp_province),str(now_page),)
			url=base % tup
			yield Request(url,callback=self.parse)

	def parse_dp(self,response):
		pat1=r'{"pn":(.*?),'
		pat2=r'"total":"(.*?)"'
		p1=re.compile(pat1)
		p2=re.compile(pat2)
		dp_base="http://lvyou.baidu.com/%s/remark/?rn=15&pn=%s&style=hot#remark-container"
		sel=response.xpath("//div[@class='remark-item clearfix']")
		for s in sel:
			l=ItemLoader(item=DPItem())
			l.add_value('dp_u',s.xpath("div[@class='ri-avatar-wrap']/a[@class='ri-uname']/text()").extract(),MapCompose(unicode.strip))
			l.add_value('dp_scene',response.xpath("//a[@class='titleheadname']/p/text()").extract(),MapCompose(unicode.strip))
			l.add_value('dp_time',s.xpath("div[@class='ri-main']/div[@class='ri-header']/div[@class='ri-time']/text()").extract(),MapCompose(unicode.strip))
			l.add_value('dp_content',s.xpath("div[@class='ri-main']/div[@class='ri-body']/div[@class='ri-remarktxt']/text()").extract(),MapCompose(unicode.strip),Join())
			l.add_value('dp_huifu',s.xpath("div[@class='ri-main']/div[@class='ri-footer clearfix']/a[@class='ri-comment']/span/text()").extract(),MapCompose(unicode.strip))
			l.add_value('dp_link',response.url)
			l.add_value('dp_usenum',s.xpath("div[@class='ri-main']/div[@class='ri-footer clearfix']/a[@class='ri-dig ri-dig-available']/span/text()").extract(),MapCompose(unicode.strip))
			yield l.load_item()
		sname=response.xpath("//a[@class='titleheadname']/@href").extract()[0].replace("/","")
		pn_now=p1.findall(response.body)
		total=int(p2.findall(response.body))
		pn=int(pn_now)+15
		if pn<=total:
			tu=tuple(str(sname),str(pn),)
			url=dp_base % tu
			yield Request(url,callback=self.parse_dp)


