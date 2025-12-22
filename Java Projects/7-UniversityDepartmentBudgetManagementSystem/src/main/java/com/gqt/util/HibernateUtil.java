package com.gqt.util;

import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class HibernateUtil {
    private static final SessionFactory sessionFactory;

    static {
        try {
            sessionFactory = new Configuration().configure().buildSessionFactory();
        } catch (Throwable ex) {
            System.out.println("Initial SessionFactory creation failed." + ex);
            throw new ExceptionInInitializerError(ex);
        }
    }

    public static SessionFactory getSessionFactory() {
        return sessionFactory;
    }
}


//CREATE DATABASE university_budget_db;
//
//USE university_budget_db;
//
//CREATE TABLE departments (
//    id INT PRIMARY KEY AUTO_INCREMENT,
//    name VARCHAR(100),
//    head VARCHAR(100)
//);
//
//CREATE TABLE budgets (
//    id INT PRIMARY KEY AUTO_INCREMENT,
//    department_id INT,
//    amount DOUBLE,
//    year INT,
//    description VARCHAR(255),
//    FOREIGN KEY (department_id) REFERENCES departments(id)
//);
