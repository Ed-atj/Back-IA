from datetime import date, time

class AgendamentoDTO:
    def __init__(self, id=None, servico: str = None, contato: str = None, local: str = None,
                 data: date = None, hora: time = None, usuario_cpf: str = None):
        self.id = id
        self.servico = servico
        self.contato = contato
        self.local = local
        self.data = data
        self.hora = hora
        self.usuario_cpf = usuario_cpf

    def to_dict(self):
        return {
            'id': self.id,
            'servico': self.servico,
            'contato': self.contato,
            'local': self.local,
            'data': self.data.strftime('%Y-%m-%d') if self.data else None,
            'hora': self.hora.strftime('%H:%M') if self.hora else None,
            'usuario_cpf': self.usuario_cpf
        }

    @classmethod
    def from_agendamento(cls, agendamento):
        return cls(
            id=agendamento.id,
            servico=agendamento.servico,
            contato=agendamento.contato,
            local=agendamento.local,
            data=agendamento.data,
            hora=agendamento.hora,
            usuario_cpf=agendamento.usuario.cpf
        )
