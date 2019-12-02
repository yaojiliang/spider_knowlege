from urllib import request
import re
import time
import random
from useragent import user_agent_url
import ssl

ssl._create_default_https_context = ssl._create_unverified_context



class FilmSkySpider(object):
    def __init__(self):

        self.url='https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'

    # 功能函数1:获取html函数-->因为有重复的函数
    def get_html(self,url):
        headers = {'User-Agent':random.choice(user_agent_url)}
        req = request.Request(url=url,headers=headers)
        resp = request.urlopen(req)
        html = resp.read().decode('gb18030','ignore')
        return html

    # 功能函数2: 解析函数
    def parse_func(self,re_bds,html):
        p = re.compile(re_bds,re.S)
        r_list = p.findall(html)
        return r_list

    # 解析提取所需数据
    def parse_html(self,one_url):
        one_html = self.get_html(one_url)
        re_bds = '<table width="100%".*?<td width="5%".*?<a href="(.*?)" class="ulink">.*?</table>'
        href_list = self.parse_func(re_bds,one_html)
        # href_list:['/html/xxxx','/html/xxxx','']
        for href in href_list:
            link = 'https://www.dytt8.net'+href
            # 向详情页发请求，提取　名字和下载链接
            self.parse_two_page(link)
            # 抓取1个电影之后,随机休眠
            time.sleep(random.randint(1,2))


    # 解析二级页面函数
    def parse_two_page(self,link):
        two_html = self.get_html(link)
        re_bds='<div class="title_all"><h1><font color="#07519a">(.*?)</font></h1></div>.*?<td style="WORD-WRAP.*?>(.*?)</a>'
        r_list = self.parse_func(re_bds,two_html)
        # r_list:[('电影名称','下载链接'),()]
        item = {}
        item['name']=r_list[0][0].strip()
        item['download']=r_list[0][1].strip()
        print(item)

    def run(self):
        for i in range(1,206):
            one_url = self.url.format(i)
            self.parse_html(one_url)

if __name__ == '__main__':
    spider = FilmSkySpider()
    spider.run()
