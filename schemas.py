from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str

class UserRead(BaseModel):
    name: str
    email: str
    created_in: datetime
    updated_in: datetime

    model_config = {
        "from_attributes": True
    }

class UserPatch(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

    model_config = {
        "from_attributes": True
    }