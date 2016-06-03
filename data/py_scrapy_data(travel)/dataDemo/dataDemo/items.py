# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DatademoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    s_name=scrapy.Field()
    mkdir_name=scrapy.Field()
    sid=scrapy.Field()
    surl=scrapy.Field()
    sname=scrapy.Field()
    uid=scrapy.Field()
    nickname=scrapy.Field()
    co_count=scrapy.Field()
    re_count=scrapy.Field()
    content=scrapy.Field()

    pass

class JDItem(scrapy.Item):
    JD_sid=scrapy.Field()
    JD_surl=scrapy.Field()
    JD_sname=scrapy.Field()
    pass
class DPItem(scrapy.Item):
    dp_u=scrapy.Field()
    dp_content=scrapy.Field()
    dp_time=scrapy.Field()
    dp_usenum=scrapy.Field()
    dp_huifu=scrapy.Field()
    dp_scene=scrapy.Field()
    dp_link=scrapy.Field()

