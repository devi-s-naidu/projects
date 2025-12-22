package com.gqt.dao;

import com.gqt.model.Department;
import com.gqt.util.HibernateUtil;
import org.hibernate.Session;
import org.hibernate.Transaction;
import java.util.List;

public class DepartmentDao {
    public void saveDepartment(Department dept) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = session.beginTransaction();
        session.save(dept);
        tx.commit();
        session.close();
    }

    public List<Department> getAllDepartments() {
        Session session = HibernateUtil.getSessionFactory().openSession();
        List<Department> departments = session.createQuery("from Department", Department.class).list();
        session.close();
        return departments;
    }

    public Department getDepartmentById(int id) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Department dept = session.get(Department.class, id);
        session.close();
        return dept;
    }
}