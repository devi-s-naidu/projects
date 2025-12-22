<%@ page import="com.gqt.model.Admin" %>
<%
    if (session.getAttribute("admin") == null) {
        response.sendRedirect("admin_login.jsp");
        return;
    }
%>
<html>
<head><title>Add Question</title></head>
<body>
<h2>Add Review Question</h2>
<form action="AddQuestionServlet" method="post">
    Question: <input type="text" name="question" required /><br/>
    <input type="submit" value="Add Question" />
</form>
</body>
</html>
