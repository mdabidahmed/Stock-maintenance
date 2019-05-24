#!C:/python34/python
import cgi
import mysql.connector
print("Content-type: text/html")
print("")

form=cgi.FieldStorage()

pn=form.getvalue("pname");

#print(pn)

cn=form.getvalue("cname");

#print(cn)

cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='stock');
if(cnx):
    print("");
cursor=cnx.cursor()
cursor.execute("""
    SELECT * FROM product where pname=%s""",(pn,))
for row in cursor:
	print(row[0])
print("""
<!DOCTYPE HTML>
<html>

<head>
  <title>Stock Maintenance</title>
  <meta name="description" content="website description" />
  <meta name="keywords" content="website keywords, website keywords" />
  <meta http-equiv="content-type" content="text/html; charset=windows-1252" />
  <link rel="stylesheet" type="text/css" href="style/style.css" />
</head>

<body>
  <div id="main">
    <div id="header">
      <div id="logo">
        <div id="logo_text">
          <!-- class="logo_colour", allows you to change the colour of the text -->
          <h1><a href="index.html">Controlling<span class="logo_colour">Stock Maintenance</span></a></h1>
         
        </div>
      </div>
      <div id="menubar">
        <ul id="menu">
          <!-- put class="selected" in the li tag for the selected page - to highlight which page you're on -->
          <li class="selected"><a href="userhome.html">Home</a></li>
          <li><a href="profile.html">My Profile</a></li>
          <li><a href="viewpro1.py">View Product</a></li>
          <li><a href="search.html">Search Product</a></li>
            <li><a href="feedback.html">Feedback</a></li>
		  <li><a href="index.html">Logout</a></li>
        </ul>
      </div>
    </div>
    <div id="content_header"></div>
    <div id="site_content">
      <div id="banner"></div>
	  <div id="sidebar_container">
        <div class="sidebar">
          <div class="sidebar_top"></div>
          <div class="sidebar_item">
            <!-- insert your sidebar items here -->
            <h3>Latest News</h3>
            <h4>New Stock Details Arrived</h4>
            <h5>February 1st, 2018</h5>
            <p>Effective and dynamic way to maintain a inventory details to reduce the man power<br /><a href="#">Read more</a></p>
          </div>
          <div class="sidebar_base"></div>
        </div>
        <div class="sidebar">
          <div class="sidebar_top"></div>
          <div class="sidebar_item">
            <h3>Useful Links</h3>
            <ul>
              <li><a href="http://www.gmail.com">Gmail</a></li>
              <li><a href="http://www.facebook.com">Facebook</a></li>
              <li><a href="http://www.twitter.com">Twitter</a></li>
              <li><a href="https://plus.google.com/discover">Google plus</a></li>
            </ul>
          </div>
          <div class="sidebar_base"></div>
        </div>
        <div class="sidebar">
          <div class="sidebar_top"></div>
          <div class="sidebar_item">
            <h3>Search</h3>
            <form method="post" action="#" id="search_form">
              <p>
                <input class="search" type="text" name="search_field" value="Enter keywords....." />
                <input name="search" type="image" style="border: 0; margin: 0 0 -9px 5px;" src="style/search.png" alt="Search" title="Search" />
              </p>
            </form>
          </div>
          <div class="sidebar_base"></div>
        </div>
      </div>
      <div id="content">
        <!-- insert the page content here -->
        <h1>Welcome to the Stock Maintenance</h1>
        <p>Welcome To User Home...
		</p>
        
       <form action="insertbuy.py" method="post">
<table id="x" align='center' cellspacing="10px" cellpadding="10px" style="border: 10px solid white;box-shadow:0px 0px 10px black">
<tr>
<td>User Name</td>
<td><input type="text" name="uname" id="name"></td>
</tr>

<tr>
<td>Email ID</td>
<td><input type="text" name="email" id="name"></td>
</tr>

<tr>
<td>Product Name</td>
<td><input type="text" name="pname" id="name"></td>
</tr>

<tr>
<td>Product Quantity</td>
<td><input type="text" name="pqty" id="name"></td>
</tr>

<tr>
<td>Delivery Address</td>
<td><textarea cols='22' rows='10' name="addr"></textarea></td>
</tr>

<tr>
<td>Contact Number</td>
<td><input type="text" name="contact" id="name"></td>
</tr>

<td><input type="submit" name="submit" id="submit"></td>
</tr>
</table>
      </div>
    </div>
    <div id="content_footer"></div>
    <div id="footer">
       <p><a href="adminhome.html">Home</a> | <a href="addpro.html">Add Product</a> | <a href="viewpro.py">View Product</a> | <a href="viewuser.py">View User</a> | <a href="index.html">Logout</a></p>
      <p>Copyright &copy; <a href="www.techciti.in">TechCiti Technology</a></p>
    </div>
  </div>
</body>
</html>""")
