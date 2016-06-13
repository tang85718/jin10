# -*- coding: utf-8 -*-

import scrapy.spiders

class Jin10Spider(scrapy.Spider):
    name = "jin10"
    allowed_domains = ["www.jin10.com"]
    start_urls = ["http://www.jin10.com"]

    def __init__(self):
        print("init")

    def parse(self, response):
        pass
