#coding=utf-8
import time,os,cookielib,urllib2,urllib  
import datetime,StringIO,gzip  
  
def getHtml(url,referurl=None,cookie=None,postdata=None,ip=None):  
    cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())#伪装cookies  
    if ip:  
        proxy_support = urllib2.ProxyHandler({'http':ip})#代理  
        opener = urllib2.build_opener(proxy_support, cookie_support, urllib2.HTTPHandler)  
        urllib2.install_opener(opener)  
    else:  
        opener = urllib2.build_opener( cookie_support, urllib2.HTTPHandler)  
        urllib2.install_opener(opener)  
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}#伪装浏览器  
    req = urllib2.Request(url,headers = headers)  
    if referurl:  
        req.add_header('referer',referurl)  
    if cookie:  
        req.add_header('Cookie', cookie)  
    if postdata:  
        try:  
            req.add_data(urllib.urlencode(postdata))  
        except:  
            req.add_data(postdata)  
    content=urllib2.urlopen(req,timeout=120).read()  
    try:  
        gzp_content = StringIO.StringIO(content)  
        gzipper = gzip.GzipFile(fileobj =gzp_content)  
        content =gzipper.read()  
    except:  
        1  
    return content


# 
import pycurl,StringIO

def getHtml1(url):
    c=pycurl.Curl()
    c.setopt(c.URL, url)
    b = StringIO.StringIO()
    c.setopt(c.WRITEFUNCTION, b.write)
    c.setopt(c.COOKIEFILE, '')
    c.setopt(pycurl.USERAGENT, "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)")
    c.setopt(c.HTTPHEADER, ['Accept: text/html', 'Accept-Charset: UTF-8'])
    c.setopt(c.SSL_VERIFYPEER, 0)
    c.setopt(c.SSL_VERIFYHOST, 0)
    c.setopt(c.FOLLOWLOCATION, 1)
    c.setopt(c.HEADER,False)
    c.perform()
    html=b.getvalue()
    b.close()
    c.close()
    return html








