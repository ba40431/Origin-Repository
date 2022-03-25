from flask import *
import json
# from model.booking import booking_model

get_booking=Blueprint("get_booking",__name__,static_folder="static",template_folder="templates")
post_booking=Blueprint("post_booking",__name__,static_folder="static",template_folder="templates")
delete_booking=Blueprint("delete_booking",__name__,static_folder="static",template_folder="templates")

# @get_booking.route("/api/booking",methods=["GET"])
# def get():

#     date={
#         "data":{
#             "attraction":{
#                 "id":,
#                 "name":,
#                 "address":,
#                 "image":
#             },
#             "date":,
#             "time":,
#             "price":
#         }
#     }

#     data={
#         "error":True,
#         "message":"自訂的錯誤訊息"
#     }

# @post_booking.route("/api/booking",methods=["POST"])
# def post():

#     data={
#         "ok":True
#     }

#     data={
#         "error":True,
#         "message":"自訂的錯誤訊息"
#     }

# @delete_booking.route("/api/booking",methods=["DELETE"])
# def delete():

#     data={
#         "ok":True
#     }

#     data={
#         "error":True,
#         "message":"自訂的錯誤訊息"
#     }