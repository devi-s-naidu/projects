package com.gqt.controller;

import java.io.IOException;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.http.*;

import com.gqt.util.DBConnection;

public class RegisterServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        String username = request.getParameter("username");
        String email = request.getParameter("email");
        String password = request.getParameter("password");

        try (Connection con = DBConnection.getConnection()) {
            PreparedStatement ps = con.prepareStatement(
                    "INSERT INTO users(username, email, password) VALUES (?, ?, ?)");
            ps.setString(1, username);
            ps.setString(2, email);
            ps.setString(3, password);

            ps.executeUpdate();
            response.sendRedirect("index.jsp?success=registered");
        } catch (Exception e) {
            e.printStackTrace();
            response.sendRedirect("register.jsp?error=exists");
        }
    }
}
