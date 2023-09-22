from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

# Initialize app
app = FastAPI()

# body format of employee
class Employee(BaseModel):
    id: int
    name: str
    age: int
    location: str


# Fake db data
employees = [
    {
        "id": 1,
        "name": "Akilan",
        "age": 34,
        "location": "Bangalore"

    },
    {
        "id": 2,
        "name": "Alex",
        "age": 35,
        "location": "Chennai"

    }
]


# Home Route
@app.get("/")
def index():
    return {"msg": "Welcome to FastAPI, Akilan"}

# Route to list employees
@app.get("/employees")
def get_employees():
    return {"employees": employees}

# Route to get specific employee
@app.get("/employee/{emp_id}")
def get_employee(emp_id: int):
    for employee in employees:
        if employee["id"] == emp_id:
            return {"employee": employee}
    return {"msg": "Employee not found"}


# Route to delete employee
@app.delete("/employee/{emp_id}")
def delete_employee(emp_id: int):
    for i, _ in enumerate(employees):
        if employees[i]["id"] == emp_id:
            del employees[i]
            return {"msg": "Employee deleted successfully..."}
    return {"msg": "Employee not found"}


# Route to add employee
@app.post("/employee")
def add_employee(employee: Employee):
    employees.append(jsonable_encoder(employee))
    return {"msg": "Employee added successfully"}

# Route to update employee
@app.put("/employee/{emp_id}")
def update_employee(emp_id: int,employee: Employee):
    for i, _ in enumerate(employees):
        print(employees[i])
        if employees[i]["id"] == emp_id:
            #print(employees[i])
            employees[i] = jsonable_encoder(employee)
            return {"msg": "Employee updated successfully..."}
    return {"msg": "Employee not found"}