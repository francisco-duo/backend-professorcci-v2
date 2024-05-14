from app.config.config_marshmallow import ma
from app.models.colaborador_model import Colaborador


class ColaboradorSchema(ma.Schema):
    class Meta:
        model = Colaborador
