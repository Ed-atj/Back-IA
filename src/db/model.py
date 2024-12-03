# src/db/model.py
from src.db.connection import Session
from src.db.connection import Base
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.declarative import declarative_base


# Definindo a classe do usuário
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome = mapped_column(String(100), nullable=False)
    email = mapped_column(String(100), nullable=False, unique=True)
    senha = mapped_column(String(100), nullable=False)

    def __repr__(self):
        return f"Usuario(id={self.id}, nome={self.nome}, email={self.email})"


def insert_user(nome, email, senha):
    session = Session()  # Cria uma nova sessão

    try:
        # Criação do novo usuário
        new_user = Usuario(nome=nome, email=email, senha=senha)

        # Adiciona o novo usuário à sessão
        session.add(new_user)

        # Salva as mudanças
        session.commit()
        print(f"Usuário {nome} inserido com sucesso!")
    except IntegrityError as e:
        print(f"Erro de integridade: {e}")
        session.rollback()
    except Exception as e:
        print(f"Erro ao inserir usuário: {e}")
        session.rollback()
    finally:
        # Fecha a sessão
        session.close()

def list_users():
    session = Session()  # Cria uma nova sessão
    try:
        # Consulta todos os usuários
        usuarios = session.query(Usuario).all()

        # Retorna a lista de usuários
        return usuarios
    except Exception as e:
        print(f"Erro ao listar usuários: {e}")
        return []
    finally:
        # Fecha a sessão
        session.close()


def update_user(user_id, nome=None, email=None, senha=None):
    session = Session()  # Cria uma nova sessão

    try:
        # Obtém o usuário pelo ID
        usuario = session.query(Usuario).filter_by(id=user_id).first()

        if not usuario:
            print(f"Usuário com ID {user_id} não encontrado.")
            return

        # Atualiza os campos informados
        if nome:
            usuario.nome = nome
        if email:
            usuario.email = email
        if senha:
            usuario.senha = senha

        # Salva as mudanças
        session.commit()
        print(f"Usuário com ID {user_id} atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")
        session.rollback()
    finally:
        # Fecha a sessão
        session.close()

def get_user_by_email(email):
    session = Session()  # Cria uma nova sessão
    try:
        # Busca o usuário pelo email
        usuario = session.query(Usuario).filter_by(email=email).first()

        if usuario:
            return usuario
        else:
            print(f"Usuário com email '{email}' não encontrado.")
            return None
    except Exception as e:
        print(f"Erro ao buscar usuário por email: {e}")
        return None
    finally:
        # Fecha a sessão
        session.close()

def delete_user(user_id):
    session = Session()  # Cria uma nova sessão
    try:
        # Busca o usuário pelo ID
        usuario = session.query(Usuario).filter_by(id=user_id).first()

        if not usuario:
            print(f"Usuário com ID {user_id} não encontrado.")
            return

        # Remove o usuário
        session.delete(usuario)
        session.commit()
        print(f"Usuário com ID {user_id} deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")
        session.rollback()
    finally:
        # Fecha a sessão
        session.close()

def login_user(email, senha):
    session = Session()  # Cria uma nova sessão
    try:
        # Busca o usuário pelo email e senha
        usuario = session.query(Usuario).filter_by(email=email, senha=senha).first()

        if usuario:
            print(f"Login bem-sucedido para o usuário: {usuario.nome}")
            return usuario
        else:
            print("Email ou senha inválidos.")
            return None
    except Exception as e:
        print(f"Erro ao fazer login: {e}")
        return None
    finally:
        # Fecha a sessão
        session.close()
