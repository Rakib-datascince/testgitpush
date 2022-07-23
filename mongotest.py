import pymongo

client = pymongo.MongoClient("mongodb+srv://Rakibsheikh:mongo123@cluster0.tfr6i.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "rakib",
    "email":"sheikhrakib352@gmail.com",
    "surname":"sheikh"

}
db1 = client['mongotest']
coll = db['test']
coll.insert_one(d )