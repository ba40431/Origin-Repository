from flask import *
import json
from model.order import order_model
import jwt
from routes.token import use_jwt
import os
from dotenv import load_dotenv

load_dotenv(".env")


api_order=Blueprint("api_order",__name__,static_folder="static",template_folder="templates")

@api_order.route("/api/order/<orderNumber>")
def order(orderNumber):
    token=use_jwt.get_token()
    jwt_key=os.getenv("jwt_key")
    if token:
        try:
            decode_token=jwt.decode(token,jwt_key,algorithms=["HS256"])
            order=order_model.order(orderNumber)
            if order==None:
                data={
                    "data":None,
                }
                response=make_response(jsonify(data))
                response.headers["Access-Control-Allow-Origin"] = "*" 
                return response
            elif order:
                image=order[4].split(" ")
                image=image[0]
                data={
                    "data": {
                        "number":order[0],
                        "price":order[7],
                        "trip": {
                            "attraction": {
                                "id":order[1],
                                "name":order[2],
                                "address":order[3],
                                "image":image
                            },
                            "date":order[5],
                            "time":order[6]
                        },
                        "contact": {
                            "name":order[9],
                            "email":order[10],
                            "phone":order[11]
                        },
                        "status":order[8]
                    }
                }
                response=make_response(jsonify(data))
                response.headers["Access-Control-Allow-Origin"] = "*" 
                return response
            else:
                data={
                    "error":True,
                    "message":"伺服器內部錯誤"
                }
                response=make_response(jsonify(data))
                response.headers["Access-Control-Allow-Origin"] = "*" 
                return response,500
        except:
            data={
                "error":True,
                "message":"未登入系統，拒絕存取"
            }
            response=make_response(jsonify(data))
            response.headers["Access-Control-Allow-Origin"] = "*" 
            return response,403
    else:
        data={
            "error":True,
            "message":"未登入系統，拒絕存取"
        }
        response=make_response(jsonify(data))
        response.headers["Access-Control-Allow-Origin"] = "*" 
        return response,403