import csv
# 当行写入:writerow
with open('film.csv','w') as f:
    write = csv.writer(f)
    write.writerow(['hahhaha','oo'])
    write.writerow(['hehhehe','cc'])
# 多行写入
with open('film.csv','w') as f:
    write = csv.writer(f)
    write.writerow([('aa','dadsd'),('sdd','dsda')])