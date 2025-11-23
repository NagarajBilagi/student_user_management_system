# 🎓 Student User Management System

A student user management system prototype that allows students to register, log in, set their academic interest, and retrieve relevant university resources such as workshops, events, and trainings.  
The project also includes a conceptual design for an AI-based recommendation system.

---

## 🚀 Features
- Student registration & login (JWT authentication)
- Store student interests
- Retrieve relevant resources based on selected interest
- Simple Streamlit UI
- FastAPI backend with MySQL database
- AI recommendation concept using SBERT (documented separately)

---

## 🛠️ Tech Stack
- **Python**
- **FastAPI** (Backend)
- **Streamlit** (Frontend UI)
- **MySQL** (Database)
- **SQLAlchemy ORM**
- **JWT Authentication**

---

## Project Structure

```text

user_management_system/
│
├── app/
│   ├── __init__.py
│   ├── config.py          # Environment variables and settings
│   ├── db.py              # Database connection, session handling
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic request/response schemas
│   ├── security.py        # Password hashing & JWT utilities
│   └── main.py            # FastAPI application (routes, logic)
│
├── ui/
│   ├── __init__.py
│   └── student_ui.py      # Streamlit frontend UI
│
├── AI_recommendation.pdf  # Task 4: AI recommendation concept
│
├── requirements.txt       # Python dependencies
├── .gitignore             # Ignored files 
├── README.md              # Project documentation
└── .env                   # Environment variables 

```

---

## 📦 Installation

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Configure MySQL
Create a database:

CREATE DATABASE student_data_base;


---

## ▶️ Running the Application

Before running the commands, make sure you are inside the project root folder:

### Start the FastAPI backend:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### Start the Streamlit UI:

```bash
streamlit run ui/student_ui.py
```


---



## 📄 Documentation

- **Architecture Details:** `ARCHITECTURE.md`  
- **AI Recommendation Approach:** `AI_RECOMMENDATION.pdf`

---


