package com.gqt.servlet;

import com.gqt.model.Student;
import com.gqt.dao.StudentDao;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;

public class LoginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String email = req.getParameter("email");
        String password = req.getParameter("password");

        StudentDao dao = new StudentDao();
        Student s = dao.getStudentByEmailAndPassword(email, password);

        if (s != null) {
            HttpSession session = req.getSession();
            session.setAttribute("student", s);
            resp.sendRedirect("dashboard.jsp");
        } else {
            resp.getWriter().println("Invalid credentials");
        }
    }
}
