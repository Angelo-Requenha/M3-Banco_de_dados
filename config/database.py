import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="140628",
            database="streaming"
        )
    except Error as e:
        print(f"Error to connect to database: {e}")
        return None
