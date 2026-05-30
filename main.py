from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows your frontend on port 5500 to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

employees = []

class Employee(BaseModel):

    #employee id in integer
    emp_id: int


    #employee name should be more than 3 alphabets can not enter abc or xyz
    name:str = Field(
        ...,
        min_length= 4,
        max_length=50,
        description= "Employee full name"

    )

    #age should be greater than 18 and less than 60
    age: int = Field(
        ...,
        ge = 18,
        le = 60
    )
    # for proper email format
    email: EmailStr

    #password must be at least 8 letters

    password: str = Field(
        ...,
        min_length=8
    )

    #contact should be numbers
    contact: str = Field(
        ...,
        pattern="^[0-9]{10}$"
    )

    department: Optional[str] = None 

    city: Optional[str] = None

@app.get("/")
def home():
    return {
        "message" : "Welcome to Employees API"
    }

@app.post("/employees",status_code=201)
def create_employee(employee: Employee):
    for existing_employee in employees:
        if existing_employee["emp_id"] == employee.emp_id:
            raise HTTPException(
                status_code=400,
                detail = "Employee with this Id already exists"
            )
    employees.append(employee.dict())
    return{
        "message" : "Employee added successfully",
        "data": employee
    }

@app.get("/employees")
def get_employees_details():
    return{
        "total_employees": len(employees),
        "employees" : employees
    }

@app.get("/employees/{emp_id}")
def get_single_employee_details(emp_id:int):
    for employee in employees:
        if employee["emp_id"] == emp_id:
            return{
                "employee" : employee
            }
    
    raise HTTPException(
        status_code=404,
        detail= "Employee with these detials not found"
    )


@app.put("/employees/{emp_id}")
def update_employee_details(
    emp_id:int,
    update_employee: Employee
):
    for employee in employees:
        if employee["emp_id"] == emp_id:
            employee.update(update_employee.dict())

            return {
                "message" : "Employee detials updated successfully",
                "data" : employee
            }
    raise HTTPException(
        status_code=404,
        detail= "Employee with these details not found. Please enter correct details"
    )

@app.delete("/employees/{emp_id}")
def remove_employee(emp_id:int):
    for employee in employees:
        if employee["emp_id"] == emp_id:
            employees.remove(employee)
            return {
                "message" : "Employee removed successfully"
            }
    
    raise HTTPException(
        status_code= 404,
        detail= "Employee with these details not found. Please enter correct details"
    )

@app.get("/search")
def search_employees(
    department:Optional[str] = None,
    city:Optional[str] = None
):
    filtered_employees = employees

    if department:
        filtered_employees = [
            employee for employee in filtered_employees
            if employee["department"].lower() == department.lower()
        ]

    if city:
        filtered_employees = [
            employee for employee in filtered_employees
            if employee["city"].lower() == city.lower()
        ]
    
    return {
        "result" : filtered_employees
    }





