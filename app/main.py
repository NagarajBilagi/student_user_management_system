from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .db import Base, engine, get_db
from .models import Student, InterestResource
from .schemas import (
    RegisterRequest, LoginRequest, TokenResponse,
    StudentResponse, InterestSelectRequest, InterestResourceResponse
)
from .security import hash_password, verify_password, create_access_token, get_current_student

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/register", response_model=StudentResponse)
def register_student(payload: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(Student).filter(Student.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    student = Student(
        name=payload.name,
        email=payload.email,
        password_hash=hash_password(payload.password),
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@app.post("/login", response_model=TokenResponse)
def login_student(payload: LoginRequest, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.email == payload.email).first()
    if not student or not verify_password(payload.password, student.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": str(student.id)})
    return TokenResponse(access_token=token)

@app.get("/me", response_model=StudentResponse)
def read_current_student(current: Student = Depends(get_current_student)):
    return current

@app.put("/me/interest", response_model=StudentResponse)
def set_interest(payload: InterestSelectRequest, current: Student = Depends(get_current_student), db: Session = Depends(get_db)):
    current.selected_interest = payload.interest
    db.commit()
    db.refresh(current)
    return current

@app.get("/me/resources", response_model=InterestResourceResponse)
def get_resources(current: Student = Depends(get_current_student), db: Session = Depends(get_db)):
    if not current.selected_interest:
        raise HTTPException(400, "Select an interest first.")

    row = db.query(InterestResource).filter(
        InterestResource.interest_tag == current.selected_interest
    ).first()

    if not row:
        raise HTTPException(404, "No resources found.")

    return row

