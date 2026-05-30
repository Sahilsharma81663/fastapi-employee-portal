# Day 8 - Employee Management API with Advanced Validation 🚀

## Topics Covered

* FastAPI CRUD Operations
* Pydantic Models
* Field Validation
* Email Validation using EmailStr
* Phone Number Validation using Regex
* Exception Handling with HTTPException
* Query Parameters
* Path Parameters
* Optional Fields
* Search Functionality

---

## Project Overview

Built an Employee Management API using FastAPI that supports:

* Create Employee
* Get All Employees
* Get Employee by ID
* Update Employee Details
* Delete Employee
* Search Employees by Department and City

---

## Validations Implemented

### Employee Name

* Minimum Length: 4
* Maximum Length: 50

### Employee Age

* Minimum Age: 18
* Maximum Age: 60

### Employee Email

* Valid email format required

### Password

* Minimum length: 8 characters

### Contact Number

* Exactly 10 digits
* Regex Validation:

```python
pattern="^[0-9]{10}$"
```

---

## API Endpoints

### Home

```http
GET /
```

### Create Employee

```http
POST /employees
```

### Get All Employees

```http
GET /employees
```

### Get Employee By ID

```http
GET /employees/{emp_id}
```

### Update Employee

```http
PUT /employees/{emp_id}
```

### Delete Employee

```http
DELETE /employees/{emp_id}
```

### Search Employees

```http
GET /search
```

Examples:

```http
/search?department=IT
```

```http
/search?city=Mohali
```

```http
/search?department=IT&city=Mohali
```

---

## Exception Handling

Implemented HTTPException for:

* Duplicate Employee ID
* Employee Not Found
* Invalid Requests

Example:

```python
raise HTTPException(
    status_code=404,
    detail="Employee not found"
)
```

---

## Key Learnings

* Building production-style CRUD APIs
* Data validation using Pydantic
* Professional API response structures
* Handling exceptions gracefully
* Working with query and path parameters
* Creating searchable APIs

---

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn

---


