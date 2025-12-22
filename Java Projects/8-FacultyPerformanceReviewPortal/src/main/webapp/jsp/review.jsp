<%@ page import="com.gqt.model.*" %>
<%@ page import="com.gqt.dao.*" %>
<%@ page import="org.hibernate.*" %>
<%@ page import="com.gqt.util.HibernateUtil" %>
<%
    Student student = (Student) session.getAttribute("student");
    if (student == null) {
        response.sendRedirect("login.jsp");
        return;
    }

    Session hSession = HibernateUtil.getSessionFactory().openSession();
    List<Faculty> faculties = hSession.createQuery("from Faculty").list();
    List<Question> questions = hSession.createQuery("from Question").list();
%>
<html>
<head><title>Review Faculty</title></head>
<body>
<h2>Submit Review</h2>
<form action="ReviewServlet" method="post">
    Faculty:
    <select name="facultyId">
        <% for(Faculty f : faculties) { %>
            <option value="<%= f.getId() %>"><%= f.getName() %></option>
        <% } %>
    </select><br/><br/>
    
    <% for(Question q : questions) { %>
        <%= q.getQuestion() %><br/>
        <input type="radio" name="q<%= q.getId() %>" value="1" required />1
        <input type="radio" name="q<%= q.getId() %>" value="2" />2
        <input type="radio" name="q<%= q.getId() %>" value="3" />3
        <input type="radio" name="q<%= q.getId() %>" value="4" />4
        <input type="radio" name="q<%= q.getId() %>" value="5" />5
        <br/><br/>
    <% } %>
    <input type="submit" value="Submit Review"/>
</form>
</body>
</html>
<%
    hSession.close();
%>
