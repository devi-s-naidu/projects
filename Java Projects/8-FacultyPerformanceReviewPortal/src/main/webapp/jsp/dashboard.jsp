<%@ page import="com.gqt.model.Student" %>
<%
    Student student = (Student) session.getAttribute("student");
    if (student == null) {
        response.sendRedirect("login.jsp");
        return;
    }
%>
<html>
<head><title>Dashboard</title></head>
<body>
<h2>Welcome, <%= student.getName() %></h2>
<a href="review.jsp">Give Faculty Review</a> |
<a href="LogoutServlet">Logout</a>
</body>
</html>
