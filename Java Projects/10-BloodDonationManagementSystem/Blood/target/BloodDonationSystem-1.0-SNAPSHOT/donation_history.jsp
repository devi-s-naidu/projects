<%@ page language="java" %>
<%@ page import="java.util.*,java.sql.*" %>
<html>
<head><title>Donation History</title></head>
<body>
    <h2>All Donation History</h2>
    <table border="1">
        <tr><th>Donor Name</th><th>Blood Group</th><th>City</th><th>Date</th></tr>
        <%
            try {
                Class.forName("com.mysql.cj.jdbc.Driver");
                Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/blood_db", "root", "abhra2004");

                Statement stmt = con.createStatement();
                ResultSet rs = stmt.executeQuery("SELECT * FROM donors");

                while (rs.next()) {
                    out.println("<tr><td>" + rs.getString("donor_name") + "</td><td>" + rs.getString("blood_group") +
                                "</td><td>" + rs.getString("city") + "</td><td>" + rs.getString("donation_date") + "</td></tr>");
                }

                con.close();
            } catch (Exception e) {
                out.println("<tr><td colspan='4'>Error: " + e.getMessage() + "</td></tr>");
            }
        %>
    </table>
</body>
</html>
