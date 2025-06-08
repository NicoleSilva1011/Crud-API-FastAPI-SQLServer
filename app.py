from fastapi import FastAPI, HTTPException, Depends
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models
import schemas
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv(".env")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/{id}", response_model=schemas.UserRead)
def read_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users", response_model=list[schemas.UserRead])
def read_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.post("/users", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    now = datetime.now(timezone.utc)
    db_user = models.User(
        name=user.name.strip(),
        email=user.email.strip().lower(),
        password=user.password, 
        created_in=now,
        updated_in=now
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.patch("/users/{id}", response_model=schemas.UserRead)
def update_user(id: int, user: schemas.UserPatch, db: Session = Depends(get_db)):
    current_user = db.query(models.User).filter(models.User.id == id).first()

    if not current_user:
        raise HTTPException(status_code=404, detail="User not found") 
    
    if user.email:
        if db.query(models.User).filter(models.User.email == user.email.strip().lower(), models.User.id != id).first():
            raise HTTPException(status_code=400, detail="Email already in use by another user")
        current_user.email = user.email.strip().lower()
        
    
    if user.name:
        current_user.name = user.name.strip()

    if user.name or user.email:
        now = datetime.now(timezone.utc)
        current_user.updated_in = now
    else:
        raise HTTPException(status_code=400, detail="At least one field must be provided for update")


    db.commit()
    db.refresh(current_user)
    return current_user