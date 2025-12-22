<%@ page contentType="text/html;charset=UTF-8" %>
<html>
<head>
    <title>User Dashboard</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="navbar">
        Welcome, User
        <a href="logout.jsp" class="logout-link">Logout</a>
    </div>
    <div class="container">
        <button onclick="location.href='raise_ticket.jsp'">Raise Ticket</button><br><br>
        <button onclick="location.href='ViewTicketsServlet'">View My Tickets</button>
    </div>
</body>
</html>
