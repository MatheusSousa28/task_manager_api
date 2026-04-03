"""
Configuração da conexão com o banco de dados e gerenciamento
das sessões do SQLAlchemy para uso na aplicação.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL")

#Cria a engine do banco, usando pool_pre_ping para validar conexões antes do uso e evitar conexões quebradas.
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

#Cria uma fábrica de sessões com controle manual de commit e flush para maior previsibilidade das transações.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#Base declarativa usada como classe base para todos os models do SQLAlchemy.
Base = declarative_base()

#Dependency do FastAPI que cria uma sessão de banco por request e garante o fechamento ao final.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
