from flask import *
import mysql.connector
import json
from connection import pool
import re

api_attraction=Blueprint("api_attraction",__name__,static_folder="static",template_folder="templates")

@api_attraction.route("/api/attraction/<attractionId>")
def attraction(attractionId):
    connection=pool.connection()
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `taipei_spots` WHERE `id`=%s ;",(attractionId,))

    attraction=cursor.fetchone()

    if attraction:
        spot_images=attraction[9].split('https://')
        images_list=[]
        for spot_image in spot_images:
            if re.compile('jpg|JPG|png|PNG$').search(spot_image):
                images_list.append('https://'+spot_image)
        data={
            "data":{
                "id":attraction[0],
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
        }
        response = make_response(jsonify(data))
        response.headers["Access-Control-Allow-Origin"] = "*" #設定跨域請求Headers
        return response,200

    elif attraction==None:
        data={
        "error": True,
        "message": "景點編號不正確"
        }
        return jsonify(data),400

    else:
        data={
        "error": True,
        "message": "伺服器內部錯誤"
        }
        return jsonify(data),500

    cursor.close()
    connection.close()