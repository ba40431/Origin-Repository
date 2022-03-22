from flask import *
import jwt
import time

class UseJWT:
    def make_token(self,id,name,email):
        key="secretkey"
        now=time.time()
        expiretime=60*60
        payload={
            "id":id,
            "name":name,
            "email":email,
            "expire":now+expiretime
        }
        token=jwt.encode(payload,key,algorithm="HS256")
        return token
    def get_cookie(self):
        jwt=request.cookies.get('token')
        return jwt

use_jwt=UseJWT()