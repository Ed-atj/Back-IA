import traceback
from datetime import datetime
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from src.db.connection import Session as DBSession
from src.model.agendamento import Agendamento
from src.model.user import Usuario


class AgendamentoRepository:

    def __init__(self, session: Session = None):
        self.session = session or DBSession()

    def insert_agendamento(self, agendamento: Agendamento):
        try:
            usuario = self.session.query(Usuario).filter_by(cpf=agendamento.usuario.cpf).first()

            if not usuario:
                raise NoResultFound("Usuário não encontrado")

            self.session.add(agendamento)
            self.session.commit()

            return agendamento

        except NoResultFound:
            raise Exception("Usuário não encontrado.")
        except Exception as e:
            self.session.rollback()
            print(f"Erro ao inserir agendamento: {e}")
            traceback.print_exc()
            raise Exception(f"Erro ao inserir agendamento: {e}")

    def list_agendamentos(self):
        try:
            # Retorna todos os agendamentos
            return self.session.query(Agendamento).all()
        except Exception as e:
            print(f"Erro ao listar agendamentos: {e}")
            return []

    def update_agendamento(self, agendamento_id: int, nome=None, cpf=None, servico=None, contato=None, local=None, data=None, hora=None):
        try:
            # Busca o agendamento pelo ID
            agendamento = self.session.query(Agendamento).filter_by(id=agendamento_id).first()
            if not agendamento:
                print(f"Agendamento com ID {agendamento_id} não encontrado.")
                return None

            # Atualiza os dados do agendamento
            if nome:
                agendamento.usuario.nome = nome  # Atualiza nome do usuário associado
            if cpf:
                agendamento.usuario.cpf = cpf  # Atualiza CPF do usuário associado
            if servico:
                agendamento.servico = servico
            if contato:
                agendamento.contato = contato
            if local:
                agendamento.local = local
            if data:
                agendamento.data = data
            if hora:
                agendamento.hora = hora

            # Faz o commit das mudanças
            self.session.commit()
            print(f"Agendamento com ID {agendamento_id} atualizado com sucesso!")
            return agendamento
        except Exception as e:
            self.session.rollback()
            print(f"Erro ao atualizar agendamento: {e}")
            return None

    def get_agendamento_by_id(self, agendamento_id: int):
        try:
            # Busca o agendamento pelo ID
            return self.session.query(Agendamento).filter_by(id=agendamento_id).first()
        except Exception as e:
            print(f"Erro ao buscar agendamento por ID: {e}")
            return None

    def delete_agendamento(self, agendamento_id: int):
        try:
            # Busca o agendamento pelo ID
            agendamento = self.session.query(Agendamento).filter_by(id=agendamento_id).first()
            if not agendamento:
                print(f"Agendamento com ID {agendamento_id} não encontrado.")
                return None

            # Deleta o agendamento
            self.session.delete(agendamento)
            self.session.commit()
            print(f"Agendamento com ID {agendamento_id} deletado com sucesso!")
        except Exception as e:
            self.session.rollback()
            print(f"Erro ao deletar agendamento: {e}")

    def drop_agendamentos_table(self):
        try:
            # Executa o comando para excluir a tabela de agendamentos
            self.session.execute(text("DROP TABLE IF EXISTS agendamentos"))
            print("Tabela 'agendamentos' excluída com sucesso!")
        except Exception as e:
            print(f"Erro ao excluir a tabela: {e}")
            traceback.print_exc()

    def get_usuario_by_cpf(self, cpf: str):
        try:
            # Realiza a busca pelo usuário com o CPF informado
            usuario = self.session.query(Usuario).filter(cpf == Usuario.cpf).first()
            return usuario
        except Exception as e:
            print(f"Erro ao buscar usuário para o CPF {cpf}: {e}")
            return None

