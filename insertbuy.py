#!C:/python34/python
import cgi
import mysql.connector
print("Content-type: text/html")
print("")


form=cgi.FieldStorage()

cn=form.getvalue("uname");

ct=form.getvalue("email");

pn=form.getvalue("pname");

pp=form.getvalue("pqty");

pd=form.getvalue("addr");

pi=form.getvalue("contact");



cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='stock')
cursor=cnx.cursor()
cursor.execute("""
    INSERT INTO buyer VALUES (%s, %s, %s, %s, %s, %s)""", (cn, ct, pn, pp, pd, pi))
print("<script>alert('Inserted')</script>")
cnx.commit()
cnx.close()
