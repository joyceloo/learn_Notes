# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import math
import cookielib
import urllib2
import urllib

def get_json(page):
	base_url='http://lvyou.baidu.com/destination/ajax/jingdian?format=ajax&cid=0&playid=0&seasonid=5&surl=beijing&pn=%s&rn=18'
	url=base_url % page
	result=requests.get(url).json()
	return result


def get_sid(page):
	json=get_json(page)
	data=json['data']
	# 所爬景点名字
	sname=data['sname']
	fname=sname+'_sid.txt'
	f=open(fname,'a')
	cur_page=data['current_page']
	total=data['scene_total']
	T_page=int(int(total)/18)+1
	s_list=data['scene_list']
	if(cur_page<=T_page):
		for s in s_list:
			s_name=s['sname']
			s_id=s['sid']
			s_url=s['surl']
			f.write("sname:"+s_name+"\t"+"sid:"+s_id+"\t"+"surl:"+s_url+"\n")
		f.close()
		cur_page=cur_page+1
		get_sid(cur_page)


filename="cookie.txt"
cookie=cookielib.MozillaCookieJar(filename)
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata=urllib.urlencode({'TPL_username_1':'溪硫smile','TPL_password_1':'lu.0609'})
url="http://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView?poiID=75595&districtId=1&districtEName=Beijing&pagenow=2&order=3.0&star=0.0&tourist=0.0&resourceId=229&resourcetype=2"
result=opener.open(url,postdata)
print result.headers



# headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
# s=requests.session()
# data={'TPL_username_1':'溪硫smile','TPL_password_1':'lu.0609'}
# r=requests.post('https://login.taobao.com/member/login.jhtml',data=data,headers=headers)
# print r.text
# url="http://weixin.sogou.com/weixin?query=%E5%8C%97%E4%BA%AC&_sug_type_=&_sug_=n&type=1&page=11&ie=utf8"
# response=requests.get(url)
# # print response.cookies

# def test(n):
# 	base_url="http://weixin.sogou.com/weixin?query=%E5%8C%97%E4%BA%AC&_sug_type_=&_sug_=n&type=1&page=%s&ie=utf8"
# 	for i in range(1,int(n)+1):
# 		url=base_url % str(i)
# 	return None














