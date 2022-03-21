from flask import *
from model.user import user_model
import json
from flask_bcrypt import bcrypt
# import jwt
# from routes.token import make_token

api_user=Blueprint("api_user",__name__,static_folder="static",template_folder="templates")

@api_user.route("/api/user",methods=["GET","POST","PATCH","DELETE"])
def user():
    session["email"]==None
    if request.method=="GET":
        if session["email"]:
            user=user_model.login(session["email"])
            data={
                "data":{
                    "id": user[0],
                    "name": user[1],
                    "email": user[2]
                }
            }
            response=make_response(jsonify(data))
            response.headers["Access-Control-Allow-Origin"] = "*" 
            return response
        else:
            data={
                "data":None
            }
            response=make_response(jsonify(data))
            response.headers["Access-Control-Allow-Origin"] = "*" 
            return response

    elif request.method=="POST":
        user_data=request.get_json()
        user=user_model.login(user_data["email"])
        if user:
            if user_data["name"]=="" or user_data["password"]=="":
                data={
                    "error": True,
                    "message": "請輸入姓名、電子郵件和密碼"
                }
                response=make_response(jsonify(data))
                response.headers["Access-Control-Allow-Origin"] = "*" 
                return response,400
            else:
                data={
                    "error": True,
                    "message": "註冊失敗，此電子信箱已被註冊"
                }
                response=make_response(jsonify(data))
                response.headers["Access-Control-Allow-Origin"] = "*" 
                return response,400
        elif user=="error":
            data={
                "error": True,
                "message": "伺服器內部錯誤"
            }
            response=make_response(jsonify(data))
            response.headers["Access-Control-Allow-Origin"] = "*" 
            return response,500
        elif user==None:
            if user_data["name"]=="" or user_data["email"]=="" or user_data["password"]=="":
                data={
                    "error": True,
                    "message": "請輸入姓名、電子郵件和密碼"
                }
                response=make_response(jsonify(data))
                response.headers["Access-Control-Allow-Origin"] = "*" 
                return response,400
            else:
                hash_password=bcrypt.hashpw(user_data["password"].encode("utf-8"),bcrypt.gensalt()) #雜湊密碼
                register=user_model.register(user_data["name"],user_data["email"],hash_password)
                data={"ok": True}
                # token=make_token(user_data["email"])
                response=make_response(jsonify(data))
                response.headers["Access-Control-Allow-Origin"] = "*" 
                return response
                # return jsonify({"message":"User created","token":token})
    
    elif request.method=="PATCH":
        user_data=request.get_json()
        user=user_model.login(user_data["email"])
        if user:
            if  user_data["email"]==user[2] and bcrypt.checkpw(user_data["password"].encode("utf-8"),user[3].encode("utf-8")):
                data={"ok": True}
                session["email"]=user[2]
                # token=make_token(user[2])
                response=make_response(jsonify(data))
                response.headers["Access-Control-Allow-Origin"] = "*" 
                return response
                # return jsonify({"message":"Authorize success","token":token})
            elif user_data["password"]=="":
                data={
                    "error": True,
                    "message": "請輸入電子信箱和密碼"
                }
                response=make_response(jsonify(data))
                response.headers["Access-Control-Allow-Origin"] = "*" 
                return response,400
            else:
                data={
                    "error": True,
                    "message": "登入失敗，電子信箱或密碼輸入錯誤"
                }
                response=make_response(jsonify(data))
                response.headers["Access-Control-Allow-Origin"] = "*" 
                return response,400
        elif user=="error":
            data={
                "error": True,
                "message": "伺服器內部錯誤"
            }
            response=make_response(jsonify(data))
            response.headers["Access-Control-Allow-Origin"] = "*" 
            return response,500
        elif user==None:
            if user_data["email"]=="" or user_data["password"]=="":
                data={
                    "error": True,
                    "message": "請輸入電子信箱和密碼"
                }
                response=make_response(jsonify(data))
                response.headers["Access-Control-Allow-Origin"] = "*" 
                return response,400
            else:
                data={
                    "error": True,
                    "message": "登入失敗，電子信箱或密碼輸入錯誤"
                }
                response=make_response(jsonify(data))
                response.headers["Access-Control-Allow-Origin"] = "*" 
                return response,400
                
    elif request.method=="DELETE":
        session["email"]=None
        data={"ok": True}
        response=make_response(jsonify(data))
        response.headers["Access-Control-Allow-Origin"] = "*" 
        return response

