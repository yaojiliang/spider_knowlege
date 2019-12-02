import re
from urllib import request

from fake_useragent import UserAgent

# 定义常用变量
url = "https://maoyan.com/board/4?offset=0"
headers = {'User-Agent': UserAgent().random}
#
# # 请求获取html
res = request.Request(url=url, headers=headers)
resp = request.urlopen(res)
html = resp.read().decode()
# # 解析提取数据re
re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
p = re.compile(re_bds, re.S)
r_list = p.findall(html)
# print(r_list)
# 保存到本地文件
with open('maoyan.txt','a') as f:
    for r in r_list:
        f.write(r[0]+'\t'+r[1].strip()+'\t'+r[2].strip()[5:15]+'\n')






# 3.解析提取数据re




