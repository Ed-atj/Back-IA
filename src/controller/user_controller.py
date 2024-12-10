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


@user_controller.route("/usuarios/login", methods=["POST"])
def login_usuario():
    try:
        dados = request.get_json()
        email = dados.get("email")
        senha = dados.get("senha")

        if not email or not senha:
            raise InvalidDataException("Email e senha são obrigatórios.")

        usuario_logado = usuario_service.login(email, senha)

        return jsonify(usuario_logado.to_dict()), 200

    except UserNotFoundException as e:
        return jsonify({"detail": str(e)}), 404
    except InvalidDataException as e:
        return jsonify({"detail": str(e)}), e.status_code
    except Exception as e:
        return jsonify({"detail": str(e)}), 500


@user_controller.route('/usuarios/<string:cpf>/agendamentos', methods=['GET'])
def get_agendamentos_por_usuario(cpf):
    try:
        # Chama o serviço para buscar os agendamentos do usuário pelo CPF
        agendamentos = usuario_service.buscar_agendamentos_por_usuario_cpf(cpf)

        if not agendamentos:
            return jsonify({"message": "Nenhum agendamento encontrado para este usuário."}), 404

        # Retorna os agendamentos em formato JSON
        return jsonify({"agendamentos": [agendamento.to_dict() for agendamento in agendamentos]}), 200

    except UserNotFoundException:
        return jsonify({"message": "Usuário não encontrado."}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500