# 🎓 Student Resource Management System

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

## 📦 Installation

### 1️⃣ Install dependencies

pip install -r requirements.txt

### 2️⃣ Configure MySQL
Create a database:

CREATE DATABASE student_data_base;


---

## ▶️ Running the Application

### Start the FastAPI backend:

uvicorn app.main:app --reload --host 127.0.0.1 --port 8000


### Start the Streamlit UI:
streamlit run ui/student_ui.py


---


---



## 📄 Documentation

- **Architecture Details:** `ARCHITECTURE.md`  
- **AI Recommendation Approach:** `AI_RECOMMENDATION.pdf`

---


