<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <title>Add Expense</title>
</head>
<body>
<form action="ExpenseServlet" method="post">
    Title: <input type="text" name="title"><br>
    Amount: <input type="number" step="0.01" name="amount"><br>
    Date: <input type="date" name="date"><br>
    <input type="submit" value="Add Expense">
</form>
</body>
</html>











