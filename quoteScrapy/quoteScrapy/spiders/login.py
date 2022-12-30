import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotescrapyItem

class LoginSpider(scrapy.Spider):
    name = 'login'
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'cortex.andy@gmail.com',
            'password': '123456'
        }, callback=self.start_scrapping)

    def start_scrapping(self, response):
        open_in_browser(response)
        items = QuotescrapyItem()

        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            title = quote.css('span.text::text').get()
            author = quote.css('.author::text').get()
            tags = quote.css('.tag::text').getall()

            items['title'] = title
            items['author']= author
            items['tags'] = tags
            yield items