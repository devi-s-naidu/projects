<%@ page import="com.gqt.dao.BudgetDao" %>
<%@ page import="com.gqt.model.Budget" %>
<%@ page import="java.util.List" %>
<%
    List<Budget> budgets = new BudgetDao().getAllBudgets();
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>View Budgets</title>
    <!-- Bootstrap CDN -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="card shadow">
            <div class="card-header bg-info text-white">
                <h4 class="mb-0">All Budgets</h4>
            </div>
            <div class="card-body">
                <table class="table table-bordered table-striped table-hover">
                    <thead class="thead-dark">
                        <tr>
                            <th>ID</th>
                            <th>Department</th>
                            <th>Amount</th>
                            <th>Year</th>
                            <th>Description</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <% for (Budget b : budgets) { %>
                            <tr>
                                <td><%= b.getId() %></td>
                                <td><%= b.getDepartment().getName() %></td>
                                <td><%= b.getAmount() %></td>
                                <td><%= b.getYear() %></td>
                                <td><%= b.getDescription() %></td>
                                <td>
                                    <a href="update_budget.jsp?id=<%= b.getId() %>" class="btn btn-sm btn-warning">Update</a>
                                    <a href="deleteBudget?id=<%= b.getId() %>" class="btn btn-sm btn-danger ml-2">Delete</a>
                                </td>
                            </tr>
                        <% } %>
                    </tbody>
                </table>
                <a href="index.jsp" class="btn btn-secondary">Back</a>
            </div>
        </div>
    </div>
</body>
</html>
