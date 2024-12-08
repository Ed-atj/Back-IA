from sqlalchemy import Integer, String, Date, Time
from sqlalchemy.orm import mapped_column
from src.db.connection import Base


class Agendamento(Base):
    __tablename__ = 'agendamentos'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome = mapped_column(String(100), nullable=False)
    cpf = mapped_column(String(11), nullable=False)
    servico = mapped_column(String(100), nullable=False)
    contato = mapped_column(String(20), nullable=False)
    local = mapped_column(String(100), nullable=False)
    data = mapped_column(Date, nullable=False)
    hora = mapped_column(Time, nullable=False)

    def __repr__(self):
        return (f"Agendamento(id={self.id}, nome={self.nome}, cpf={self.cpf}, "
                f"servico={self.servico}, contato={self.contato}, "
                f"local={self.local}, data={self.data}, hora={self.hora})")

