from flask import jsonify
from flask_restful import Resource

from utils.colaborador_utils import (
    inserir_colaboradores_na_db, atualizar_colaboradores_na_db
)


class ColaboradorResource(Resource):
    def get(self) -> jsonify:
        inserir_colaboradores_na_db()
        return jsonify({"status": ""})

    def post(self) -> jsonify:
        atualizar_colaboradores_na_db()
        return jsonify({"status": ""})
