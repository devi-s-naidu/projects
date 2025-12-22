<%@ page contentType="text/html;charset=UTF-8" %>
<html>
<head>
    <title>Online Help Desk</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
<div class="container">
    <h1>Welcome to the Online Help Desk</h1>

<% String error = request.getParameter("error"); %>
<% if (error != null) { %>
    <p class="error">
        <%= "invalid".equals(error) ? "Invalid login credentials. Please try again." :
             "exception".equals(error) ? "Something went wrong. Please try again later." :
             "Unknown error." %>
    </p>
<% } %>


    <h2>Login</h2>
    <form method="post" action="login">
        <label for="email">Email:</label>
        <input type="text" name="email" required /><br/>

        <label for="password">Password:</label>
        <input type="password" name="password" required /><br/>

        <button type="submit">Login</button>
    </form>

    <p>Don't have an account? <a href="register.jsp">Register here</a></p>
</div>
</body>
</html>
