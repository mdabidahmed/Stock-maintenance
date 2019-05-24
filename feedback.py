#!C:/python34/python
import cgi
import mysql.connector
print("Content-type: text/html")
print("")


form=cgi.FieldStorage()

cn=form.getvalue("uname");

ct=form.getvalue("sub");

pn=form.getvalue("desc");

pp=form.getvalue("rate");




cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='stock')
cursor=cnx.cursor()
cursor.execute("""
    INSERT INTO feedback VALUES (%s, %s, %s, %s)""", (cn, ct, pn, pp))
print("<script>alert('Inserted')</script>")
cnx.commit()
cnx.close()
