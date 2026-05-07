from fastapi import FastAPI
from employee_routes import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Employee Management API Running"
    }