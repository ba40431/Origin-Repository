from flask import *
import json
from flask_bcrypt import bcrypt
import jwt
from routes.token import use_jwt
import time
from datetime import date
import urllib.request as req
import os
import re
from dotenv import load_dotenv
from model.orders import orders_model

load_dotenv(".env")


api_orders=Blueprint("api_orders",__name__,static_folder="static",template_folder="templates")

@api_orders.route("/api/orders",methods=["POST"])
def orders():
    token=use_jwt.get_token()
    booking_data=request.get_json()
    jwt_key=os.getenv("jwt_key")
    phone_pattern="^09[0-9]{8}$"
    if token:
        if re.match(phone_pattern,booking_data["order"]["contact"]["phone"]):
            try:
                decode_token=jwt.decode(token,jwt_key,algorithms=["HS256"])
                number=str(int(time.time()))+"-"+str(decode_token["id"]) #訂單號碼
                orders=orders_model.new_orders(
                    number,
                    booking_data["order"]["trip"]["attraction"]["id"],
                    booking_data["order"]["trip"]["attraction"]["name"],
                    booking_data["order"]["trip"]["date"],
                    booking_data["order"]["trip"]["time"],
                    booking_data["order"]["price"],
                    booking_data["order"]["contact"]["name"],
                    booking_data["order"]["contact"]["email"],
                    booking_data["order"]["contact"]["phone"]
                    )
                if orders==None:
                    tappay_api="https://sandbox.tappaysdk.com/tpc/payment/pay-by-prime"
                    tappay_headers={
                        "Content-Type":"application/json",
                        "x-api-key":os.getenv("partner_key")
                    }
                    tappay_data={
                        "prime":booking_data["prime"],
                        "partner_key":os.getenv("partner_key"),
                        "merchant_id":os.getenv("merchant_id"),
                        "details":"Taipei Trip 台北一日遊",
                        "amount": booking_data["order"]["price"],
                        "cardholder": {
                            "phone_number":booking_data["order"]["contact"]["phone"],
                            "name":booking_data["order"]["contact"]["name"],
                            "email":booking_data["order"]["contact"]["email"],
                        },
                        "remember": True
                    }
                    tappay_request=req.Request(tappay_api,method="POST",headers=tappay_headers,data=json.dumps(tappay_data).encode("utf-8"))
                    with req.urlopen(tappay_request) as response:
                        result=response.read().decode("utf-8")
                    result=json.loads(result)
                    print(result["status"],result["msg"])
                    if result["status"]==0 and result["msg"]=="Success":
                        status=orders_model.update_status(number)
                        if status==None:
                            delete_booking=orders_model.delete_booking(booking_data["order"]["contact"]["email"])
                            if delete_booking=="error":
                                    data={
                                        "error":True,
                                        "message":"伺服器內部錯誤"
                                    }
                                    response=make_response(jsonify(data),500)
                            else:
                                data={
                                    "data": {
                                        "number":number,
                                        "payment": {
                                            "status": 1,
                                            "message": "付款成功"
                                        }
                                    }
                                }
                                response=make_response(jsonify(data),200)
    
                        elif status=="error":
                            data={
                                "error":True,
                                "message":"伺服器內部錯誤"
                            }
                            response=make_response(jsonify(data),500)
                        else:
                            data={
                                "data": {
                                    "number":number,
                                    "payment": {
                                        "status": 0,
                                        "message": "付款失敗"
                                    }
                                }
                            }
                            response=make_response(jsonify(data),400)
                    else:
                        data={
                            "data": {
                                "number":number,
                                "payment": {
                                    "status": 0,
                                    "message": "付款失敗"
                                }
                            }
                        }
                        response=make_response(jsonify(data),400)
                elif orders=="error":
                    data={
                        "error":True,
                        "message":"伺服器內部錯誤"
                    }
                    response=make_response(jsonify(data),500)
                else:
                    data={
                        "error":True,
                        "message":"訂單建立失敗，輸入不正確或其他原因"
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
                "message":"請填寫正確的手機號碼格式"
            }
            response=make_response(jsonify(data),400)
    else:
        data={
            "error":True,
            "message":"未登入系統，拒絕存取"
        }
        response=make_response(jsonify(data),403)

    return response