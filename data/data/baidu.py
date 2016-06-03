#coding=utf-8
import urllib
import urllib2
import cookielib
import requests
import re
import thread
import time,Queue,datetime
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
from bs4 import BeautifulSoup

urlset=set()
urlqueue=Queue.Queue()
user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"
headers={'User-Agent':user_agent}
cookie=cookielib.CookieJar()

def zh_url(m):
	url=""
	url='http://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn={}&rn=10'.format(str(m))
	return url

url='http://lvyou.baidu.com/search/ajax/search?format=ajax&word=%E6%95%85%E5%AE%AB&pn=740&surl=gugong&rn=10&t=1460951982167'
# url='http://lvyou.baidu.com/destination/ajax/jingdian?format=ajax&cid=0&playid=0&seasonid=5&surl=beijing&pn=2&rn=18'
#base='http://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn={}&rn=10&t=146034{}'.format(str(i),str(ss))
#print url
# 根据url解析网址,进一步分析
def get_html(url):
	try:
		response=requests.get(url)
		pageCode=response.json()
		return pageCode
	except Exception,e:
		return e.reason


def get_html1(url):
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


def get_link_url(sid,sname,surl,pn):
	base_yj='http://lvyou.baidu.com/search/ajax/search?format=ajax&word=%s&pn=%s&surl=%s&rn=10'
	base_dp='http://lvyou.baidu.com/user/ajax/remark/getsceneremarklist?xid=%s&score=0&pn=%s&rn=15&style=hot&format=ajax&flag=1'
	tuple_yj=(str(sname),str(pn),str(surl))
	tuple_dp=(str(sid),str(pn))
	yj_jurl=base_yj % tuple_yj
	dp_jurl=base_dp % tuple_dp


# 点评解析
def parse_dp(url):
	html=get_html(url)
	if not html:
		return None
	j_html=html['data']
	current_pn=j_html['pn']
	rn=j_html['rn']
	total=j_html['total']
	name=j_html['name']
	print total
	total_page=(int(total)/int(rn))+1
	if (current_pn <= total_page):
		fname=name+'_dp.txt'
		f=open(fname,'a')
		dp_list=j_html['list']
		for i in dp_list:
			#评论详情
			user=i['user']['uid'] #用来判断是否已写入
			contents=[]
			contents=i['content']
			f.write(contents)
			f.write('\n')
		f.close()


def parse_yj(url):
	html=get_html(url)
	if not html:
		return None
	j_html=html['data']['search_res']
	rn=10
	total=j_html['page']['total']
	current_pn=j_html['page']['pn']
	hilight_word=j_html['hilight_word']
	name=hilight_word[0]
	total_page=int(total)
	if (current_pn <= total_page):
		fname=name+'_yj.txt'
		f=open(fname,'a')
		dp_list=j_html['notes_list']
		for i in dp_list:
			# 游记
			title=i['title']
			link=i['loc']
			content=i['content']
			author=i['nickname']
			f.write(title+'\n')
			f.write(content)
			f.write('\n\n')
		f.close()
u_url='http://lvyou.com.baidu/user/bc984940cbfbc0a968001ab1'
def parse_user(u_url):
	html=get_html2(u_url)
	print html

response=requests.get(url)
m=response.cookies
print m
response=requests.post(u_url,m)


























