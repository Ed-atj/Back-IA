from sqlalchemy.orm import Session

from src.db.connection import Session as DBSession
from src.dto.user_dto import UsuarioDTO
from src.exceptions.user_exception import UserNotFoundException, UserAlreadyExistsException
from src.mapper.user_mapper import dto_to_entity, entity_to_dto
from src.repository.user_repository import UsuarioRepository


class UsuarioService:

    def __init__(self, session: Session = None):
        self.session = session or DBSession()
        self.usuario_repo = UsuarioRepository(self.session)

    def criar_usuario(self, usuario_dto: UsuarioDTO):
        if self.usuario_repo.get_user_by_cpf(usuario_dto.cpf):
            raise UserAlreadyExistsException("CPF já existe.")

        if self.usuario_repo.get_user_by_email(usuario_dto.email):
            raise UserAlreadyExistsException("E-mail já existe.")

        usuario = self.usuario_repo.insert_user(
            nome=usuario_dto.nome,
            email=usuario_dto.email,
            senha=usuario_dto.senha,
            cpf=usuario_dto.cpf,
            contato=usuario_dto.contato
        )

        if not usuario:
            raise Exception("Erro ao criar o usuário. Usuário não foi inserido.")

        return entity_to_dto(usuario)

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



