import requests
from lxml import etree

url = "https://www.89ip.cn/"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}

r = requests.get(url, headers=headers)
html = etree.HTML(r.text)
print(html.xpath(
    '/html/body//div[3]/div[1]/div/div[1]/table/tbody//td//text()'))
