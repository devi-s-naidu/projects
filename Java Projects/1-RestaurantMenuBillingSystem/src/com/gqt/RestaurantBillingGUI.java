package com.gqt;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.List;

public class RestaurantBillingGUI extends JFrame {

    private JComboBox<MenuItem> itemComboBox;
    private JTextField quantityField;
    private JTextArea billArea;
    private Menu menu;
    private Bill bill;

    public RestaurantBillingGUI() {
        setTitle("🍽 Restaurant Menu Billing System");
        setSize(800, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout(10, 10));

        menu = new Menu();
        bill = new Bill();

        JLabel title = new JLabel("Welcome to Java Restaurant", JLabel.CENTER);
        title.setFont(new Font("Segoe UI", Font.BOLD, 24));
        title.setForeground(new Color(128, 0, 64));
        add(title, BorderLayout.NORTH);

        JPanel inputPanel = new JPanel();
        inputPanel.setBorder(BorderFactory.createTitledBorder("Order Section"));
        inputPanel.setLayout(new BoxLayout(inputPanel, BoxLayout.Y_AXIS));
        inputPanel.setBackground(new Color(255, 248, 220));

        itemComboBox = new JComboBox<>(menu.getItems().toArray(new MenuItem[0]));
        itemComboBox.setFont(new Font("Segoe UI", Font.PLAIN, 16));
        quantityField = new JTextField(5);
        quantityField.setFont(new Font("Segoe UI", Font.PLAIN, 16));
        JButton addButton = new JButton("Add to Bill");
        addButton.setBackground(new Color(50, 205, 50));
        addButton.setFont(new Font("Segoe UI", Font.BOLD, 16));

        JPanel row1 = new JPanel(new FlowLayout(FlowLayout.LEFT));
        row1.setBackground(inputPanel.getBackground());
        row1.add(new JLabel("Select Item: "));
        row1.add(itemComboBox);
        inputPanel.add(row1);

        JPanel row2 = new JPanel(new FlowLayout(FlowLayout.LEFT));
        row2.setBackground(inputPanel.getBackground());
        row2.add(new JLabel("Quantity:    "));
        row2.add(quantityField);
        inputPanel.add(row2);

        JPanel row3 = new JPanel(new FlowLayout(FlowLayout.CENTER));
        row3.setBackground(inputPanel.getBackground());
        row3.add(addButton);
        inputPanel.add(row3);

        add(inputPanel, BorderLayout.WEST);

        billArea = new JTextArea();
        billArea.setFont(new Font("Monospaced", Font.PLAIN, 14));
        billArea.setEditable(false);
        billArea.setBorder(BorderFactory.createTitledBorder("Bill Details"));
        billArea.setBackground(new Color(245, 245, 245));
        JScrollPane scrollPane = new JScrollPane(billArea);
        add(scrollPane, BorderLayout.CENTER);

        JPanel menuPanel = new JPanel(new BorderLayout());
        menuPanel.setBorder(BorderFactory.createTitledBorder("Available Menu"));
        JTable menuTable = createMenuTable();
        menuPanel.add(new JScrollPane(menuTable), BorderLayout.CENTER);
        menuPanel.setPreferredSize(new Dimension(300, 0));
        add(menuPanel, BorderLayout.EAST);

        JButton finalizeButton = new JButton("Generate Final Bill");
        finalizeButton.setFont(new Font("Segoe UI", Font.BOLD, 16));
        finalizeButton.setBackground(new Color(70, 130, 180));
        finalizeButton.setForeground(Color.WHITE);
        add(finalizeButton, BorderLayout.SOUTH);

        addButton.addActionListener(e -> {
            try {
                MenuItem selected = (MenuItem) itemComboBox.getSelectedItem();
                int quantity = Integer.parseInt(quantityField.getText());

                if (quantity <= 0) throw new NumberFormatException();

                OrderItem oi = new OrderItem(selected, quantity);
                bill.addOrderItem(oi);
                billArea.append(oi.getDetails() + "\n");
                quantityField.setText("");

            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "Enter a valid quantity!", "Input Error", JOptionPane.ERROR_MESSAGE);
            }
        });

        finalizeButton.addActionListener(e -> {
            billArea.append("\n" + bill.generateBill());
            finalizeButton.setEnabled(false);
        });

        setVisible(true);
    }

    private JTable createMenuTable() {
        String[] columnNames = {"ID", "Item Name", "Price (₹)"};
        List<MenuItem> items = menu.getItems();
        Object[][] data = new Object[items.size()][3];

        for (int i = 0; i < items.size(); i++) {
            MenuItem mi = items.get(i);
            data[i][0] = mi.getId();
            data[i][1] = mi.getName();
            data[i][2] = String.format("%.2f", mi.getPrice());
        }

        JTable table = new JTable(data, columnNames);
        table.setFont(new Font("Segoe UI", Font.PLAIN, 14));
        table.setRowHeight(28);
        table.setGridColor(Color.LIGHT_GRAY);
        table.setEnabled(false);
        table.getTableHeader().setFont(new Font("Segoe UI", Font.BOLD, 15));
        table.getTableHeader().setBackground(new Color(230, 230, 250));
        table.setBackground(new Color(255, 250, 240));

        return table;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(RestaurantBillingGUI::new);
    }
}
