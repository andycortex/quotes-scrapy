import scrapy
from ..items import QuotescrapyItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        # title = response.css('title::text').get()  #extract() coloca el title en array
        # link = response.css('li.next a').xpath('@href').get()
        # yield {
        #     'title': title,
        #     'link': link,
        # }
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
        next_page = 'http://quotes.toscrape.com/page/'+ str(QuotesSpider.page_number) +'/' #response.css('li.next a::attr(href)').get()
        if QuotesSpider.page_number < 11:
            QuotesSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
