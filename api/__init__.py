from flask_restful import Api

from .colaborador_api import ColaboradorResource


def init_app(api: Api):
    api.add_resource(ColaboradorResource, "/utils/inserir/colaboradores")
