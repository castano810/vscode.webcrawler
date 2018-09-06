from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
import scrapy

class MyItem():
    url = Field()

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://www.twitter.com',
    ]

    rules = (Rule(SgmlLinkExtractor(), callback='parse_url', follow=False), )

    def parse_url(self,response):
        item = MyItem()
        item['url'] = response.url
        return item