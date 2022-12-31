import scrapy


class RugSpider(scrapy.Spider):
    name = 'rug'
    start_urls = ['https://www.therugshopuk.co.uk/rugs-by-type/rugs.html']

    def parse(self, response):
        items = response.css('div.product-item-info')
        for item in items:
            title = item.css('img.product-image-photo.image::attr(alt)').get()
            link = item.css('a.product-item-link::attr(href)').get() 
            price = item.css('span.price::text').get() 

            yield {
                'title': title,
                'link': link,
                'price': price,
            }
        next_page = response.css('a[title=Next]::attr(href)').get()
        if next_page is not None:
            print(next_page)
            yield response.follow(next_page, callback =  self.parse)