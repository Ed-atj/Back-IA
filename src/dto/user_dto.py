# src/dto/user_dto.py

class UsuarioDTO:
    def __init__(self, id=None, nome=None, email=None, cpf=None, senha=None, contato=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha
        self.contato = contato

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf,
            'senha': self.senha,
            'contato': self.contato
        }
