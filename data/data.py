from flask import *
import urllib.request as request
import json
import re
import mysql.connector
from connection import pool

connection=pool.connection()
cursor=connection.cursor()

with open("taipei-attractions.json","r",encoding="UTF-8") as file:
    data = json.load(file)
    spot_data=data["result"]["results"]
    for spot_item in spot_data:
        spot_name=spot_item["stitle"]
        spot_category=spot_item["CAT2"]
        spot_description=spot_item["xbody"]
        spot_address=spot_item["address"]
        spot_transport=spot_item["info"]
        spot_mrt=spot_item["MRT"]
        spot_latitude=spot_item["latitude"]
        spot_longitude=spot_item["longitude"]
        spot_images=spot_item["file"].split('https://')
        spot_image_list=[]

        for spot_image in spot_images:
            if re.compile('jpg|JPG|png|PNG$').search(spot_image):
                spot_image="https://"+spot_image
                spot_image_list.append(spot_image)

        # print(spot_name,spot_category,spot_description,spot_address,spot_transport,spot_mrt,spot_latitude,spot_longitude,spot_image_list)
                
        cursor.execute("INSERT INTO `taipei_spots`(`name`,`category`,`description`,`address`,`transport`,`mrt`,`latitude`,`longitude`,`images`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);",
        (str(spot_name),str(spot_category),str(spot_description),str(spot_address),str(spot_transport),str(spot_mrt),int(spot_latitude),int(spot_longitude),str(spot_image_list)))


cursor.close()
connection.commit() #如果需要更動到資料時需寫此指令
connection.close()
