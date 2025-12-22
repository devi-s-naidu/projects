package com.gqt.dao;

import com.gqt.model.Student;
import com.gqt.util.HibernateUtil;
import org.hibernate.*;

public class StudentDao {
    public void saveStudent(Student s) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = session.beginTransaction();
        session.save(s);
        tx.commit();
        session.close();
    }

    public Student getStudentByEmailAndPassword(String email, String password) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Query q = session.createQuery("from Student where email=:e and password=:p");
        q.setParameter("e", email);
        q.setParameter("p", password);
        Student s = (Student) q.uniqueResult();
        session.close();
        return s;
    }
}
