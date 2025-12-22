package com.gqt.controller;

import java.io.IOException;
import java.sql.*;
import java.util.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

import com.gqt.util.DBConnection;

public class ViewTicketsServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

    	HttpSession session = request.getSession(false);

    	if (session == null || session.getAttribute("userId") == null) {
    	    System.out.println("❌ Session not found or userId is missing.");
    	    response.sendRedirect("index.jsp?error=sessionExpired");
    	    return;
    	}

    	int userId = (int) session.getAttribute("userId"); 

        List<Map<String, String>> tickets = new ArrayList<>();

        try (Connection con = DBConnection.getConnection()) {
            PreparedStatement ps = con.prepareStatement("SELECT * FROM tickets WHERE user_id = ?");
            ps.setInt(1, userId);
            ResultSet rs = ps.executeQuery();

            while (rs.next()) {
                Map<String, String> ticket = new HashMap<>();
                ticket.put("ticket_id", rs.getString("ticket_id"));
                ticket.put("category", rs.getString("category"));
                ticket.put("priority", rs.getString("priority"));
                ticket.put("description", rs.getString("description"));
                ticket.put("status", rs.getString("status"));
                ticket.put("created_at", rs.getString("created_at"));
                tickets.add(ticket);
            }

            request.setAttribute("myTickets", tickets);
            RequestDispatcher dispatcher = request.getRequestDispatcher("view_tickets.jsp");
            dispatcher.forward(request, response);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
