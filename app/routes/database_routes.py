from flask import jsonify, Blueprint

from app.utils.colaborador_utils import inserir_colaboradores_na_db

banco_blueprint = Blueprint('database', __name__)


@banco_blueprint.route("/inserir-banco-de-dados", methods=["GET"])
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
