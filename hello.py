from flask import Flask,redirect,url_for,request,render_template

app = Flask(__name__)

#11111111111111111111111111111111111111111111111111111

@app.route("/")
def hello_world():
		return "HELLO THIS IS FLASK"

#111111111111111111111111111111111111111111111111111111

@app.route("/name")
def hello_globe():
		return "THE NAME IS FLASK"

#111111111111111111111111111111111111111111111111111111

@app.route("/test")
def hello_test():
		return "JUST TESTING"

#111111111111111111111111111111111111111111111111111111

@app.route("/greeting/<name>")
def my_greeting(name):
		return "Hello %s" % name

#111111111111111111111111111111111111111111111111111111

@app.route("/intnumber/<int:num>")
def int_function(num):
	return "The Int Number Entered is :%d " % num

#1111111111111111111111111111111111111111111111111111111

@app.route("/floatnumber/<float:num>")
def float_function(num):
	return "The Float Number Entered Is : %f " % num

#1111111111111111111111111111111111111111111111111111111

@app.route('/admin')
def greet_admin():
	return 'Hello Admin'

@app.route('/guest/<g_name>')
def greet_guest(g_name):
	return 'Hello %s you are a guest.'%g_name


@app.route('/user/<name>')
def greet_user(name):
	if name == 'admin':
		return redirect(url_for('greet_admin'))
	else:
		return redirect(url_for('greet_guest',g_name=name))


#11111111111111111111111111111111111111111111111111111111

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

#11111111111111111111111111111111111111111111111111111111

@app.route('/template')
def index():
   return '<html><body><h1 style="color:blue;">Hello world</h1></body></html>'

@app.route('/hello/<user>')
def hello_name(user):
	return render_template("hello.html", name=user)

name

if __name__ == "__main__":
	app.run(debug=True)



