# -*- coding: utf-8 -*-

import scrapy.spiders
from jin10.items import Jin10Item


class Jin10Spider(scrapy.Spider):
    name = "jin10"
    allowed_domains = ["www.jin10.com"]
    start_urls = ["http://www.jin10.com"]

    def __init__(self, **kwargs):
        super(Jin10Spider, self).__init__(**kwargs)
        print("Jin10Spider __init__")

    def parse(self, response):
        for sel in response.xpath("//div[@class='newsline']"):
            item = Jin10Item()
            mid = sel.xpath("./attribute::id").extract()
            list = sel.xpath("./table/tr/td[@id]/text()").extract()

            if len(list) > 0:
                content = ''.join(list)
                item['content'] = content.encode('utf-8')
                item['mid'] = int(''.join(mid))
                item['type'] = 0
                yield item
