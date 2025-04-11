from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EventBase(BaseModel):
    title: str
    location: str
    description: Optional[str]
    start_date: datetime
    end_date: datetime


class EventCreate(EventBase):
    pass


class EventOut(EventBase):
    id: int
    owner_id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class EventUpdate(BaseModel):
    title: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
