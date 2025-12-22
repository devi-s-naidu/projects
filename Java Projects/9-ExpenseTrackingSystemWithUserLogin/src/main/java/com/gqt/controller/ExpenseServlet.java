package com.gqt.controller;

import com.gqt.model.*;
import com.gqt.util.HibernateUtil;
import org.hibernate.Session;
import org.hibernate.Transaction;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class ExpenseServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String title = request.getParameter("title");
        double amount = Double.parseDouble(request.getParameter("amount"));
        String dateStr = request.getParameter("date");

        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
        Date date = null;
        try { date = sdf.parse(dateStr); } catch (Exception e) { }

        HttpSession hs = request.getSession();
        User user = (User) hs.getAttribute("user");

        Expense exp = new Expense();
        exp.setTitle(title);
        exp.setAmount(amount);
        exp.setDate(date);
        exp.setUser(user);

        Session hibSession = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = hibSession.beginTransaction();
        hibSession.save(exp);
        tx.commit();
        hibSession.close();

        response.sendRedirect("home.jsp");
    }
}
