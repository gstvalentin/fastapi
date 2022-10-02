# GET - GET AN INFORMATION
# POST - CREATE SOMETHING NEW
# PUT - UPDATE
# DELETE - DELETE SOMETHING
from fastapi import FastAPI, Path
from typing import Optional
from matplotlib.pyplot import cla
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        'name': 'john',
        'age': 25,
        'class': 'year 151'
    }
}

class Student(BaseModel):
    name: str
    gate: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get('/')
def index():
    return {"name": "data"}

@app.get('/get-student/{student_id}')
def get_student(student_id: int = Path(None, description='the ID of the student you want to view', gt=0, lt=3)):
    return students[student_id]
# gt = need to be greater than "some number like 0"
# lt = need to be less than "some number like 3"

@app.get('/get-by-name/{student_id}')
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {'Data': 'Not found'}

@app.post('/create-student/{student_id}')
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {'Error': 'Student already exists'}
    
    students[student_id] = student
    return students[student_id]

@app.put('/update-student/{student_id}')
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {'Error': 'Student does not exist'}
    students[student_id] = student
    return students[student_id]