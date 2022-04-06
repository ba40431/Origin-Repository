from flask import *
import mysql.connector
from connection import pool

class OrdersModel:
    def connection(self):
        try:
            connection=pool.connection()
            return connection
        except:
            return "error"

    def new_orders(self,orderNumber,attractionId,attractionName,date,time,price,userName,userEmail,userPhone):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("""INSERT INTO `orders`  (`number`,`attraction_id`,`attraction_name`,`date`,`time`,
            `price`,`user_name`,`user_email`,`user_phone`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);""",
            (orderNumber,attractionId,attractionName,date,time,price,userName,userEmail,userPhone))
            orders=cursor.fetchone()
            return orders
        except:
            return "error"
        finally:
            cursor.close()
            connection.commit()
            connection.close()

    def update_status(self,orderNumber):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("UPDATE `orders` SET `status`=1 WHERE `number`=%s;",(orderNumber,))
            status=cursor.fetchone()
            return status
        except:
            return "error"
        finally:
            cursor.close()
            connection.commit()
            connection.close()

    def delete_booking(self,userEmail):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("DELETE FROM `booking` WHERE `user_email`=%s ;",(userEmail,))
            delete=cursor.fetchone()
            return delete
        except:
            return "error"
        finally:
            cursor.close()
            connection.commit()
            connection.close()

orders_model=OrdersModel()