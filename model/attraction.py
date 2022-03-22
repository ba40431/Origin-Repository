from flask import *
import mysql.connector
from connection import pool

class AttractionModel:
    def get_attraction(self,attractionId):
        try:
            connection=pool.connection()
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM `taipei_spots` WHERE `id`=%s ;",(attractionId,))
            attraction=cursor.fetchone()
            return attraction
        except:
            return "error"
        finally:
            cursor.close()
            connection.close()

attraction_model=AttractionModel()