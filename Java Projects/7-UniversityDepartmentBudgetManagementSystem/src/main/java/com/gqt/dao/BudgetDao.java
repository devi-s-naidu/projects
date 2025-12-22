package com.gqt.dao;

import com.gqt.model.Budget;
import com.gqt.util.HibernateUtil;
import org.hibernate.Session;
import org.hibernate.Transaction;

import java.util.List;

public class BudgetDao {

    public void saveBudget(Budget budget) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = session.beginTransaction();
        session.save(budget);
        tx.commit();
        session.close();
    }

    public List<Budget> getAllBudgets() {
        Session session = HibernateUtil.getSessionFactory().openSession();
        List<Budget> budgets = session.createQuery("from Budget", Budget.class).list();
        session.close();
        return budgets;
    }

    public Budget getBudgetById(int id) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Budget budget = session.get(Budget.class, id);
        session.close();
        return budget;
    }

    public void updateBudget(Budget budget) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = session.beginTransaction();
        session.update(budget);
        tx.commit();
        session.close();
    }

    public void deleteBudget(int id) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = session.beginTransaction();
        Budget budget = session.get(Budget.class, id);
        if (budget != null) {
            session.delete(budget);
        }
        tx.commit();
        session.close();
    }
}