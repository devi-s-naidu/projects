package com.gqt;

import java.util.*;

public class Bill {
    private List<OrderItem> orderItems;

    public Bill() {
        orderItems = new ArrayList<>();
    }

    public void addOrderItem(OrderItem oi) {
        orderItems.add(oi);
    }

    public String generateBill() {
        double subtotal = 0;
        StringBuilder sb = new StringBuilder();
        sb.append("\n----- Final Bill -----\n");

        for (OrderItem oi : orderItems) {
            sb.append(oi.getDetails()).append("\n");
            subtotal += oi.getPrice();
        }

        double tax = subtotal * 0.05;
        double total = subtotal + tax;

        sb.append("\nSubtotal: ₹").append(String.format("%.2f", subtotal));
        sb.append("\nGST (5%): ₹").append(String.format("%.2f", tax));
        sb.append("\nTotal: ₹").append(String.format("%.2f", total));
        sb.append("\n-----------------------\nThank you! Please Visit Again!");

        return sb.toString();
    }
}

