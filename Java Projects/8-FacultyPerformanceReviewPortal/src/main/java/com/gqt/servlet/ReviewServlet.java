package com.gqt.servlet;

import com.gqt.dao.ReviewDao;
import com.gqt.model.*;

import com.gqt.util.HibernateUtil;
import org.hibernate.Session;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;
import java.util.List;

public class ReviewServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        HttpSession httpSession = req.getSession();
        Student student = (Student) httpSession.getAttribute("student");

        int facultyId = Integer.parseInt(req.getParameter("facultyId"));

        Session session = HibernateUtil.getSessionFactory().openSession();
        Faculty faculty = session.get(Faculty.class, facultyId);
        List<Question> questions = session.createQuery("from Question").list();

        session.beginTransaction();
        for (Question q : questions) {
            String ratingStr = req.getParameter("q" + q.getId());
            if (ratingStr != null) {
                int rating = Integer.parseInt(ratingStr);
                Review review = new Review();
                review.setStudent(student);
                review.setFaculty(faculty);
                review.setQuestion(q);
                review.setRating(rating);
                session.save(review);
            }
        }
        session.getTransaction().commit();
        session.close();

        resp.sendRedirect("dashboard.jsp");
    }
}
