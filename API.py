from flask import Flask,redirect,url_for,request,render_template
import json

reg_database="DATABASE\REGISTER.JSON"

app = Flask(__name__)


   
#111111111111111111111111111111111111111111111111111111111

#PYTHON SIGN IN APP

#DISPLAY ROUTES

@app.route("/home_page")
def home():
	return render_template("homepage.html")

@app.route("/registeration_page")
def registeration():
	return render_template("register.html")


@app.route('/signin_page')
def signin_func():
	return render_template("signin.html")


#FUNCTION ROUTES

@app.route("/register",methods=['POST','GET'])
def register_database():
	item_data={}
	with open(reg_database,"r") as file:
		temp=json.load(file)
		
	item_data["username"]=request.form["usersname"]
	item_data["userpassword"]=request.form["userspassword"]

	temp.append(item_data)
	with open(reg_database,"w") as file:
		json.dump(temp,file,indent=4)
	
	return render_template("signin.html")

	

@app.route('/signin',methods = ['POST', 'GET'])
def signin():
   if request.method == 'POST' and len(request.form['username'])>0 and len(request.form['userpassword'])>=5:
	   name = request.form['username']
	   password = request.form['userpassword']
	   return render_template('signinoutput.html',namein=name,passin=password)
   else:
	   return render_template('signinerror.html')
	   
	   


if __name__ == "__main__":
	app.run(debug=True)



