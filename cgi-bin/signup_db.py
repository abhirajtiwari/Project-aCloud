#!/usr/bin/python3
import cgitb
import cgi
import pymysql
import webbrowser
import time
cgitb.enable()

form = cgi.FieldStorage()

database = pymysql.connect(
	host = "localhost",
	db = "Project_aCloud",
	user = "root",
	passwd = "your_password")
c = database.cursor()

print ("Content-type: text/html")
print()

fst_name = form['first_name'].value
lst_name = form['last_name'].value
username = form['user_name'].value
password = form['password_create'].value
password_c = form['password_confirm'].value
insert = "INSERT INTO users (usr_name,usr_password,f_name,l_name,signup_date) VALUES (%s,%s,%s,%s,CURDATE())"
data_to_be_inserted = (username,password,fst_name,lst_name)
success = """<body>Username registered successfully!...<br>
<a href = "http://192.168.1.222/cgi-bin/login.py">Login</a><br>
<a href = "http://192.168.1.222">Homepage</a></body>"""
create_inbox_sql = 'CREATE TABLE '+username+' (compose_date DATE NOT NULL, compose_time TIME NOT NULL,subject VARCHAR(120), message TEXT, status VARCHAR(1) NOT NULL)'
#data_tobeinserted_in_create_inbox = (username)
#final_inbox_stmt = create_inbox_sql % (data_tobeinserted_in_create_inbox)

c.execute("SELECT * FROM users")
data = c.fetchall()
already_exists = False
for row in data:
	if row[0] == username:
		already_exists = True
	else:
		pass

def main():
	c.execute(insert,data_to_be_inserted)

def main2():
	#drop_stmt = "DROP TABLE IF ALREADY EXISTS %s"
	#data_drop_stmt = (username)
	#c.execute(drop_stmt,data_drop_stmt)
	#check rules for making a table like what you have to use etc
	c.execute(create_inbox_sql)
	print(success)
	database.commit()

if password != password_c:
	print("Passwords do not match... Press 'back' or 'backspace'...")
	#time.sleep(10)
	#webbrowser.open("http://192.168.1.222/cgi-bin/signup.py")
	database.close()
elif already_exists == True:
	print("This username already exists...Press 'back' or 'backspace'...")
	#time.sleep(10)
	#webbrowser.open("http://192.168.1.222/cgi-bin/signup.py")
	database.close()
else:
	main()
	main2()
	database.close()
