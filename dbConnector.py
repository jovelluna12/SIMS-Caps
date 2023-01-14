import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv('.env')

db=mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    database=os.getenv('DB')
)
dbcursor=db.cursor()
