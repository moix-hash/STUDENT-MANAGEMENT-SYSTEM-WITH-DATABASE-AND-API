from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db

# Create database tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="A simple CRUD API for managing students using FastAPI + SQLite",
    version="1.0.0"
)


@app.post("/create-student/", response_model=schemas.StudentResponse, status_code=201)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    """
    Create a new student record.
    - **name**: Full name of the student
    - **email**: Must be a valid and unique email address
    - **age**: Must be a positive integer
    - **course**: Name of the enrolled course
    """
    db_student = db.query(models.Student).filter(models.Student.email == student.email).first()
    if db_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/students-all/", response_model=list[schemas.StudentResponse])
def get_all_students(db: Session = Depends(get_db)):
    """
    Retrieve a list of all students in the database.
    """
    return db.query(models.Student).all()

@app.get("/student/{id}", response_model=schemas.StudentResponse)
def get_student(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single student by their ID.
    - Returns **404** if the student is not found.
    """
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
    
@app.put("/update-students/{id}", response_model=schemas.StudentResponse)
def update_student(id: int, updated_data: schemas.StudentCreate, db: Session = Depends(get_db)):
    """
    Update an existing student's information by their ID.
    - All fields (name, email, age, course) will be updated.
    - Returns **404** if the student is not found.
    """
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    for key, value in updated_data.dict().items():
        setattr(student, key, value)
    db.commit()
    db.refresh(student)
    return student

@app.delete("/delete-students/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):
    """
    Delete a student record by their ID.
    - Returns **404** if the student is not found.
    """
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}
