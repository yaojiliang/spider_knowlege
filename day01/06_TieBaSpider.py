# 爬去百度贴吧
import random
import time
from urllib import request, parse

from useragent import user_agent_url


class TieBaSpider(object):
    def __init__(self):
        # 定义常用变量
        self.url = 'https://tieba.baidu.com/f?kw={}&pn={}'


    # 1,请求
    def get_html(self, url):
        headers = {'User-Agent': random.choice(user_agent_url)}
        req = request.Request(url=url, headers=headers)
        resp = request.urlopen(req)
        html = resp.read().decode()
        return html

    # 2,解析
    def parse_html(self):
        pass

    # 3,保存
    def save_html(self, filename, html):
        with open(filename, 'w') as f:
            f.write(html)

    # 4,入口函数
    def run(self):
        name = input('请输入贴吧名：')
        begin = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))
        params = parse.quote(name)
        # for循环-拼接地址,发请求,保存
        for page in range(begin, end + 1):
            pn = (page - 1) * 50
            url = self.url.format(params, pn)
            html = self.get_html(url=url)
            filename = name + '-第%s页.html' % str(page)
            self.save_html(filename=filename, html=html)

            print('第%s页抓取成功' % page)
            # time.sleep(random.randint(1,2))
            time.sleep(random.uniform(0, 1))


if __name__ == '__main__':
    tieba = TieBaSpider()
    tieba.run()
