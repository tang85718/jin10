# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Jin10Item(scrapy.Item):
    # define the fields for your item here like:
    mid = scrapy.Field()
    content = scrapy.Field()
    actual = scrapy.Field()
    before = scrapy.Field()
    exep = scrapy.Field()
    type = scrapy.Field()
