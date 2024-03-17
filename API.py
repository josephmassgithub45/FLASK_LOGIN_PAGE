from re import I
from flask import Flask,redirect,url_for,request,render_template,session
import json
from flask_socketio import join_room,leave_room,send,SocketIO
import random
from string import ascii_uppercase



app = Flask(__name__)
app.config["SECRET_KEY"] = "blueflaskchat"
socketio = SocketIO(app)



'''
server="http://127.0.0.1:5000" 
'''

#111111111111111111111111111111111111111111111111111111111

#CREATION OF DATABASE

reg_database="DATABASE\REGISTER.JSON"


#---------------------CHAT APP DEVELOPMENT------------------
rooms={}

def generate_unique_code(length):
	while True:
		code = ""
		for _ in range(length):
			code += random.choice(ascii_uppercase)
		
		if code not in rooms:
			break
		
	return code

@app.route("/",methods=["POST","GET"])
def test():
	session.clear()
	if request.method=="POST":
		name=request.form.get("name")
		code=request.form.get("code")
		join=request.form.get("join",False)
		create=request.form.get("create",False)
		
		if not name:
			return render_template("home.html",error="Please enter a name.",code=code,name=name)
		
		if join != False and not code:
			return render_template("home.html",error="Please enter a room code.",code=code,name=name)
		
		room = code
		
		if create != False:
			room = generate_unique_code(4)
			rooms["room"] = {"members":0,"messages":[]}
		
		elif code not in rooms:
			return render_template("home.html",error="Room does not exist",code=code,name=name)
		
		session["room"] = room
		session["name"] = name
		
		return redirect(url_for("room"))
	return render_template("home.html")

@app.route("/room")
def room():
	return render_template("room.html")

#----------------------TEMPLATE ROUTES----------------------

@app.route("/code_entry") 
def entry():
	return render_template("index.html")

@app.route("/home_page")
def home():
	return render_template("homepage.html")

@app.route("/registration_page")
def registeration():
	return render_template("register.html")


@app.route('/signin_page')
def signin_func():
	return render_template("signin.html")

@app.route("/signin_to_registration")
def signregister():
	return render_template("register.html")


#----------------------FUNCTION ROUTES---------------------

'''
@app.route("/homepage",methods=['POST','GET'])
def home_database():
'''

@app.route("/register",methods=['POST','GET'])
def register_database():
	if request.method == 'POST' and len(request.form['username'])>0 and len(request.form['contact'])>0 and len(request.form['firstname'])>0 and len(request.form['lastname'])>0 and len(request.form['gender'])>0 and len(request.form['email'])>0:
		if len(request.form['userpassword'])>=7: 
			item_data={}
			with open(reg_database,"r") as file:
				temp=json.load(file)
		
			item_data["FIRSTNAME"]=request.form["firstname"]
			item_data["MIDDLENAME"]=request.form["middlename"]
			item_data["LASTNAME"]=request.form["lastname"]
			item_data["GENDER"]=request.form["gender"]
			item_data["CONTACT"]=request.form["contact"]
			item_data["EMAIL"]=request.form["email"]
			item_data["USERNAME"]=request.form["username"]
			item_data["USERPASSWORD"]=request.form["userpassword"]

			temp["registration_data"].append(item_data)
			with open(reg_database,"w") as file:
				json.dump(temp,file,indent=4)
	
			#return temp["registeration_data"]
			return render_template("signin.html")
		else:
			return render_template("registrationpasserror.html")
	else:
		return render_template('registrationerror.html')


	

@app.route('/signin',methods = ['POST', 'GET'])
def signin():
	if request.method == 'POST' and len(request.form['username'])>0 and len(request.form['userpassword'])>6:
		with open(reg_database,"r") as file:
			temp=json.load(file)
		
		usernamein=request.form['username']
		userpasswordin=request.form['userpassword']
			
		index=0
		while index<len(temp.get("registration_data")):
			if usernamein==temp.get("registration_data")[index].get("USERNAME") and userpasswordin==temp.get("registration_data")[index].get("USERPASSWORD"):
				return render_template("startpage.html")
			index=index+1
		return render_template("startpageerror.html")
	
		
		'''
		username = temp[0]["username"]
		userpassword = temp[0]["userpassword"]
		return username+"-------"+userpassword
		'''
		
	else:
	   return render_template('signinerror.html')   




@app.route('/submit_code',methods = ['POST', 'GET'])
def submission():
	if request.method == 'POST' and len(request.form['code_entry'])>0:
		with open(reg_database,"r") as file:
			temp=json.load(file)

		codein=request.form['code_entry']
		
		index=0
		while index<len(temp.get("code_data")):
			if codein==temp.get("code_data")[index].get("CODE"):
				return render_template("homepage.html")
			index=index+1
		return render_template("code_entry_error.html")
	else:
		return render_template("code_entry_error.html")
	
if __name__ == "__main__":
	socketio.run(app,debug=True)


