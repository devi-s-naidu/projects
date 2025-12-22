<%@ page import="java.util.List" %>
<%@ page import="com.blooddonation.dao.DonorDAO" %>
<%@ page import="com.blooddonation.model.Donor" %>
<!DOCTYPE html>
<html>
<head>
    <title>View All Donors</title>
</head>
<body>
    <h2>All Donors</h2>
    <table border="1" cellpadding="10">
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Blood Group</th>
            <th>Contact</th>
            <th>City</th>
        </tr>
        <%
            DonorDAO dao = new DonorDAO();
            List<Donor> donors = dao.getAllDonors();
            
            if (donors != null && !donors.isEmpty()) {
                for (Donor donor : donors) {
        %>
            <tr>
                <td><%= donor.getName() %></td>
                <td><%= donor.getAge() %></td>
                <td><%= donor.getBloodGroup() %></td>
                <td><%= donor.getContact() %></td>
                <td><%= donor.getCity() %></td>
            </tr>
        <%
                }
            } else {
        %>
            <tr>
                <td colspan="5">No donor data found</td>
            </tr>
        <%
            }
        %>
    </table>
</body>
</html>
