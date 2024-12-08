from src.dto.agendamento_dto import AgendamentoDTO
from src.model.agendamento import Agendamento

def entity_to_dto(agendamento):

    if not agendamento:
        return None

    return AgendamentoDTO(
        id=agendamento.id,
        nome=agendamento.nome,
        cpf=agendamento.cpf,
        servico=agendamento.servico,
        contato=agendamento.contato,
        local=agendamento.local,
        data=agendamento.data,
        hora=agendamento.hora
    )

def dto_to_entity(dto):

    if not dto:
        return None

    return Agendamento(
        id=dto.id,
        nome=dto.nome,
        cpf=dto.cpf,
        servico=dto.servico,
        contato=dto.contato,
        local=dto.local,
        data=dto.data,
        hora=dto.hora
    )
