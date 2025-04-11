from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from typing import Optional


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(primary_key=True, index=True, default=None)
    email: str = Field(index=True, unique=True, nullable=False)
    firstname: str = Field(nullable=False)
    lastname: str = Field(nullable=False)
    hashed_password: str = Field(nullable=False)
    created_at: datetime = Field(default=datetime.now(
        timezone.utc).replace(tzinfo=None), nullable=False)

    events: list["Event"] = Relationship(back_populates="owner")
    comments: list["Comment"] = Relationship(back_populates="user")
