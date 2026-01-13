from pydantic import BaseModel, EmailStr

# Request schema for creating a new user
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str

# Response schema for returning user info (without password)
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str

    class Config:
        orm_mode = True
