import logging

from src.dto.agendamento_dto import AgendamentoDTO
from src.mapper.agendamento_mapper import dto_to_entity
from src.mapper.user_mapper import entity_to_dto
from src.repository.agendamento_repository import AgendamentoRepository
from src.model.agendamento import Agendamento
from src.db.connection import Session
from datetime import datetime

from src.repository.user_repository import UsuarioRepository


class AgendamentoService:
    def __init__(self, session: Session = None):
        self.agendamento_repo = AgendamentoRepository(session)

    def create_agendamento(self, dto: AgendamentoDTO):
        try:
            usuario = self.agendamento_repo.get_usuario_by_cpf(dto.usuario_cpf)

            if not usuario:
                raise Exception(f"Usuário com CPF {dto.usuario_cpf} não encontrado.")

            new_agendamento = Agendamento(servico=dto.servico,
                                          contato=dto.contato,
                                          local=dto.local,
                                          data=dto.data,
                                          hora=dto.hora,
                                          usuario=usuario)
            agendamento = self.agendamento_repo.insert_agendamento(new_agendamento)

            return agendamento
        except Exception as e:
            logging.error(f"Erro ao criar agendamento: {str(e)}")
            raise Exception(f"Erro ao criar agendamento: {e}")

    def list_agendamentos(self):
        try:
            agendamentos = self.agendamento_repo.list_agendamentos()
            return agendamentos
        except Exception as e:
            print(f"Erro ao listar agendamentos: {e}")
            raise Exception(f"Erro ao listar agendamentos: {e}")

    def update_agendamento(self, agendamento_id, nome=None, cpf=None, servico=None, contato=None, local=None, data=None,
                           hora=None):
        try:
            agendamento = self.agendamento_repo.update_agendamento(agendamento_id, nome, cpf, servico, contato, local,
                                                                   data, hora)
            if not agendamento:
                print(f"Agendamento com ID {agendamento_id} não encontrado para atualização.")
            return agendamento
        except Exception as e:
            print(f"Erro ao atualizar agendamento: {e}")
            raise Exception(f"Erro ao atualizar agendamento: {e}")

    def delete_agendamento(self, agendamento_id):
        try:
            self.agendamento_repo.delete_agendamento(agendamento_id)
        except Exception as e:
            print(f"Erro ao deletar agendamento: {e}")
            raise Exception(f"Erro ao deletar agendamento: {e}")

    def get_agendamentos_by_cpf(self, cpf):
        try:
            agendamentos = self.agendamento_repo.get_agendamentos_by_cpf(cpf)
            return agendamentos
        except Exception as e:
            print(f"Erro ao buscar agendamentos para o CPF {cpf}: {e}")
            raise Exception(f"Erro ao buscar agendamentos para o CPF {cpf}: {e}")
