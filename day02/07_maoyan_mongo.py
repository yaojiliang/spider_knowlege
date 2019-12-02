'''
    把猫眼数据存储到mongodb
'''
from urllib import request
import re
import time
import random
from day02.useragent import user_agent_url
import pymongo

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        # 计数变量
        self.i = 0
        self.conn = pymongo.MongoClient('localhost',27017)
        self.db = self.conn['maoyandb']
        self.myset = self.db['maoyan_set']

    def get_html(self,url):
        # 有一些User-Agent不能用导致部分URL地址无法获取数据
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

    def save_html(self,film_list):

        for film in film_list:
            item = {}
            item['name']=film[0].strip()
            item['star']=film[1].strip()
            item['time']=film[2].strip()[5:15]
            self.i += 1
            # 把数据存入到mongodb数据库
            self.myset.insert_one(item)

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








































