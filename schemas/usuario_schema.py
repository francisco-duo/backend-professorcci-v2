from config.config_marshmallow import ma


class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ("username", "password")
