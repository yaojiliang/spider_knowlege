from urllib import request
import json

url = 'http://httpbin.org/get'
response = request.urlopen(url)
# agent=response.header()
html = response.read().decode()
print(html)
print(type(html))
h1 = json.loads(html)
print(h1['headers'])
