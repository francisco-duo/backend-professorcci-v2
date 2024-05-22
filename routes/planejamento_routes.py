from flask import jsonify, Blueprint, request
from flask_jwt_extended import jwt_required

from config.config_database import db, salvar, remover
from models.planejamento_model import Planejamento
from schemas.planejamento_schema import PlanejamentoSchema

PLANEJAMENTO_SCHEMA = PlanejamentoSchema()
PLANEJAMENTO_SCHEMAS = PlanejamentoSchema(many=True)

planejamento_blueprint: Blueprint = Blueprint("planejamentos", __name__)


@planejamento_blueprint.route("/planejamento", methods=["POST"])
def inserir_planejamento() -> jsonify:
    """Insere um dados referentes ao modelo no banco de dados"""

    dados_planejamento = request.get_json()

    if not dados_planejamento:
        return jsonify({"error": "Dados não enviados ou inválidos"}), 400

    modelo_planejamento = Planejamento(
        turma=dados_planejamento.get("turma", ""),
        disciplinas=dados_planejamento.get("disciplinas", ""),
        taxonomias=dados_planejamento.get("taxonomias", ""),
        dt_inicio=dados_planejamento.get("dt_inicio", ""),
        dt_termino=dados_planejamento.get("dt_termino", ""),
        dt_registro=dados_planejamento.get("dt_registro", ""),
        cod_classroom=dados_planejamento.get("cod_classroom"),
        cod_classroom_material=dados_planejamento.get("cod_classroom_material"),  # noqa: E501
        publicado=dados_planejamento.get("publicado")
    )
    salvar(modelo_planejamento)

    return jsonify({"messagem": "Planejamento inserido com sucesso!"})


@jwt_required
@planejamento_blueprint.route("/planejamento", methods=["GET"])
def listar_planejamentos() -> jsonify:
    """Retorna todos os dados na tabela Planejamento"""
    try:
        print(request.headers["Authorization"])
        return jsonify(PLANEJAMENTO_SCHEMAS.dump(db.session.query(Planejamento).all())), 200  # noqa:E501
    except Exception as err:
        return jsonify({"error": err}), 404


@planejamento_blueprint.route("/planejamento/<int:plan_id>", methods=["GET"])
def ver_planejamento(plan_id: int) -> jsonify:
    """Lista um registro por id do planejamento"""
    try:
        return jsonify(PLANEJAMENTO_SCHEMA.dump(db.session.query(Planejamento).filter_by(id=plan_id).first())), 200  # noqa: E501
    except Exception as err:
        return jsonify({"error": f"Planejamento de id {plan_id} não encontrada\n{err}"}), 404  # noqa: E501


@planejamento_blueprint.route("/planejamento/<int:plan_id>", methods=["PUT"])
def atualizar_planejamento(plan_id: int) -> jsonify:
    """Atualiza um planejamento a partir do seu id"""
    try:
        dados_planejamento = request.get_json()

        if not dados_planejamento:
            return jsonify({"erro": "Dados enviados inválidos"})

        consulta = db.session.query(Planejamento).filter_by(id=plan_id).first()

        if not consulta:
            return jsonify({"erro": "Registro não encontrado"})

        consulta.turma = dados_planejamento.get("turma", consulta.turma)
        consulta.disciplinas = dados_planejamento.get("disciplinas", consulta.disciplinas)  # noqa: E501
        consulta.taxonomias = dados_planejamento.get("taxonomias", consulta.taxonomias)  # noqa: E501
        consulta.dt_inicio = dados_planejamento.get("dt_inicio", consulta.dt_inicio)  # noqa: E501
        consulta.dt_termino = dados_planejamento.get("dt_termino", consulta.dt_termino)  # noqa: E501
        consulta.dt_registro = dados_planejamento.get("dt_registro", consulta.dt_registro)  # noqa: E501
        consulta.cod_classroom = dados_planejamento.get("cod_classroom", consulta.cod_classroom)  # noqa: E501
        consulta.cod_classroom_material = dados_planejamento.get("cod_classroom_material", consulta.cod_classroom_material)  # noqa: E501
        consulta.publicado = dados_planejamento.get("publicado", consulta.publicado)  # noqa: E501

        salvar(consulta)

        return jsonify({"mensagem": "Atualizado com sucesso"}), 200
    except Exception as err:
        return jsonify({"err": str(err)}), 500


@planejamento_blueprint.route("/planejamento/<int:plan_id>", methods=["DELETE"])  # noqa: E501
def remover_planejamento(plan_id: int) -> jsonify:
    """Remove um planejamento baseado no id passado"""
    try:
        consulta = db.session.query(Planejamento).filter_by(id=plan_id).first()

        if not consulta:
            return jsonify({"erro": "Registro não encontrado"})

        remover(consulta)

        return jsonify({"mensagem": "Removido com sucesso"}), 200
    except Exception as err:
        return jsonify({"error": str(err)})
