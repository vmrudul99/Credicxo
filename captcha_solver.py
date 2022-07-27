import requests
from scrapy.http import HtmlResponse
from PIL import Image
from pytesseract import pytesseract

import urllib.request

if __name__ == '__main__':
    url = 'https://www.amazon.com/errors/validateCaptcha'
    with requests.Session() as s:
        resp = s.get(url=url)
        response = HtmlResponse(url='',body=resp.content)
        captcha_img_link = response.xpath('//div[@class="a-row a-text-center"]/img/@src').get()
        urllib.request.urlretrieve(str(captcha_img_link), "00000001.jpg")
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image_path = r"00000001.jpg"
        img = Image.open(image_path)
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(img)
        if text != None:
            text = text.strip().replace('\n','')
        print("Captcha text ------> ",text)

        fill_up_captcha = f'https://www.amazon.com/errors/validateCaptcha?amzn=vac3Ri%2BlTsAct2GvJyz9JQ%3D%3D&amzn-r=%2F&field-keywords={text}'
        resp1 = s.get(url=fill_up_captcha)
        response1 = HtmlResponse(url='',body=resp1.content)

        print("Done")


