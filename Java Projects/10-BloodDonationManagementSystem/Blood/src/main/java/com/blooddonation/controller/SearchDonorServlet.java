package com.blooddonation.controller;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class SearchDonorServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String blood = request.getParameter("blood");
        String city = request.getParameter("city");

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<h2>Search Results</h2>");
        out.println("<style>.error { color: red; }.result { margin: 10px; }</style>");

        try {

            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/blood_db", "root", "2003");

            PreparedStatement ps = con.prepareStatement("SELECT * FROM donors WHERE bloodGroup=? AND city=?");
            ps.setString(1, blood);
            ps.setString(2, city);

            ResultSet rs = ps.executeQuery();
            
            if (!rs.next()) {
                out.println("<div class='result'>No donors found matching your criteria.</div>");
            } else {
                do {
                    out.println("<div class='result'>");
                    out.println("<p>Name: " + rs.getString("name") + "</p>");
                    out.println("<p>Blood Group: " + rs.getString("bloodGroup") + "</p>");
                    out.println("<p>City: " + rs.getString("city") + "</p>");
                    out.println("</div>");
                } while (rs.next());
            }

            rs.close();
            ps.close();
            con.close();
        } catch (ClassNotFoundException e) {
            out.println("<div class='error'>MySQL driver not found. Please ensure MySQL JDBC driver is in your classpath.</div>");
        } catch (SQLException e) {
            out.println("<div class='error'>Database error: " + e.getMessage() + "</div>");
        } catch (Exception e) {
            out.println("<div class='error'>An error occurred: " + e.getMessage() + "</div>");
        }
    }
}
