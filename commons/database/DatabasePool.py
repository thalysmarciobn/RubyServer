import mysql.connector

import mysql.connector.pooling
from mysql.connector import ProgrammingError, InterfaceError

from commons.util import Logging


class DatabasePool:
    __pool = None

    @staticmethod
    def connect(pool_name: str, pool_size: int, pool_reset_session: bool, database: str):
        try:
            DatabasePool.__pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name=pool_name,
                pool_size=pool_size,
                pool_reset_session=pool_reset_session,
                **database)
            return True
        except ProgrammingError as error:
            Logging.exception(f"Can't connect to database, error: {error}")
        except InterfaceError as error:
            Logging.exception(f"Can't connect to database, error: {error}")
        return False

    @staticmethod
    def execute(sql: str, args: object=None, commit: bool=False):
        conn = DatabasePool.__pool.get_connection()
        cursor = conn.cursor(dictionary=True)
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
            if len(res) > 0:
                return res[0]
            return None

    @staticmethod
    def executemany(sql: str, args: object, commit: bool=False):
        conn = DatabasePool.__pool.get_connection()
        cursor = conn.cursor(dictionary=True)
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
