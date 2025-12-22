<%@ page import="com.gqt.model.*" %>
<%@ page import="java.util.*" %>
<%@ page import="org.hibernate.*" %>
<%@ page import="com.gqt.util.HibernateUtil" %>

<%
User user = (User) session.getAttribute("user");
if (user == null) {
    response.sendRedirect("login.jsp");
}

Session hibSession = HibernateUtil.getSessionFactory().openSession();
List expenses = hibSession.createQuery("FROM Expense WHERE user.id = :uid")
                          .setParameter("uid", user.getId()).list();
hibSession.close();
%>

<h3>Welcome, <%= user.getName() %></h3>
<a href="add_expense.jsp">Add New Expense</a>

<table border="1">
<tr><th>Title</th><th>Amount</th><th>Date</th></tr>
<% for(Object o : expenses) {
    com.gqt.model.Expense e = (com.gqt.model.Expense) o;
%>
<tr>
    <td><%= e.getTitle() %></td>
    <td><%= e.getAmount() %></td>
    <td><%= e.getDate() %></td>
</tr>
<% } %>
</table>
