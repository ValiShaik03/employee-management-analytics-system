from fastapi import APIRouter, HTTPException
from database import conn, cursor

router = APIRouter()

# ---------------- GET ALL EMPLOYEES ---------------- #

@router.get("/employees")
def get_employees():

    query = "SELECT * FROM Employees"

    cursor.execute(query)

    rows = cursor.fetchall()

    employees = []

    for row in rows:

        employees.append({
            "emp_id": row[0],
            "name": row[1],
            "dept_id": row[2],
            "salary": row[3],
            "joining_date": str(row[4])
        })

    return employees


# ---------------- GET EMPLOYEE BY ID ---------------- #

@router.get("/employee/{emp_id}")
def get_employee(emp_id: int):

    query = """
    SELECT *
    FROM Employees
    WHERE emp_id = %s
    """

    cursor.execute(query, (emp_id,))

    row = cursor.fetchone()

    if row is None:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return {
        "emp_id": row[0],
        "name": row[1],
        "dept_id": row[2],
        "salary": row[3],
        "joining_date": str(row[4])
    }


# ---------------- ADD EMPLOYEE ---------------- #

@router.post("/employee")
def add_employee(
        emp_id: int,
        name: str,
        dept_id: int,
        salary: int,
        joining_date: str
):

    query = """
    INSERT INTO Employees
    (emp_id, name, dept_id, salary, joining_date)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        emp_id,
        name,
        dept_id,
        salary,
        joining_date
    )

    try:

        cursor.execute(query, values)

        conn.commit()

        return {
            "message": "Employee Added Successfully"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ---------------- UPDATE EMPLOYEE SALARY ---------------- #

@router.put("/employee/{emp_id}")
def update_salary(emp_id: int, salary: int):

    query = """
    UPDATE Employees
    SET salary = %s
    WHERE emp_id = %s
    """

    values = (salary, emp_id)

    cursor.execute(query, values)

    conn.commit()

    if cursor.rowcount == 0:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return {
        "message": "Salary Updated Successfully"
    }


# ---------------- DELETE EMPLOYEE ---------------- #

@router.delete("/employee/{emp_id}")
def delete_employee(emp_id: int):

    query = """
    DELETE FROM Employees
    WHERE emp_id = %s
    """

    cursor.execute(query, (emp_id,))

    conn.commit()

    if cursor.rowcount == 0:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return {
        "message": "Employee Deleted Successfully"
    }


# ---------------- SEARCH EMPLOYEE ---------------- #

@router.get("/search/{emp_name}")
def search_employee(emp_name: str):

    query = """
    SELECT *
    FROM Employees
    WHERE name LIKE %s
    """

    cursor.execute(query, (f"%{emp_name}%",))

    rows = cursor.fetchall()

    employees = []

    for row in rows:

        employees.append({
            "emp_id": row[0],
            "name": row[1],
            "dept_id": row[2],
            "salary": row[3],
            "joining_date": str(row[4])
        })

    return employees


# ---------------- TOP 3 HIGHEST SALARIES ---------------- #

@router.get("/top-salaries")
def top_salaries():

    query = """
    SELECT name, salary
    FROM (
        SELECT name,
               salary,
               ROW_NUMBER() OVER (
                   ORDER BY salary DESC
               ) AS rn
        FROM Employees
    ) t
    WHERE rn <= 3
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    result = []

    for row in rows:

        result.append({
            "name": row[0],
            "salary": row[1]
        })

    return result


# ---------------- DEPARTMENT AVERAGE SALARY ---------------- #

@router.get("/department-average")
def department_average():

    query = """
    SELECT d.dept_name,
           AVG(e.salary) AS avg_salary
    FROM Employees e
    JOIN Departments d
    ON e.dept_id = d.dept_id
    GROUP BY d.dept_name
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    result = []

    for row in rows:

        result.append({
            "department": row[0],
            "average_salary": float(row[1])
        })

    return result