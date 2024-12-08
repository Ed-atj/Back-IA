from sqlalchemy.orm import Session
from src.db.connection import Session as DBSession
from src.dto.agendamento_dto import AgendamentoDTO
from src.exceptions.agendamento_exception import AgendamentoNotFoundException
from src.mapper.agendamento_mapper import dto_to_entity, entity_to_dto
from src.repository.agendamento_repository import AgendamentoRepository


class AgendamentoService:

    def __init__(self, session: Session = None):
        self.session = session or DBSession()
        self.agendamento_repo = AgendamentoRepository(self.session)

    def criar_agendamento(self, agendamento_dto: AgendamentoDTO):
        # Verificar se já existe um agendamento com o mesmo CPF e data/hora
        existing_agendamento = self.agendamento_repo.get_agendamentos_by_cpf(agendamento_dto.cpf)
        for agendamento in existing_agendamento:
            if agendamento.data == agendamento_dto.data and agendamento.hora == agendamento_dto.hora:
                raise AgendamentoNotFoundException("Já existe um agendamento para este CPF na data e hora informada.")

        # Inserir novo agendamento
        agendamento = self.agendamento_repo.insert_agendamento(
            nome=agendamento_dto.nome,
            cpf=agendamento_dto.cpf,
            servico=agendamento_dto.servico,
            contato=agendamento_dto.contato,
            local=agendamento_dto.local,
            data=agendamento_dto.data,
            hora=agendamento_dto.hora
        )

        if not agendamento:
            raise Exception("Erro ao criar o agendamento. Agendamento não foi inserido.")

        return entity_to_dto(agendamento)

    def buscar_agendamento_por_cpf(self, cpf: str):
        # Buscar todos os agendamentos por CPF
        agendamentos = self.agendamento_repo.get_agendamentos_by_cpf(cpf)
        if not agendamentos:
            raise AgendamentoNotFoundException("Nenhum agendamento encontrado para o CPF informado.")
        return [entity_to_dto(agendamento) for agendamento in agendamentos]

    def buscar_agendamento_por_id(self, agendamento_id: int):
        # Buscar agendamento por ID
        agendamento = self.agendamento_repo.get_agendamento_by_id(agendamento_id)
        if not agendamento:
            raise AgendamentoNotFoundException("Agendamento não encontrado.")
        return entity_to_dto(agendamento)

    def atualizar_agendamento(self, agendamento_dto: AgendamentoDTO):
        # Buscar o agendamento pelo ID
        agendamento = self.agendamento_repo.get_agendamento_by_id(agendamento_dto.id)
        if not agendamento:
            raise AgendamentoNotFoundException("Agendamento não encontrado.")

        # Atualizar as informações do agendamento
        agendamento_entity = dto_to_entity(agendamento_dto)
        updated_agendamento = self.agendamento_repo.update_agendamento(
            agendamento.id,
            nome=agendamento_entity.nome,
            cpf=agendamento_entity.cpf,
            servico=agendamento_entity.servico,
            contato=agendamento_entity.contato,
            local=agendamento_entity.local,
            data=agendamento_entity.data,
            hora=agendamento_entity.hora
        )

        return entity_to_dto(updated_agendamento)

    def deletar_agendamento(self, agendamento_id: int):
        # Buscar o agendamento pelo ID
        agendamento = self.agendamento_repo.get_agendamento_by_id(agendamento_id)
        if not agendamento:
            raise AgendamentoNotFoundException("Agendamento não encontrado.")

        # Deletar o agendamento
        self.agendamento_repo.delete_agendamento(agendamento_id)
