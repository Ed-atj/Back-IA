from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column
from src.db.connection import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome = mapped_column(String(100), nullable=False)
    email = mapped_column(String(100), nullable=False, unique=True)
    senha = mapped_column(String(100), nullable=False)
    cpf = mapped_column(String(11), nullable=False, unique=True)
    contato = mapped_column(String(15), nullable=False)


    def __repr__(self):
        return f"Usuario(id={self.id}, nome={self.nome}, email={self.email})"