from flask import jsonify
from flask_restful import Resource

from utils.colaborador_utils import inserir_colaboradores_na_db


class ColaboradorResource(Resource):
    def get(self) -> jsonify:
        return jsonify(inserir_colaboradores_na_db())
