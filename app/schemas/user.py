from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):   # schema for creating a new user
    email: EmailStr
    password: str
    full_name: str | None = None

class UserResponse(BaseModel):   # schema for returning user information
    id:int
    email: EmailStr
    full_name: str | None = None

    class config:          # configuration to work with ORM objects
        orm_mode = True