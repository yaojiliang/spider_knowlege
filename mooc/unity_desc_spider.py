import bs4
import requests
from bs4 import BeautifulSoup
'''
实例1:中国大学排名定向爬虫
采用requests-bs4路线实现了中国大学排名定向爬虫
对中英文混排输出问题进行优化

'''

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except Exception as e:
        print(e)
        return ""

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append(
                        [tds[0].string,
                        tds[1].string,
                        tds[3].string]
                         )


def printUnivList(ulist,num):
    '''
    可以采用中文字符的空格填充chr(12288)
    :param ulist:
    :param num:
    :return:
    '''
    tblt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tblt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tblt.format(u[0],u[1],u[2],chr(12288)))

def main():
    unifo=[]
    url="http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
    html=getHTMLText(url)
    fillUnivList(unifo,html)
    printUnivList(unifo,20)# 20 univs

main()