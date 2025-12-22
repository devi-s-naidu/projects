<%@ page contentType="text/html;charset=UTF-8" %>
<html>
<head>
    <title>Register</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
<div class="container">
    <h2>User Registration</h2>
    <form method="post" action="register">
        <input type="text" name="username" placeholder="Enter Username" required />
        <input type="email" name="email" placeholder="Enter Email" required />
        <input type="password" name="password" placeholder="Enter Password" required />
        <button type="submit">Register</button>
    </form>
</div>
</body>
</html>
