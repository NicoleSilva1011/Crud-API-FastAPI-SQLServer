from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Integer, String, DateTime
from datetime import datetime

class Base(DeclarativeBase): 
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    created_in: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_in: Mapped[datetime] = mapped_column(DateTime, nullable=False)