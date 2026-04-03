# Finance Dashboard Backend

A backend system for managing financial records with role-based access control, JWT authentication, and PostgreSQL persistence.

---

## Overview

This project implements a backend service for a finance dashboard where users can:

- Manage financial records (income and expenses)
- View analytics and summaries
- Access data based on role permissions

The system is designed with clear structure, secure authentication, and reliable data handling.

---

## Tech Stack

- Backend: FastAPI  
- Database: PostgreSQL (Render Cloud DB)  
- ORM: SQLAlchemy  
- Authentication: JWT (JSON Web Tokens)  
- Password Hashing: bcrypt (Passlib)  
- API Documentation: Swagger UI  

---

## Live API

- Swagger Documentation:  
  https://finance-data-1.onrender.com/docs

---

## Project Structure


app/
├── core/
│ ├── auth.py
│ ├── security.py
│ ├── database.py
│ ├── deps.py
│ └── response.py
│
├── models/
│ └── db_models.py
│
├── schemas/
│ ├── user.py
│ └── record.py
│
├── services/
│ ├── user_service.py
│ └── record_service.py
│
├── routes/
│ ├── auth.py
│ ├── users.py
│ ├── records.py
│ └── dashboard.py
│
└── main.py


---

## Features

### Authentication & Authorization

- JWT-based login system  
- Secure password hashing using bcrypt  
- Role-based access control  

---

### User Management

- Create and manage users  
- Assign roles (Admin, Analyst, Viewer)  
- Maintain active/inactive status  

---

### Financial Records

Supports full CRUD operations:

- Create records  
- View records  
- Update records  
- Delete records  

Fields:

- Amount  
- Type (income / expense)  
- Category  
- Date  
- Notes  

Filtering support:

- By type  
- By category  
- Pagination support  

---

### Dashboard APIs

Provides aggregated data:

- Total income  
- Total expenses  
- Net balance  
- Category-wise totals  
- Monthly trends  
- Recent activity  

---

## Access Control

| Role    | Permissions                          |
|---------|--------------------------------------|
| Viewer  | View records and dashboard           |
| Analyst | View records and analytics           |
| Admin   | Full access (users + records CRUD)   |

---

## Authentication Flow

1. Register a user  
2. Login to receive JWT token  
3. Click **Authorize** in Swagger  
4. Enter:


Bearer <your_token>


---

## API Endpoints

### Auth

- `POST /auth/register` — Register user  
- `POST /auth/login` — Login and get token  

---

### Users

- `POST /users/` — Create user (Admin only)  
- `GET /users/` — Get users  
- `PUT /users/{id}` — Update user  

---

### Records

- `POST /records/` — Create record (Admin only)  
- `GET /records/` — Get records (role-based access)  
- `PUT /records/{id}` — Update record (Admin only)  
- `DELETE /records/{id}` — Delete record (Admin only)  

---

### Dashboard

- `GET /dashboard/summary`  
- `GET /dashboard/recent`  
- `GET /dashboard/monthly-trends`  

---

## Setup Instructions (Local)

### 1. Clone Repository


git clone https://github.com/Mohamed-Fasidh/Finance-Data.git

cd Finance-Data


---

### 2. Create Virtual Environment


python -m venv venv

venv\Scripts\activate


---

### 3. Install Dependencies


pip install -r requirements.txt


---

### 4. Configure Environment Variables

Create `.env` file:


DATABASE_URL=postgresql://username:password@localhost:5432/finance_db

SECRET_KEY=your_secret_key


---

### 5. Run Server


uvicorn app.main:app --reload


---

### 6. Access API Docs


http://127.0.0.1:8000/docs


---

## Deployment

- Deployed on Render  
- Uses managed PostgreSQL instance  
- Environment variables configured securely  
- Public API accessible via Swagger  

---
## Render Free Tier Limitation

This project is deployed on Render using the free tier.

- The service automatically goes to sleep after ~15 minutes of inactivity :contentReference[oaicite:0]{index=0}  
- The first request after inactivity may take **20–30 seconds** due to cold start :contentReference[oaicite:1]{index=1}  
- Subsequent requests are fast and respond normally  

This behavior is expected in the free tier and does not affect functionality.

For production use, upgrading to a paid plan removes this delay.

---

## Design Decisions

- JWT used for stateless authentication  
- Role-based access enforced via dependency checks  
- SQLAlchemy used for structured database operations  
- PostgreSQL used for reliable persistence  
- Data isolation implemented per user  

---

## Assumptions

- Email is unique per user  
- Admin has full control  
- Records are linked via user_id  
- Simplified validation for demonstration  

---

## Validation and Error Handling

- Input validation using Pydantic schemas  
- Proper HTTP status codes  
- Clear error messages for invalid operations  

---

## Future Improvements

- Refresh token mechanism  
- Advanced filtering and search  
- Pagination metadata  
- Docker support  
- Unit and integration testing  
- Rate limiting  

---

## Evaluation Coverage

- Backend structure and modular design  
- Role-based access control implementation  
- CRUD operations with filtering  
- Dashboard aggregation logic  
- PostgreSQL data persistence  
- Validation and error handling  
- API documentation and deployment  

---

## Author

Mohamed Fasidh  