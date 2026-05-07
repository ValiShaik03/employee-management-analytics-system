# Employee Management Analytics System

A full-stack Employee Management and Analytics System built using:

- FastAPI
- MySQL
- Streamlit
- Railway Cloud MySQL
- Render Deployment

---

# 🚀 Live Deployments

## 🌐 Streamlit Frontend
https://employee-management-analytics-system.streamlit.app/

## ⚡ FastAPI Backend
https://employee-management-analytics-system.onrender.com

## 📘 Swagger API Docs
https://employee-management-analytics-system.onrender.com/docs

---

# 📌 Features

## ✅ Employee Management
- Add Employee
- Update Employee
- Delete Employee
- Search Employee

## ✅ Analytics
- Top 3 Highest Salaries
- Department Average Salary
- Employee Attendance Tracking
- Project Management

## ✅ Database Features
- SQL Joins
- Group By
- Window Functions
- Views
- CTEs
- Indexes

## ✅ Deployment Features
- Railway Cloud MySQL
- Render Backend Deployment
- Streamlit Frontend Deployment

---

# 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| Python | Backend Logic |
| FastAPI | REST API |
| MySQL | Database |
| Streamlit | Frontend UI |
| Railway | Cloud Database |
| Render | Backend Hosting |
| GitHub | Version Control |

---

# 📂 Project Structure

```bash
employee-management-analytics-system/
│
├── main.py
├── database.py
├── employee_routes.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/employee-management-analytics-system.git
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create `.env`

```env
DB_HOST=your_host
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=EmployeeAnalytics
DB_PORT=your_port
```

---

# ▶️ Run FastAPI Backend

```bash
uvicorn main:app --reload
```

Backend URL:

```bash
http://127.0.0.1:8000
```

Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

---

# 📊 Sample API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /employees | Get all employees |
| POST | /add-employee | Add employee |
| PUT | /update-employee/{id} | Update employee |
| DELETE | /delete-employee/{id} | Delete employee |
| GET | /search/{name} | Search employee |
| GET | /top-salaries | Top 3 salaries |
| GET | /department-average | Department average salary |

---

# 📈 SQL Concepts Used

- Joins
- Group By
- Aggregate Functions
- Window Functions
- CTEs
- Views
- Indexes
- Subqueries

---

# 🎯 Learning Outcomes

- Built REST APIs using FastAPI
- Connected FastAPI with MySQL
- Performed SQL analytics queries
- Created Streamlit frontend
- Deployed cloud database on Railway
- Deployed backend on Render
- Deployed frontend on Streamlit Cloud

---

# 👨‍💻 Author

- [Vali Shaik](https://www.linkedin.com/in/mahaboobvalishaik/) 

## ⭐ Support

If you found this project useful, please ⭐ star the repository!
