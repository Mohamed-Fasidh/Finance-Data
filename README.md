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
- Secure password hashing  
- Role-based access control  

---

### User Management

- Create users  
- Assign roles (Admin, Analyst, Viewer)  
- Manage active/inactive status  

---

### Financial Records

- Create, update, delete records  

Fields:

- Amount  
- Type (income / expense)  
- Category  
- Date  
- Notes  

Filtering:

- By type  
- By category  
- Pagination support  

---

### Dashboard APIs

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

1. Register user  
2. Login to get JWT token  
3. Click **Authorize** in Swagger  
4. Enter:


Bearer <your_token>


---

## API Endpoints

### Auth

- POST /auth/register  
- POST /auth/login  

---

### Users

- POST /users/ (Admin only)  
- GET /users/  
- PUT /users/{id}  

---

### Records

- POST /records/ (Admin only)  
- GET /records/  
- PUT /records/{id}  
- DELETE /records/{id}  

---

### Dashboard

- GET /dashboard/summary  
- GET /dashboard/recent  
- GET /dashboard/monthly-trends  

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

### 4. Environment Variables

Create `.env` file:


DATABASE_URL=postgresql://username:password@localhost:5432/finance_db

SECRET_KEY=your_secret_key


---

### Secret Key

Generate secure key:


python -c "import secrets; print(secrets.token_hex(32))"


---

### 5. Run Server


uvicorn app.main:app --reload


---

### 6. API Docs


http://127.0.0.1:8000/docs


---

## Deployment (Render)

- Backend deployed on Render  
- PostgreSQL hosted on Render  
- Environment variables configured securely  

## Render Free Tier Limitation

This project is deployed on Render using the free tier.

- The service automatically goes to sleep after ~15 minutes of inactivity :contentReference[oaicite:0]{index=0}  
- The first request after inactivity may take **20–30 seconds** due to cold start :contentReference[oaicite:1]{index=1}  
- Subsequent requests are fast and respond normally  

This behavior is expected in the free tier and does not affect functionality.

For production use, upgrading to a paid plan removes this delay.

### Environment Variables


DATABASE_URL=<Internal Render DB URL>

SECRET_KEY=<your_secret>

PYTHON_VERSION=3.10.13


---

## Connecting PostgreSQL to pgAdmin

1. Copy **External Database URL** from Render  

Example:


postgresql://user:password@host:5432/db_name


---

### pgAdmin Setup

- Host: host  
- Port: 5432  
- Database: db_name  
- Username: user  
- Password: password  

---

### SSL Configuration

Set:


SSL Mode = require


---

### Run Queries


SELECT * FROM users;

SELECT * FROM records;


---

## Render Free Tier Limitation

- Service sleeps after ~15 minutes inactivity  
- First request may take 20–30 seconds  
- Subsequent requests are fast  

---

## Design Decisions

- JWT authentication  
- Role-based access control  
- SQLAlchemy ORM  
- PostgreSQL persistence  
- User-level data isolation  

---

## Assumptions

- Email is unique  
- Admin has full access  
- Records linked via user_id  

---

## Validation & Error Handling

- Input validation using Pydantic  
- Proper HTTP status codes  
- Clear error messages  

---

## Future Improvements

- Refresh tokens  
- Advanced filtering  
- Docker support  
- Testing  
- Rate limiting  

---

## Author

Mohamed Fasidh