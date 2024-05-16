from config.config_marshmallow import ma


class ColaboradorSchema(ma.Schema):
    class Meta:
        fields = ("id", "codigo", "nome", "email", "leciona")
