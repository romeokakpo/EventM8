from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import events, auth, comments, likes, recommendations, users
from app.database import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(comments.router, prefix="/events", tags=["Comments"])
app.include_router(likes.router, tags=["Likes"])
app.include_router(recommendations.router, tags=["Recommendations"])
