from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from pydantic import EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserRead(BaseModel):
    name: str
    email: EmailStr
    created_in: datetime
    updated_in: datetime

    model_config = {
        "from_attributes": True
    }

class UserPatch(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

    model_config = {
        "from_attributes": True
    }