'''
分组总结：
1、在网页中,想要什么内容,就加()
2、先按整体正则匹配,然后再提取分组()中的内容
  如果有2个及以上分组(),则结果中以元组形式显示
  [('小区1','500万'),('小区2','600万'),()]
'''
import re

s = 'A B C D'
p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))
# 结果: ['A B','C D']

p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))
# 第1步: ['A B','C D']
# 第2步: ['A','C']

p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s))
# 第1步: ['A B','C D']
# 第2步: [('A','B'),('C','D')]