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

to = form['to'].value
subject = form['subject'].value
message = form['message'].value
username = form['username'].value
first_name = form['first_name'].value

#c.execute("SELECT * FROM users")
#data2 = c.fetchall()
#for entry in data2:
#	if entry[0] == username:
#		first_name = entry[2]
#		break
#	else:
#		pass



subject_me = "Sent: "+subject
subject_sent = subject+' - '+first_name

c.execute("SELECT * FROM users")
data = c.fetchall()
exists = False
for row in data:
	if row[0] == to:
		c.execute("""INSERT INTO  """+username+""" VALUES (CURDATE(),CURTIME()," """+subject_me+""" "," """+message+""" ",0)""")
		database.commit()
		c.execute("""INSERT INTO """+to+""" VALUES (CURDATE(),CURTIME()," """+subject_sent+""" "," """+message+""" ",0)""")
		database.commit()
		exists = True
		break
	else:
		exists = False

if exists == False:
	print ("Reciever's address does not exist... Try again")
	database.close()
else:
	print('Message sent successfully... <a href = "javascript:history.go(-2)">Continue</a>')
	database.close()
