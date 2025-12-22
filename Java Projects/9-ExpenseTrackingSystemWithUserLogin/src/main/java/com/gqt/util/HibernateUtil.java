package com.gqt.util;

import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class HibernateUtil {
    private static final SessionFactory sessionFactory;
    static {
        try {
            sessionFactory = new Configuration().configure().buildSessionFactory();
        } catch (Throwable ex) {
            throw new ExceptionInInitializerError(ex);
        }
    }

    public static SessionFactory getSessionFactory() {
        return sessionFactory;
    }
}

//SQL script
//CREATE DATABASE expense_db;

//USE expense_db;

//CREATE TABLE users (
    //id INT PRIMARY KEY AUTO_INCREMENT,
    //name VARCHAR(100),
    //email VARCHAR(100) UNIQUE,
    //password VARCHAR(100)
//);

//CREATE TABLE expenses (
    //id INT PRIMARY KEY AUTO_INCREMENT,
    //title VARCHAR(100),
    //amount DOUBLE,
    //date DATE,
    //user_id INT,
    //FOREIGN KEY (user_id) REFERENCES users(id)
//);
