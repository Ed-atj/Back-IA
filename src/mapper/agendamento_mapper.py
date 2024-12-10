from src.dto.agendamento_dto import AgendamentoDTO
from src.model.agendamento import Agendamento

def entity_to_dto(agendamento):

    if not agendamento:
        return None

    return AgendamentoDTO(
        id=agendamento.id,
        servico=agendamento.servico,
        contato=agendamento.contato,
        local=agendamento.local,
        data=agendamento.data,
        hora=agendamento.hora,
        usuario_cpf=agendamento.usuario.cpf
    )

def dto_to_entity(dto):

    if not dto:
        return None

    return Agendamento(
        id=dto.id,
        servico=dto.servico,
        contato=dto.contato,
        local=dto.local,
        data=dto.data,
        hora=dto.hora,
        usuario_cpf=dto.usuario_cpf
    )
