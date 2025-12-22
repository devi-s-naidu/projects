package com.gqt.controller;

import java.io.IOException;
import java.sql.*;
import java.util.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

import com.gqt.util.DBConnection;

public class AdminTicketServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        List<Map<String, String>> tickets = new ArrayList<>();

        try (Connection con = DBConnection.getConnection()) {
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM tickets");

            while (rs.next()) {
                Map<String, String> ticket = new HashMap<>();
                ticket.put("ticket_id", rs.getString("ticket_id"));
                ticket.put("user_id", rs.getString("user_id"));
                ticket.put("category", rs.getString("category"));
                ticket.put("priority", rs.getString("priority"));
                ticket.put("description", rs.getString("description"));
                ticket.put("status", rs.getString("status"));
                tickets.add(ticket);
            }

            request.setAttribute("tickets", tickets);
            RequestDispatcher dispatcher = request.getRequestDispatcher("manage_tickets.jsp");
            dispatcher.forward(request, response);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
