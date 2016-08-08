#!/usr/bin/python3
import cgitb
import cgi
cgitb.enable()

form = cgi.FieldStorage()
username = form['username'].value
f_name = form['first_name'].value
print ("Content-type: text/html")
print()

print("""
<html>
	<head>
	<title>
		 Compose Mail
	</title>
	<link rel = "stylesheet" type = "text/css" href ="http://192.168.1.222/css/compose_mail.css">
	</head>
	
<body>
<header id = "heading">
	<div><h1>aCloud</h1></div>
</header>
<div>
	<form action = "javascript:history.go(-1)">
		<input id = "inbox" type = "submit" value = "Inbox" name = "inbox_btn">
	</form>
</div>	

<div class = "clearfix">
	<form action = "compose_mail_db.py" method = POST  id = "compose_form">
		<input type = "submit" id = "inbox" style = "float:left" value = "Send">
		<input type = "text"  placeholder = "To:  " name = "to">
		<input type = "text"  placeholder = "Subject:  " name = "subject">
		<input type = "hidden" value = " """+username+""" " name = "username">
		<input type = "hidden" value = " """+f_name+""" " name = "first_name">
	</form>
	<textarea cols = "100%" form = "compose_form" name = "message" placeholder = "Message..."></textarea>
</div>

<footer id = "footer">
	&copy;2016, Abhiraj Tiwari. All Rights Reserved
</footer>	
</body>
</html>
""")
