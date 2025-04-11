from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.auth import Token
from app.schemas.user import UserCreate, UserOut
from app.database import SessionDep
from app.services.security import create_access_token, hash_password, authenticate_user, get_current_user
from app.models.user import User
from sqlmodel import select
router = APIRouter()


@router.post('/register', response_model=Token, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: SessionDep):
    existing_user = db.exec(select(User).where(
        User.email == user_data.email)).first()
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
def login(form_data: UserCreate, db: SessionDep) -> Token:
    user = authenticate_user(db, form_data.email, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": str(user.id)})

    return Token(access_token=access_token, token_type="bearer")


@router.get('/me', response_model=UserOut)
def get_me(auth_user: User = Depends(get_current_user)):
    user_out = UserOut.model_validate(auth_user)
    print(user_out)
    return auth_user
