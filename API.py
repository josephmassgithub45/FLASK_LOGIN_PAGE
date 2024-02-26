from flask import Flask,redirect,url_for,request,render_template
import json

reg_database="DATABASE\REGISTER.JSON"

app = Flask(__name__)

'''
server="http://127.0.0.1:5000"
'''
#111111111111111111111111111111111111111111111111111111111

#PYTHON SIGN IN APP

#----------------------DISPLAY ROUTES----------------------

@app.route("/home_page")
def home():
	return render_template("homepage.html")


@app.route("/registeration_page")
def registeration():
	return render_template("register.html")


@app.route('/signin_page')
def signin_func():
	return render_template("signin.html")


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

			temp["registeration_data"].append(item_data)
			with open(reg_database,"w") as file:
				json.dump(temp,file,indent=4)
	
			#return temp["registeration_data"]
			return render_template("signin.html")
		else:
			return render_template("registerationpasserror.html")
	else:
		return render_template('registerationerror.html')

	

@app.route('/signin',methods = ['POST', 'GET'])
def signin():
	if request.method == 'POST' and len(request.form['username'])>0:
		with open(reg_database,"r") as file:
			temp=json.load(file)
			
		
		user_name_h = request.form["username"]
		user_password_h = request.form["userpassword"]

		if user_name_h in temp["registeration_data"]:
			return "signed in"
		else:
			return "not signed in"
		
		'''
		username = temp[0]["username"]
		userpassword = temp[0]["userpassword"]
		return username+"-------"+userpassword
		'''
		
	else:
	   return render_template('signinerror.html')   


if __name__ == "__main__":
	app.run(debug=True)



