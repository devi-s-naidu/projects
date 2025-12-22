package com.gqt.controller;

import java.io.IOException;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.http.*;

import com.gqt.util.DBConnection;

public class LoginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        String email = request.getParameter("email");     
        String password = request.getParameter("password");

        try (Connection con = DBConnection.getConnection()) {
            PreparedStatement ps = con.prepareStatement("SELECT * FROM users WHERE email=? AND password=?");
            ps.setString(1, email);                        
            ps.setString(2, password);

            ResultSet rs = ps.executeQuery();

            if (rs.next()) {
                String role = rs.getString("role");
                String username = rs.getString("username");  
                
                HttpSession session = request.getSession();
                session.setAttribute("username", username);
                session.setAttribute("userId", rs.getInt("id"));
                session.setAttribute("role", role);

                if ("admin".equals(role)) {
                    response.sendRedirect("dashboard_admin.jsp");
                } else {
                    response.sendRedirect("dashboard_user.jsp");
                }
            } else {
                response.sendRedirect("index.jsp?error=invalid");
            }
        } catch (Exception e) {
            e.printStackTrace();
            response.sendRedirect("index.jsp?error=unknown");
        }
    }
}
