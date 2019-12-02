import csv
from urllib import request
import re
import time
import random
from fake_useragent import UserAgent
import pymysql

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        # 计数变量
        self.i = 0
        # 数据库连接
        self.db=pymysql.connect(
            'localhost',
            'root',
            '123456',
            'maoyandb',
            charset='utf8'
        )
        self.cursor = self.db.cursor()
        # 定义列表,用来存放所有电影的元组
        self.L=[]

    def get_html(self,url):
        headers = { 'User-Agent':UserAgent().random }
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

    # mysql存储
    def save_html(self,film_list):
        for film in film_list:
            self.L.append(
                (film[0].strip(),
                film[1].strip(),
                 film[2].strip()[5:15]
                 )
            )

    def run(self):
        for offset in range(0,91,10):
            url = self.url.format(offset)
            self.get_html(url)
            # 休眠
            time.sleep(random.uniform(1,2))
        ins = 'insert into filmtab values(%s,%s,%s)'
        # executemany　存取速度
        self.cursor.executemany(ins, self.L)
        self.db.commit()
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    start = time.time()
    spider = MaoyanSpider()
    spider.run()
    end = time.time()
    print('执行时间:%.2f' % (end-start))








































