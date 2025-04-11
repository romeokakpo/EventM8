from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from typing import Optional


class Event(SQLModel, table=True):
    __tablename__ = "events"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    title: str = Field(nullable=False)
    description: str | None
    start_date: datetime = Field(nullable=False)
    end_date: datetime = Field(nullable=False)
    location: str = Field(nullable=False)
    created_at: datetime = Field(default=datetime.now(
        timezone.utc).replace(tzinfo=None), nullable=False)

    owner_id: Optional[int] = Field(default=None, foreign_key="users.id")
    owner: Optional["User"] = Relationship(back_populates="events")

    comments: list["Comment"] = Relationship(
        back_populates="event", cascade_delete=True)
