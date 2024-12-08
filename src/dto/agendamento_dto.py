from datetime import date, time

class AgendamentoDTO:
    def __init__(self, id=None, nome: str = None, cpf: str = None, servico: str = None,
                 contato: str = None, local: str = None, data: date = None, hora: time = None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.servico = servico
        self.contato = contato
        self.local = local
        self.data = data
        self.hora = hora

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'servico': self.servico,
            'contato': self.contato,
            'local': self.local,
            'data': self.data.strftime('%Y-%m-%d') if self.data else None,  # Formato 'YYYY-MM-DD'
            'hora': self.hora.strftime('%H:%M:%S') if self.hora else None  # Formato 'HH:MM:SS'
        }

    def __repr__(self):
        return (f"AgendamentoDTO(id={self.id}, nome={self.nome}, cpf={self.cpf}, "
                f"servico={self.servico}, contato={self.contato}, local={self.local}, "
                f"data={self.data}, hora={self.hora})")
