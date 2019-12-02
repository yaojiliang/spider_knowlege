import csv
from urllib import request
import re
import time
import random
from fake_useragent import UserAgent

from day02.useragent import user_agent_url


class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        # 计数变量
        self.i = 0

    def get_html(self,url):
        headers = { 'User-Agent':random.choice(user_agent_url) }
        req = request.Request(url=url,headers=headers)
        resp = request.urlopen(req)
        html = resp.read().decode('utf-8')
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self,html):
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
        p = re.compile(re_bds,re.S)
        # film_list: [('','',''),()]
        film_list = p.findall(html)
        # 直接调用保存函数
        self.save_html(film_list)

    # writerow
    # def save_html(self,film_list):
    #     with open('maoyan.csv','a') as f:
    #         writer = csv.writer(f)
    #         for film in film_list:
    #             L = [
    #                 film[0].strip(),
    #                  film[1].strip(),
    #                  film[2].strip()[5:15]
    #                  ]
    #             writer.writerow(L)
    def save_html(self,film_list):
        L = []
        with open('maoyan1.csv','a') as f:
            writer = csv.writer(f)
            for film in film_list:
                t=(film[0].strip(),
                   film[1].strip(),
                   film[2].strip()[5:15]
                   )
                L.append(t)
            writer.writerows(L)

    def run(self):
        for offset in range(0,41,10):
            url = self.url.format(offset)
            self.get_html(url)
            # 休眠
            time.sleep(random.uniform(1,2))
        print('数量:',self.i)

if __name__ == '__main__':
    start = time.time()
    spider = MaoyanSpider()
    spider.run()
    end = time.time()
    print('执行时间:%.2f' % (end-start))








































