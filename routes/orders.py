from flask import *
import json
from flask_bcrypt import bcrypt
import jwt
from routes.token import use_jwt
# from model.orders import orders_model

api_orders=Blueprint("api_orders",__name__,static_folder="static",template_folder="templates")

@api_orders.route("/api/orders",methods=["POST"])
def orders():
    token=use_jwt.get_token()
    booking_data=request.get_json()
    jwt_key="secretkey"
    try:
        decode_token=jwt.decode(token,jwt_key,algorithms=["HS256"])
        data={
            "data": {
                "number": "20210425121135",
                "payment": {
                "status": 0,
                "message": "付款成功"
                }
            }
            }
        response=make_response(jsonify(data))
        response.headers["Access-Control-Allow-Origin"] = "*" 
        return response,200
    except:
        data={
            "error":True,
            "message":"未登入系統，拒絕存取"
        }
        response=make_response(jsonify(data))
        response.headers["Access-Control-Allow-Origin"] = "*" 
        return response,403