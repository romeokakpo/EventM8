from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EventBase(BaseModel):
    title: str
    description: Optional[str]
    start_date: datetime
    end_date: datetime


class EventCreate(EventBase):
    pass


class EventOut(EventBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True
