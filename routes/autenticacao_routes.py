from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

from models.usuario_model import Usuario
from schemas.usuario_schema import UsuarioSchema
from config.config_database import salvar

USUARIO_SCHEMA = UsuarioSchema()
USUARIOS_SCHEMA = UsuarioSchema(many=True)

autenticacao_blueprint: Blueprint = Blueprint("autenticacao", __name__)


@autenticacao_blueprint.route("/autenticacao/cadastro", methods=["POST"])
def registrar_usuario():
    dados = request.get_json()

    if not dados:
        return jsonify({
            "error": "Dados não enviados ou inválidos"
        })

    username = dados["username"]
    password = dados["password"]

    modelo_usuario = Usuario(
        username=username,
        password=password
    )
    salvar(modelo_usuario)

    return jsonify(USUARIO_SCHEMA.dump(Usuario.query.filter_by(username=username).first())), 200  # noqa: E501


@autenticacao_blueprint.route("/autenticacao/login", methods=["POST"])
def autenticacao():
    dados = request.get_json()

    if not dados:
        return jsonify({
            "error": "Dados não enviados ou inválidos"
        })

    username = dados["username"]
    password = dados["password"]

    usuario = Usuario.query.filter_by(username=username).first_or_404()

    if not usuario.verificar_senha(password=password):
        return jsonify({"error": "Senha ou usuário inválidos."}), 403

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)
