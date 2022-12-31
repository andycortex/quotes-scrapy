import scrapy


class PlantsSpider(scrapy.Spider):
    name = 'plants'
    allowed_domains = ['www.fake-plants.co.uk']
    start_urls = ['http://www.fake-plants.co.uk/']

    def parse(self, response):
        links = response.css('li.product-category a::attr(href)')
        for link in links:
           yield response.follow(link.get(), callback=self.parse_categories)
    
    def parse_categories(self, response):
        products = response.css('div.astra-shop-summary-wrap')
        for product in products:
            yield {
                'name': product.css('span.ast-woo-product-category::text').get().strip(),
                'category': product.css('h2.woocommerce-loop-product__title::text').get().strip(),
            }
