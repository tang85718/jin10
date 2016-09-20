# -*- coding: utf-8 -*-

import scrapy.spiders
from jin10.items import Jin10Item


class Jin10Spider(scrapy.Spider):
    name = "jin10"
    allowed_domains = ["www.jin10.com"]
    start_urls = ["http://www.jin10.com"]

    def parse(self, response):
        for sel in response.xpath("//div[@class='newsline']"):
            mid = self._getmid(sel)
            item = self._getcontent1(mid, sel)
            if item != None:
                yield item
                continue

            item = self._getcontent2(mid, sel)
            if item != None:
                yield item
                continue

            print("*** 没有对应的规则 ***")

    def _builditem(self, mid, content, type):
        joins = ''.join(content)
        item = Jin10Item()
        item['content'] = joins.encode('utf-8')
        item['mid'] = int(mid)
        item['type'] = type
        return item

    def _getmid(self, sel):
        """
        :param sel:
        :return: string
        """
        mid = sel.xpath("./attribute::id").extract()
        return ''.join(mid)

    def _getcontent1(self, mid, sel):
        """
        :param sel:
        :return:
        """
        list = sel.xpath("./table/tr/td[@id]/text()").extract()
        if len(list) == 0:
            return None

        str = ''.join(list)
        return self._builditem(mid, str, 0)

    def _getcontent2(self, mid, sel):
        """
        :param sel:
        :return:
        """
        list = sel.xpath("./table/tr/td[@id]/b/text()").extract()
        if len(list) == 0:
            return None

        str = ''.join(list)
        return self._builditem(mid, str, 0)
