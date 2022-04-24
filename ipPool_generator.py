# 建立属于自己的开放代理IP池
import requests
import random
import time
from lxml import etree
from fake_useragent import UserAgent


class IpPool:
    def __init__(self):
        # self.test_url = 'http://httpbin.org/get'  # 测试ip是否可用的 url
        self.test_url = "http://www.baidu.com/"
        self.url = 'https://www.89ip.cn/index_{}.html'   # 获取IP的目标 url
        self.headers = {
            'User-Agent': UserAgent(verify_ssl=False).random
        }   # 获取随机的UA

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text
        return html

    def get_proxy(self, url):
        html = self.get_html(url=url)
        elemt = etree.HTML(html)

        ips_list = elemt.xpath('//table/tbody/tr/td[1]/text()')
        ports_list = elemt.xpath('//table/tbody/tr/td[2]/text()')

        for ip, port in zip(ips_list, ports_list):
            # 拼接ip与port
            proxy = ip.strip() + ":" + port.strip()
            self.test_proxy(proxy)

    def test_proxy(self, proxy):
        proxies = {
            'http': 'http://{}'.format(proxy),
            'https': 'https://{}'.format(proxy),
        }
        try:
            resp = requests.get(
                url=self.test_url, proxies=proxies, headers=self.headers, timeout=5)

            if resp.status_code == 200:
                print(proxy, "\033[31m可用\033[0m")
                with open("ip_pool.txt", "a") as f:
                    f.write(proxy + "\n")
            else:
                print(proxy, '不可用')
        except Exception as e:
            print(proxy, '不可用')

    # 执行函数
    def crawl(self):
        # 这里只获取前100页提供的免费代理IP测试
        for i in range(1, 150):
            page_url = self.url.format(i)
            time.sleep(random.randint(1, 2))  # 控制抓取频率
            self.get_proxy(url=page_url)

    def test(self):
        with open("ip_pool.txt", "r") as f:
            print("正在读取已有ip")
            for proxy in f.readlines():
                proxy = proxy.strip()
                proxies = {
                    'http': 'http://{}'.format(proxy),
                    'https': 'https://{}'.format(proxy),
                }
                try:
                    resp = requests.get(
                        url=self.test_url, proxies=proxies, headers=self.headers, timeout=10)

                    if resp.status_code == 200:
                        print(proxy, "\033[31m可用\033[0m")
                    else:
                        print(proxy, '不可用')
                except Exception as e:
                    print(proxy, '不可用')


class ip_pool:
    def __init__(self):
        self.ips = []
        self.test_url = "http://www.baidu.com/"
        self.headers = {
            'User-Agent': UserAgent(verify_ssl=False).random
        }
        with open("ip_pool.txt", "r") as f:
            print("正在读取已有ip")
            for proxy in f.readlines():
                proxy = proxy.strip()
                proxies = {
                    'http': 'http://{}'.format(proxy),
                    'https': 'https://{}'.format(proxy),
                }
                try:
                    resp = requests.get(
                        url=self.test_url, proxies=proxies, headers=self.headers, timeout=10)

                    if resp.status_code == 200:
                        print(proxy, "\033[31m可用\033[0m")
                        self.ips.append(proxy)
                    else:
                        print(proxy, '不可用')
                except Exception as e:
                    print(proxy, '不可用')

    def random_ip(self):
        return random.choice(self.ips)


if __name__ == '__main__':
    # ip = ip_pool()
    # print(ip.random_ip())
    # print(ip.random_ip())
    # print(ip.random_ip())
    # print(ip.random_ip())
    ip = IpPool()
    ip.crawl()
