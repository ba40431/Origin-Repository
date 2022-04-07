from flask import *
import mysql.connector
from connection import pool


class OrderModel:
    def connection(self):
        try:
            connection=pool.connection()
            return connection
        except:
            return "error"

    def order(self,orderNumber):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("""SELECT `orders`.`number`,`orders`.`attraction_id`,`orders`.`attraction_name`,`taipei_spots`.`address`,`taipei_spots`.`images`,
            `orders`.`date`,`orders`.`time`,`orders`.`price`,`orders`.`status`,
            `orders`.`user_name`,`orders`.`user_email`,`orders`.`user_phone` 
            FROM `orders`  
            LEFT JOIN `taipei_spots` ON `orders`.`attraction_id`=`taipei_spots`.`id`
            LEFT JOIN `user` ON `orders`.`user_email`=`user`.`email` WHERE `orders`.`number`=%s ;"""
            ,(orderNumber,))
            order=cursor.fetchone()
            return order
        except:
            connection.rollback()
            return "error"
        finally:
            cursor.close()
            connection.commit()
            connection.close()

order_model=OrderModel()