<%@ page contentType="text/html;charset=UTF-8" %>
<%@ page import="java.util.*" %>
<html>
<head>
    <title>My Tickets</title>
    <link rel="stylesheet" href="css/style.css">

</head>
<body>
<div class="container">
    <h2>My Submitted Tickets</h2>
    <table>
        <tr>
            <th>ID</th>
            <th>Category</th>
            <th>Priority</th>
            <th>Description</th>
            <th>Status</th>
            <th>Date</th>
        </tr>
        <%
            List<Map<String, String>> tickets = (List<Map<String, String>>) request.getAttribute("myTickets");
            if (tickets != null && !tickets.isEmpty()) {
                for (Map<String, String> ticket : tickets) {
        %>
        <tr>
            <td><%= ticket.get("ticket_id") %></td>
            <td><%= ticket.get("category") %></td>
            <td><%= ticket.get("priority") %></td>
            <td><%= ticket.get("description") %></td>
            <td><%= ticket.get("status") %></td>
            <td><%= ticket.get("created_at") %></td>
        </tr>
        <%
                }
            } else {
        %>
        <tr><td colspan="6">No tickets found.</td></tr>
        <% } %>
    </table>
</div>
</body>
</html>
