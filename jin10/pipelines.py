# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from database import Database


class Jin10Pipeline(object):
    def __init__(self):
        # self.__db = Database('spider')
        print("Jin10Pipeline __init__")

    def process_item(self, item, spider):
        mid = item['mid']
        content = item['content']
        # self.__db.create_or_update(mid, content)

        # print("mid:%s" % mid)
        print('content:%s' % content)

        return item
