from pymongo import MongoClient

client = MongoClient("mongodb+srv://0619973969:WkpJdIEvnBXcWhUn@cluster0.qeymtn1.mongodb.net/?retryWrites=true&w=majority")
db = client.dbDynamicGroup

