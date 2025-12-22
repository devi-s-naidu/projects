<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="java.util.List" %>
<%@ page import="com.gqt.model.Expense" %>
<%@ page import="org.hibernate.*" %>
<%@ page import="com.gqt.util.HibernateUtil" %>
<%@ page import="com.gqt.model.User" %>

<%
User user = (User) session.getAttribute("user");
if (user == null) {
    response.sendRedirect("login.jsp");
    return;
}

Session hibSession = HibernateUtil.getSessionFactory().openSession();
List<Expense> expenses = hibSession.createQuery("FROM Expense WHERE user.id = :uid", Expense.class)
                                   .setParameter("uid", user.getId())
                                   .list();
hibSession.close();
%>

<!DOCTYPE html>
<html>
<head>
    <title>My Expenses</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="card shadow-lg">
            <div class="card-header bg-primary text-white">
                <h4 class="mb-0">Expense List for <%= user.getName() %></h4>
            </div>
            <div class="card-body">
                <% if (expenses.isEmpty()) { %>
                    <p class="text-muted">No expenses found.</p>
                <% } else { %>
                <div class="table-responsive">
                    <table class="table table-striped table-bordered align-middle">
                        <thead class="table-dark">
                            <tr>
                                <th>Title</th>
                                <th>Amount (₹)</th>
                                <th>Date</th>
                            </tr>
                        </thead>
                        <tbody>
                        <% for (Expense e : expenses) { %>
                            <tr>
                                <td><%= e.getTitle() %></td>
                                <td>₹<%= e.getAmount() %></td>
                                <td><%= e.getDate() %></td>
                            </tr>
                        <% } %>
                        </tbody>
                    </table>
                </div>
                <% } %>
                <a href="home.jsp" class="btn btn-secondary mt-3">← Back to Dashboard</a>
            </div>
        </div>
    </div>
</body>
</html>
