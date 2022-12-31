import scrapy
from bs4 import BeautifulSoup

class WeblogSpider(scrapy.Spider):
    name = 'weblog'
    allowed_domains = ['scoutapm.com']
    start_urls = ['https://scoutapm.com/blog/categories/engineering']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        content = soup.find_all('div', {'class': 'post-partial'})
        
        for post in content:
            yield {
                'title': post.find('h4').text,
                'link': post.find('a')['href']
            }
        next_page = soup.find('a', {'title': 'Next page'}, href=True)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)