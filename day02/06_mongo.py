import pymongo

# 连接对象
con = pymongo.MongoClient('localhost',27017)
# 库对象
db = con['studb']
# 集合对象
myset = db['stu_set']

myset.insert_one({'name':'小明'})