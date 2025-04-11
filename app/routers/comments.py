from fastapi import APIRouter, Depends, HTTPException, status
from app.services.security import get_current_user
from app.database import SessionDep
from app.schemas.comment import CommentCreate
from app.models.comment import Comment
from sqlmodel import select

router = APIRouter()


@router.post("/{id}/comments")
def add_comment(id: int, comment_data: CommentCreate, db: SessionDep, user=Depends(get_current_user)):
    comment = Comment(content=comment_data.content,
                      event_id=id, user_id=user.id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


@router.get("/{id}/comments")
def get_comments(id: int, db: SessionDep):
    return db.exec(select(Comment).where(Comment.event_id == id)).all()
