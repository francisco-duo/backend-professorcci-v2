from config.config_marshmallow import ma


class TurmaSchema(ma.Schema):
    class Meta:
        fields = ("id", "codigo", "nome", "curso", "disciplina", "fk_colaborador")  # noqa: E501
