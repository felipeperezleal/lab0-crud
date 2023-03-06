import mysql.connector

database = mysql.connector.connect(
    #Change with respective credentials
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'lab0db'
)