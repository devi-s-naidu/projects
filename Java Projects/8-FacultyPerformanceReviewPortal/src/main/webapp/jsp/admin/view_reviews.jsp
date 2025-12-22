<%@ page import="com.gqt.dao.ReviewDao" %>
<%@ page import="com.gqt.model.Faculty" %>
<%@ page import="org.hibernate.*" %>
<%@ page import="com.gqt.util.HibernateUtil" %>
<%
    if (session.getAttribute("admin") == null) {
        response.sendRedirect("admin_login.jsp");
        return;
    }

    Session hSession = HibernateUtil.getSessionFactory().openSession();
    List<Faculty> faculties = hSession.createQuery("from Faculty").list();
    ReviewDao reviewDao = new ReviewDao();
%>
<html>
<head><title>Review Results</title></head>
<body>
<h2>Faculty Review Results</h2>
<% for (Faculty f : faculties) { %>
    <h3><%= f.getName() %> - <%= f.getDepartment() %></h3>
    <ul>
        <% for (Object[] row : reviewDao.getAverageRatingByFaculty(f.getId())) { %>
            <li><b><%= row[0] %></b> — Avg Rating: <%= row[1] %></li>
        <% } %>
    </ul>
<% } %>
</body>
</html>
<%
    hSession.close();
%>
