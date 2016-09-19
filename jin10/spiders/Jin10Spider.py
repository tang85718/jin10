# -*- coding: utf-8 -*-

import scrapy.spiders
from jin10.items import Jin10Item


class Jin10Spider(scrapy.Spider):
    name = "jin10"
    allowed_domains = ["www.jin10.com"]
    start_urls = ["http://www.jin10.com"]

    def _buildItem(self, mid, content, type):
        joins = ''.join(content)
        item = Jin10Item()
        item['content'] = joins.encode('utf-8')
        item['mid'] = int(''.join(mid))
        item['type'] = type
        return item

    def parse(self, response):
        for sel in response.xpath("//div[@class='newsline']"):
            mid = sel.xpath("./attribute::id").extract()
            content = sel.xpath("./table/tr/td[@id]/text()").extract()
            length = len(content)

            if length > 0:
                print("执行了一级")
                item = self._buildItem(mid, content, 0)
                yield item

            content = sel.xpath("./table/tr/td[@id]/b/text()").extract()
            length = len(content)
            if length > 0:
                print("执行了二级")
                item = self._buildItem(mid, content, 0)
                yield item
