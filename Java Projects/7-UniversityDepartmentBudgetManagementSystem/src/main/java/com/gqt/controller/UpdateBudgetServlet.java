package com.gqt.controller;

import com.gqt.dao.BudgetDao;
import com.gqt.dao.DepartmentDao;
import com.gqt.model.Budget;
import com.gqt.model.Department;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;

public class UpdateBudgetServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        int budgetId = Integer.parseInt(request.getParameter("id"));
        int deptId = Integer.parseInt(request.getParameter("department"));
        double amount = Double.parseDouble(request.getParameter("amount"));
        int year = Integer.parseInt(request.getParameter("year"));
        String description = request.getParameter("description");

        Department dept = new DepartmentDao().getDepartmentById(deptId);

        Budget budget = new BudgetDao().getBudgetById(budgetId);
        budget.setAmount(amount);
        budget.setYear(year);
        budget.setDescription(description);
        budget.setDepartment(dept);

        new BudgetDao().updateBudget(budget);
        response.sendRedirect("view_budgets.jsp");
    }
}
