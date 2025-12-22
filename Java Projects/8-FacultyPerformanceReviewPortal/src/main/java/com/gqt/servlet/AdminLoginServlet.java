package com.gqt.servlet;

import com.gqt.model.Admin;
import org.hibernate.*;
import com.gqt.util.HibernateUtil;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;

public class AdminLoginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String username = req.getParameter("username");
        String password = req.getParameter("password");

        Session session = HibernateUtil.getSessionFactory().openSession();
        Query query = session.createQuery("from Admin where username = :un and password = :pw");
        query.setParameter("un", username);
        query.setParameter("pw", password);
        Admin admin = (Admin) query.uniqueResult();

        if (admin != null) {
            req.getSession().setAttribute("admin", admin);
            resp.sendRedirect("admin_dashboard.jsp");
        } else {
            resp.getWriter().println("Invalid admin credentials");
        }
        session.close();
    }
}
