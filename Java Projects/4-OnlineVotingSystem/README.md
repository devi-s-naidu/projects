# Online Voting System 🗳️💻

A Java-based Online Voting System that allows users to cast votes securely through a graphical interface. This application demonstrates core Java concepts, object-oriented programming, and GUI-based workflow simulation for an election process.

---

## 📌 Features

- 👤 Voter authentication (basic validation)
- 🗳️ Vote casting for multiple candidates
- ❌ Prevention of multiple voting
- 📊 Real-time vote counting
- 🖥️ User-friendly Java Swing interface
- ⚠️ Input validation and alert messages

---

## 🛠️ Technologies Used

- Java (JDK 8+)
- Java Swing
- AWT Event Handling
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```

OnlineVotingSystem/
│
├── src/
│   └── com/gqt/
│       ├── OnlineVotingSystemGUI.java   # Main GUI and entry point
│       ├── Voter.java                   # Voter model
│       ├── Candidate.java               # Candidate model
│       └── VoteManager.java             # Vote handling and counting logic
│
├── bin/
│   └── com/gqt/                          # Compiled class files
│
└── README.md

```

---

## ▶️ How to Run the Project

### 1️⃣ Prerequisites
- Java JDK 8 or above
- Java IDE (Eclipse / IntelliJ IDEA / NetBeans) or terminal

---

### 2️⃣ Run Using IDE (Recommended)

1. Open your IDE
2. Import the project as an Existing Java Project
3. Navigate to:
```

src/com/gqt/OnlineVotingSystemGUI.java

````
4. Run the file

---

### 3️⃣ Run Using Terminal

```bash
cd src
javac com/gqt/*.java
java com.gqt.OnlineVotingSystemGUI
````

---

## 🗳️ Application Workflow

1. User enters voter ID
2. System validates voting eligibility
3. User selects a candidate
4. Vote is recorded securely
5. System updates vote count instantly

---

## 🚀 Future Enhancements

* 🗄️ Database integration for voters and results
* 🔐 Strong authentication & encryption
* 🌐 Web-based voting system
* 📊 Admin dashboard for result analytics
* 🧾 Audit logs for transparency

---

## 📜 License

This project is developed for educational and academic purposes and is free to use and modify.

---