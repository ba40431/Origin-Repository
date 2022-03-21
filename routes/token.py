import jwt
import time

def make_token(email):
    key="secretkey"
    now=time.time()
    expiretime=60*60
    payload={
    "email":email,
    "expire":now+expiretime
    }
    return jwt.encode(payload,key,algorithm = 'HS256')