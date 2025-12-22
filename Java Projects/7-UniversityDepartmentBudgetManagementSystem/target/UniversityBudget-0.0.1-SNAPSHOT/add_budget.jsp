<%@ page import="com.gqt.dao.DepartmentDao" %>
<%@ page import="com.gqt.model.Department" %>
<%@ page import="java.util.List" %>
<%
    List<Department> departments = new DepartmentDao().getAllDepartments();
%>
<html>
<head><title>Add Budget</title></head>
<body>
    <h2>Add Budget</h2>
    <form action="addBudget" method="post">
        Department:
        <select name="department">
            <% for (Department d : departments) { %>
                <option value="<%= d.getId() %>"><%= d.getName() %></option>
            <% } %>
        </select><br>
        Amount: <input type="number" step="0.01" name="amount" required><br>
        Year: <input type="number" name="year" required><br>
        Description: <input type="text" name="description"><br>
        <input type="submit" value="Add Budget">
    </form>
    <a href="index.jsp">Back</a>
</body>
</html>
