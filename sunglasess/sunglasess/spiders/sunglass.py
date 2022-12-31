import json
import scrapy


class SunglassSpider(scrapy.Spider):
    name = 'sunglass'
    allowed_domains = ['https://www.sunglasshut.com/']
    start_urls = ['https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651836?isProductNeeded=true&isChanelCategory=false&pageSize=18&orderBy=default&responseFormat=json&currency=USD&orderBy=default&viewTaskName=CategoryDisplayView&storeId=10152&DM_PersistentCookieCreated=true&pageView=image&catalogId=20602&top=Y&beginIndex=0&langId=-1&currentPage=1&categoryId=3074457345626651836&orderBy=default&currentPage=1']

    def parse(self, response):
        data = json.loads(response.body)
        yield from data['plpView']['products']['products']['product']

        next_page = data['plpView']['nextPageURL']
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
