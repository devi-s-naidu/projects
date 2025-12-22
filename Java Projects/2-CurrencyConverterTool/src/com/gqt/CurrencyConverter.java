package com.gqt;
import javax.swing.*;
import javax.swing.Timer;

import java.awt.*;
import java.awt.event.*;
import java.text.SimpleDateFormat;
import java.util.*;

public class CurrencyConverter extends JFrame implements ActionListener {

    private JComboBox<String> fromCurrency, toCurrency;
    private JTextField amountField;
    private JLabel resultLabel, timeLabel;
    private JTextArea historyArea;
    private JButton convertButton, clearButton;

    private HashMap<String, Double> exchangeRates;

    public CurrencyConverter() {
        setTitle("Currency Converter Tool");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        setLocationRelativeTo(null);

        initializeExchangeRates();
        initUI();
        updateTime();
    }

    private void initializeExchangeRates() {
        exchangeRates = new HashMap<>();
        exchangeRates.put("USD", 1.0);      
        exchangeRates.put("INR", 85.68);
        exchangeRates.put("EUR", 0.88);
        exchangeRates.put("JPY", 144.63);
        exchangeRates.put("GBP", 0.74);
        exchangeRates.put("AUD", 1.54);
    }

    private void initUI() {
        // Title Panel
        JPanel titlePanel = new JPanel(new BorderLayout());
        JLabel titleLabel = new JLabel("💱 Currency Converter", SwingConstants.CENTER);
        titleLabel.setFont(new Font("Verdana", Font.BOLD, 22));
        titlePanel.add(titleLabel, BorderLayout.CENTER);
        timeLabel = new JLabel("", SwingConstants.RIGHT);
        timeLabel.setFont(new Font("Arial", Font.PLAIN, 12));
        titlePanel.add(timeLabel, BorderLayout.SOUTH);
        add(titlePanel, BorderLayout.NORTH);

        // Input Panel
        JPanel inputPanel = new JPanel(new GridBagLayout());
        inputPanel.setBorder(BorderFactory.createTitledBorder("Conversion Panel"));
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 10, 10, 10);
        gbc.fill = GridBagConstraints.HORIZONTAL;

        String[] currencies = exchangeRates.keySet().toArray(new String[0]);

        gbc.gridx = 0; gbc.gridy = 0;
        inputPanel.add(new JLabel("From Currency:"), gbc);
        gbc.gridx = 1;
        fromCurrency = new JComboBox<>(currencies);
        inputPanel.add(fromCurrency, gbc);

        gbc.gridx = 0; gbc.gridy = 1;
        inputPanel.add(new JLabel("To Currency:"), gbc);
        gbc.gridx = 1;
        toCurrency = new JComboBox<>(currencies);
        inputPanel.add(toCurrency, gbc);

        gbc.gridx = 0; gbc.gridy = 2;
        inputPanel.add(new JLabel("Amount:"), gbc);
        gbc.gridx = 1;
        amountField = new JTextField();
        inputPanel.add(amountField, gbc);

        gbc.gridx = 0; gbc.gridy = 3;
        convertButton = new JButton("Convert");
        convertButton.setBackground(new Color(34, 139, 34));
        convertButton.setForeground(Color.WHITE);
        convertButton.addActionListener(this);
        inputPanel.add(convertButton, gbc);

        gbc.gridx = 1;
        clearButton = new JButton("Clear");
        clearButton.setBackground(Color.DARK_GRAY);
        clearButton.setForeground(Color.WHITE);
        clearButton.addActionListener(e -> clearFields());
        inputPanel.add(clearButton, gbc);

        gbc.gridx = 0; gbc.gridy = 4; gbc.gridwidth = 2;
        resultLabel = new JLabel("Converted amount: ", SwingConstants.CENTER);
        resultLabel.setFont(new Font("Arial", Font.BOLD, 16));
        inputPanel.add(resultLabel, gbc);

        add(inputPanel, BorderLayout.CENTER);

        // History Panel
        JPanel historyPanel = new JPanel(new BorderLayout());
        historyPanel.setBorder(BorderFactory.createTitledBorder("Conversion History"));
        historyArea = new JTextArea(5, 30);
        historyArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(historyArea);
        historyPanel.add(scrollPane, BorderLayout.CENTER);

        add(historyPanel, BorderLayout.SOUTH);
    }

    private void updateTime() {
        Timer timer = new Timer(1000, e -> {
            String timeStamp = new SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss").format(new Date());
            timeLabel.setText("🕒 " + timeStamp + "   ");
        });
        timer.start();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String from = (String) fromCurrency.getSelectedItem();
        String to = (String) toCurrency.getSelectedItem();
        String input = amountField.getText();

        try {
            double amount = Double.parseDouble(input);
            double inUSD = amount / exchangeRates.get(from);
            double converted = inUSD * exchangeRates.get(to);

            String result = String.format("%.2f %s = %.2f %s", amount, from, converted, to);
            resultLabel.setText("✔ " + result);
            historyArea.append(result + "\n");

        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Enter a valid numeric amount.", "Invalid Input", JOptionPane.WARNING_MESSAGE);
        }
    }

    private void clearFields() {
        amountField.setText("");
        resultLabel.setText("Converted amount: ");
        historyArea.setText("");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new CurrencyConverter().setVisible(true));
    }
}
