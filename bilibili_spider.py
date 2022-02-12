from selenium import webdriver
import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import common
import numpy as np
import json
import requests
from lxml import etree
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import jieba 
from PIL import Image
%matplotlib inline


class Video():
    def __init__(self, BV, driver_path=r"/Users/zcz/Desktop/python project/chromedriver"):
        self.url = "https://www.bilibili.com/video/" + BV
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        self.driver = webdriver.Chrome(driver_path, chrome_options=option)
        self.driver.implicitly_wait(10)
        self.BV = BV

    def get_comment(self):
        self.driver.get(self.url)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="bilibiliPlayer"]/div[1]/div[1]/div[16]').click()
        js = "return action=document.body.scrollHeight"
        height = self.driver.execute_script(js)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        print("current url : ", self.url)
        
        t1 = int(time.time())
        n = 0

        while 1:
            t2 = int(time.time())
            if t2 - t1 < 30:
                new_height = self.driver.execute_script(js)
                # print(new_height)
                if new_height > height:
                    time.sleep(0.5)
                    new_js = "window.scrollTo(0, document.body.scrollHeight)"
                    self.driver.execute_script(new_js)
                    height = new_height
                    t1 = int(time.time())
            elif n < 3:
                print(f"Sticking {n}")
                time.sleep(1)
                n += 1
            else:
                print("Getting pagesourse")
                # driver.execute_script("window.scrollTo(0, 0)")
                break
        self.comments = [i.text for i in self.driver.find_elements_by_xpath("//p[@class='text']")]
        self.driver.quit()
    
    def save_comment(self, path="comment.txt"):
        print("Saving Begin.")
        print("path : ", os.path.join(os.getcwd(), path))
        with open(path, "w") as f:
            for comment in self.comments:
                f.write(comment)
                f.write("\n")
        print("Saving End.")
        
    def get_barrage(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        }
        tmp = f"https://api.bilibili.com/x/player/pagelist?bvid={self.BV}&jsonp=jsonp"
        r = requests.get(tmp, headers=headers)
        cid = json.loads(r.text).get("data")[0]["cid"]
        url = "https://api.bilibili.com/x/v1/dm/list.so?oid="+str(cid)
        r = requests.get(url)
        html = etree.HTML(r.content)
        self.barrages = html.xpath("//d/text()")

    def save_barrage(self, path="barrage.txt"):
        print("Saving Begin.")
        print("path : ", os.path.join(os.getcwd(), path))
        with open(path, "w") as f:
            for barrage in self.barrages:
                f.write(barrage)
                f.write("\n")
        print("Saving End.")

    def show_word_graph(self):
        # pic_path = "/Users/zcz/Desktop/汤姆猫.jpg"
        # background_image = np.array(Image.open(pic_path))
        # pic_color = ImageColorGenerator(background_image)
        comment_text = "".join(self.comments)
        cut_comment = "".join(jieba.cut(comment_text, cut_all=False))
        wordcloud1 = WordCloud(font_path="/Library/Fonts/Arial Unicode.ttf", background_color="white",
                      width=1000, height=1000).generate(cut_comment)
        
        barrage_txt = "".join(self.barrages)
        cut_barrage = "".join(jieba.cut(barrage_txt, cut_all=False))
        wordcloud2 = WordCloud(font_path="/Library/Fonts/Arial Unicode.ttf", background_color="white",
                      width=1000, height=1000).generate(cut_barrage)

        plt.figure(figsize=(10, 20), dpi=100)
        plt.subplot(121)
        # plt.imshow(wordcloud1.recolor(color_func=pic_color), interpolation="bilinear")
        plt.imshow(wordcloud1)
        plt.xticks([])
        plt.yticks([])
        plt.title("comment")

        plt.subplot(122)
        plt.imshow(wordcloud2)
        plt.xticks([])
        plt.yticks([])
        plt.title("barrage")

        plt.show()