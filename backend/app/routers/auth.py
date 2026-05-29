#Handles HTTP requests like: POST /auth/login, POST /auth/register
#receives data from frontend
#calls validation (schemas)
#calls security functions (hashing, token creation)
#interacts with database
#returns response

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.models.users import User
from app.schemas.auth_schemas import RegisterRequest, LoginRequest, UserResponse, TokenResponse
from app.core.security import hash_password, verify_password, create_access_token
from app.db.dependencies import get_db



router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse, status_code=201) #201 Created status code indicates that the user was successfully created
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    email = data.email.lower()

    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=email,
        username=data.username,
        password_hash=hash_password(data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    email = data.email.lower()

    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": str(user.id)})

    return {
        "access_token": token,
        "token_type": "bearer"
    }