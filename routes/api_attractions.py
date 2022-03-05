from flask import *
import mysql.connector
import json
from connection import pool
import re

api_attractions=Blueprint("api_attractions",__name__,static_folder="static",template_folder="templates")

@api_attractions.route("/api/attractions")
def attractions():
    page=request.args.get("page",0,type=int)
    keyword=request.args.get("keyword")
    connection=pool.connection()
    cursor=connection.cursor()

    
    if keyword:
        cursor.execute("SELECT * FROM `taipei_spots` WHERE `name`LIKE %s LIMIT %s,12;",("%"+keyword+"%",12*page))
        attractions=cursor.fetchall()
        attractions_list=[]
        cursor.execute("SELECT COUNT(*) FROM `taipei_spots` WHERE `name`LIKE %s;",("%"+keyword+"%",))
        count=cursor.fetchone()

        for attraction in attractions:
            spot_images=attraction[9].split('https://')
            images_list=[]
            for spot_image in spot_images:
                if re.compile('jpg|JPG|png|PNG$').search(spot_image):
                    images_list.append('https://'+spot_image)            

            data={"id":attraction[0],
                "name":attraction[1],
                "category":attraction[2],
                "description":attraction[3],
                "address":attraction[4],
                "transport":attraction[5],
                "mrt":attraction[6],
                "latitude":attraction[7],
                "longitude":attraction[8],
                "images":images_list
                }
            attractions_list.append(data)

        if count[0]-12*page<=12:
            attractions_data={
                "nextPage":None,
                "data":attractions_list
            }
            response = make_response(jsonify(attractions_data))
            response.headers["Access-Control-Allow-Origin"] = "*" 
            return response 
        elif count[0]-12*page>12:
            attractions_data={
                "nextPage":page+1,
                "data":attractions_list
            }
            response = make_response(jsonify(attractions_data))
            response.headers["Access-Control-Allow-Origin"] = "*" 
            return response    
        else:
            attractions_data={
                "error": True,
                "message": "伺服器內部錯誤"
            }
            response = make_response(jsonify(attractions_data))
            response.headers["Access-Control-Allow-Origin"] = "*" 
            return response,500

    if keyword==None:
        cursor.execute("SELECT * FROM `taipei_spots` LIMIT %s,12;",(12*page,))
        attractions=cursor.fetchall()
        attractions_list=[]
        cursor.execute("SELECT COUNT(*) FROM `taipei_spots`;")
        count=cursor.fetchone()

        for attraction in attractions:
            spot_images=attraction[9].split('https://')
            images_list=[]
            for spot_image in spot_images:
                if re.compile('jpg|JPG|png|PNG$').search(spot_image):
                    images_list.append('https://'+spot_image)  

            data={"id":attraction[0],
                "name":attraction[1],
                "category":attraction[2],
                "description":attraction[3],
                "address":attraction[4],
                "transport":attraction[5],
                "mrt":attraction[6],
                "latitude":attraction[7],
                "longitude":attraction[8],
                "images":images_list
                }
            attractions_list.append(data)
        if count[0]-12*page>12:
            attractions_data={
                "nextPage":page+1,
                "data":attractions_list
            }
            response = make_response(jsonify(attractions_data))
            response.headers["Access-Control-Allow-Origin"] = "*" 
            return response 
        elif count[0]-12*page<=12:
            attractions_data={
                "nextPage":None,
                "data":attractions_list
            }
            response = make_response(jsonify(attractions_data))
            response.headers["Access-Control-Allow-Origin"] = "*" 
            return response 
        else:
            attractions_data={
                "error": True,
                "message": "伺服器內部錯誤"
            }
            response = make_response(jsonify(attractions_data))
            response.headers["Access-Control-Allow-Origin"] = "*" 
            return response,500

    cursor.close()
    connection.close()