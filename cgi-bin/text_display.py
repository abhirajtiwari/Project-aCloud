#!/usr/bin/python3
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

message = form['message'].value
#subject = form['sub'].value

html = """<html>
<head>
	<title>
		Mail
	</title>
	<link rel = "stylesheet" type = "text/css" href = "http://192.168.1.222/css/login.css">
</head>

<body>

<header id = "heading">
<div>
<h1>aCloud</h1>
</header>"""+message+"""<footer id = "footer">
	&copy;2016, Abhiraj Tiwari. All Rights Reserved
</footer>
</body>
</html>"""

print("Content-type: text/html")
print()
print(html)
