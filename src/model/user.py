# src/models/usuario.py

from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship
from src.db.connection import Base
import bcrypt

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome = mapped_column(String(100), nullable=False)
    email = mapped_column(String(100), nullable=False, unique=True)
    senha = mapped_column(String(255), nullable=False)
    cpf = mapped_column(String(11), nullable=False, unique=True)
    contato = mapped_column(String(15), nullable=False)

    # Relacionamento com agendamentos
    agendamentos = relationship('Agendamento', back_populates='usuario', uselist=True)

    def __init__(self, nome, email, senha, cpf, contato):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.contato = contato

    def gerar_hash_senha(self, senha):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(senha.encode('utf-8'), salt).decode('utf-8')

    def validar_senha(self, senha):
        checking = bcrypt.checkpw(senha.encode('utf-8'), self.senha.encode('utf-8'))
        return checking

    def __repr__(self):
        return f"Usuario(id={self.id}, nome={self.nome}, email={self.email})"
