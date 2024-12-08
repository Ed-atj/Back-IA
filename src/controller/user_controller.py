from flask import Blueprint, request, jsonify
from src.service.user_service import UsuarioService
from src.dto.user_dto import UsuarioDTO
from src.exceptions.user_exception import UserNotFoundException, UserAlreadyExistsException, InvalidDataException

user_controller = Blueprint('user_controller', __name__)

usuario_service = UsuarioService()

@user_controller.route("/usuarios/create", methods=["POST"])
def criar_usuario():
    try:
        usuario_dto = UsuarioDTO(**request.get_json())
        usuario_criado = usuario_service.criar_usuario(usuario_dto)
        return jsonify(usuario_criado.to_dict()), 201

    except UserAlreadyExistsException as e:
        return jsonify({"detail": str(e)}), 400
    except InvalidDataException as e:
        return jsonify({"detail": str(e)}), e.status_code
    except Exception as e:
        return jsonify({"detail": str(e)}), 500

@user_controller.route("/usuarios/<string:cpf>", methods=["GET"])
def buscar_usuario_por_cpf(cpf):
    try:
        usuario = usuario_service.buscar_usuario_por_cpf(cpf)
        return jsonify(usuario.to_dict()), 200

    except UserNotFoundException as e:
        return jsonify({"detail": str(e)}), 404
    except Exception as e:
        return jsonify({"detail": str(e)}), 500
