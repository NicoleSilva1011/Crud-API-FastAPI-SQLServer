from pydantic import BaseModel
from datetime import datetime

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