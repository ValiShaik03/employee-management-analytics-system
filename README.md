# 🚀 Employee Management & Analytics System

A full-stack Employee Management System built using:

- FastAPI
- MySQL
- Streamlit
- Python

The project supports:
- Employee CRUD operations
- Employee search
- Salary analytics
- Department-wise reporting
- REST APIs
- Interactive Streamlit dashboard

---

# 📌 Features

## ✅ CRUD Operations
- Add Employee
- View Employees
- Update Employee Salary
- Delete Employee

## ✅ Analytics APIs
- Top 3 Highest Salaries
- Department Average Salary
- Employee Search

## ✅ Frontend Dashboard
Built using Streamlit for easy interaction with APIs.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| FastAPI | REST API Framework |
| MySQL | Database |
| Streamlit | Frontend Dashboard |
| Requests | API Communication |
| Python-Dotenv | Environment Variables |

---

# 📂 Project Structure

```text
EmployeeAnalytics/
│
├── main.py
├── database.py
├── employee_routes.py
├── streamlit_app.py
├── .env
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/employee-management-analytics-system.git
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Create `.env` File

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=YOUR_PASSWORD
DB_NAME=EmployeeAnalytics
```

---

# ▶️ Run FastAPI Backend

```bash
uvicorn main:app --reload
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

---

# 📊 APIs Implemented

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /employees | Get all employees |
| GET | /employee/{id} | Get employee by ID |
| POST | /employee | Add employee |
| PUT | /employee/{id} | Update salary |
| DELETE | /employee/{id} | Delete employee |
| GET | /search/{name} | Search employee |
| GET | /top-salaries | Top 3 salaries |
| GET | /department-average | Department average salary |

---

# 🧠 SQL Concepts Used

- JOINS
- GROUP BY
- Window Functions
- ROW_NUMBER()
- Aggregations
- Filtering
- Advanced Queries

---

# 📌 Future Improvements

- JWT Authentication
- Role-Based Access
- Docker Deployment
- Cloud Database
- Charts & Visualizations

---

# 👨‍💻 Author

Developed by ValiShaik
