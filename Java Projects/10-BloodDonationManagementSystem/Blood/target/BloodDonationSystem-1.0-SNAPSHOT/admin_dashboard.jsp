<%@ page language="java" %>
<%@ page import="javax.servlet.http.*,javax.servlet.*" %>
<%
    if (session == null || session.getAttribute("admin") == null) {
        response.sendRedirect("admin_login.jsp");
        return;
    }
%>
<html>
<head><title>Admin Dashboard</title></head>
<body>
    <h2>Welcome Admin</h2>
    <ul>
        <li><a href="search_donor.jsp">Search Donor</a></li>
        <li><a href="donation_history.jsp">Donation History</a></li>
        <li><a href="logout.jsp">Logout</a></li>
    </ul>
</body>
</html>
