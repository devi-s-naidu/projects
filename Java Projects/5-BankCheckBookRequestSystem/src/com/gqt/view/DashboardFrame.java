package com.gqt.view;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import com.gqt.model.User;

public class DashboardFrame extends JFrame {
    private User user;
    
    public DashboardFrame(User user) {
        this.user = user;
        createUI();
    }
    
    private void createUI() {
        setTitle("Bank Cheque Book Request System - Dashboard");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        
        JPanel panel = new JPanel(new BorderLayout(10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        JPanel headerPanel = new JPanel(new BorderLayout());
        JLabel welcomeLabel = new JLabel("Welcome, " + user.getUsername());
        welcomeLabel.setFont(new Font("Arial", Font.BOLD, 18));
        headerPanel.add(welcomeLabel, BorderLayout.WEST);
        
        JLabel accountLabel = new JLabel("Account: " + user.getAccountNumber());
        headerPanel.add(accountLabel, BorderLayout.EAST);
        
        panel.add(headerPanel, BorderLayout.NORTH);

        JPanel menuPanel = new JPanel(new GridLayout(2, 1, 10, 10));
        menuPanel.setBorder(BorderFactory.createTitledBorder("Services"));
        
        JButton requestChequeBookBtn = new JButton("Request Cheque Book");
        requestChequeBookBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new RequestChequeBookFrame(user).setVisible(true);
            }
        });
        
        JButton viewRequestsBtn = new JButton("View My Requests");
        viewRequestsBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(DashboardFrame.this, 
                    "This feature would show your past requests in a real application",
                    "View Requests", JOptionPane.INFORMATION_MESSAGE);
            }
        });
        
        menuPanel.add(requestChequeBookBtn);
        menuPanel.add(viewRequestsBtn);
        
        panel.add(menuPanel, BorderLayout.CENTER);
        
        JPanel footerPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT));
        JButton logoutBtn = new JButton("Logout");
        logoutBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
                new LoginFrame().setVisible(true); 
            }
        });
        footerPanel.add(logoutBtn);
        panel.add(footerPanel, BorderLayout.SOUTH);
        
        add(panel);
    }
}