import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mylib"]

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mylib" in dblist:
  print("The database exists.")
else:
    print ("the database does not exists")

collist = mydb.list_collection_names()
if "books" in collist:
    print("The collection exists.")
else:
    print("The collection does not exists")

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#to insert only one entry
'''
mydict = {"name": "John", "address":"Highway 37"}

x = mycol.insert_one(mydict)
print (x.inserted_id)
'''

#to insert many entries
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
#List With IDS if you dont specify, MongoDB is gonna generate it for you
myListWithIDs = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
#x = mycol.insert_many(myListWithIDs)

#print list of the _id values of the inserted documents:
#print(x.inserted_ids)


for x in mycol.find():
  print(x)

# to retrieve data we use find
for x in mycol.find():
  print(x)

#to return name and addresses
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

#to retrieve data
# In this particular case: All addreses that start with S 
myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
# to retrieve all the data sorted by names in order 
mydoc = mycol.find().sort("name", -1)
#to retrieve all the data sorted by names in reverse order
mydoc = mycol.find().sort("name", -1)
for x in mydoc:
  print(x)
  
# Delete all entries 
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)


#Delete all the entries that start with S 
myquery = { "address": {"$regex": "^S"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")


# Delete all documents in a collection 
myquery = { "address": {"$regex": "^S"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")

#Dropping collections
mycol.drop()


#Updating address with the value 345
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)

 #Update all documents that start with S
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")



#Limited 
# to return the first the first 5 documents 
myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)
