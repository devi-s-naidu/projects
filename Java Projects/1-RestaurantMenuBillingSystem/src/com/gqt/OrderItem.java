package com.gqt;

public class OrderItem {
    private MenuItem item;
    private int quantity;

    public OrderItem(MenuItem item, int quantity) {
        this.item = item;
        this.quantity = quantity;
    }

    public double getTotalPrice() {
        return item.getPrice() * quantity;
    }

    public String getDetails() {
        return item.getName() + " x " + quantity + " = ₹" + String.format("%.2f", getTotalPrice());
    }

    public double getPrice() {
        return getTotalPrice();
    }
}
