from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

header = """
		<!DOCTYPE html>
		<html>
			<head>
				<title>User Signup Assignment</title>
			</head>
			<body>
				<h2>Signup</h2>
		"""

footer = """
			</body>
		</html>
		"""

@app.route("/")
def index():
	content = header + """
				<form action="/signup" method="post">
					<label for="username">Username 
					<input type="text" name="username" id="username" />
					</label>
					<input type="submit" value="Submit" />
				</form>
		""" + footer

	return content

@app.route("/signup", methods=["POST"])
def welcome_user():
	new_user = request.form["username"]
	content = header + new_user + footer
	return content

app.run()
