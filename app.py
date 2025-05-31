from fastapi import FastAPI, HTTPException
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models
import schemas

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/{id}")
def read_user_by_id(id: int, db: Session = next(get_db())):
    users = db.query(models.User).all()
    return users

@app.get("/users")
def read_users(db: Session = next(get_db())):
    users = db.query(models.User).all()
    return users

@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = next(get_db())):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user