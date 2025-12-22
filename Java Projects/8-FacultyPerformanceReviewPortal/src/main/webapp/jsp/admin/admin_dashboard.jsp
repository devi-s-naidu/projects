<%@ page import="com.gqt.model.Admin" %>
<%
    Admin admin = (Admin) session.getAttribute("admin");
    if (admin == null) {
        response.sendRedirect("admin_login.jsp");
        return;
    }
%>
<html>
<head><title>Admin Dashboard</title></head>
<body>
<h2>Welcome, Admin</h2>
<ul>
    <li><a href="add_faculty.jsp">Add Faculty</a></li>
    <li><a href="add_question.jsp">Add Review Question</a></li>
    <li><a href="view_reviews.jsp">View Faculty Review Results</a></li>
    <li><a href="LogoutServlet">Logout</a></li>
</ul>
</body>
</html>
