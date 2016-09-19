# -*- coding: utf-8 -*-

from jin10.spiders.Jin10Spider import Jin10Spider
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

setting = get_project_settings()
process = CrawlerProcess(setting)
process.crawl(Jin10Spider)
process.start() # the script will block here until the crawling is finished

# from scrapy.cmdline import execute
#
# execute(['scrapy', 'crawl', 'jin10'])