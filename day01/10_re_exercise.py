import re
html='''
<div class="animal">
    <p class="name">
		<a title="Tiger"></a>
    </p>
    <p class="content">
		Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
		<a title="Rabbit"></a>
    </p>

    <p class="content">
		Small white rabbit white and white
    </p>
</div>
'''
p = re.compile('<div class="animal">.*?<a title="(.*?)".*?<p class="content">(.*?)</p>',re.S)
r_list=p.findall(html)
print(r_list)
print('*'*50)
for i in r_list:
    print("动物名称："+i[0],"动物描述："+i[1].strip())
    print('*'*50)

# 1.strip()# 去除左右两侧空白
# 2.split()# 分裂　'东方|200万'．split('|')
# 3.replace()# 替换
# 4.startswith()# 以什么开始
# 5.endswith()# 以什么结束
# 6.join()# 拼接
# 7.切片