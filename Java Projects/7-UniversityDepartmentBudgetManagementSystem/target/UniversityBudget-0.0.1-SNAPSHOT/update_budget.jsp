<%@ page import="com.gqt.dao.BudgetDao" %>
<%@ page import="com.gqt.dao.DepartmentDao" %>
<%@ page import="com.gqt.model.Budget" %>
<%@ page import="com.gqt.model.Department" %>
<%@ page import="java.util.List" %>
<%
    int id = Integer.parseInt(request.getParameter("id"));
    Budget budget = new BudgetDao().getBudgetById(id);
    List<Department> departments = new DepartmentDao().getAllDepartments();
%>
<html>
<head><title>Update Budget</title></head>
<body>
    <h2>Update Budget</h2>
    <form action="updateBudget" method="post">
        <input type="hidden" name="id" value="<%= budget.getId() %>"/>
        Department:
        <select name="department">
            <% for (Department d : departments) { %>
                <option value="<%= d.getId() %>" <%= (d.getId() == budget.getDepartment().getId()) ? "selected" : "" %>>
                    <%= d.getName() %>
                </option>
            <% } %>
        </select><br>
        Amount: <input type="number" name="amount" value="<%= budget.getAmount() %>" required><br>
        Year: <input type="number" name="year" value="<%= budget.getYear() %>" required><br>
        Description: <input type="text" name="description" value="<%= budget.getDescription() %>"><br>
        <input type="submit" value="Update">
    </form>
    <a href="view_budgets.jsp">Back</a>
</body>
</html>
