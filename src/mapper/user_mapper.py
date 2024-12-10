from src.model.user import Usuario
from src.dto.user_dto import UsuarioDTO


def dto_to_entity(usuario_dto: UsuarioDTO) -> Usuario:
    return Usuario(
        nome=usuario_dto.nome,
        email=usuario_dto.email,
        senha=usuario_dto.senha,
        cpf=usuario_dto.cpf,
        contato=usuario_dto.contato
    )
def entity_to_dto(usuario: Usuario) -> UsuarioDTO:
    return UsuarioDTO(
        id=usuario.id,
        nome=usuario.nome,
        email=usuario.email,
        senha=usuario.senha,
        cpf=usuario.cpf,
        contato=usuario.contato
    )
