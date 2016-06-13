# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Jin10Pipeline(object):

    def __init__(self):
        print("Jin10Pipeline __init__")

    def process_item(self, item, spider):
        return item
