package com.gqt.servlet;

import com.gqt.model.Student;
import com.gqt.dao.StudentDao;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;

public class RegisterServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Student s = new Student();
        s.setName(req.getParameter("name"));
        s.setEmail(req.getParameter("email"));
        s.setPassword(req.getParameter("password"));

        StudentDao dao = new StudentDao();
        dao.saveStudent(s);

        resp.sendRedirect("login.jsp");
    }
}
