from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import get_password_hash

# Get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Create a new user
def create_user(db: Session, email: str, password: str, full_name: str):
    hashed_password = get_password_hash(password)
    user = User(email=email, hashed_password=hashed_password, full_name=full_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
