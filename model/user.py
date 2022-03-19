from flask import *
import mysql.connector
from connection import pool

class UserModel:
    def get_user(self,user):
        try:
            connection=pool.connection()
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM `taipei_spots` WHERE `id`=%s ;",(user,))
            atuser=cursor.fetchone()
            return user
        except:
            return "error"
        finally:
            cursor.close()
            connection.close()

user_model=UserModel()