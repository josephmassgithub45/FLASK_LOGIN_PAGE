from flask import Flask,redirect,url_for,request,render_template

app = Flask(__name__)


   
#111111111111111111111111111111111111111111111111111111111

#PYTHON SIGN IN APP

@app.route('/signin_page')
def signin_func():
	return render_template("signin.html")


	

@app.route('/signin',methods = ['POST', 'GET'])
def signin():
   if request.method == 'POST':
	   name = request.form['username']
	   password = request.form['userpassword']
	   return render_template('signinoutput.html',namein=name,passin=password)



if __name__ == "__main__":
	app.run(debug=True)



