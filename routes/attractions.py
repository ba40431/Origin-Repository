from flask import *
import json
from model.attractions import attractions_model,keyword_attractions_model
import re

api_attractions=Blueprint("api_attractions",__name__,static_folder="static",template_folder="templates")

@api_attractions.route("/api/attractions")
def attractions():
    page=request.args.get("page",0,type=int)
    keyword=request.args.get("keyword")

    if keyword:
        attractions_list=[]
        attractions=keyword_attractions_model.get_keyword_attractions(keyword,page)
        count=keyword_attractions_model.get_keyword_count(keyword)
        for attraction in attractions:
            spot_images=attraction[9].split('https://')
            images_list=[]
            for spot_image in spot_images:
                if re.compile('jpg|JPG|png|PNG$').search(spot_image):
                    images_list.append('https://'+spot_image)            

            data={"id":attraction[0],
                "name":attraction[1],
                "category":attraction[2],
                "description":attraction[3],
                "address":attraction[4],
                "transport":attraction[5],
                "mrt":attraction[6],
                "latitude":attraction[7],
                "longitude":attraction[8],
                "images":images_list
                }
            attractions_list.append(data)

        if count[0]-12*page<=12:
            attractions_data={
                "nextPage":None,
                "data":attractions_list
            }
            response=make_response(jsonify(attractions_data),200)
        elif count[0]-12*page>12:
            attractions_data={
                "nextPage":page+1,
                "data":attractions_list
            }
            response=make_response(jsonify(attractions_data),200)
            return response    
        elif attractions=="error":
            attractions_data={
                "error": True,
                "message": "伺服器內部錯誤"
            }
            response=make_response(jsonify(attractions_data),500)
        elif count=="error":
            attractions_data={
                "error": True,
                "message": "伺服器內部錯誤"
            }
            response=make_response(jsonify(attractions_data),500)

    else:
        attractions=attractions_model.get_attractions(page)
        count=attractions_model.get_count()
        attractions_list=[]

        for attraction in attractions:
            spot_images=attraction[9].split('https://')
            images_list=[]
            for spot_image in spot_images:
                if re.compile('jpg|JPG|png|PNG$').search(spot_image):
                    images_list.append('https://'+spot_image)  

            data={"id":attraction[0],
                "name":attraction[1],
                "category":attraction[2],
                "description":attraction[3],
                "address":attraction[4],
                "transport":attraction[5],
                "mrt":attraction[6],
                "latitude":attraction[7],
                "longitude":attraction[8],
                "images":images_list
                }
            attractions_list.append(data)
        if count[0]-12*page>12:
            attractions_data={
                "nextPage":page+1,
                "data":attractions_list
            }
            response = make_response(jsonify(attractions_data),200)
        elif count[0]-12*page<=12:
            attractions_data={
                "nextPage":None,
                "data":attractions_list
            }
            response = make_response(jsonify(attractions_data),200)
        elif attractions=="error":
            attractions_data={
                "error": True,
                "message": "伺服器內部錯誤"
            }
            response = make_response(jsonify(attractions_data),500)
        elif count=="error":
            attractions_data={
                "error": True,
                "message": "伺服器內部錯誤"
            }
            response = make_response(jsonify(attractions_data),500)

    return response
