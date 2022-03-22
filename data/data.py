from flask import *
import urllib.request as request
import json
import re
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(".env")
connection=mysql.connector.connect(
    host=os.getenv("host"),
    port=os.getenv("port"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("database"),
    buffered=True #buffered=True會把結果集保存到本地並一次性返回，這樣可以提高性能
)

try:
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
            spot_image_list=""

            for spot_image in spot_images:
                if re.compile('jpg|JPG|png|PNG$').search(spot_image):
                    spot_image="https://"+spot_image
                    spot_image_list=spot_image_list+spot_image+" "
                    
            cursor.execute("INSERT INTO `taipei_spots`(`name`,`category`,`description`,`address`,`transport`,`mrt`,`latitude`,`longitude`,`images`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);",
            (str(spot_name),str(spot_category),str(spot_description),str(spot_address),str(spot_transport),str(spot_mrt),str(spot_latitude),str(spot_longitude),spot_image_list))

except:
    print("連接Connection Pool失敗！")

finally:
    cursor.close()
    connection.commit() #如果需要更動到資料時需寫此指令
    connection.close()
