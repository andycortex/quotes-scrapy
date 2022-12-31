import scrapy
from ..items import MagnatilesItem
from scrapy.loader import ItemLoader

class MagnatilSpider(scrapy.Spider):
    name = 'magnatil'
    allowed_domains = ['www.magnatiles.com']
    start_urls = ['https://www.magnatiles.com/products/']

    def parse(self, response):
        products = response.css('ul.products li')

        for product in products:
            il = ItemLoader(item=MagnatilesItem(), selector=product)
            il.add_css('sku', 'a.button::attr(data-product_sku)')
            il.add_css('name', 'h2')
            il.add_css('price','span.price bdi')

            yield il.load_item()

        # next_page = response.css('ul.page-numbers a.next::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
