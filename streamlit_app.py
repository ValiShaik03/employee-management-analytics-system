import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Employee Management System")


# ---------------- VIEW EMPLOYEES ---------------- #

if st.button("View Employees"):

    response = requests.get(f"{BASE_URL}/employees")

    data = response.json()

    st.subheader("Employee Records")

    st.write(data)


# ---------------- ADD EMPLOYEE ---------------- #

st.subheader("Add Employee")

emp_id = st.number_input("Employee ID", step=1)

name = st.text_input("Name")

dept_id = st.number_input("Department ID", step=1)

salary = st.number_input("Salary", step=1000)

joining_date = st.text_input("Joining Date (YYYY-MM-DD)")


if st.button("Add Employee"):

    response = requests.post(
        f"{BASE_URL}/employee",
        params={
            "emp_id": int(emp_id),
            "name": name,
            "dept_id": int(dept_id),
            "salary": int(salary),
            "joining_date": joining_date
        }
    )

    st.success(response.json()["message"])


# ---------------- SEARCH EMPLOYEE ---------------- #

st.subheader("Search Employee")

search_name = st.text_input("Enter Employee Name")


if st.button("Search"):

    response = requests.get(
        f"{BASE_URL}/search/{search_name}"
    )

    st.write(response.json())


# ---------------- TOP 3 HIGHEST SALARIES ---------------- #

if st.button("Top 3 Highest Salaries"):

    response = requests.get(
        f"{BASE_URL}/top-salaries"
    )

    st.subheader("Top Paid Employees")

    st.write(response.json())


# ---------------- DEPARTMENT AVERAGE SALARY ---------------- #

if st.button("Department Average Salary"):

    response = requests.get(
        f"{BASE_URL}/department-average"
    )

    st.subheader("Department Salary Report")

    st.write(response.json())

# ---------------- UPDATE EMPLOYEE SALARY ---------------- #

st.subheader("Update Employee Salary")

update_emp_id = st.number_input(
    "Employee ID to Update",
    step=1,
    key="update_id"
)

new_salary = st.number_input(
    "New Salary",
    step=1000,
    key="new_salary"
)

if st.button("Update Salary"):

    response = requests.put(
        f"{BASE_URL}/employee/{int(update_emp_id)}",
        params={
            "salary": int(new_salary)
        }
    )

    st.success(response.json()["message"])

# ---------------- DELETE EMPLOYEE ---------------- #

st.subheader("Delete Employee")

delete_emp_id = st.number_input(
    "Employee ID to Delete",
    step=1,
    key="delete_id"
)

if st.button("Delete Employee"):

    response = requests.delete(
        f"{BASE_URL}/employee/{int(delete_emp_id)}"
    )

    st.success(response.json()["message"])