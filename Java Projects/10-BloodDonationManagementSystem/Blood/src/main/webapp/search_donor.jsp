<%@ page language="java" contentType="text/html; charset=UTF-8" %>
<%@ page import="javax.servlet.http.*,javax.servlet.*" %>
<%

    if (session == null || session.getAttribute("admin") == null) {
        response.sendRedirect("admin_login.jsp");
        return;
    }
%>
<html>
<head><title>Search Donor</title></head>
<body>
    <h2>Search Donor</h2>
    <form action="searchDonor" method="get">
        Blood Group: <input type="text" name="blood"><br>
        City: <input type="text" name="city"><br>
        <input type="submit" value="Search">
    </form>
</body>
</html>
