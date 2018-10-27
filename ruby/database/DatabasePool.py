import mysql.connector

import mysql.connector.pooling

from ruby.utils import Logging


class DatabasePool:

    def __init__(self, config):
        self.__pool_name = config["Database"]
        self.__pool_size = config["PoolSize"]
        self.__database = {
            "host": config["Host"],
            "port": config["Port"],
            "user": config["User"],
            "password": config["Password"],
            "database": config["Database"]
        }
        self.__pool = None

    def connect(self):
        try:
            self.__pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name=self.__pool_name,
                pool_size=self.__pool_size,
                pool_reset_session=True,
                **self.__database)
            return True
        except:
            Logging.warn("Can't connect to database")
            return False

    def execute(self, sql, args=None, commit=False):
        conn = self.__pool.get_connection()
        cursor = conn.cursor()
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)
        if commit:
            conn.commit()
            cursor.close()
            conn.close()
            return None
        else:
            res = cursor.fetchall()
            cursor.close()
            conn.close()
            return res

    def executemany(self, sql, args, commit=False):
        conn = self.__pool.get_connection()
        cursor = conn.cursor()
        cursor.executemany(sql, args)
        if commit is True:
            conn.commit()
            cursor.close()
            conn.close()
            return None
        else:
            res = cursor.fetchall()
            cursor.close()
            conn.close()
            return res
