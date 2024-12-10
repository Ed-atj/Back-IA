import logging

from flask import Blueprint, request, jsonify
from src.service.agendamento_service import AgendamentoService
from src.dto.agendamento_dto import AgendamentoDTO
from src.exceptions.agendamento_exception import AgendamentoNotFoundException, InvalidDataException

agendamento_controller = Blueprint('agendamento_controller', __name__)
agendamento_service = AgendamentoService()

# Utilitário para respostas de erro
def error_response(message, status_code):
    return jsonify({"detail": message}), status_code

@agendamento_controller.route("/agendamentos/create", methods=["POST"])
def criar_agendamento():
    try:
        dados_agendamento = request.get_json()

        campos_obrigatorios = ['servico', 'contato', 'local', 'data', 'hora', 'usuario_cpf']
        for campo in campos_obrigatorios:
            if campo not in dados_agendamento:
                raise InvalidDataException(f"O campo '{campo}' é obrigatório.")

        agendamento_dto = AgendamentoDTO(**dados_agendamento)
        agendamento_criado = agendamento_service.create_agendamento(agendamento_dto)

        return jsonify(agendamento_criado.to_dict()), 201

    except InvalidDataException as e:
        logging.error(f"Erro de dados inválidos: {str(e)}")
        return error_response(str(e), 400)
    except AgendamentoNotFoundException as e:
        logging.error(f"Agendamento não encontrado: {str(e)}")
        return error_response(str(e), 404)
    except Exception as e:
        logging.error(f"Erro inesperado: {str(e)}")
        return error_response("Erro interno no servidor.", 500)



@agendamento_controller.route("/agendamentos/cpf/<string:cpf>", methods=["GET"])
def listar_agendamentos(cpf):
    try:
        agendamentos = agendamento_service.get_agendamentos_by_cpf(cpf)

        if not agendamentos:
            raise AgendamentoNotFoundException("Nenhum agendamento encontrado para o CPF fornecido.")

        return jsonify([agendamento.to_dict() for agendamento in agendamentos]), 200

    except AgendamentoNotFoundException as e:
        return error_response(str(e), 404)
    except Exception as e:
        return error_response("Erro interno no servidor.", 500)


@agendamento_controller.route("/agendamentos/id/<int:agendamento_id>", methods=["GET"])
def buscar_agendamento_por_id(agendamento_id):
    try:
        agendamento = agendamento_service.get_agendamento_by_id(agendamento_id)

        if not agendamento:
            raise AgendamentoNotFoundException("Agendamento não encontrado.")

        return jsonify(agendamento.to_dict()), 200

    except AgendamentoNotFoundException as e:
        return error_response(str(e), 404)
    except Exception as e:
        return error_response("Erro interno no servidor.", 500)


@agendamento_controller.route("/agendamentos/update", methods=["PUT"])
def atualizar_agendamento():
    try:
        dados_agendamento = request.get_json()

        if 'id' not in dados_agendamento:
            raise InvalidDataException("O campo 'id' é obrigatório para atualizar um agendamento.")

        agendamento_dto = AgendamentoDTO(**dados_agendamento)
        agendamento_atualizado = agendamento_service.update_agendamento(agendamento_dto)

        return jsonify(agendamento_atualizado.to_dict()), 200

    except InvalidDataException as e:
        return error_response(str(e), 400)
    except AgendamentoNotFoundException as e:
        return error_response(str(e), 404)
    except Exception as e:
        return error_response("Erro interno no servidor.", 500)


@agendamento_controller.route("/agendamentos/delete/<int:agendamento_id>", methods=["DELETE"])
def deletar_agendamento(agendamento_id):
    try:
        agendamento_service.delete_agendamento(agendamento_id)
        return jsonify({"message": "Agendamento deletado com sucesso."}), 200

    except AgendamentoNotFoundException as e:
        return error_response(str(e), 404)
    except Exception as e:
        return error_response("Erro interno no servidor.", 500)
