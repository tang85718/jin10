# -*- coding: utf-8 -*-

import scrapy.spiders
from jin10.items import Jin10Item

class Jin10Spider(scrapy.Spider):
    name = "jin10"
    allowed_domains = ["www.jin10.com"]
    start_urls = ["http://www.jin10.com"]

    def __init__(self):
        print("Jin10Spider __init__")

    def parse(self, response):
        for sel in response.xpath("//div[@class='newsline']"):
            # item = Jin10Item()
            # print sel
            id = sel.xpath("./attribute::id").extract()
            print id

            content = sel.xpath("./table/tr/td[@id]/text()").extract()
            print type(content)

            if len(content) > 0:
                str = content[0]
                utf8str = str.encode('utf-8')
                print utf8str
            # utf8str = content.encode('utf-8')
            # print utf8str
            # print("%s" % type(content), content)

