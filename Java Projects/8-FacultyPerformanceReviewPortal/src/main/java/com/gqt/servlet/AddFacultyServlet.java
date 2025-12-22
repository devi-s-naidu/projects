package com.gqt.servlet;

import com.gqt.model.Faculty;
import com.gqt.util.HibernateUtil;
import org.hibernate.*;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;

public class AddFacultyServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String name = req.getParameter("name");
        String dept = req.getParameter("department");

        Faculty f = new Faculty();
        f.setName(name);
        f.setDepartment(dept);

        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = session.beginTransaction();
        session.save(f);
        tx.commit();
        session.close();

        resp.sendRedirect("admin_dashboard.jsp");
    }
}
