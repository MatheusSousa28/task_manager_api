#Schemas Pydantic para entrada e saída da API

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128)


class UserResponse(UserBase):
    user_id: int
    active: bool
    creation_date: datetime

    model_config = ConfigDict(from_attributes=True)


class UserPatch(BaseModel):
    name: str | None = Field(None, min_length=3, max_length=100)
    email: EmailStr | None = None
    password: str | None = Field(None, min_length=8, max_length=128)
    active: bool | None = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TaskBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str | None = Field(None, max_length=1000)


class TaskCreate(TaskBase):
    user_id: int


class TaskResponse(TaskBase):
    task_id: int
    completed: bool
    creation_date: datetime
    update_date: datetime
    user_id: int

    model_config = ConfigDict(from_attributes=True)


class TaskPatch(BaseModel):
    title: str | None = Field(None, min_length=3, max_length=100)
    description: str | None = Field(None, max_length=1000)
    completed: bool | None = None
