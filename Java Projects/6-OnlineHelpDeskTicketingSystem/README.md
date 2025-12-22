# Online Help Desk Ticketing System 🎫💻

A Java-based Online Help Desk Ticketing System that allows users to raise support tickets and track their status through a simple graphical interface. This project simulates a real-world IT support workflow and demonstrates Java GUI development and object-oriented programming concepts.

---

## 📌 Features

- 📝 Create new support tickets
- 🆔 Auto-generated ticket ID
- 📂 View all submitted tickets
- 🔄 Track ticket status (Open / In Progress / Closed)
- 🖥️ User-friendly Java Swing GUI
- ⚠️ Input validation and alert messages
- 🎯 Efficient ticket management simulation

---

## 🛠️ Technologies Used

- Java (JDK 8+)
- Java Swing
- AWT Event Handling
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```

OnlineHelpDeskTicketingSystem/
│
├── src/
│   └── com/gqt/
│       ├── HelpDeskTicketingGUI.java   # Main GUI and entry point
│       ├── Ticket.java                # Ticket model
│       ├── User.java                  # User details
│       └── TicketManager.java         # Ticket handling logic
│
├── bin/
│   └── com/gqt/                        # Compiled class files
│
└── README.md

```

---

## ▶️ How to Run the Project

### 1️⃣ Prerequisites
- Java JDK 8 or higher
- Java IDE (Eclipse / IntelliJ IDEA / NetBeans) or terminal

---

### 2️⃣ Run Using IDE (Recommended)

1. Open your IDE
2. Import the project as an Existing Java Project
3. Navigate to:
```

src/com/gqt/HelpDeskTicketingGUI.java

````
4. Run the file

---

### 3️⃣ Run Using Terminal

```bash
cd src
javac com/gqt/*.java
java com.gqt.HelpDeskTicketingGUI
````

---

## 🎫 Application Workflow

1. User enters issue details
2. System generates a ticket ID
3. Ticket is added with Open status
4. User can view and track ticket progress
5. Status updates simulate support resolution

---

## 🚀 Future Enhancements

* 🗄️ Database integration (MySQL / MongoDB)
* 🔐 User authentication and role-based access
* 📧 Email notifications for ticket updates
* 📊 Admin dashboard and analytics
* 🌐 Web-based help desk system

---

## 📜 License

This project is developed for educational and academic purposes and is free to use and modify.

---