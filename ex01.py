#연습) 모든 학생의 이름, 국어, 영어, 수학을 출력
#연습) 국어점수가 80점이상인 학생의 이름과 국어점수
#           를 출력
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
mydb = client.bit
mycol = mydb.student
s = {"name":"김슬지","kor":100,"eng":80,"math":90}
mycol.insert_one(s)
print(s)



