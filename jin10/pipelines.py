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
        actual = item['actual']
        before = item['before']
        exep = item['exep']
        # self.__db.create_or_update(mid, content)

        # print("mid:%s" % mid)
        print('%s %s, %s, %s' % (content, actual, before, exep))

        return item
