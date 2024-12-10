from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from src.db.connection import Session as DBSession
from src.model.user import Usuario
import traceback

class UsuarioRepository:

    def __init__(self, session: Session = None):
        self.session = session or DBSession()

    def insert_user(self, usuario: Usuario):
        try:
            self.session.add(usuario)
            self.session.commit()
            self.session.refresh(usuario)

            print(f"Usuário {usuario.nome} inserido com sucesso!")
            return usuario
        except IntegrityError as e:
            print(f"Erro de integridade: {e}")
            self.session.rollback()
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
            self.session.rollback()
        finally:
            self.session.close()

    def list_users(self):
        try:
            return self.session.query(Usuario).all()
        except Exception as e:
            print(f"Erro ao listar usuários: {e}")
            return []
        finally:
            self.session.close()

    def update_user(self, user_id, nome=None, email=None, senha=None, cpf=None, contato=None):
        try:
            usuario = self.session.query(Usuario).filter_by(id=user_id).first()
            if not usuario:
                print(f"Usuário com ID {user_id} não encontrado.")
                return None

            if nome:
                usuario.nome = nome
            if email:
                usuario.email = email
            if senha:
                usuario.senha = senha
            if cpf:
                usuario.cpf = cpf
            if contato:
                usuario.contato = contato

            self.session.commit()
            print(f"Usuário com ID {user_id} atualizado com sucesso!")
            return usuario
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            self.session.rollback()
        finally:
            self.session.close()

    def get_user_by_email(self, email):
        try:
            return self.session.query(Usuario).filter_by(email=email).first()
        except Exception as e:
            print(f"Erro ao buscar usuário por email: {e}")
            return None
        finally:
            self.session.close()

    def delete_user(self, user_id):
        try:
            usuario = self.session.query(Usuario).filter_by(id=user_id).first()
            if not usuario:
                print(f"Usuário com ID {user_id} não encontrado.")
                return None

            self.session.delete(usuario)
            self.session.commit()
            print(f"Usuário com ID {user_id} deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            self.session.rollback()
        finally:
            self.session.close()

    def login_user(self, email, senha):
        try:
            usuario = self.session.query(Usuario).filter_by(email=email, senha=senha).first()
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
            self.session.close()

    def drop_users_table(self):
        try:
            self.session.execute(text("DROP TABLE IF EXISTS usuarios"))
            print("Tabela 'usuarios' excluída com sucesso!")
        except Exception as e:
            print(f"Erro ao excluir a tabela: {e}")
            traceback.print_exc()
        finally:
            self.session.close()

    def get_user_by_cpf(self, cpf):
        try:
            return self.session.query(Usuario).filter_by(cpf=cpf).first()
        except Exception as e:
            print(f"Erro ao buscar usuário por CPF: {e}")
            return None
        finally:
            self.session.close()

    def get_user_by_id(self, usuario_id: int):
        try:
            return self.session.query(Usuario).filter_by(id=usuario_id).first()
        except Exception as e:
            print(f"Erro ao buscar usuário por ID: {e}")
            return None
        finally:
            self.session.close()


