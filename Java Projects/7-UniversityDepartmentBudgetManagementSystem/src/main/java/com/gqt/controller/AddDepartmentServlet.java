package com.gqt.controller;

import com.gqt.dao.DepartmentDao;
import com.gqt.model.Department;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;

public class AddDepartmentServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String name = request.getParameter("name");
        String head = request.getParameter("head");

        Department dept = new Department();
        dept.setName(name);
        dept.setHead(head);

        new DepartmentDao().saveDepartment(dept);

        response.sendRedirect("index.jsp");
    }
}
