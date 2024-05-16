from flask import jsonify, Blueprint

from config.config_database import db
from models.turma_model import Turma
from models.colaborador_model import Colaborador
from schemas.turma_schema import TurmaSchema

TURMAS_SCHEMA = TurmaSchema(many=True)

turma_blueprint: Blueprint = Blueprint("turmas", __name__)


@turma_blueprint.route("/turmas/<string: email>", methods=["GET"])
def obeter_turmas_do_colaborador(email: str):
    """Retorna o corpo dos objetos filtrados apartir do email passado na url"""

    try:
        consulta_colaborador = db.session.query(Colaborador).filter_by(email=email).firt()
        
        try:
            consultar_turmas = db.session.query(Turma).filter_by(fk_colaborador=consulta_colaborador.id)
            
            return 
    except Exception as err_consulta_colaborador:
        
        return jsonify({"status": "404", "response": "Colaborador não encontrado"})
