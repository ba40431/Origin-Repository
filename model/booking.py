from flask import *
import mysql.connector
from connection import pool

class BookingModel:
    def connection(self):
        try:
            connection=pool.connection()
            return connection
        except:
            return "error"
    def check_booking(self,userId):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM `booking` WHERE `user_id`=%s;",(userId,))
            user=cursor.fetchone()
            return user
        except:
            return "error"
        finally:
            cursor.close()
            connection.close()

    def booking(self,attractionId,date,time,price,userId):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("INSERT INTO `booking` (`attraction_id`,`date`,`time`,`price`,`user_id`) VALUES (%s,%s,%s,%s,%s);",
            (attractionId,date,time,price,userId))
            booking=cursor.fetchone()
            return booking
        except:
            return "error"
        finally:
            cursor.close()
            connection.commit()
            connection.close()
    
    def update_booking(self,attractionId,date,time,price,userId):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("UPDATE `booking` SET `attraction_id`=%s,`date`=%s,`time`=%s,`price`=%s WHERE `user_id`=%s ;",
            (attractionId,date,time,price,userId))
            booking=cursor.fetchone()
            return booking
        except:
            return "error"
        finally:
            cursor.close()
            connection.commit()
            connection.close()
    def booking_data(self,userId):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("""SELECT `attraction_id`,`name`,`address`,`images`,`date`,`time`,`price`
	        FROM `booking` JOIN `taipei_spots` ON `attraction_id`=`taipei_spots`.`id` WHERE `user_id`=%s;"""
            ,(userId,))
            booking=cursor.fetchone()
            return booking
        except:
            return "error"
        finally:
            cursor.close()
            connection.commit()
            connection.close()
    def delete_booking(self,userId):
        try:
            connection=self.connection()
            cursor=connection.cursor()
            cursor.execute("DELETE FROM `booking` WHERE `user_id`=%s ;",(userId,))
            delete=cursor.fetchone()
            return delete
        except:
            return "error"
        finally:
            cursor.close()
            connection.commit()
            connection.close()

booking_model=BookingModel()