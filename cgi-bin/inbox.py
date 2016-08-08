#!/usr/bin/python3
import cgitb
import cgi
import pymysql
import webbrowser
cgitb.enable()

form = cgi.FieldStorage()
database = pymysql.connect(
		host = "localhost",
		db = "Project_aCloud",
		user = "root",
		passwd = "your_password")
c = database.cursor()

print("Content-type: text/html")
print()

username = form['username'].value
password = form['password'].value

c.execute("SELECT * FROM users")
data = c.fetchall()
exists = False
for row in data:
	if row[0] == username:
		if row[1] == password:
			f_name = row[2]
			exists = True	
	else:
		pass

def inbox_maker() :
	c.execute("SELECT * FROM "+username+" ORDER BY compose_date DESC")
	inbox = c.fetchall()
	inbox_lay = '<div class = "clearfix">'
	for row in inbox:
		inbox_lay += '''<form action = "text_display.py" method= POST>
		<input type = "hidden" value = "'''+row[3]+'''" name ="message">
		<input type = "submit" value = "'''+str(row[0])+" "+row[2]+'''" id = "unread"></form>'''
	return inbox_lay

html1 = """
<html>
	<head>
	<title>
		"""+f_name+""" | Inbox
	</title>
	
	<link rel = "stylesheet" type = "text/css" href ="http://192.168.1.222/css/inbox.css">
	</head>
	
<body>
<header id = "heading">
	<div><h1>aCloud</h1></div>
</header>
<div>
	<form action = "http://192.168.1.222/cgi-bin/compose_mail.py">
		<input id = "compose" type = "submit" value = "compose" name = "compose_btn">
		<input type = "hidden" value  = " """+username+""" " name = "username">
		<input type = "hidden" value = " """+f_name+""" " name= "first_name">
	</form>
</div>"""		

html3 = """
<footer id = "footer">
	&copy;2016, Abhiraj Tiwari. All Rights Reserved
</footer>
</body>
</html>
"""

html2 = inbox_maker() 

def main():
	print(html1,html2,html3)

if exists == True:
	main()
	database.close()
elif exists == False:
	print('Username / Password wrong... Please return')
	database.close()
else:
	print('Some error occured... Please try again...')
	database.close()
