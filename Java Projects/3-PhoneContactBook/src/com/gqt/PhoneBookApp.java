package com.gqt;

import javax.swing.*;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
import java.awt.*;
import java.util.List;
import java.util.stream.Collectors;

public class PhoneBookApp extends JFrame {
    private ContactManager contactManager = new ContactManager();
    private DefaultListModel<Contact> listModel = new DefaultListModel<>();
    private JList<Contact> contactJList = new JList<>(listModel);

    private JTextField searchField = new JTextField();
    private java.util.List<Contact> allContacts = new java.util.ArrayList<>();

    public PhoneBookApp() {
        setTitle("Phone Contact Book");
        setSize(400, 550);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout(10, 10));
        setResizable(false);

        JPanel inputPanel = new JPanel(new GridLayout(3, 2, 5, 5));
        inputPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        JTextField nameField = new JTextField();
        JTextField phoneField = new JTextField();

        JButton addButton = new JButton("Add Contact");
        addButton.setBackground(new Color(76, 175, 80));
        addButton.setForeground(Color.WHITE);

        inputPanel.add(new JLabel("Name:"));
        inputPanel.add(nameField);
        inputPanel.add(new JLabel("Phone Number:"));
        inputPanel.add(phoneField);
        inputPanel.add(new JLabel());
        inputPanel.add(addButton);

        JPanel searchPanel = new JPanel(new BorderLayout(5, 5));
        searchPanel.setBorder(BorderFactory.createEmptyBorder(0, 10, 0, 10));
        searchPanel.add(new JLabel("Search:"), BorderLayout.WEST);
        searchPanel.add(searchField, BorderLayout.CENTER);

        contactJList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        contactJList.setFont(new Font("SansSerif", Font.PLAIN, 14));
        JScrollPane listScrollPane = new JScrollPane(contactJList);
        listScrollPane.setBorder(BorderFactory.createTitledBorder("Your Contacts"));

        JButton deleteButton = new JButton("Delete Selected");
        deleteButton.setBackground(new Color(244, 67, 54));
        deleteButton.setForeground(Color.WHITE);

        JButton editButton = new JButton("Edit Selected");
        editButton.setBackground(new Color(255, 152, 0));
        editButton.setForeground(Color.WHITE);

        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 20, 10));
        buttonPanel.add(editButton);
        buttonPanel.add(deleteButton);

        JPanel centerPanel = new JPanel(new BorderLayout());
        centerPanel.add(searchPanel, BorderLayout.NORTH);
        centerPanel.add(listScrollPane, BorderLayout.CENTER);

        add(inputPanel, BorderLayout.NORTH);
        add(centerPanel, BorderLayout.CENTER);
        add(buttonPanel, BorderLayout.SOUTH);

        contactManager.loadContactsFromFile();
        allContacts = contactManager.getAllContacts();
        updateList(allContacts);

        addButton.addActionListener(e -> {
            String name = nameField.getText().trim();
            String phone = phoneField.getText().trim();
            if (!name.isEmpty() && !phone.isEmpty()) {
                Contact contact = new Contact(name, phone);
                contactManager.addContact(contact);
                allContacts.add(contact);
                updateList(filterContacts(searchField.getText().trim()));
                nameField.setText("");
                phoneField.setText("");
            } else {
                JOptionPane.showMessageDialog(this, "Please enter both name and phone number.");
            }
        });

        deleteButton.addActionListener(e -> {
            Contact selected = contactJList.getSelectedValue();
            if (selected != null) {
                int confirm = JOptionPane.showConfirmDialog(this, "Are you sure you want to delete " + selected.getName() + "?", "Confirm Delete", JOptionPane.YES_NO_OPTION);
                if (confirm == JOptionPane.YES_OPTION) {
                    contactManager.deleteContact(selected);
                    allContacts.remove(selected);
                    updateList(filterContacts(searchField.getText().trim()));
                }
            }
        });

        editButton.addActionListener(e -> {
            Contact selected = contactJList.getSelectedValue();
            if (selected != null) {
                String newName = JOptionPane.showInputDialog(this, "Edit Name:", selected.getName());
                String newPhone = JOptionPane.showInputDialog(this, "Edit Phone Number:", selected.getPhoneNumber());

                if (newName != null && newPhone != null && !newName.trim().isEmpty() && !newPhone.trim().isEmpty()) {
                    contactManager.editContact(selected, new Contact(newName.trim(), newPhone.trim()));
                    allContacts = contactManager.getAllContacts();
                    updateList(filterContacts(searchField.getText().trim()));
                }
            }
        });

        searchField.getDocument().addDocumentListener(new DocumentListener() {
            public void insertUpdate(DocumentEvent e) {
                updateList(filterContacts(searchField.getText().trim()));
            }

            public void removeUpdate(DocumentEvent e) {
                updateList(filterContacts(searchField.getText().trim()));
            }

            public void changedUpdate(DocumentEvent e) {
                updateList(filterContacts(searchField.getText().trim()));
            }
        });
    }

    private void updateList(List<Contact> contacts) {
        listModel.clear();
        for (Contact c : contacts) {
            listModel.addElement(c);
        }
    }

    private List<Contact> filterContacts(String query) {
        if (query.isEmpty()) {
            return allContacts;
        }
        return allContacts.stream()
                .filter(c -> c.getName().toLowerCase().contains(query.toLowerCase()))
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new PhoneBookApp().setVisible(true));
    }
}
