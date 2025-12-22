package com.gqt.servlet;

import com.gqt.model.Question;
import com.gqt.util.HibernateUtil;
import org.hibernate.*;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;

public class AddQuestionServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String q = req.getParameter("question");

        Question question = new Question();
        question.setQuestion(q);

        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = session.beginTransaction();
        session.save(question);
        tx.commit();
        session.close();

        resp.sendRedirect("admin_dashboard.jsp");
    }
}
