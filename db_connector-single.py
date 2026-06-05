import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class MySQLConnector:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows

    def fetch_one(self, query, params=None):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    def fetch_all(self, query, params=None):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
