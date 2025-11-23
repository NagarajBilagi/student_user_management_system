#  Student Resource Management & Recommendation System

A student user management system prototype designed for student registration, interest selection, and retrieval of relevant university resources (events, workshops, trainings).  
Built using **Python (FastAPI + Streamlit)**, **MySQL**.

---

##  Project Overview

This system allows students to:

- Register and authenticate using email/password  
- Set their academic interests  
- Retrieve relevant resources based on interests  
- AI-based recommendations using SBERT (Concept)  

The project demonstrates system architecture, backend implementation, database design, and UI integration.

---

##  Features

### ✔ Student Registration & Authentication  
Secure login using hashed passwords and JWT tokens.

### ✔ Interest Selection  
Students choose their interest (AI, Data Science, Robotics, etc.).

### ✔ Resource Retrieval  
Fetch events, workshops, trainings based on selected interest.


---

## 🧩  Use Cases

### **Use Case 1: Student Registration & Login**
**Description:** A student creates an account and logs into the system.  
**Flow:**  
1. Student enters name, email, password.  
2. System hashes password and stores student record.  
3. Student logs in with credentials.  
4. System returns JWT token for authentication.

---

### **Use Case 2: Student Selects Interest & Receives Relevant Resources**
**Description:** A student selects their academic interest, and the system provides all relevant workshops, events, and trainings associated with that interest.

**Flow:**  
1. Student logs in using valid credentials.  
2. Student selects an academic interest (e.g., AI, Robotics, Data Science).  
3. System stores the selected interest inside the `students_data` table.  
4. Student requests relevant resources.  
5. System reads the student’s stored interest.  
6. System queries the `interest_resources` table for matching interest tags.  
7. System returns all associated workshops, trainings and events.  
8. UI displays the retrieved resources to the student.


## 🏗 System Architecture

###  Overview
Streamlit UI <------> FastAPI Backend <------> MySQL Database


- **Streamlit UI**  
  Handles student interaction (Register, Login, Set Interest, View Resources)

- **FastAPI Backend**  
  Provides API endpoints, authentication (JWT), logic and resource retrieval

- **MySQL Database**  
  Stores student data and interest-based resources


---

                     +---------------------------+
                     |    Student Input Data     |
                     |---------------------------|
                     | - Email / Password        |
                     | - Selected Interest       |
                     +---------------------------+
                                  |
                                  v
                 +--------------------------------------+
                 |           Streamlit UI               |
                 |--------------------------------------|
                 | - Sends login data to backend        |
                 | - Sends selected interest to backend |
                 | - Displays returned resources        |
                 +-----------------+--------------------+
                                   |
                                   |  HTTP (JSON, REST API)
                                   v
                 +--------------------------------------+
                 |           FastAPI Backend            |
                 |--------------------------------------|
                 | - /login: authenticate student       |
                 | - /me: get current student           |
                 | - /me/interest: store interest       |
                 | - /resources: fetch resources        |
                 +-----------------+--------------------+
                                   |
                                   |  SQLAlchemy ORM
                                   v
             +------------------------------------------------+
             |                 MySQL Database                 |
             |------------------------------------------------|
             |  Table: students_data                          |
             |    - id, name, email, password_hash, interest  |
             |                                                |
             |  Table: interest_resources                     |
             |    - id, interest_tag, workshop, training,     |
             |      event                                     |
             +-----------------+------------------------------+
                                   |
                                   |  Query:
                                   |  SELECT * FROM interest_resources
                                   |   WHERE interest_tag = student.interest
                                   v
                 +--------------------------------------+
                 |     Filtered Resources Returned      |
                 |--------------------------------------|
                 | - Matching workshops                 |
                 | - Matching trainings                 |
                 | - Matching events                    |
                 +-----------------+--------------------+
                                   |
                                   v
                      +-----------------------------+
                      |    Streamlit UI Output      |
                      |-----------------------------|
                      | - Shows relevant resources  |
                      |   based on student's        |
                      |   selected interest         |
                      +-----------------------------+

---


## 🧩  Main Components / Services

### **1. Streamlit UI**
- Registration form  
- Login form  
- Interest selection  
- View recommended resources  
- Communicates with FastAPI via HTTP  

### **2. FastAPI Backend**
- **Authentication Service**  
  - `/register`, `/login`, `/me`  
  - JWT-based authentication  
- **Student Service**  
  - `/me/interest`  
- **Resource Service**  
  - `/resources?interest=AI`  
- **Recommendation Logic (Basic)**  
  - Matches interest to related resources  

### **3. MySQL Database**
- Stores student accounts  
- Stores interests  
- Stores resources (workshops, trainings, events)  
- Accessed using SQLAlchemy ORM  

---

## 🔄  Data Flow Between Components


### **1. Registration Flow**
UI → /register → FastAPI → MySQL

### **2. Login Flow**
UI → /login → FastAPI → JWT → UI stores token

### **3. Set Interest**
UI → /me/interest (JWT) → FastAPI → MySQL (update column)

### **4. Retrieve Resources**
UI → /resources (JWT)
→ FastAPI (reads interest from students_data)
→ MySQL (finds matching rows in interest_resources)
← returns workshops/events/trainings


---

## 🗄️ Database Schema

### **Table 1 — students_data**
| Column        | Type       | Description                  |
|---------------|------------|------------------------------|
| id            | INT        | Unique ID                    |
| name          | VARCHAR    | Student name                 |
| email         | VARCHAR    | Unique email                 |
| password_hash | VARCHAR    | Hashed password              |
| interest      | VARCHAR    | Selected interest            |

---

### **Table 2 — interest_resources**
| Column       | Type     | Description                         |
|--------------|----------|-------------------------------------|
| id           | INT      | Resource ID                         |
| interest_tag | VARCHAR  | AI, Robotics, DS, etc.              |
| workshop     | TEXT     | Workshop description                |
| training     | TEXT     | Training description                |
| event        | TEXT     | Event detail                        |

---









