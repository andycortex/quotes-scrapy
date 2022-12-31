
from requests_html import HTMLSession
import pandas as pd

urls = ['https://www.whiskyshop.com/glenfiddich-21-year-old-gran-reserva']

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    try:
        product = {
            'title': r.html.xpath("//h1[contains(text(),'Glenfiddich 21 Year Old')]",first=True).text,
            
        }
        print(product)
    except:
        product = {
            'title': r.html.xpath("//h1[contains(text(),'Glenfiddich 21 Year Old')]",first=True).text,
            
        }
        print(product)
    return product

tvprices = []
for url in urls:
    tvprices.append(getPrice(url))

print(len(tvprices))

pricesdf = pd.DataFrame(tvprices)
pricesdf.to_excel('tvprices.xlsx', index=False)