from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from typing import Optional
from .user import User
from .event import Event


class Comment(SQLModel, table=True):
    __tablename__ = "comments"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    content: str = Field(nullable=False)
    created_at: datetime = Field(default=datetime.now(
        timezone.utc).replace(tzinfo=None), nullable=False)

    user_id: int = Field(foreign_key="users.id")
    event_id: int = Field(foreign_key="events.id")

    user: User = Relationship(back_populates="comments")
    event: Event = Relationship(back_populates="comments")
