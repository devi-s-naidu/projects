<%@ page import="com.gqt.dao.BudgetDao" %>
<%@ page import="com.gqt.model.Budget" %>
<%@ page import="java.util.List" %>
<%
    List<Budget> budgets = new BudgetDao().getAllBudgets();
%>
<html>
<head><title>View Budgets</title></head>
<body>
    <h2>All Budgets</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Department</th>
            <th>Amount</th>
            <th>Year</th>
            <th>Description</th>
            <th>Actions</th>
        </tr>
        <% for (Budget b : budgets) { %>
            <tr>
                <td><%= b.getId() %></td>
                <td><%= b.getDepartment().getName() %></td>
                <td><%= b.getAmount() %></td>
                <td><%= b.getYear() %></td>
                <td><%= b.getDescription() %></td>
                <td>
                    <a href="update_budget.jsp?id=<%= b.getId() %>">Update</a> |
                    <a href="deleteBudget?id=<%= b.getId() %>">Delete</a>
                </td>
            </tr>
        <% } %>
    </table>
    <a href="index.jsp">Back</a>
</body>
</html>
