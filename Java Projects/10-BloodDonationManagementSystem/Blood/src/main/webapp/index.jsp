<%@ page language="java" contentType="text/html; charset=UTF-8" %>
<html>
<head>
    <title>Blood Donation Management System</title>
    <style>
        body {
            font-family: Arial;
            background-color: #f2f2f2;
            padding: 40px;
        }
        h1 {
            color: crimson;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
        }
        a {
            text-decoration: none;
            color: #007bff;
            font-size: 18px;
        }
        a:hover {
            color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Welcome to Blood Donation System</h1>
    <ul>
        <li><a href="donor_form.jsp">Register as Donor</a></li>
        <li><a href="view_donor.jsp">View All Donors</a></li>
        <li><a href="admin_login.jsp">Admin Login</a></li>
    </ul>
</body>
</html>
