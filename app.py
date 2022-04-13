from flask import *
from routes.attractions import api_attractions
from routes.attraction import api_attraction
# ---------------使用session----------------
# from routes.user_session import get_user,post_user,patch_user,delete_user 
# import os
# from dotenv import load_dotenv

# load_dotenv(".env")
# -----------------使用JWT------------------
from routes.user_jwt import get_user,post_user,patch_user,delete_user 
from routes.booking import get_booking,post_booking,delete_booking
from routes.orders import api_orders
from routes.order import api_order
from routes.member import member_orders,member_update

app=Flask(__name__)
# app.secret_key=os.getenv("secret_key") #使用session
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True
app.register_blueprint(api_attractions)
app.register_blueprint(api_attraction)
app.register_blueprint(get_user)
app.register_blueprint(post_user)
app.register_blueprint(patch_user)
app.register_blueprint(delete_user)
app.register_blueprint(get_booking)
app.register_blueprint(post_booking)
app.register_blueprint(delete_booking)
app.register_blueprint(api_orders)
app.register_blueprint(api_order)
app.register_blueprint(member_orders)
app.register_blueprint(member_update)

# Pages
@app.route("/")
def index():
	return render_template("index.html")
@app.route("/attraction/<id>")
def attraction(id):
	return render_template("attraction.html")
@app.route("/booking")
def booking():
	return render_template("booking.html")
@app.route("/thankyou")
def thankyou():
	return render_template("thankyou.html")
@app.route("/member")
def member():
	return render_template("member.html")

app.run(host="0.0.0.0",port=3000)