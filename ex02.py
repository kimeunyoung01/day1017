from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient('localhost',27017)
db = client.bit
students = db.student
# arr = students.find({},{"_id":0})
arr = students.find({"kor":{"$gte":90}},{"name":1,"kor":1,"_id":0})
r = dumps(arr, ensure_ascii=False)
print(r)
# print(arr)
# for student in arr:
#     print(student)