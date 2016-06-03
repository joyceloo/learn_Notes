#coding=utf-8
import urllib
import urllib2
import re
import thread
import time
import os
from bs4 import BeautifulSoup

"""
http://m.ctrip.com/restapi/soa2/10994/json/GetFloatUI?callback=Floating.BuildHTML&PlatformType=pc&pageParameter=%7BRefer%3Ayou.ctrip.com%2CUA%3AMozilla%252F5.0%2520(Macintosh%253B%2520Intel%2520Mac%2520OS%2520X%252010_10_4)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F49.0.2623.110%2520Safari%252F537.36%2CPageID%3A290570%2CVID%3A1460026191375.2eh0kr%7D&marketParameter=%7BAID%3A4899%2CSID%3A130678%7D&terminalParameter=%7BUserID%3A%2CCityID%3A%7D&pcAuthCodeParamet=%7BIsGetAuthCode%3Atrue%2CAppID%3A%22%22%2CLength%3A4%7D
"""
user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"
headers={'User-Agent':user_agent}
youji_file="XC_youji.txt"
wenda_file="XC_wenda.txt"

# 根据url解析网址。进一步分析
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


# 获取相关链接
# 一级深度（ 问答 游记等信息的页面链接 ）
def get_relative_urls(url):
	base="http://you.ctrip.com"
	htmls=get_html(url)
	if not htmls:
		print "一级深度执行失败：链接：%s" %(str(url)) 
		return None
	# 开始进行页面解析
	mudidi_find="District"
	jingdian_find="Sight"
	meishi_find="Restaurant"
	gouwu_find="Shopping"
	jiaotong_find="Traffic"
	wanle_find="Recreation"
	wenda_find="Asks"
	youji_find="Travels"
	user_find=""
	youji_url=""
	wenda_url=""
	soup=BeautifulSoup(htmls,'lxml')
	ul=soup.find('ul',class_="list-tabs")
	urls=ul.find_all("a")
	results=[]
	for i in range(len(urls)):
		m=urls[i]["href"]
		# if (youji_find in m):
		# 	youji_url=base+m
		# 	# print youji_url
		# 	results.append(youji_url)
		# elif(wenda_find in m):
		# 	wenda_url=base+m
		# 	# print wenda_url
		url=base+m
		results.append(url)
	return results
# end


# 二级深度
def get_two(url,key,pat,fname):
	htmls=get_html(url)
	base="http://you.ctrip.com"
	keyword="http://you.ctrip.com/"+key
	results=[]
	if not htmls:
		print "一级深度执行失败：链接：%s" %(str(url)) 
		return None
	soup=BeautifulSoup(htmls,'lxml')
	# 获取下一页链接
	next_link=get_nextlink(soup)
	uls=soup.find("ul",class_=pat)
	lis=uls.find_all("li")
	for li in range(len(lis)):
		details=lis[li].find("dl")
		results.append(str(details))
	f=open(fname,'a')
	for i in results:
		f.write(i)
		f.write("\n")
	f.close()
	return next_link

# 翻页
def get_nextlink(soup):
	# soup=BeautifulSoup(html,'lxml')
	base="http://you.ctrip.com"
	next_link=soup.find("a",text="下一页")["href"]
	if next_link:
		next_link=base+next_link
		return next_link
	else:
		return None

# 判断
def Mark(url):
	mark=0
	if("Travels" in url):
		mark=1
	elif ("Asks" in url):
		mark=2
	return mark

# 根据初始url选择执行方法
def select(mark):
	results=[]
	key=""
	pat=""
	f=""
	if(mark==1):
		key="travels"
		pat="youji-ul"
		f="XC_youji.txt"
		results.append(key+" "+pat+" "+f)
		return results
	elif(mark==2):
		key="asks"
		pat="wenda-ul"
		f="XC_wenda.txt"
		results.append(key+" "+pat+" "+f)
		return results
	else:
		return None




test_url="http://you.ctrip.com/searchsite/?query=%25e5%258c%2597%25e4%25ba%25ac"
urls=get_relative_urls(test_url)
# # yjf=open(youji_file,'w')
# next=get_youji(url,youji_file)
# while next:
# 	next=get_youji(url,youji_file)
for m in urls:
	mark=Mark(m)
	n=select(mark)
	if n:
		ns=n[0].split(" ")
		next_url=m
		print m
		while(next_url):
			url=next_url
			next_url=get_two(url,ns[0],ns[1],ns[2])










