#  Finance Dashboard Backend

A production-style backend system for managing financial records with role-based access control (RBAC), JWT authentication, and PostgreSQL persistence.

---

##  Overview

This project implements a backend for a finance dashboard where users can:

* Manage financial records (income / expense)
* View analytics and summaries
* Access data based on roles (**Admin, Analyst, Viewer**)

The system is designed with clean architecture, secure authentication, and scalable data handling.

---

##  Tech Stack

* **Backend:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Authentication:** JWT (JSON Web Tokens)
* **Password Hashing:** bcrypt (via Passlib)
* **API Docs:** Swagger UI (FastAPI built-in)

---

##  Project Structure

```
app/
├── core/
│   ├── auth.py
│   ├── security.py
│   ├── database.py
│   ├── deps.py
│   └── response.py
│
├── models/
│   └── db_models.py
│
├── schemas/
│   ├── user.py
│   └── record.py
│
├── services/
│   ├── user_service.py
│   └── record_service.py
│
├── routes/
│   ├── auth.py
│   ├── users.py
│   ├── records.py
│   └── dashboard.py
│
└── main.py
```

---

##  Features

###  Authentication & Authorization

* JWT-based login system
* Secure password hashing
* Role-Based Access Control (RBAC)

---

###  User Management

* Create users
* Assign roles (**Admin, Analyst, Viewer**)
* Manage active/inactive status

---

###  Financial Records

* Create, update, delete records

**Fields:**

* Amount
* Type (income / expense)
* Category
* Date
* Notes

**Filtering:**

* By type
* By category
* By date

---

###  Dashboard APIs

* Total income
* Total expenses
* Net balance
* Category-wise breakdown
* Monthly trends
* Recent activity

---

##  Access Control

| Role    | Permissions                        |
| ------- | ---------------------------------- |
| Viewer  | View records & dashboard only      |
| Analyst | View records + analytics           |
| Admin   | Full access (CRUD users & records) |

---

##  API Documentation

* Swagger UI:
  http://127.0.0.1:8000/docs

* Public (ngrok example):
  https://your-ngrok-url/docs

---

##  Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/Mohamed-Fasidh/Finance-Data.git
cd Finance-Data
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Configure Database

Update `.env` or config:

```
DATABASE_URL=postgresql://username:password@localhost:5432/finance_db
```

### 5. Run Server

```
uvicorn app.main:app --reload
```

### 6. Open API Docs

```
http://127.0.0.1:8000/docs
```

---

##  Authentication Flow

1. Register user
2. Login → get JWT token
3. Click **Authorize** in Swagger
4. Paste token:

```
Bearer <your_token>
```

---

##  API Endpoints

###  Auth

* `POST /auth/register` → Register user
* `POST /auth/login` → Login & get token

---

###  Users

* `POST /users/` → Create user (Admin only)
* `GET /users/` → Get users
* `PUT /users/{id}` → Update user

---

###  Records

* `POST /records/` → Create record
* `GET /records/` → Get records
* `PUT /records/{id}` → Update record
* `DELETE /records/{id}` → Delete record

---

###  Dashboard

* `GET /dashboard/summary`
* `GET /dashboard/recent`
* `GET /dashboard/monthly-trends`

---

##  Design Decisions

* JWT authentication for stateless security
* Role-based access control for authorization
* SQLAlchemy ORM for scalable DB operations
* PostgreSQL for reliable persistence
* User-level data isolation for security

---

##  Assumptions

* Users are uniquely identified by email
* Admin role has full access
* Records are linked via `user_id`
* Simplified validation for demo purposes

---

##  Future Improvements

* Pagination for records
* Advanced filtering & search
* Refresh tokens
* Docker deployment
* Unit & integration tests
* API rate limiting

---
