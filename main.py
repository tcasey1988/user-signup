from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/signup")
def index():
	return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def validate_form():
	username = request.form["username"]
	password = request.form["password"]
	verify = request.form["verify"]
	email = request.form["email"]

	user_error = ""
	password_error = ""
	verify_error = ""
	email_error = ""

	if username == "" or len(username) < 3 or len(username) > 20 or " " in username:
		user_error = "That's not a valid username"
		username = ""
	else:
		username = username

	if password == "" or len(password) < 3 or len(password) > 20 or " " in password:
		password_error = "That's not a valid password"
		password = ""
	else:
		password = password

	if verify != password or verify == "":
		verify_error = "Your passwords don't match"
		verify = ""
		password = ""
	else:
		verify = verify
	
	if email == "":
		email = ""
	else:
		if len(email) < 3 or len(email) > 20 or " " in email or "@" not in email or "." not in email:
			email_error = "That's not a valid email"
			email = ""
		else:
			email = email

	if user_error != "" or email_error != "":
		password = ""
		verify = ""

	if not user_error and not password_error and not verify_error and not email_error:
		return redirect("/welcome?username={0}".format(username))
	else:
		return render_template("signup.html", username=username, password=password, verify=verify,
							user_error=user_error, password_error=password_error, verify_error=verify_error,
							email=email, email_error=email_error)

@app.route("/welcome")
def welcome_user():
	user = request.args.get("username")
	escaped_user = cgi.escape(user)
	return render_template("welcome.html", escaped_user=escaped_user)
	
app.run()
