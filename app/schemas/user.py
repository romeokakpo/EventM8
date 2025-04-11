from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    firstname: Optional[str] = None
    lastname: Optional[str] = None


class UserOut(BaseModel):
    id: int
    email: EmailStr
    firstname: str
    lastname: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
