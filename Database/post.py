from Database.database import Database

class Book:

    @staticmethod
    def add_to_mongo_directly(data):
        mongo_data= Database.insert(collection='books', data=data)
        return mongo_data

    @staticmethod
    def from_mongo(query):
        mongo_data =  Database.find_one_data(collection='books', query={'isbn':int(query)})
        if mongo_data == None:
            return None
        else:
            return dict(mongo_data)

    @staticmethod
    def update_mongo_book(query, updates):
        Database.update(collection='books', myquery={'isbn':int(query)}, updates={'$set':updates})

    @staticmethod
    async def delete_from_mongo(query):
       await Database.delete_one(collection='books', query={'isbn':int(query)})

    @staticmethod
    async def find_isbn_mongo(query):
        isbn_book =  [isbn_book for isbn_book in Database.find_data(collection='books', query={'isbn': int(query)})]
        return isbn_book