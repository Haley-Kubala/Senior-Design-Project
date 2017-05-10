import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client['STUDENT_INFO']
collection = db["id_student"]
collection2 = db["student_log"]
