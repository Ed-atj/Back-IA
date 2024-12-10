import bcrypt
from sqlalchemy.orm import Session

from src.db.connection import Session as DBSession
from src.dto.user_dto import UsuarioDTO
from src.exceptions.user_exception import UserNotFoundException, UserAlreadyExistsException, InvalidDataException
from src.mapper.user_mapper import dto_to_entity, entity_to_dto
from src.model.user import Usuario
from src.repository.user_repository import UsuarioRepository
from src.repository.agendamento_repository import AgendamentoRepository


class UsuarioService:

    def __init__(self, session: Session = None):
        self.session = session or DBSession()
        self.usuario_repo = UsuarioRepository(self.session)
        self.agendamento_repo = AgendamentoRepository(self.session)

    def login(self, email, senha):
        usuario = self.buscar_usuario_por_email(email)
        user_entity = dto_to_entity(usuario)

        if not user_entity.validar_senha(senha):
            raise InvalidDataException("Senha inválida.")

        return usuario

    def criar_usuario(self, usuario_dto: UsuarioDTO):
        if self.usuario_repo.get_user_by_cpf(usuario_dto.cpf):
            raise UserAlreadyExistsException("Usuário já existe.")

        salt = bcrypt.gensalt()
        senha_hash = bcrypt.hashpw(usuario_dto.senha.encode('utf-8'), salt).decode('utf-8')

        novo_usuario = Usuario(
            nome=usuario_dto.nome,
            email=usuario_dto.email,
            senha=senha_hash,
            cpf=usuario_dto.cpf,
            contato=usuario_dto.contato
        )
        self.usuario_repo.insert_user(novo_usuario)
        return entity_to_dto(novo_usuario)

    def buscar_usuario_por_cpf(self, cpf: str):
        usuario = self.usuario_repo.get_user_by_cpf(cpf)
        if not usuario:
            raise UserNotFoundException("CPF não existe.")
        return entity_to_dto(usuario)

    def buscar_usuario_por_email(self, email: str):
        usuario = self.usuario_repo.get_user_by_email(email)
        if not usuario:
            raise UserNotFoundException("Email não existe.")
        return entity_to_dto(usuario)

    def atualizar_usuario(self, user_dto: UsuarioDTO):
        usuario = self.usuario_repo.get_user_by_cpf(user_dto.cpf)
        if not usuario:
            raise UserNotFoundException("CPF não existe.")

        user_entity = dto_to_entity(user_dto)
        updated_usuario = self.usuario_repo.update_user(usuario.id, user_entity)

        return entity_to_dto(updated_usuario)

    def deletar_usuario(self, cpf: str):
        usuario = self.usuario_repo.get_user_by_cpf(cpf)
        if not usuario:
            raise UserNotFoundException("CPF não existe.")

        self.usuario_repo.delete_user(usuario.id)

    def buscar_agendamentos_por_usuario_cpf(self, cpf: str):
        usuario = self.usuario_repo.get_user_by_cpf(cpf)
        if not usuario:
            raise UserNotFoundException("Usuário não encontrado.")

        agendamentos = usuario.agendamentos.all()
        return agendamentos


