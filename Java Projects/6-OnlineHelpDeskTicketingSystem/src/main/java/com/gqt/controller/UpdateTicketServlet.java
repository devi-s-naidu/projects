package com.gqt.controller;

import java.io.IOException;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

import com.gqt.util.DBConnection;

public class UpdateTicketServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        int ticketId = Integer.parseInt(request.getParameter("ticket_id"));
        String status = request.getParameter("status");
        String comment = request.getParameter("comment");

        try (Connection con = DBConnection.getConnection()) {
            PreparedStatement ps = con.prepareStatement(
                "UPDATE tickets SET status=?, resolution_comment=? WHERE ticket_id=?");
            ps.setString(1, status);
            ps.setString(2, comment);
            ps.setInt(3, ticketId);

            ps.executeUpdate();
            response.sendRedirect("AdminTicketServlet");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
