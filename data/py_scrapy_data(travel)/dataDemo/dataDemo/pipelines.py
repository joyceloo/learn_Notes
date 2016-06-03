# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
class DatademoPipeline(object):
	# def __init__(self):
	# 	self.file=open('dp.txt','w')
	# def process_item(self, item, spider):
	# 	self.file.write("uid:"+item['uid'].encode('utf-8'))
	# 	self.file.write("nickname"+item['nickname'].encode('utf-8'))
	# 	self.file.write("content:"+item['content'].encode('utf-8'))
	# 	self.file.write("comment_count:"+item['co_count'].encode('utf-8'))
	# 	self.file.write("recomment_count:"+item['re_count'].encode('utf-8'))
	# 	self.file.write('\n')
	# 	self.file.write('\n')
	# 	return item
	def process_item(self, item, spider):
		# if not os.path.exists("shandong"):
		# 	os.mkdir("shandong")
		# s_file=open("shandong"+"/"+item['s_name']+".txt",'a')
		# s_file.write("uid:"+item['uid'].encode('utf-8'))
		# s_file.write("nickname"+item['nickname'].encode('utf-8'))
		# s_file.write("content:"+item['content'].encode('utf-8'))
		# s_file.write("comment_count:"+item['co_count'].encode('utf-8'))
		# s_file.write("recomment_count:"+item['re_count'].encode('utf-8'))
		# s_file.write('\n')
		# s_file.write('\n')
		return item
