import mysql.connector
import os
from dotenv import load_dotenv

env_loc=".env"
load_dotenv(env_loc)

db=mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    database=os.getenv('DB')
)
dbcursor=db.cursor()
