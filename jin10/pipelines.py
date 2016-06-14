# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import database

class Jin10Pipeline(object):

    def __init__(self):
        print("Jin10Pipeline __init__")
        # self.__db = database('localhost', 'root', '12345', 'spider', 3306)

    def process_item(self, item, spider):

        print type(item)

        # content = item['content']
        # date = item['date']
        # print("%s" % content)
        return item
