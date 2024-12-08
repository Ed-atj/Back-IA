from flask import Blueprint, request, jsonify
from src.service.agendamento_service import AgendamentoService
from src.dto.agendamento_dto import AgendamentoDTO
from src.exceptions.agendamento_exception import AgendamentoNotFoundException

agendamento_controller = Blueprint('agendamento_controller', __name__)

agendamento_service = AgendamentoService()

@agendamento_controller.route("/agendamentos/create", methods=["POST"])
def criar_agendamento():
    try:
        agendamento_dto = AgendamentoDTO(**request.get_json())
        agendamento_criado = agendamento_service.criar_agendamento(agendamento_dto)
        return jsonify(agendamento_criado.to_dict()), 201

    except AgendamentoNotFoundException as e:
        return jsonify({"detail": str(e)}), 404
    except Exception as e:
        return jsonify({"detail": str(e)}), 500


@agendamento_controller.route("/agendamentos/cpf/<string:cpf>", methods=["GET"])
def listar_agendamentos(cpf):
    try:
        agendamentos = agendamento_service.buscar_agendamento_por_cpf(cpf)
        return jsonify([agendamento.to_dict() for agendamento in agendamentos]), 200

    except AgendamentoNotFoundException as e:
        return jsonify({"detail": str(e)}), 404
    except Exception as e:
        return jsonify({"detail": str(e)}), 500


@agendamento_controller.route("/agendamentos/id/<int:agendamento_id>", methods=["GET"])
def buscar_agendamento_por_id(agendamento_id):
    try:
        agendamento = agendamento_service.buscar_agendamento_por_id(agendamento_id)
        return jsonify(agendamento.to_dict()), 200

    except AgendamentoNotFoundException as e:
        return jsonify({"detail": str(e)}), 404
    except Exception as e:
        return jsonify({"detail": str(e)}), 500


@agendamento_controller.route("/agendamentos/update", methods=["PUT"])
def atualizar_agendamento():
    try:
        agendamento_dto = AgendamentoDTO(**request.get_json())
        agendamento_atualizado = agendamento_service.atualizar_agendamento(agendamento_dto)
        return jsonify(agendamento_atualizado.to_dict()), 200

    except AgendamentoNotFoundException as e:
        return jsonify({"detail": str(e)}), 404
    except Exception as e:
        return jsonify({"detail": str(e)}), 500


@agendamento_controller.route("/agendamentos/delete/<int:agendamento_id>", methods=["DELETE"])
def deletar_agendamento(agendamento_id):
    try:
        agendamento_service.deletar_agendamento(agendamento_id)
        return jsonify({"message": "Agendamento deletado com sucesso."}), 200

    except AgendamentoNotFoundException as e:
        return jsonify({"detail": str(e)}), 404
    except Exception as e:
        return jsonify({"detail": str(e)}), 500
