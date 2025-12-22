<%@ page import="java.util.*, com.blooddonation.model.Donor" %>
<!DOCTYPE html>
<html>
<head>
    <title>Donor List</title>
</head>
<body>
    <h2>All Donors</h2>
    <table border="1" cellpadding="10">
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Blood Group</th>
            <th>Contact</th>
        </tr>
        <%
            List<Donor> donors = (List<Donor>) request.getAttribute("donors");
            if (donors != null) {
                for (Donor d : donors) {
        %>
            <tr>
                <td><%= d.getName() %></td>
                <td><%= d.getAge() %></td>
                <td><%= d.getBloodGroup() %></td>
                <td><%= d.getContact() %></td>
            </tr>
        <%
                }
            } else {
        %>
            <tr><td colspan="4">No donor data found.</td></tr>
        <%
            }
        %>
    </table>
</body>
</html>
