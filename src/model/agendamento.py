# src/models/agendamento.py

from sqlalchemy import Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from src.db.connection import Base

class Agendamento(Base):
    __tablename__ = 'agendamentos'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    servico = mapped_column(String(100), nullable=False)
    contato = mapped_column(String(20), nullable=False)
    local = mapped_column(String(100), nullable=False)
    data = mapped_column(Date, nullable=False)
    hora = mapped_column(Time, nullable=False)

    usuario_id = mapped_column(Integer, ForeignKey('usuarios.id'), nullable=False)

    usuario = relationship('Usuario', back_populates='agendamentos')

    def __repr__(self):
        return (f"Agendamento(id={self.id}, nome={self.usuario.nome}, cpf={self.usuario.cpf}, "
                f"servico={self.servico}, contato={self.contato}, "
                f"local={self.local}, data={self.data}, hora={self.hora})")

    def to_dict(self):
        return {
            "id": self.id,
            "servico": self.servico,
            "contato": self.contato,
            "local": self.local,
            "data": self.data.isoformat() if self.data else None,
            "hora": str(self.hora) if self.hora else None,
            "usuario": {
                "id": self.usuario.id,
                "nome": self.usuario.nome,
                "cpf": self.usuario.cpf,
                "email": self.usuario.email
            }
        }