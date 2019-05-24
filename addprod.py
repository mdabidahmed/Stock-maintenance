#!C:/python34/python
import cgi
import mysql.connector
print("Content-type: text/html")
print("")


form=cgi.FieldStorage()

cn=form.getvalue("cat_name");

ct=form.getvalue("cat_type");

pn=form.getvalue("prod_name");

pp=form.getvalue("prod_price");

pd=form.getvalue("prod_descri");

pi=form.getvalue("prod_img");



cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='stock')
cursor=cnx.cursor()
cursor.execute("""
    INSERT INTO product VALUES (%s, %s, %s, %s, %s, %s)""", (cn, ct, pn, pp, pd, pi))
print("<script>alert('Inserted')</script>")
cnx.commit()
cnx.close()
