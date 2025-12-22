<%@ page contentType="text/html;charset=UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>University Budget Management</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body class="bg-light">
    <div class="container text-center mt-5">
        <div class="card shadow">
            <div class="card-header bg-dark text-white">
                <h3>University Department Budget Management System</h3>
            </div>
            <div class="card-body">
                <p class="lead">Welcome! Please choose an action:</p>
                <a href="add_department.jsp" class="btn btn-primary btn-block mb-2">Add Department</a>
                <a href="add_budget.jsp" class="btn btn-success btn-block mb-2">Add Budget</a>
                <a href="view_budgets.jsp" class="btn btn-info btn-block">View All Budgets</a>
            </div>
        </div>
    </div>
</body>
</html>
