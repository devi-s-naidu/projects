<%@ page import="com.gqt.model.Admin" %>
<%
    if (session.getAttribute("admin") == null) {
        response.sendRedirect("admin_login.jsp");
        return;
    }
%>
<html>
<head><title>Add Faculty</title></head>
<body>
<h2>Add Faculty</h2>
<form action="AddFacultyServlet" method="post">
    Name: <input type="text" name="name" required /><br/>
    Department: <input type="text" name="department" required /><br/>
    <input type="submit" value="Add Faculty" />
</form>
</body>
</html>
