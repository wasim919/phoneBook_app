<html>
<head>
	<title>html form</title>
</head>
<body>
	<center><h2>PHONE BOOK</h2></center>
	<form action = "http://127.0.0.1:8000/phonebook/get/" method = "GET">
		Enter your name:<input type = "text" name = "cname"><br>
		Enter your number:<input type = "text" name = "number"><br>
		Enter your address:<input type = "text" name = "address"><br>
		<input type = "submit" value = "submit">
	</form>
	<form action = "http://127.0.0.1:8000/phonebook/gen/" method = "GET">
	<center><h2>Search</h2></center>
	Enter the number of the customer:<input type = "text" name = "number"><br>
	<input type = "submit" value = "submit">
	</form>
</body>
</html>