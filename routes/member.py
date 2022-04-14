from flask import *
import json
from model.member import member_model
from flask_bcrypt import bcrypt
import re
import jwt
from routes.token import use_jwt
import os
from dotenv import load_dotenv

load_dotenv(".env")

member_orders=Blueprint("member_orders",__name__,static_folder="static",template_folder="templates")
member_update=Blueprint("member_update",__name__,static_folder="static",template_folder="templates")

@member_orders.route("/api/member",methods=["GET"])
def get_member():
    token=use_jwt.get_token()
    jwt_key=os.getenv("jwt_key")
    if token:
        try:
            decode_token=jwt.decode(token,jwt_key,algorithms=["HS256"])
            orders=member_model.get_orders(decode_token["email"])
            if orders:
                orders_list=[]
                for order in orders:
                    orders_data={
                            "number":order[1],
                            "attractionName":order[3],
                            "date":order[4],
                            "price":order[6]
                    }
                    orders_list.append(orders_data)

                data={
                    "data":orders_list
                }

                response=make_response(jsonify(data),200)
            elif orders=="error":
                data={
                    "error": True,
                    "message": "伺服器內部錯誤"
                }
                response=make_response(jsonify(data),500)
            else:
                data={
                    "data":None
                }
                response=make_response(jsonify(data),200)

        except:
            data={
                "error":True,
                "message":"未登入系統，拒絕存取"
            }
            response=make_response(jsonify(data),403)
    else:
        data={
            "error":True,
            "message":"未登入系統，拒絕存取"
        }
        response=make_response(jsonify(data),403)

    return response

@member_update.route("/api/member",methods=["PATCH"])
def update_password():
    token=use_jwt.get_token()
    user_data=request.get_json()
    password_pattern="^[0-9a-zA-Z_]+$"
    jwt_key=os.getenv("jwt_key")
    if token:
        try:
            decode_token=jwt.decode(token,jwt_key,algorithms=["HS256"])
            if re.match(password_pattern,user_data["password"]):
                hashed_password=bcrypt.hashpw(user_data["password"].encode("utf-8"),bcrypt.gensalt()) #雜湊密碼
                update_user=member_model.update_password(hashed_password,decode_token["email"])
                if update_user=="error":
                    data={
                        "error": True,
                        "message": "伺服器內部錯誤"
                    }
                    response=make_response(jsonify(data),500)
                elif update_user==None:
                    data={"ok": True}
                    response=make_response(jsonify(data),200)
                else:
                    data={
                        "error": True,
                        "message": "更新密碼失敗"
                    }
                    response=make_response(jsonify(data),400)
            elif user_data["password"]=="":
                data={
                    "error": True,
                    "message": "請輸入密碼"
                }
                response=make_response(jsonify(data),400)

        except:
            data={
                "error":True,
                "message":"未登入系統，拒絕存取"
            }
            response=make_response(jsonify(data),403)
    else:
        data={
            "error":True,
            "message":"未登入系統，拒絕存取"
        }
        response=make_response(jsonify(data),403)

    return response


