from urllib import request

# urlopen(): 向URL发请求，返回响应对象
response=request.urlopen('http://www.baidu.com/')
# 响应对象的方法read()获取内容
html=response.read().decode()
# 获取响应码
code = response.getcode()
# 获取响应地址
url = response.geturl()
# print(html)
print(code,url)