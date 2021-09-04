from typing import Optional
from pydantic import BaseModel, HttpUrl

class UserBase(BaseModel):
    username: str
    email: str  

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    id: int
    avatar_url: Optional[str] = None
    is_active: bool

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    avatar_url: Optional[str] = None
    is_active: bool