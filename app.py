from fastapi import FastAPI, HTTPException, Depends
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models
import schemas
from datetime import datetime, timezone

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
        name=user.name,
        email=user.email,
        created_in=now,
        updated_in=now
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user