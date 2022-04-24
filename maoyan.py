import requests
from lxml import etree
from fake_useragent import UserAgent
import os
import time
import random

UA = UserAgent()
url = "http://www.cits0871.com/sort/xuanhuan/"
proxies = {
    "http:": "http://119.28.155.202:9999"
}
headers = {
    'user-agent': UA.random,
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.cits0871.com/sort/xuanhuan/',
    'Upgrade-Insecure-Requests': "1"
}


def get_info(url):
    global proxies
    headers = {
        'user-agent': UA.random,
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://www.cits0871.com/sort/xuanhuan/',
        'Upgrade-Insecure-Requests': "1"
    }
    r = requests.get(url, proxies=proxies, headers=headers)
    html = etree.HTML(r.text)
    web_list = html.xpath('//span[@class="s3"]/a/@href')
    name_list = html.xpath('//span[@class="s3"]/a/text()')
    url_list = list(map(lambda x: "http://www.cits0871.com" + x, web_list))
    return url_list, name_list


def scraper(url, name, path):
    global proxies
    headers = {
        'user-agent': UA.random,
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://www.cits0871.com/sort/xuanhuan/',
        'Upgrade-Insecure-Requests': "1"
    }
    print(f"Scraping {url}, named {name}")
    try:
        r = requests.get(url, headers=headers, proxies=proxies)
        html = etree.HTML(r.text)
        data = "\n".join(html.xpath('//*[@id="content"]//text()'))
        with open(f"{path}/{name}.txt", "w") as f:
            f.write(data)
        print("Successfully")
    except:
        print("Error")


if not os.path.exists("novel"):
    os.mkdir("novel")

for i in range(1, 200):
    url = f"http://www.cits0871.com/sort/xuanhuan/{i}.html"
    url_list, name_list = get_info(url)
    for url, name in [*zip(url_list, name_list)]:
        scraper(url, name, "novel")
        time.sleep(1)
