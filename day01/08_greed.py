import re
html = '''
<div><p>九霄龙吟惊天变</p></div>
<div><p>风云际会浅水游</p></div>
'''
# .* 贪婪匹配一直往后面匹配
#p = re.compile('<div><p>.*</p></div>',re.S)
# .*? 爬虫常用--->非贪婪匹配，(.*?)<加括号是分组>
p = re.compile('<div><p>(.*?)</p></div>',re.S)
r_list = p.findall(html)
print(r_list)
print(len(r_list))

