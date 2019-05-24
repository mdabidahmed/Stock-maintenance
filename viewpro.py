#!C:/python34/python
import cgi
import mysql.connector
print("Content-type: text/html")
print("")
print("""
<html>

<head>
  <title>Stock Maintenance</title>
  <meta name="description" content="website description" />
  <meta name="keywords" content="website keywords, website keywords" />
  <meta http-equiv="content-type" content="text/html; charset=windows-1252" />
  <link rel="stylesheet" type="text/css" href="style/style.css" />
<style>
table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    text-align: left;
    padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2}

th {
    background-color: #4CAF50;
    color: white;
}
</style>
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
          <li class="selected"><a href="adminhome.html">Home</a></li>
          <li><a href="addpro.html">Add Product</a></li>
          <li><a href="viewpro.py">View Product</a></li>
          <li><a href="viewuser.py">View User</a></li>
		   <li><a href="viewfeed.py">View Feedback</a></li>
		  <li><a href="viewcon.py">View Buy Details</a></li>
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
        <p>Welcome To Admin Home...
		</p>   
   <table>
  <tr>
    <th>Category Name</th>
    <th>Category Type</th>
    <th>Product Name</th>
	<th>Product Price</th>
	<th>Product Description</th>
	<th>Product Image</th>


  </tr>""")
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='stock');
if(cnx):
    print("");
cursor=cnx.cursor()
cursor.execute("""
    SELECT * FROM product""")
for row in cursor:
	print("<tr>");
	print("<td>",row[0],"</td>")
	print("<td>",row[1],"</td>")
	print("<td>",row[2],"</td>")	
	print("<td>",row[3],"</td>")
	print("<td>",row[4],"</td>")
	print("<td>",row[5],"</td>")
	print("<tr>");
print("<table>");

print("""
</div>
    </div>
    <div id="content_footer"></div>
    <div id="footer">
      <p><a href="adminhome.html">Home</a> | <a href="addpro.html">Add Product</a> | <a href="viewpro.py">View Product</a> | <a href="viewuser.py">View User</a> | <a href="index.html">Logout</a></p>
      <p>Copyright &copy; <a href="www.techciti.in">TechCiti Technology</a></p>    </div>
  </div>
</body>
</html>
""");
