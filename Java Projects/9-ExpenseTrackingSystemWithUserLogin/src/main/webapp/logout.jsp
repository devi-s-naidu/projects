<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    session.invalidate(); 
%>
<!DOCTYPE html>
<html>
<head>
    <title>Logout - Expense Tracker</title>
    <meta http-equiv="refresh" content="3;url=login.jsp"> 
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container d-flex justify-content-center align-items-center vh-100">
        <div class="text-center">
            <div class="alert alert-success shadow-lg" role="alert">
                <h4 class="alert-heading">You have been logged out!</h4>
                <p>Thank you for using Expense Tracker.</p>
                <hr>
                <p class="mb-0">Redirecting to <a href="login.jsp">login page</a>...</p>
            </div>
        </div>
    </div>
</body>
</html>
