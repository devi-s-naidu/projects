<%@ page contentType="text/html;charset=UTF-8" %>
<html>
<head>
    <title>Admin Dashboard</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="navbar">
        Welcome, Admin
        <a href="logout.jsp" class="logout-link">Logout</a>
    </div>
    <div class="container">
        <button onclick="location.href='manage_tickets.jsp'">Manage Tickets</button>
    </div>
</body>
</html>
