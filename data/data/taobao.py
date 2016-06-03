#coding=utf-8
import urllib
import urllib2
import re
import thread
import time,Queue,datetime
import os
import json
from bs4 import BeautifulSoup

urlset=set()
urlqueue=Queue.Queue()
user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"
headers={'User-Agent':user_agent}
fname='notes_nids.txt'
def zh_url(m):
	url=""
	url='http://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn={}&rn=10'.format(str(m))
	return url


#url='http://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn=187&rn=10&t=1460340000000'
#base='http://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn={}&rn=10&t=146034{}'.format(str(i),str(ss))
#print url
# 根据url解析网址,进一步分析
def get_html(url):
	try:
		request=urllib2.Request(url,headers=headers)
		response=urllib2.urlopen(request)
		pageCode=response.read()
		return pageCode
	except urllib2.URLError,e:
		if hasattr(e,"reason"):
			print e.reason
			return None


# 查找nid
def seek_nid(url):
	global urlset
	html=get_html(url)
	global fname
	baidu=r''
	if not html:
		print "seek_links 执行失败：错误链接：%s" %(str(url)) 
		return None
	s1=r'"nid":"(.*?)"'
	pat_ids=re.compile(s1)
	ids=[]
	ids=re.findall(pat_ids,html)
	if ids:
		f=open(fname,'a')
		for nid in ids:
			if(nid  not in urlset):
				urlset.add(nid)
				f.write(nid)
				f.write("\n")
		f.close()
		return ids
	else:
		return None

def get_sets():	
	i=0
	while (i<=100):
		url=zh_url(i)
		seek_nid(url)
		i=i+1


get_sets()




















