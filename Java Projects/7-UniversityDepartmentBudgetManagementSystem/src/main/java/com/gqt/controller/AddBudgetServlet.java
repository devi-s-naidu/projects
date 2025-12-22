package com.gqt.controller;

import com.gqt.dao.BudgetDao;
import com.gqt.dao.DepartmentDao;
import com.gqt.model.Budget;
import com.gqt.model.Department;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;

public class AddBudgetServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        int deptId = Integer.parseInt(request.getParameter("department"));
        double amount = Double.parseDouble(request.getParameter("amount"));
        int year = Integer.parseInt(request.getParameter("year"));
        String desc = request.getParameter("description");

        Department dept = new DepartmentDao().getDepartmentById(deptId);

        Budget budget = new Budget();
        budget.setDepartment(dept);
        budget.setAmount(amount);
        budget.setYear(year);
        budget.setDescription(desc);

        new BudgetDao().saveBudget(budget);
        response.sendRedirect("view_budgets.jsp");
    }
}
