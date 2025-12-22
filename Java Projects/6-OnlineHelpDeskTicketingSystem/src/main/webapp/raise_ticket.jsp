<%@ page contentType="text/html;charset=UTF-8" %>
<html>
<head>
    <title>Raise Ticket</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
<div class="container">
    <h2>Raise Support Ticket</h2>
    
    <% if ("true".equals(request.getParameter("error"))) { %>
        <p class="error">Error submitting ticket. Please fill all fields.</p>
    <% } %>
    
    <form method="post" action="submitTicket">
        <label for="category">Category:</label>
        <select name="category" required>
            <option value="">-- Select Category --</option>
            <option value="Technical">Technical</option>
            <option value="Billing">Billing</option>
            <option value="Account">Account</option>
        </select><br/>

        <label for="priority">Priority:</label>
        <select name="priority" required>
            <option value="">-- Select Priority --</option>
            <option value="High">High</option>
            <option value="Medium">Medium</option>
            <option value="Low">Low</option>
        </select><br/>

        <label for="description">Description:</label><br/>
        <textarea name="description" placeholder="Describe your issue..." rows="5" required></textarea><br/>

        <button type="submit">Submit Ticket</button>
    </form>
</div>
</body>
</html>
