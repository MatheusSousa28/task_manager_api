"""
Schemas Pydantic responsáveis pela validação e tipagem
dos dados de entrada e saída da API.
"""

from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from typing import Optional

#Campos base compartilhados (não incluem senha)
class UserBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr

#Schema para criação de usuário
class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128)

#Schema para resposta da API
class UserResponse(UserBase):
    user_id: int
    active: bool
    creation_date: datetime

    model_config = ConfigDict(from_attributes=True)

#Schema para atualização parcial (PATCH)
class UserPatch(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

#Campos base da tarefa
class TaskBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str | None = Field(None, max_length=1000)

#Schema para criação de tarefa
class TaskCreate(TaskBase):
    user_id: int

#Schema para resposta da API
class TaskResponse(TaskBase):
    task_id: int
    completed: bool
    cration_date: datetime
    update_time: datetime

    model_config = ConfigDict(from_attributes=True)

#Schema para atualização parcial (PATCH)
class TaskPatch(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None