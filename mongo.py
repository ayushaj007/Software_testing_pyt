from pymongo import MongoClient

# Connect to the MongoDB server running on localhost at the default port 27017
client = MongoClient('localhost', 27017)

# Get the 'mydatabase' database
db = client['mydatabase']

# Get the 'users' collection
collection = db['users']

# Find and print all documents in the 'users' collection
for user in collection.find():
    print(user)
