# 📞 Call Monitoring System

A **real-time EPBX call monitoring system** with a web dashboard.

The system listens to **EPBX call events**, stores call records in a database, and streams **live updates to a monitoring dashboard using WebSockets**.

---

## 🚀 Features

- Real-time call monitoring
- EPBX event listener
- Call data storage
- Live dashboard updates using WebSockets
- Web interface for monitoring call activity

---

## 🏗 System Architecture

```
EPBX Server
     │
     │ (Call Events)
     ▼
epbx_listener.py
     │
     ▼
database.py
     │
     ▼
websocket_manager.py
     │
     ▼
Dashboard (HTML + WebSocket)
```

---

## 📂 Project Structure

```
call_monitoring_system
│
├── app
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── epbx_listener.py
│   ├── websocket_manager.py
│   └── main.py
│
├── templates
│   └── dashboard.html
│
├── run.py
├── dashboard_server.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/CKChiranjivi/call_monitoring_system.git
```

Move into the project directory:

```bash
cd call_monitoring_system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the System

Start the application:

```bash
python run.py
```

Then open the **dashboard in your browser**.

---

## 🧰 Technologies Used

- Python  
- WebSockets  
- HTML Dashboard  
- EPBX Integration  
- Database Logging  

---

## 🔮 Future Improvements

- Call analytics dashboard  
- Searchable call history  
- Alert system for missed calls  
- Multi-tenant monitoring  

---

## 👨‍💻 Author

**Mr. C.K. Chiranjivi**

GitHub:  
https://github.com/CKChiranjivi
