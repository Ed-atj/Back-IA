from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from src.db.connection import Session as DBSession
from src.model.agendamento import Agendamento
import traceback

class AgendamentoRepository:

    def __init__(self, session: Session = None):
        self.session = session or DBSession()

    def insert_agendamento(self, nome, cpf, servico, contato, local, data, hora):
        try:
            novo_agendamento = Agendamento(
                nome=nome, cpf=cpf, servico=servico,
                contato=contato, local=local, data=data, hora=hora
            )

            self.session.add(novo_agendamento)
            self.session.commit()

            self.session.refresh(novo_agendamento)

            print(f"Agendamento para {nome} inserido com sucesso!")
            return novo_agendamento
        except IntegrityError as e:
            print(f"Erro de integridade: {e}")
            self.session.rollback()
        except Exception as e:
            print(f"Erro ao inserir agendamento: {e}")
            self.session.rollback()
        finally:
            self.session.close()

    def list_agendamentos(self):
        try:
            return self.session.query(Agendamento).all()
        except Exception as e:
            print(f"Erro ao listar agendamentos: {e}")
            return []
        finally:
            self.session.close()

    def update_agendamento(self, agendamento_id, nome=None, cpf=None, servico=None, contato=None, local=None, data=None, hora=None):
        try:
            agendamento = self.session.query(Agendamento).filter_by(id=agendamento_id).first()
            if not agendamento:
                print(f"Agendamento com ID {agendamento_id} não encontrado.")
                return None

            if nome:
                agendamento.nome = nome
            if cpf:
                agendamento.cpf = cpf
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

            self.session.commit()
            print(f"Agendamento com ID {agendamento_id} atualizado com sucesso!")
            return agendamento
        except Exception as e:
            print(f"Erro ao atualizar agendamento: {e}")
            self.session.rollback()
        finally:
            self.session.close()

    def get_agendamento_by_id(self, agendamento_id):
        try:
            return self.session.query(Agendamento).filter_by(id=agendamento_id).first()
        except Exception as e:
            print(f"Erro ao buscar agendamento por ID: {e}")
            return None
        finally:
            self.session.close()

    def delete_agendamento(self, agendamento_id):
        try:
            agendamento = self.session.query(Agendamento).filter_by(id=agendamento_id).first()
            if not agendamento:
                print(f"Agendamento com ID {agendamento_id} não encontrado.")
                return None

            self.session.delete(agendamento)
            self.session.commit()
            print(f"Agendamento com ID {agendamento_id} deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar agendamento: {e}")
            self.session.rollback()
        finally:
            self.session.close()

    def drop_agendamentos_table(self):
        try:
            self.session.execute(text("DROP TABLE IF EXISTS agendamentos"))
            print("Tabela 'agendamentos' excluída com sucesso!")
        except Exception as e:
            print(f"Erro ao excluir a tabela: {e}")
            traceback.print_exc()
        finally:
            self.session.close()

    def get_agendamentos_by_cpf(self, cpf):
        try:
            return self.session.query(Agendamento).filter(Agendamento.cpf == cpf).all()
        except Exception as e:
            print(f"Erro ao buscar agendamentos para o CPF {cpf}: {e}")
            return []
        finally:
            self.session.close()
