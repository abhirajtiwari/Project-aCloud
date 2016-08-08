#!/usr/bin/python3
import cgitb
cgitb.enable()

print("Content-type: text/html")
print()
print("""
<html>
<head>
	<title>
		aCloud | Login
	</title>
	<link rel = "stylesheet" type = "text/css" href = "http://192.168.1.222/css/login.css">
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
			<form action = "inbox.py" method = "post">
				<label for = "usrname">Username: </label><br>
				<input type = "text" id = "usrname" name = "username"><br>
				<label for = "pswd">Password: </label><br>
				<input type = "password" id = "pswd" name = "password"><br>
				<input type = "submit" value = "Login">
			</form>
		</div>
	</div>
</div>
</div>
<footer id = "footer">
	&copy;2016, Abhiraj Tiwari. All Rights Reserved
</footer>
</body>
</html>""")
