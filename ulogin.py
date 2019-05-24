#!C:/python34/python
import cgi
import mysql.connector
print("Content-type: text/html")
print("")

a=0;
form=cgi.FieldStorage()

e=form.getvalue("username");

p=form.getvalue("pass");
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='stock');
cursor=cnx.cursor()
cursor.execute("""
    SELECT * FROM reg where username=%s and pass=%s""",(e, p))
for row in cursor:
	a=1;
if(a==1):
	redirectURL = "http://localhost/Stock%20maintenance/userhome.html"
	print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
   
else:
   print("<script>alert('Username or Password Incoorect')</script>");
	