from flask import *
import json
from model.booking import booking_model
from flask_bcrypt import bcrypt
import jwt
from routes.token import use_jwt
from datetime import datetime,date
import os
from dotenv import load_dotenv

load_dotenv(".env")

get_booking=Blueprint("get_booking",__name__,static_folder="static",template_folder="templates")
post_booking=Blueprint("post_booking",__name__,static_folder="static",template_folder="templates")
delete_booking=Blueprint("delete_booking",__name__,static_folder="static",template_folder="templates")


@get_booking.route("/api/booking",methods=["GET"])
def get():
    token=use_jwt.get_token()
    booking_data=request.get_json()
    jwt_key=os.getenv("jwt_key")
    if token:
        try:
            decode_token=jwt.decode(token,jwt_key,algorithms=["HS256"])
            booking=booking_model.booking_data(decode_token["id"])
            if booking:
                image=booking[3].split(" ")
                image=image[0]
                data={
                    "data":{
                        "attraction":{
                            "id":booking[0],
                            "name":booking[1],
                            "address":booking[2],
                            "image":image
                        },
                        "date":booking[4],
                        "time":booking[5],
                        "price":booking[6]
                    }
                }
                response=make_response(jsonify(data),200)
            elif booking=="error":
                data={
                    "error":True,
                    "message":"伺服器內部錯誤"
                }
                response=make_response(jsonify(data),500)
            else:
                data={
                    "data":None,
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

@post_booking.route("/api/booking",methods=["POST"])
def post():
    token=use_jwt.get_token()
    booking_data=request.get_json()
    jwt_key=os.getenv("jwt_key")
    day=datetime.strptime(booking_data["date"], "%Y-%m-%d")
    if token:
        if day>datetime.now():
            if booking_data["time"]=="morning" or booking_data["time"]=="afternoon":
                try:
                    decode_token=jwt.decode(token,jwt_key,algorithms=["HS256"])
                    reserved=booking_model.check_booking(decode_token["id"])
                    if reserved:
                        booking=booking_model.update_booking(booking_data["attractionId"],booking_data["date"],booking_data["time"],booking_data["price"],decode_token["id"])
                        data={
                            "ok":True
                        }
                        response=make_response(jsonify(data),200)
                    elif reserved==None:
                        booking=booking_model.booking(booking_data["attractionId"],booking_data["date"],booking_data["time"],booking_data["price"],decode_token["id"],decode_token["email"])
                        data={
                            "ok":True
                        }
                        response=make_response(jsonify(data),200)
                    elif reserved=="error":
                        data={
                            "error":True,
                            "message":"伺服器內部錯誤"
                        }
                        response=make_response(jsonify(data),500)
                    else:
                        data={
                            "error":True,
                            "message":"建立失敗，輸入不正確或其他原因"
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
                "message":"請輸入正確的日期與時間"
                }
                response=make_response(jsonify(data),400)
        else:
            data={
            "error":True,
            "message":"請輸入正確的日期與時間"
            }
            response=make_response(jsonify(data),400)
    else:
        data={
            "error":True,
            "message":"未登入系統，拒絕存取"
        }
        response=make_response(jsonify(data),403)

    return response

@delete_booking.route("/api/booking",methods=["DELETE"])
def delete():
    token=use_jwt.get_token()
    jwt_key=os.getenv("jwt_key")
    if token:
        try:
            decode_token=jwt.decode(token,jwt_key,algorithms=["HS256"])
            reserved=booking_model.check_booking(decode_token["id"])
            if reserved:
                delete=booking_model.delete_booking(decode_token["id"])
                if delete=="error":
                    data={
                        "error":True,
                        "message":"伺服器內部錯誤"
                    }
                    response=make_response(jsonify(data),500)
                else:
                    data={
                    "ok":True
                    }
                    response=make_response(jsonify(data),200)
            elif reserved=="error":
                data={
                    "error":True,
                    "message":"伺服器內部錯誤"
                }
                response=make_response(jsonify(data),500)
            else:
                data={
                    "error":True,
                    "message":"未登入系統，拒絕存取"
                }
                response=make_response(jsonify(data),403)
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