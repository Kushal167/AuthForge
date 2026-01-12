from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import get_user_by_email, create_user
from app.schemas.auth import LoginRequest
from app.core.security import verify_password
from app.core.tokens import create_access_token
from app.models.user import User


router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)    # Endpoint for user registration
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, email=user_in.email)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email is already registered."
        )
    user = create_user(db=db, email=user_in.email, password=user_in.password, full_name=user_in.full_name)
    return user



@router.post("/login")     # Endpoint for user login and JWT token generation
def login_user(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}



@router.get("/protected")     # A protected route to test JWT authentication
def protected():
    return {"message": "JWT is working!"}
