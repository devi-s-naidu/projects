package com.gqt.controller;

import com.gqt.dao.BudgetDao;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;

public class DeleteBudgetServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        int budgetId = Integer.parseInt(request.getParameter("id"));
        new BudgetDao().deleteBudget(budgetId);
        response.sendRedirect("view_budgets.jsp");
    }
}
