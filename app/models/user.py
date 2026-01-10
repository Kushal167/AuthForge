from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func  # for timestamp fields

from app.db.base import Base # Importing the Base class for model definitions

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # timestamp when the user is created
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())        # timestamp when the user is updated