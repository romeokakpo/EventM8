from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    firstname: str
    lastname: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    firstname: str
    lastname: str
    created_at: datetime

    class Config:
        orm_mode = True
