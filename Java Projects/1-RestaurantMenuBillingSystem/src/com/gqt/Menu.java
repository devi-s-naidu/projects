package com.gqt;

import java.util.*;

public class Menu {
    private List<MenuItem> items;

    public Menu() {
        items = new ArrayList<>();
        items.add(new MenuItem(1, "Masala Dosa", 40));
        items.add(new MenuItem(2, "Idli Vada", 30));
        items.add(new MenuItem(3, "Paneer Butter Masala", 120));
        items.add(new MenuItem(4, "Veg Pulao", 80));
        items.add(new MenuItem(5, "Coffee", 20));
    }

    public List<MenuItem> getItems() {
        return items;
    }
}
