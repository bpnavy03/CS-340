from pymongo import MongoClient
from bson.objectid import ObjectId

# Bryan Pirrone
# CS 340
# Project One
# 04/06/2024

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'changeme'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30629
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True  # Return True if insert is successful
            except Exception as e:
                print(f"An error occurred: {e}")
                return False  # Return False if insert fails
        else:
            raise ValueError("Nothing to save, because data parameter is empty")

# Read method to implement the R in CRUD.
    def read(self, criteria=None):
        if criteria is None:
            criteria = {}  # If no criteria is given, set it to an empty dictionary
        try:
            documents = self.collection.find(criteria)
            return list(documents)  # Convert cursor to list and return
        except Exception as e:
            print(f"An error occurred: {e}")
            return []  # Return an empty list if query fails

# Update method to implement the U in CRUD.
    def update(self, query, update_values):
        """ Update document(s) in the MongoDB database. """
        if query is None or update_values is None:
            raise ValueError("Query and update values cannot be None")

        try:
            result = self.collection.update_many(query, {'$set': update_values})
            return result.modified_count  # Return the count of modified documents
        except Exception as e:
            print(f"An error occurred during update: {e}")
            return 0  # Return 0 if update fails

# Delete method to implement in the D in CRUD.
    def delete(self, query):
        """ Delete document(s) from the MongoDB database. """
        if query is None:
            raise ValueError("Query cannot be None")

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count  # Return the count of deleted documents
        except Exception as e:
            print(f"An error occurred during delete: {e}")
            return 0  # Return 0 if delete fails
    