<%@ page import="com.gqt.dao.DepartmentDao" %>
<%@ page import="com.gqt.model.Department" %>
<%@ page import="java.util.List" %>
<%
    List<Department> departments = new DepartmentDao().getAllDepartments();
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Add Budget</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="card shadow">
            <div class="card-header bg-primary text-white">
                <h4 class="mb-0">Add Budget</h4>
            </div>
            <div class="card-body">
                <form action="addBudget" method="post">
                    <div class="form-group">
                        <label for="department">Department</label>
                        <select class="form-control" name="department" id="department" required>
                            <% for (Department d : departments) { %>
                                <option value="<%= d.getId() %>"><%= d.getName() %></option>
                            <% } %>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="amount">Amount</label>
                        <input type="number" step="0.01" class="form-control" name="amount" id="amount" required>
                    </div>
                    <div class="form-group">
                        <label for="year">Year</label>
                        <input type="number" class="form-control" name="year" id="year" required>
                    </div>
                    <div class="form-group">
                        <label for="description">Description</label>
                        <input type="text" class="form-control" name="description" id="description">
                    </div>
                    <button type="submit" class="btn btn-success">Add Budget</button>
                    <a href="index.jsp" class="btn btn-secondary ml-2">Back</a>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
