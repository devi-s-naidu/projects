<%@ page language="java" %>
<html>
<head><title>Login</title></head>
<body>
<h2>Student Login</h2>
<form action="LoginServlet" method="post">
    Email: <input type="text" name="email" required /><br/>
    Password: <input type="password" name="password" required /><br/>
    <input type="submit" value="Login" />
</form>
<a href="register.jsp">New user? Register here</a>
</body>
</html>
