package com.gqt.dao;

import com.gqt.model.*;
import com.gqt.util.HibernateUtil;
import org.hibernate.*;

import java.util.List;

public class ReviewDao {

    // Save a single review
    public void saveReview(Review review) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = session.beginTransaction();
        session.save(review);
        tx.commit();
        session.close();
    }

    // Get all reviews
    public List<Review> getAllReviews() {
        Session session = HibernateUtil.getSessionFactory().openSession();
        List<Review> reviews = session.createQuery("from Review").list();
        session.close();
        return reviews;
    }

    // Get average rating per question for a faculty
    public List<Object[]> getAverageRatingByFaculty(int facultyId) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        String hql = "SELECT r.question.question, AVG(r.rating) FROM Review r WHERE r.faculty.id = :fid GROUP BY r.question.id";
        Query query = session.createQuery(hql);
        query.setParameter("fid", facultyId);
        List<Object[]> result = query.list();
        session.close();
        return result;
    }

    // Get reviews submitted by a specific student
    public List<Review> getReviewsByStudent(int studentId) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Query query = session.createQuery("from Review where student.id = :sid");
        query.setParameter("sid", studentId);
        List<Review> reviews = query.list();
        session.close();
        return reviews;
    }

    // Delete reviews by faculty ID (optional, for admin use)
    public void deleteReviewsByFaculty(int facultyId) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = session.beginTransaction();
        Query query = session.createQuery("delete from Review where faculty.id = :fid");
        query.setParameter("fid", facultyId);
        query.executeUpdate();
        tx.commit();
        session.close();
    }
}
