package com.gqt.view;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Date;
import java.util.UUID;
import com.gqt.model.User;
import com.gqt.model.ChequeBookRequest;

public class RequestChequeBookFrame extends JFrame {
    private User user;
    private JComboBox<Integer> leavesComboBox;
    
    public RequestChequeBookFrame(User user) {
        this.user = user;
        createUI();
    }
    
    private void createUI() {
        setTitle("Request Cheque Book");
        setSize(500, 300);
        setLocationRelativeTo(null);
        
        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 10, 10, 10);
        gbc.fill = GridBagConstraints.HORIZONTAL;
        
        JLabel titleLabel = new JLabel("Cheque Book Request");
        titleLabel.setFont(new Font("Arial", Font.BOLD, 18));
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridwidth = 2;
        gbc.anchor = GridBagConstraints.CENTER;
        panel.add(titleLabel, gbc);
        
        gbc.gridy = 1;
        gbc.gridwidth = 2;
        panel.add(new JLabel("Account Number: " + user.getAccountNumber()), gbc);

        gbc.gridy = 2;
        gbc.gridwidth = 1;
        panel.add(new JLabel("Number of Leaves:"), gbc);
        
        gbc.gridx = 1;
        Integer[] leavesOptions = {25, 50, 100};
        leavesComboBox = new JComboBox<>(leavesOptions);
        panel.add(leavesComboBox, gbc);
        
        gbc.gridx = 0;
        gbc.gridy = 3;
        gbc.gridwidth = 2;
        JButton submitButton = new JButton("Submit Request");
        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                submitRequest();
            }
        });
        panel.add(submitButton, gbc);
        
        add(panel);
    }
    
    private void submitRequest() {
        int numberOfLeaves = (Integer) leavesComboBox.getSelectedItem();

        String requestId = UUID.randomUUID().toString().substring(0, 8);
        ChequeBookRequest request = new ChequeBookRequest(
            requestId, 
            user.getAccountNumber(), 
            new Date(), 
            "Pending", 
            numberOfLeaves
        );
        
        JOptionPane.showMessageDialog(this, 
            "Cheque book request submitted successfully!\n" +
            "Request ID: " + requestId + "\n" +
            "Number of Leaves: " + numberOfLeaves + "\n" +
            "Status: Pending",
            "Request Submitted", 
            JOptionPane.INFORMATION_MESSAGE);
        
        dispose(); 
    }
}