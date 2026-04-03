"""
Definição dos modelos ORM da aplicação, representando as entidades
do sistema e seus relacionamentos no banco de dados.
"""

from core.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func  #Função SQL que delega ao banco a geração do timestamp

class User(Base):
    __tablename__ = "User"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    #Email único usado para identificação do usuário; indexado para otimizar consultas
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)
    ative = Column(Boolean, default=True, nullable=False)
    creation_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    #Relacionamento 1:N entre usuário e tarefas, com cascade para remoção automática das tarefas
    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan", passive_deletes=True)

class Task(Base):
    __tablename__ = "Task"
    task_id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(1000))
    completed = Column(Boolean, default=False)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    update_date = Column(
        DateTime(timezone=True), 
        server_default=func.now(), 
        onupdate=func.now() #Atualizado automaticamente pelo banco a cada alteração do registro
    )
    user_id = Column(Integer, ForeignKey("User.id_user", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="tasks")