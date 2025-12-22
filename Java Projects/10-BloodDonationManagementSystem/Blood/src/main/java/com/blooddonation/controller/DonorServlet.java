package com.blooddonation.controller;

import com.blooddonation.dao.DonorDAO;
import com.blooddonation.model.Donor;

import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;
import java.util.List;

public class DonorServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String name = request.getParameter("name");
        int age = Integer.parseInt(request.getParameter("age"));
        String bloodGroup = request.getParameter("bloodGroup");
        String contact = request.getParameter("contact");
        String city = request.getParameter("city");

        Donor donor = new Donor();
        donor.setName(name);
        donor.setAge(age);
        donor.setBloodGroup(bloodGroup);
        donor.setContact(contact);
        donor.setCity(city);

        DonorDAO dao = new DonorDAO();
        try {
            dao.saveDonor(donor);
            System.out.println("Donor saved successfully: " + donor.getName());
        } catch (Exception e) {
            System.out.println("Error saving donor: " + e.getMessage());
            e.printStackTrace();
        }

        List<Donor> donors = dao.getAllDonors();
        if (donors != null) {
            System.out.println("Retrieved " + donors.size() + " donors from database");
        } else {
            System.out.println("Error retrieving donors");
        }
        request.setAttribute("donors", donors);
        RequestDispatcher rd = request.getRequestDispatcher("donor_list.jsp");
        rd.forward(request, response);
    }
}
