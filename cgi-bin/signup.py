#!/usr/bin/python3
import cgitb
cgitb.enable()

print("Content-type: text/html")
print()

print("""
<html>
<head>
	<title>
		aCloud | Signup
	</title>
	<link rel = "stylesheet" type = "text/css" href = "http://192.168.1.222/css/signup.css">	 	
</head>

<body>

<header id = "heading">
<div>
<h1>aCloud</h1>
</header>

<div id = "page">
<div id = "box">
	<div id = "text">
		<div id="form">
			<form action = "signup_db.py" method = POST>
				<div>
				<div style  = "float:left;width:49%;">
					<label for = "1stname">First Name: </label><br>
					<input type = "text" id = "1stname" name = "first_name">
				</div>
				<div style  = "float:right;width:49%;">
					<label for = "lastname">Last Name: </label><br>
					<input type = "text" id = "lastname" name = "last_name">
				</div>
				</div>
				
				<div>
					<label for = "usrname">Choose a username: </label><br>
					<input type = "text" id  = "usrname" name = "user_name">
				</div>
				
				<div>
					<label for = "pswd_create">Create a password: </label><br>
					<input type = "password" id = "pswd_create" name = "password_create">
				</div>
				
				<div>
					<label for = "pswd_confirm">Confirm password: </label><br>
					<input type = "password" id = "pswd_confirm" name = "password_confirm">
				</div>
				<!-- you can add birthday, gender, mobile phone, location, current email addr.-->
				<input type = "submit" value = "Create">
			</form>
		</div>
	</div>
</div>
</div>
<footer id = "footer">
	&copy;2016, Abhiraj Tiwari. All Rights Reserved
</footer>
</body>
</html>
""")
