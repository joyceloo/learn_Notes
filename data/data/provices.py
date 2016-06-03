# #coding=utf-8
# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )
# import urllib
# import urllib2
# import re
# import thread
# import time
# import os
# from bs4 import BeautifulSoup

# #os.mkdir("guangdong")
# #全国
# '''https://shopsearch.taobao.com/search?app=shopsearch&q=%E5%86%9C&js=1&initiative_id=staobaoz_20160322&ie=utf8&loc=&sort=sale-desc'''
# #beijing
# '''https://shopsearch.taobao.com/search?app=shopsearch&q=%E5%86%9C&imgfile=&commend=all&ssid=s5-e&search_type=shop&sourceId=tb.index&spm=a21bo.7724922.8452-taobao-item.1&ie=utf8&initiative_id=tbindexz_20160322&sort=sale-desc&loc=%E5%8C%97%E4%BA%AC&s=20'''
# provices=["安徽","福建","甘肃","广东","广西","贵州","海南","河北","河南","湖北","湖南","江苏","江西","吉林","辽宁","宁夏","青海","山东","山西","陕西","云南","四川","西藏","新疆","浙江","澳门","香港","台湾","内蒙古","黑龙江","北京","上海","天津","重庆"]
# print len(provices)

# # http://you.ctrip.com/searchsite/?query=%25e5%258c%2597%25e4%25ba%25ac

# class YXL:
#   #初始化方法，定义一些变量
#   def __init__(self):
#     self.pageIndex=1
#     self.user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"
#     self.headers={'User-Agent':self.user_agent}
#     self.stories=[]
#     self.enable=False

#   def getPage1(self,url):
#     try:
#       request=urllib2.Request(url,headers=self.headers)
#       response=urllib2.urlopen(request)
#       pageCode=response.read()
#       return pageCode
#     except urllib2.URLError,e:
#       if hasattr(e,"reason"):
#         print e.reason
#         return None

#   #传入某省编号，获取代码
#   def getPage(self,procode):
#     try:
#       #area=urllib.quote(pageIndex)
#       url="http://you.ctrip.com/searchsite/?query="+str(procode)
#       print url
#       request=urllib2.Request(url,headers=self.headers)
#       response=urllib2.urlopen(request)
#       pageCode=response.read()
#       return pageCode
#     except urllib2.URLError,e:
#       if hasattr(e,"reason"):
#         print u"链接失败，错误原因：",e.reason
#         return None
# # 获取省级数据的相关的url
#   def get_urls(self,procode):
#     pageCode=self.getPage(procode)
#     base="http://you.ctrip.com"
#     mudidi_find="District"
#     jingdian_find="Sight"
#     meishi_find="Restaurant"
#     gouwu_find="Shopping"
#     jiaotong_find="Traffic"
#     wanle_find="Recreation"
#     wenda_find="Asks"
#     youji_find="Travels"
#     user_find=""
#     youji_url=""
#     wenda_url=""
#     results=[]
#     if not pageCode:
#       print "页面加载失败...."
#       return None
#     soup=BeautifulSoup(pageCode,'lxml')
#     ul=soup.find("ul",class_="list-tabs")
#     urls=ul.find_all("a")
#     for i in range(len(urls)):
#       m=urls[i]["href"]
#       if (youji_find in m):
#         youji_url=base+m
#         results.append(youji_url)
#       elif(wenda_find in m):
#         wenda_url=base+m
#         results.append(wenda_url)
#     return results

# # 根据url进行抓取
#   def get_datas(self,procode):
#     urls=[]
#     urls=self.get_urls(procode)
#     if not urls:
#       return None
#     # 获取游记

#     # 获取问答

#   def get_wenda(self,url):
#     pageCode=self.getPage1(url)
#     print url
#     if not pageCode:
#       return None
#     # 进行抓取
#     soup=BeautifulSoup(pageCode,'lxml')
#     wenda_ul=soup.find("ul",class_="wenda-ul")
#     wenda_lis=wenda_ul.find_all("li")
#     for i in wenda_lis:
#       title=i.find("dt").find("a").get_text().strip()
#       content=i.find("dd").get_text().strip()
#       details=str(i.find("dd",class_="color-999").get_text().strip())
#       print details


#     return None


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
    if (youji_find in m):
      youji_url=base+m
      # print youji_url
      results.append(youji_url)
    elif(wenda_find in m):
      wenda_url=base+m
      # print wenda_url
      results.append(wenda_url)
  return results

# 二级深度
def get_two(url,fname,key,ul):
  htmls=get_html(url)
  base="http://you.ctrip.com"
  key="travels"
  ul="youji-ul"
  keyword="http://you.ctrip.com/"+key
  results=[]
  if not htmls:
    print "一级深度执行失败：链接：%s" %(str(url)) 
    return None
  
  soup=BeautifulSoup(htmls,'lxml')
  # 获取下一页链接
  next_link=get_nextlink(soup)
  # print next_link
  youji_ul=soup.find("ul",class_=ul)
  youji_lis=youji_ul.find_all("li",class_="cf")
  for i in range(len(youji_lis)):
    youji_de=youji_lis[i].find("dl")
    results.append(str(youji_de))
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

test_url="http://you.ctrip.com/searchsite/?query=%25e5%258c%2597%25e4%25ba%25ac"
url=get_relative_urls(test_url)[1]

next=get_youji()

























