from flask import jsonify, Blueprint

from utils.colaborador_utils import inserir_colaboradores_na_db
from utils.turma_utils import _inserir_turmas_no_db

banco_blueprint = Blueprint('database', __name__)


@banco_blueprint.route("/inserir-colaboradores-banco-de-dados", methods=["GET"])  # noqa: E501
def inserir_colaborador_no_banco_de_dados() -> jsonify:
    try:
        inserir_colaboradores_na_db()
        return jsonify({
            "status": "200",
            "descrição": "Colaboradores inseridos com sucesso"
        })
    except Exception as err_inserir_colaboradores:
        return jsonify({
            "status": "404",
            'descrição': err_inserir_colaboradores
        })


@banco_blueprint.route("/inserir-turmas-banco-de-dados", methods=["GET"])
def inserir_turmas_no_banco_de_dados() -> jsonify:
    try:
        _inserir_turmas_no_db()
        return jsonify({
            "status": "200",
            "descrição": "Turmas inseridas com sucesso"
        })
    except Exception as err_inserir_turmas:
        return jsonify({
            "status": "404",
            'descrição': err_inserir_turmas
        })
