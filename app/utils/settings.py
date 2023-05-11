import os
from dotenv import load_dotenv


load_dotenv()

DATABASE_URI = os.getenv('DATABASE_URI', 'mongodb://localhost:27017/')
DATABASE_NAME = 'getamanpower'
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
