import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import pooling

load_dotenv()


class MySQLConnector:

    _connection_pool = None

    @classmethod
    def initialize_pool(cls):
        """
        Initialize pool only once.
        """

        if cls._connection_pool is None:

            cls._connection_pool = pooling.MySQLConnectionPool(
                pool_name=os.getenv(
                    "DB_POOL_NAME",
                    "mysql_pool"
                ),
                pool_size=int(
                    os.getenv(
                        "DB_POOL_SIZE",
                        10
                    )
                ),
                pool_reset_session=True,
                host=os.getenv("DB_HOST"),
                port=int(os.getenv("DB_PORT")),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )

    def __init__(self):

        if MySQLConnector._connection_pool is None:
            MySQLConnector.initialize_pool()

        self.connection = (
            MySQLConnector._connection_pool
            .get_connection()
        )

    def execute_query(self, query, params=None):

        cursor = self.connection.cursor()

        try:
            cursor.execute(query, params)
            self.connection.commit()

            return cursor.rowcount

        finally:
            cursor.close()

    def fetch_one(self, query, params=None):

        cursor = self.connection.cursor(
            dictionary=True
        )

        try:
            cursor.execute(query, params)

            return cursor.fetchone()

        finally:
            cursor.close()

    def fetch_all(self, query, params=None):

        cursor = self.connection.cursor(
            dictionary=True
        )

        try:
            cursor.execute(query, params)

            return cursor.fetchall()

        finally:
            cursor.close()

    def close(self):

        if self.connection.is_connected():
            # Returns connection back to pool
            self.connection.close()