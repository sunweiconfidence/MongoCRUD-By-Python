#coding:utf-8
import pymongo
# 默认没有密码，所以可以这么写。如果设置了密码需要使用授权方法db.auth("用户名","密码")
conn = pymongo.MongoClient(host="localhost", port=29032)
# 选择一个数据库
db = conn.test
# 选择一个collection
collection = db.user

def show(collection):
    # 查找
    for item in collection.find():
        print(item)

# 插入
dic = {
    'name': '凤凰传奇',
    'age': 23,
    'address': '北京朝阳',
    'blog': '博客世界'
}
collection.insert(dic)
show(collection)
print(collection)

#插入多条记录
many = []
import copy
for index in range(1, 8):
    tempdic = copy.deepcopy(dic)
    tempdic['age'] = index**2
    many.append(tempdic)

collection.insert_many(many)
show(collection)

#更新一条记录
collection.update({'name': '凤凰传奇'}, {'$set': {"address": "江苏淮安"}})
show(collection)

#更新符合条件的所有记录
collection.update_many({'name': '凤凰传奇'}, {'$set': {"name": "可爱的Mongodb"}})
show(collection)

# 删除操作ivan
collection.remove({'name':'ivan'})
show(collection)

#查询 某个符合要求的字段

#大于： $gt
#小于 : $lt
#大于等于: $gte
#小于等于: $lte
#不等于 : $ne
# 带有查询条件的查询
items = collection.find({"age": {'$gt': 20}})
for item in items:
    print(item)


#查询限制条数
items = collection.find({"age": {'$gt': 20}}).limit(2)
for item in items:
    print(item)

# 指定查询字段的查询
items = collection.find({"age": {'$gt': 20}}, ['name', 'blog']).limit(5)
for item in items:
    print(item)

# 查询collection中到底有多少条记录
count = collection.count()
print("user 集合中共有{} 条数据".format(count))


#对查询结果排序输出
items = collection.find().sort([('age', pymongo.ASCENDING), ('address', pymongo.DESCENDING)])
for item in items:
    print(item)

# 模糊查询
items = collection.find({"address": {"$regex": r'^江苏.*'}})
for item in items:
    print(item)


# 存在性查询
items = collection.find({'address': {'$exists': True}})
for item in items:
    print(item)


# in 查询
items = collection.find({'age': {'$in': [18, 25, 22, 28]}})
for item in items:
    print(item)

# not in 查询
items = collection.find({'age': {'$nin': [18, 19, 28]}})
for item in items:
    print(item)