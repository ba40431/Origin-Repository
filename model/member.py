from flask import *
import mysql.connector
from connection import pool

class MemberModel:
    def connection(self):
            try:
                connection=pool.connection()
                return connection
            except:
                return "error"
    def get_orders(self,userEmail):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM `orders` WHERE `user_email`=%s;",(userEmail,))
            orders=cursor.fetchall()
            return orders
        except:
            connection.rollback()
            return "error"
        finally:
            cursor.close()
            connection.close()
    def update_password(self,userPassword,userEmail):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("UPDATE `user` SET `password`=%s WHERE `email`=%s;",(userPassword,userEmail))
            user=cursor.fetchone()
            return user
        except:
            connection.rollback()
            return "error"
        finally:
            cursor.close()
            connection.commit()
            connection.close()

member_model=MemberModel()