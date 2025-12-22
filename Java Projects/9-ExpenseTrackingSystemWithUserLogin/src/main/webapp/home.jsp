<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="com.gqt.model.*" %>
<%@ page import="java.util.*" %>
<%@ page import="org.hibernate.*" %>
<%@ page import="com.gqt.util.HibernateUtil" %>

<%
User user = (User) session.getAttribute("user");
if (user == null) {
    response.sendRedirect("login.jsp");
    return;
}

Session hibSession = HibernateUtil.getSessionFactory().openSession();
List expenses = hibSession.createQuery("FROM Expense WHERE user.id = :uid")
                          .setParameter("uid", user.getId()).list();
hibSession.close();
%>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>View Expenses</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
        <span class="navbar-brand">Expense Tracker</span>
        <div class="d-flex">
            <a href="dashboard.jsp" class="btn btn-outline-light me-2">Dashboard</a>
            <a href="logout.jsp" class="btn btn-outline-danger">Logout</a>
        </div>
    </div>
</nav>

<div class="container mt-5">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h3>Welcome, <%= user.getName() %></h3>
        <a href="add_expense.jsp" class="btn btn-primary">➕ Add New Expense</a>
    </div>

    <div class="table-responsive">
        <table class="table table-bordered table-striped table-hover shadow-sm">
            <thead class="table-dark">
                <tr>
                    <th>Title</th>
                    <th>Amount (₹)</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody>
                <% for(Object o : expenses) {
                    com.gqt.model.Expense e = (com.gqt.model.Expense) o;
                %>
                <tr>
                    <td><%= e.getTitle() %></td>
                    <td><%= e.getAmount() %></td>
                    <td><%= e.getDate() %></td>
                </tr>
                <% } %>
            </tbody>
        </table>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
