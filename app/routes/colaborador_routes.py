from flask import Blueprint, jsonify

from app.models.colaborador_model import Colaborador
from app.schemas.colaborador_schema import ColaboradorSchema
from app.config.config_database import db

COLABORADORES_SCHEMA = ColaboradorSchema(many=True)
COLABORADORE_SCHEMA = ColaboradorSchema()

colaborador_blueprint: Blueprint = Blueprint("colaborador", __name__)


@colaborador_blueprint.route("/<string:email>", methods=["GET"])
def obter_colaborador(email: str) -> jsonify:
    consulta = db.session.query(Colaborador).filter_by(email=email).first()  # noqa: E501

    if consulta:
        return jsonify(COLABORADORE_SCHEMA.dump(consulta))
    else:
        return jsonify({"status": "404", "response": "colaborador não encontrado", "consulta": consulta})  # noqa: E501
