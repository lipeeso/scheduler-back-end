from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime





class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    

class UserUpdateSchema(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]

class UserPublicSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    update_at: datetime


class UserListPublicSchema(BaseModel):
    users: list[UserPublicSchema]
    offset: int
    limit: int


