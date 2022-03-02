from flask import *
import mysql.connector
import json
from connection import pool

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

        for attraction in attractions:
            data={"id":attraction[0],
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
            attractions_list.append(data)
        if attractions:
            attractions_data={
                "nextPage":None,
                "data":attractions_list
            }
            response = make_response(jsonify(attractions_data))
            return response 
        else:
            attractions_data={
                "error": True,
                "message": "無資料"
            }
            response = make_response(jsonify(attractions_data))
            return response 

    if keyword==None:
        cursor.execute("SELECT * FROM `taipei_spots` LIMIT %s,12;",(12*page,))
        attractions=cursor.fetchall()
        attractions_list=[]
        for attraction in attractions:
            data={"id":attraction[0],
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
            attractions_list.append(data)
        if page<4:
            attractions_data={
                "nextPage":page+1,
                "data":attractions_list
            }
            response = make_response(jsonify(attractions_data))
            return response 
        elif page==4:
            attractions_data={
                "nextPage":None,
                "data":attractions_list
            }
            response = make_response(jsonify(attractions_data))
            return response 
        elif page>4:
            attractions_data={
                "error": True,
                "message": "無資料"
            }
            response = make_response(jsonify(attractions_data))
            return response 
        else:
            attractions_data={
                "error": True,
                "message": "伺服器內部錯誤"
            }
            response = make_response(jsonify(attractions_data))
            return response,500

    cursor.close()
    connection.close()