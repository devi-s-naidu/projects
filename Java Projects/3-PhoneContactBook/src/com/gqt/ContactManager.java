package com.gqt;

import java.io.*;
import java.util.ArrayList;

public class ContactManager {
    private ArrayList<Contact> contactList = new ArrayList<>();
    private final String FILE_NAME = "contacts.txt";

    public void addContact(Contact contact) {
        contactList.add(contact);
        saveContactsToFile();
    }

    public void deleteContact(Contact contact) {
        contactList.remove(contact);
        saveContactsToFile();
    }

    public void editContact(Contact oldContact, Contact newContact) {
        int index = contactList.indexOf(oldContact);
        if (index != -1) {
            contactList.set(index, newContact);
            saveContactsToFile();
        }
    }

    public ArrayList<Contact> getAllContacts() {
        return contactList;
    }

    public void loadContactsFromFile() {
        contactList.clear();
        try (BufferedReader br = new BufferedReader(new FileReader(FILE_NAME))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",", 2);
                if (parts.length == 2) {
                    contactList.add(new Contact(parts[0], parts[1]));
                }
            }
        } catch (IOException e) {
            System.out.println("No existing file found. Starting with empty contact list.");
        }
    }

    public void saveContactsToFile() {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(FILE_NAME))) {
            for (Contact c : contactList) {
                bw.write(c.getName() + "," + c.getPhoneNumber());
                bw.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
