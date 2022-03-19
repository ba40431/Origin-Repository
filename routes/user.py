from flask import *
from model.user import user_model
import json

api_user=Blueprint("api_user",__name__,static_folder="static",template_folder="templates")

@api_user.route("/api/user")
def user():
    return 