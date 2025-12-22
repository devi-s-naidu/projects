package com.blooddonation.controller;

import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;

public class AdminLoginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String uname = request.getParameter("username");
        String pass = request.getParameter("password");

        if ("admin".equals(uname) && "admin123".equals(pass)) {
            HttpSession session = request.getSession();
            session.setAttribute("admin", uname);
            response.sendRedirect("admin_dashboard.jsp");
        } else {
            request.setAttribute("message", "Invalid credentials!");
            RequestDispatcher rd = request.getRequestDispatcher("admin_login.jsp");
            rd.forward(request, response);
        }
    }
}
