import os
from typing import Annotated
from fastapi import Depends
from app.models import User, Event, Comment
from sqlmodel import SQLModel, Session, create_engine
from app.services.config import settings

DATABASE_URL = settings.DATABASE_URL

# Connecteur spécial pour SQLite
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith(
    "sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
