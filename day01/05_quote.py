from urllib import request,parse

word = input('请输入要搜索的内容:')
parmes = parse.quote(word)
url = 'http://www.baidu.com/s?wd={}'.format(parmes)
# print(url)
# 发送请求获取响应对象
# header
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'}

# 创建req对象
req = request.Request(url=url,headers=headers)
# 获取response对象
response = request.urlopen(req)
# 获取内容
html=response.read().decode()

# print(html)

# 保存文件
filename = word+'.html'
with open(filename,'w') as f:
    f.write(html)
