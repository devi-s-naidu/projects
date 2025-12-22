# Restaurant Menu Billing System 🍽️💳

A Java Swing–based desktop application that simulates a simple restaurant billing system.  
The application allows users to select menu items, specify quantities, generate a bill, and calculate GST automatically with a clean and user-friendly GUI.

---

## 📌 Features

- 📋 Predefined restaurant menu with item prices
- ➕ Add multiple items with quantity selection
- 🧾 Auto-generated bill with:
  - Item-wise total
  - Subtotal
  - GST (5%)
  - Final payable amount
- 🖥️ Modern Swing-based GUI
- ❌ Input validation and user-friendly alerts
- 🧮 Accurate price calculations

---

## 🛠️ Technologies Used

- Java (JDK 8+)
- Java Swing (GUI)
- AWT Event Handling
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```

RestaurantMenuBillingSystem/
│
├── src/
│   └── com/gqt/
│       ├── RestaurantBillingGUI.java   # Main GUI and application entry point
│       ├── Menu.java                   # Menu management
│       ├── MenuItem.java               # Menu item model
│       ├── OrderItem.java              # Order item with quantity
│       └── Bill.java                   # Bill generation and calculations
│
├── bin/
│   └── com/gqt/                         # Compiled .class files
│
└── README.md

```

---

## ▶️ How to Run the Project

### 1️⃣ Prerequisites
- Java JDK 8 or higher
- Any Java IDE (Eclipse / IntelliJ IDEA / NetBeans) or terminal

---

### 2️⃣ Run Using IDE (Recommended)

1. Open your IDE
2. Import the project as Existing Java Project
3. Navigate to:
```

src/com/gqt/RestaurantBillingGUI.java

````
4. Run the file

---

### 3️⃣ Run Using Terminal

```bash
cd src
javac com/gqt/*.java
java com.gqt.RestaurantBillingGUI
````

---

## 🧾 Sample Bill Output

```
Item            Qty     Price
--------------------------------
Masala Dosa     2       ₹80
Coffee          1       ₹20

Subtotal: ₹100.00
GST (5%): ₹5.00
Total: ₹105.00
--------------------------------
Thank you! Please Visit Again!
```

---

## 🔍 Core Classes Overview

* RestaurantBillingGUI

  * Handles UI, user interaction, and event handling
* Menu

  * Stores and provides available menu items
* MenuItem

  * Represents a food item with ID, name, and price
* OrderItem

  * Represents selected menu item with quantity
* Bill

  * Calculates subtotal, GST, and total amount
  * Generates formatted bill output

---

## 🚀 Future Enhancements

* 🗄️ Database integration (MySQL)
* 🧾 Print / PDF bill generation
* 👤 User login and role management
* 🍕 Dynamic menu management
* 📊 Daily sales reports

---

## 📜 License

This project is developed for educational and academic purposes and is free to use and modify.

---