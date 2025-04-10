from fastapi import APIRouter, Depends, HTTPException, status
from ..schemas.auth import Token, TokenData
from ..schemas.user import UserCreate
from ..database import SessionDep
from ..services.security import create_access_token, hash_password
from ..models.user import User
router = APIRouter()


@router.post('/register', response_model=Token)
def register(user_data: UserCreate, db: SessionDep):
    existing_user = db.get(User).filter(
        User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    hashed_pwd = hash_password(user_data.password)

    user = User(
        email=user_data.email,
        firstname=user_data.firstname,
        lastname=user_data.lastname,
        hashed_password=hashed_pwd
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    access_token = create_access_token(data={"sub": str(user.id)})

    return Token(access_token=access_token, token_type="bearer")


@router.post('/login')
def login():
    pass


@router.get('/me')
def get_me():
    pass
