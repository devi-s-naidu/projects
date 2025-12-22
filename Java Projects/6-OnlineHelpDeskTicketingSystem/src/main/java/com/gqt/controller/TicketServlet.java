package com.gqt.controller;

import java.io.IOException;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

import com.gqt.util.DBConnection;

public class TicketServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        HttpSession session = request.getSession(false); 

        if (session == null || session.getAttribute("userId") == null) {
            System.out.println("❌ userId not found in session. Redirecting...");
            response.sendRedirect("index.jsp?error=sessionExpired");
            return;
        }

        int userId = (Integer) session.getAttribute("userId");

        String category = request.getParameter("category");
        String priority = request.getParameter("priority");
        String description = request.getParameter("description");

        try (Connection con = DBConnection.getConnection()) {
            PreparedStatement ps = con.prepareStatement(
                    "INSERT INTO tickets(user_id, category, priority, description) VALUES (?, ?, ?, ?)");
            ps.setInt(1, userId);
            ps.setString(2, category);
            ps.setString(3, priority);
            ps.setString(4, description);

            int inserted = ps.executeUpdate();
            System.out.println("✅ Ticket inserted. Rows affected: " + inserted);

            response.sendRedirect("dashboard_user.jsp?ticket=success");
        } catch (Exception e) {
            e.printStackTrace();
            response.sendRedirect("raise_ticket.jsp?error=true");
        }
    }
}
