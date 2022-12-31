
from requests_html import HTMLSession
import pandas as pd

urls = ['https://www.amazon.co.uk/Samsung-GU43BU8079U-109-2-Ultra-Smart/dp/B09VTGR1PM/ref=sr_1_4?content-id=amzn1.sym.d191d14d-5ea3-4792-ae6c-e1de8a1c8780&pd_rd_r=e682cd9f-2485-4cc8-85ea-f759f6e13f29&pd_rd_w=b7dJB&pd_rd_wg=BYbT0&pf_rd_p=d191d14d-5ea3-4792-ae6c-e1de8a1c8780&pf_rd_r=WJ22YB43QNMMRXXVM86Z&qid=1672417492&refinements=p_n_size_browse-bin%3A9591878031&s=electronics&sr=1-4',
          'https://www.amazon.co.uk/dp/B01EJIH88U/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B01EJIH88U&pd_rd_w=vl0cX&content-id=amzn1.sym.15c0cc83-c6c5-4d44-aa3d-0de17a9f3682&pf_rd_p=15c0cc83-c6c5-4d44-aa3d-0de17a9f3682&pf_rd_r=J3KKGZ4721YT3PXNSNFN&pd_rd_wg=6TwQS&pd_rd_r=9e503762-64a9-41dc-a045-3cf4732da921&s=electronics&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw',
          'https://www.amazon.co.uk/dp/B01F5GMYBQ/ref=sspa_dk_detail_5?psc=1&pd_rd_i=B01F5GMYBQ&pd_rd_w=b8pn1&content-id=amzn1.sym.00b0073a-c363-4c4d-a2c8-d51ea12ea8c0&pf_rd_p=00b0073a-c363-4c4d-a2c8-d51ea12ea8c0&pf_rd_r=J3KKGZ4721YT3PXNSNFN&pd_rd_wg=6TwQS&pd_rd_r=9e503762-64a9-41dc-a045-3cf4732da921&s=electronics&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy']

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    try:
        product = {
            'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'price': r.html.xpath("//body/div[@id='a-page']/div[@id='dp']/div[@id='dp-container']/div[@id='ppd']/div[@id='centerCol']/div[@id='apex_desktop']/div[@id='corePriceDisplay_desktop_feature_div']/div/span/span", first=True).text
        }
        print(product)
    except:
        product = {
            'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'price': 'item unavailable'
        }
        print(product)
    return product

tvprices = []
for url in urls:
    tvprices.append(getPrice(url))

print(len(tvprices))

pricesdf = pd.DataFrame(tvprices)
pricesdf.to_excel('tvprices.xlsx', index=False)