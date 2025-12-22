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
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Update Budget</title>
    <!-- Bootstrap CDN -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="card shadow">
            <div class="card-header bg-warning text-dark">
                <h4 class="mb-0">Update Budget</h4>
            </div>
            <div class="card-body">
                <form action="updateBudget" method="post">
                    <input type="hidden" name="id" value="<%= budget.getId() %>"/>
                    
                    <div class="form-group">
                        <label for="department">Department</label>
                        <select class="form-control" name="department" id="department" required>
                            <% for (Department d : departments) { %>
                                <option value="<%= d.getId() %>" <%= (d.getId() == budget.getDepartment().getId()) ? "selected" : "" %>>
                                    <%= d.getName() %>
                                </option>
                            <% } %>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="amount">Amount</label>
                        <input type="number" class="form-control" name="amount" id="amount" value="<%= budget.getAmount() %>" required>
                    </div>

                    <div class="form-group">
                        <label for="year">Year</label>
                        <input type="number" class="form-control" name="year" id="year" value="<%= budget.getYear() %>" required>
                    </div>

                    <div class="form-group">
                        <label for="description">Description</label>
                        <input type="text" class="form-control" name="description" id="description" value="<%= budget.getDescription() %>">
                    </div>

                    <button type="submit" class="btn btn-warning">Update</button>
                    <a href="view_budgets.jsp" class="btn btn-secondary ml-2">Back</a>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
