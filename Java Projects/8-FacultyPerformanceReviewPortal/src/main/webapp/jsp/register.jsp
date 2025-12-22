<%@ page language="java" %>
<html>
<head><title>Register</title></head>
<body>
<h2>Student Registration</h2>
<form action="RegisterServlet" method="post">
    Name: <input type="text" name="name" required /><br/>
    Email: <input type="text" name="email" required /><br/>
    Password: <input type="password" name="password" required /><br/>
    <input type="submit" value="Register" />
</form>
<a href="login.jsp">Already have an account? Login</a>
</body>
</html>
