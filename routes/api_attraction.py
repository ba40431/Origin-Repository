from flask import *
import mysql.connector
import json
from connection import pool

api_attraction=Blueprint("api_attraction",__name__,static_folder="static",template_folder="templates")

@api_attraction.route("/api/attraction/<attractionId>/")
def attraction(attractionId):
    connection=pool.connection()
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `taipei_spots` WHERE `id`=%s ;",(attractionId,))

    attraction=cursor.fetchone()

    if attraction:
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
                "images":attraction[9]
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