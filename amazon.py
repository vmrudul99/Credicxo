import json
from pprint import pprint
import pandas as pd
import requests
from scrapy.http import HtmlResponse

if __name__ == '__main__':
    excel = pd.read_excel('inputs.xlsx')
    asin_num = excel['asin']
    country_code = excel['country']
    output_list = list()
    product_found = list()
    product_not_found = list()
    for asin,country in zip(asin_num,country_code):
        url = f'https://www.amazon.{country}/dp/{asin}'
        headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
            }
        resp = requests.get(url=url,headers=headers)
        output = dict()
        if resp.status_code == 200:
            response = HtmlResponse(url='',body=resp.content)
            output['product_title'] = response.xpath('//title/text()').get()
            product_price = response.xpath('//*[contains(text(),"Buy used")]/../span[2]/text()').get()
            if product_price == None:
                product_price = response.xpath('//span[contains(text(),"€")]/text()').get()
            elif product_price == None:
                product_price = ""

            product_dscr = response.xpath('//ul[@class="a-unordered-list a-vertical a-spacing-mini"]/li//text()').get()
            if product_dscr == None:
                product_dscr = " ".join(response.xpath('//*[contains(text(),"Produktbeschreibungen")]/../div[2]//text()').getall())

            product_img = response.xpath('//div[@id="imgTagWrapperId"]/img/@src').get()
            if product_img == None:
                product_img = response.xpath('//div[@id="img-wrapper"]//img/@src').get()

            output['product_price'] = product_price
            output['product_dscr'] = product_dscr
            output['product_img'] = product_img
            output['url'] = resp.url
            pprint(output)
            product_found.append(output)
        else:
            output[str(resp.url)] = "Product not available!! statuscode is ",resp.status_code

            print("product not available-----> ",resp.url)
            product_not_found.append(output)
            pass
    output_list.append(product_found)
    output_list.append(product_not_found)
    f = open("amazon_data.json","w")
    file = f.write(json.dumps(output_list))

    print("successful export!!!")
