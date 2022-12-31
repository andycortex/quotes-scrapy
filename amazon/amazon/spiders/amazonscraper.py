import scrapy

class AmazonscraperSpider(scrapy.Spider):
    name = 'amazonscraper'
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
