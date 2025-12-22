package com.gqt;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class VotingGUI extends JFrame {
    public VotingGUI() {
        setTitle("Online Voting System");
        setSize(500, 350);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        getContentPane().setBackground(new Color(230, 245, 255));

        JLabel heading = new JLabel("Welcome to the Online Voting System");
        heading.setFont(new Font("Segoe UI", Font.BOLD, 18));
        heading.setHorizontalAlignment(SwingConstants.CENTER);
        heading.setForeground(new Color(0, 51, 102));

        JButton loginBtn = new JButton("Login");
        JButton registerBtn = new JButton("Register");
        JButton adminBtn = new JButton("Admin Panel");

        Font btnFont = new Font("Segoe UI", Font.PLAIN, 16);
        loginBtn.setFont(btnFont);
        registerBtn.setFont(btnFont);
        adminBtn.setFont(btnFont);

        JPanel buttonPanel = new JPanel();
        buttonPanel.setBackground(new Color(230, 245, 255));
        buttonPanel.setLayout(new GridLayout(3, 1, 15, 15));
        buttonPanel.setBorder(BorderFactory.createEmptyBorder(30, 100, 30, 100));
        buttonPanel.add(loginBtn);
        buttonPanel.add(registerBtn);
        buttonPanel.add(adminBtn);

        add(heading, BorderLayout.NORTH);
        add(buttonPanel, BorderLayout.CENTER);

        loginBtn.addActionListener(e -> showLoginScreen());
        registerBtn.addActionListener(e -> showRegisterScreen());
        adminBtn.addActionListener(e -> showAdminPanel());

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                DataStore.saveData();
            }
        });

        setVisible(true);
    }

    private void showRegisterScreen() {
        JTextField userField = new JTextField();
        JPasswordField passField = new JPasswordField();
        Object[] fields = {
                "Username:", userField,
                "Password:", passField
        };

        int option = JOptionPane.showConfirmDialog(this, fields, "Register", JOptionPane.OK_CANCEL_OPTION);
        if (option == JOptionPane.OK_OPTION) {
            String user = userField.getText();
            String pass = new String(passField.getPassword());
            if (!DataStore.voters.containsKey(user)) {
                DataStore.voters.put(user, new Voter(user, pass));
                DataStore.saveData();
                JOptionPane.showMessageDialog(this, "Registration Successful.");
            } else {
                JOptionPane.showMessageDialog(this, "User already exists.");
            }
        }
    }

    private void showLoginScreen() {
        JTextField userField = new JTextField();
        JPasswordField passField = new JPasswordField();
        Object[] fields = {
                "Username:", userField,
                "Password:", passField
        };

        int option = JOptionPane.showConfirmDialog(this, fields, "Login", JOptionPane.OK_CANCEL_OPTION);
        if (option == JOptionPane.OK_OPTION) {
            String user = userField.getText();
            String pass = new String(passField.getPassword());

            Voter voter = DataStore.voters.get(user);
            if (voter != null && voter.getPassword().equals(pass)) {
                if (voter.hasVoted()) {
                    JOptionPane.showMessageDialog(this, "You have already voted.");
                } else {
                    showVotingScreen(voter);
                }
            } else {
                JOptionPane.showMessageDialog(this, "Invalid credentials.");
            }
        }
    }

    private void showVotingScreen(Voter voter) {
        String[] candidates = DataStore.candidates.keySet().toArray(new String[0]);
        if (candidates.length == 0) {
            JOptionPane.showMessageDialog(this, "No candidates available.");
            return;
        }

        String selected = (String) JOptionPane.showInputDialog(this, "Vote for:", "Voting",
                JOptionPane.PLAIN_MESSAGE, null, candidates, candidates[0]);

        if (selected != null) {
            DataStore.candidates.get(selected).incrementVotes();
            voter.setVoted(true);
            DataStore.saveData();
            JOptionPane.showMessageDialog(this, "Vote cast successfully.");
        }
    }

    private void showAdminPanel() {
        JPasswordField passField = new JPasswordField();
        int option = JOptionPane.showConfirmDialog(this, passField, "Admin Login (password: admin)", JOptionPane.OK_CANCEL_OPTION);
        if (option == JOptionPane.OK_OPTION && new String(passField.getPassword()).equals("admin")) {
            String[] choices = {"Add Candidate", "Remove Candidate", "View Results"};
            String selected = (String) JOptionPane.showInputDialog(this, "Choose Action:", "Admin Panel",
                    JOptionPane.PLAIN_MESSAGE, null, choices, choices[0]);

            if ("Add Candidate".equals(selected)) {
                String name = JOptionPane.showInputDialog(this, "Enter candidate name:");
                if (name != null && !name.trim().isEmpty()) {
                    DataStore.candidates.put(name, new Candidate(name));
                    DataStore.saveData();
                    JOptionPane.showMessageDialog(this, "Candidate added.");
                }
            } else if ("Remove Candidate".equals(selected)) {
                String name = JOptionPane.showInputDialog(this, "Enter candidate name to remove:");
                if (name != null && DataStore.candidates.containsKey(name)) {
                    DataStore.candidates.remove(name);
                    DataStore.saveData();
                    JOptionPane.showMessageDialog(this, "Candidate removed.");
                }
            } else if ("View Results".equals(selected)) {
                StringBuilder sb = new StringBuilder("Voting Results:\n");
                for (Candidate c : DataStore.candidates.values()) {
                    sb.append(c.getName()).append(": ").append(c.getVotes()).append(" votes\n");
                }
                JOptionPane.showMessageDialog(this, sb.toString());
            }
        } else {
            JOptionPane.showMessageDialog(this, "Access Denied.");
        }
    }

    public static void main(String[] args) {
        DataStore.loadData();
        SwingUtilities.invokeLater(VotingGUI::new);
    }
}
