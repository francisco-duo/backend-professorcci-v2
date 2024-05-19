from flask import jsonify, Blueprint

from config.config_database import db
from models.planejamento_model import Planejamento
from schemas.planejamento_schema import PlanejamentoSchema

PLANEJAMENTO_SCHEMA = PlanejamentoSchema()
PLANEJAMENTO_SCHEMAS = PlanejamentoSchema(many=True)

planejamento_blueprint: Blueprint = Blueprint("planejamentos", __name__)


@planejamento_blueprint.route("/planejamento", methods=["POST"])
def inserir_planejamento() -> jsonify: ...


@planejamento_blueprint.route("/planejamento", methods=["GET"])
def listar_planejamentos() -> jsonify: ...


@planejamento_blueprint.route("/planejamento/<int:plan_id>", methods=["GET"])
def ver_planejamento(plan_id: int) -> jsonify: ...


@planejamento_blueprint.route("/planejamento/<int:plan_id>", methods=["PUT"])
def atualizar_planejamento(plan_id: int) -> jsonify: ...


@planejamento_blueprint.route("/planejamento/<int:plan_id>", methods=["DELETE"])  # noqa: E501
def remover_planejamento(plan_id: int) -> jsonify: ...
