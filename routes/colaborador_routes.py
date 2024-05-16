from flask import Blueprint, jsonify

from models.colaborador_model import Colaborador
from schemas.colaborador_schema import ColaboradorSchema
from config.config_database import db

COLABORADORES_SCHEMA = ColaboradorSchema(many=True)
COLABORADOR_SCHEMA = ColaboradorSchema()

colaborador_blueprint: Blueprint = Blueprint("colaborador", __name__)


@colaborador_blueprint.route("/colaborador/<string:email>", methods=["GET"])
def obter_colaborador(email: str) -> jsonify:
    consulta = db.session.query(Colaborador).filter_by(email=email).first()  # noqa: E501

    if consulta:
        return jsonify(COLABORADOR_SCHEMA.dump(consulta))
    else:
        return jsonify({"status": "404", "response": "colaborador não encontrado", "consulta": consulta})  # noqa: E501
