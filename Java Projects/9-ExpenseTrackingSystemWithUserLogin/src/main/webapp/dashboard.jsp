<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User Dashboard - Expense Tracker</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container-fluid">
        <span class="navbar-brand">Expense Tracker</span>
        <div class="d-flex">
            <a href="logout.jsp" class="btn btn-outline-light">Logout</a>
        </div>
    </div>
</nav>

<div class="container mt-5">
    <div class="text-center mb-4">
        <h2 class="text-primary">Welcome to Your Dashboard</h2>
        <p class="text-muted">Manage your expenses efficiently</p>
    </div>

    <div class="row justify-content-center">
        <div class="col-md-4 mb-3">
            <a href="add_expense.jsp" class="text-decoration-none">
                <div class="card shadow-sm border-0">
                    <div class="card-body text-center">
                        <h5 class="card-title">➕ Add New Expense</h5>
                        <p class="card-text text-muted">Record your latest spending</p>
                    </div>
                </div>
            </a>
        </div>

        <div class="col-md-4 mb-3">
            <a href="view_expenses.jsp" class="text-decoration-none">
                <div class="card shadow-sm border-0">
                    <div class="card-body text-center">
                        <h5 class="card-title">📋 View All Expenses</h5>
                        <p class="card-text text-muted">See your expense history</p>
                    </div>
                </div>
            </a>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
