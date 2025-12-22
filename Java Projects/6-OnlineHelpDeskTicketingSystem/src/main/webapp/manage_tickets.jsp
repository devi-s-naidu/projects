<%@ page contentType="text/html;charset=UTF-8" %>
<%@ page import="java.util.*" %>
<html>
<head>
    <title>Manage Tickets</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
<div class="container">
    <h2>All Support Tickets</h2>
    <table>
        <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Subject</th>
            <th>Description</th>
            <th>Status</th>
            <th>Created</th>
            <th>Action</th>
        </tr>
        <%
            List<List<String>> tickets = (List<List<String>>) request.getAttribute("tickets");
            if (tickets != null && !tickets.isEmpty()) {
                for (List<String> ticket : tickets) {
        %>
        <tr>
            <td><%= ticket.get(0) %></td> <!-- ID -->
            <td><%= ticket.get(1) %></td> <!-- Username -->
            <td><%= ticket.get(2) %></td> <!-- Subject -->
            <td><%= ticket.get(3) %></td> <!-- Description -->
            <td><%= ticket.get(4) %></td> <!-- Status -->
            <td><%= ticket.get(5) %></td> <!-- Created Date -->
            <td>
                <form method="post" action="UpdateTicketServlet">
                    <input type="hidden" name="ticketId" value="<%= ticket.get(0) %>" />
                    <select name="status">
                        <option <%= ticket.get(4).equals("Open") ? "selected" : "" %>>Open</option>
                        <option <%= ticket.get(4).equals("In Progress") ? "selected" : "" %>>In Progress</option>
                        <option <%= ticket.get(4).equals("Resolved") ? "selected" : "" %>>Resolved</option>
                    </select>
                    <button type="submit">Update</button>
                </form>
            </td>
        </tr>
        <% } } else { %>
        <tr><td colspan="7">No tickets available.</td></tr>
        <% } %>
    </table>
</div>
</body>
</html>
