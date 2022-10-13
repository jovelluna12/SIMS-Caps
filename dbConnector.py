import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="simscaps"
)
dbcursor=db.cursor()
