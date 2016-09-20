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
            item = self._parse_kind_1(mid, sel)
            if item != None:
                yield item
                continue

            item = self._parse_kind_2(mid, sel)
            if item != None:
                yield item
                continue

            item = self._parse_kind_3(mid, sel)
            if item != None:
                yield item
                continue

            print("*** 没有对应的规则 ***")

    def _builditem(self, mid, content, type, actual='', before='', exep=''):
        joins = ''.join(content)
        item = Jin10Item()
        item['mid'] = int(mid)
        item['content'] = joins.encode('utf-8')
        item['actual'] = actual.encode('utf-8')
        item['before'] = before.encode('utf-8')
        item['exep'] = exep.encode('utf-8')
        item['type'] = type
        return item

    def _getmid(self, sel):
        """
        :param sel:
        :return: string
        """
        mid = sel.xpath("./attribute::id").extract()
        return ''.join(mid)

    def _parse_kind_1(self, mid, sel):
        """
        :param sel:
        :return:
        """
        list = sel.xpath("./table/tr/td[@id]/text()").extract()
        if len(list) == 0:
            return None

        str = ''.join(list)
        return self._builditem(mid, str, 0)

    def _parse_kind_2(self, mid, sel):
        """
        :param sel:
        :return:
        """
        list = sel.xpath("./table/tr/td[@id]/b/text()").extract()
        if len(list) == 0:
            return None

        str = ''.join(list)
        return self._builditem(mid, str, 0)

    def _parse_kind_3(self, mid, sel):
        """
        :param sel:
        :return:
        """
        sel_title = sel.xpath("./table/tr/td[3]/table/tr/td[3]/text()").extract()
        if len(sel_title) == 0:
            return None
        str_title = ''.join(sel_title).strip()

        sel_actual = sel.xpath("./table/tr/td[3]/table/tr[1]/td[5]/text()").extract()
        if len(sel_actual) == 0:
            return None
        str_actual = ''.join(sel_actual).strip().strip(u"实际：")

        sel_before = sel.xpath("./table/tr/td[3]/table/tr[2]/td/text()").extract()
        if len(sel_before) == 0:
            return None
        str_before = ''.join(sel_before).strip().strip(u"前值：").replace(u"预期：", u"|")

        bs = str_before.split(u"|")
        str_before = bs[0].strip()
        str_except = bs[1].strip()

        return self._builditem(mid, str_title, 1, str_actual, str_before, str_except)
