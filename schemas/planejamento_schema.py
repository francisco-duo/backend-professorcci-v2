from config.config_marshmallow import ma


class PlanejamentoSchema(ma.Schema):
    class Meta:
        fields = ("id", "turma", "disciplinas", "taxonomias", "dt_inicio",
                  "dt_termino", "dt_registro", "dt_registro", "cod_classroom",
                  "cod_classroom_material", "publicado")
