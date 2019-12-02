from urllib import request

# 定义常用变量
url = 'http://httpbin.org/get'  # 测试响应头的地址
header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"}
# 创建请求对象
req = request.Request(url=url, headers=header)
# 获取响应对象
response = request.urlopen(req)
# 获取响应的内容
html = response.read().decode()
print(html)
