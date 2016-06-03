# coding="utf-8"
import scrapy
from scrapy.spiders import Spider 
from scrapy.http import Request
from dataDemo.items import DatademoItem
import json


class Baidu(Spider):
	name='baiduSP'
	# start_urls=[]
	start_urls=['http://lvyou.baidu.com/destination/ajax/jingdian?format=ajax&cid=0&playid=0&seasonid=5&surl=shandong&pn=1&rn=18']



	def parse(self,response):
		base_url="http://lvyou.baidu.com/destination/ajax/jingdian?format=ajax&cid=0&playid=0&seasonid=5&surl=shandong&pn=%s&rn=18"
		two_url="http://lvyou.baidu.com/user/ajax/remark/getsceneremarklist?xid=%s&score=0&pn=0&rn=15&style=hot&format=ajax&flag=1"
		url_list=[]
		js=json.loads(response.body)
		data=js['data']
		s_name=data['sname']
		now_page=data['current_page']
		total=int(data['scene_total'])
		All=int(total/18)+1
		s_list=data['scene_list']
		if(All>=now_page):
			for s in s_list:
				# item=DatademoItem()
				# item['sid']=s['sid']
				# item['surl']=s['surl']
				# item['sname']=s['sname']
				url_list.append(two_url % s['sid'])
				# yield item
			now_page=now_page+1
			url=base_url % str(now_page)
			yield Request(url,callback=self.parse)
		for url in url_list:
			yield Request(url,callback=self.next_parse)

	def next_parse(self,response):
		two_url="http://lvyou.baidu.com/user/ajax/remark/getsceneremarklist?xid=%s&score=0&pn=%s&rn=15&style=hot&format=ajax&flag=1"
		js=json.loads(response.body)
		data=js['data']
		name=data['name']
		cu_page=data['pn']
		rn=int(data['rn'])
		mark=int(cu_page)
		total=int(data['total'])
		dp_list=data['list']
		s_id=dp_list[0]['sid']
		if(total>=mark):
			for dp in dp_list:
				item=DatademoItem()
				# item['mkdir_name']=dp['parent_sid']		
				item['s_name']=dp['sname']
				item['uid']=dp['user']['uid']
				item['nickname']=dp['user']['nickname']
				item['co_count']=str(dp['comment_count'])
				item['re_count']=str(dp['recommend_count'])
				item['content']=dp['content']
				yield item
			mark=mark+rn
			tupl=(str(s_id),str(mark),)
			n_url=two_url % tupl
			yield Request(n_url,callback=self.next_parse)





		






		