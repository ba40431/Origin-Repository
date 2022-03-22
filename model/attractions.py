from flask import *
import mysql.connector
from connection import pool


class KeywordAttractionsModel:
    def connection(self):
        try:
            connection=pool.connection()
            return connection
        except:
            return "error"
    def get_keyword_attractions(self,keyword,page):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM `taipei_spots` WHERE `name`LIKE %s LIMIT %s,12;",("%"+keyword+"%",12*page))
            attractions=cursor.fetchall()
            return attractions
        except:
            return "error"
        finally:
            cursor.close()
            connection.close()

    def get_keyword_count(self,keyword):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM `taipei_spots` WHERE `name`LIKE %s;",("%"+keyword+"%",))
            count=cursor.fetchone()
            return count
        except:
            return "error"
        finally:
            cursor.close()
            connection.close()

class AttractionsModel:
    def connection(self):
        try:
            connection=pool.connection()
            return connection
        except:
            return "error"
    def get_attractions(self,page):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM `taipei_spots` LIMIT %s,12;",(12*page,))
            attractions=cursor.fetchall()
            return attractions
        except:
            return "error"
        finally:
            cursor.close()
            connection.close()

    def get_count(self):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM `taipei_spots`;")
            count=cursor.fetchone()
            return count
        except:
            return "error"
        finally:
            cursor.close()
            connection.close()

keyword_attractions_model=KeywordAttractionsModel()
attractions_model=AttractionsModel()