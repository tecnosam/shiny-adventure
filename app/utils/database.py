from pymongo import MongoClient

from app.utils.settings import DATABASE_NAME, DATABASE_URI


mongo_client = MongoClient(DATABASE_URI)
main_database = mongo_client.get_database(DATABASE_NAME)
