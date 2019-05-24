#!C:/python34/python
import cgi
import mysql.connector
print("Content-type: text/html")
print("")


form=cgi.FieldStorage()

e=form.getvalue("email");

p=form.getvalue("pass");
if e=="admin@gmail.com" and p=="admin":
	redirectURL = "http://localhost/Stock%20maintenance/adminhome.html"
	print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
   
else:
   print("<script>alert('Username or Password Incoorect')</script>");