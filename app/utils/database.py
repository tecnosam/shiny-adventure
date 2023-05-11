from pymongo import MongoClient

from app.utils.settings import DATABASE_NAME


mongo_client = MongoClient('mongodb://localhost:27017/')
main_database = mongo_client.get_database(DATABASE_NAME)
