from flask import Flask
from flask_cors import CORS

from routes import database_routes
from routes import colaborador_routes
from routes import planejamento_routes
from routes import autenticacao_routes

from config.config_database import db
from config.config_migrate import migrate
from config.config_marshmallow import ma
from config.config_flask import Desenvolvimento
from config.config_jwt import jwt

# Modelos de .models/
from models.colaborador_model import Colaborador  # noqa: F401
from models.turma_model import Turma  # noqa: F401
from models.planejamento_model import Planejamento  # noqa: F401
from models.usuario_model import Usuario  # noqa: F401


def register_blueprints(app: Flask):
    app.register_blueprint(database_routes.banco_blueprint)
    app.register_blueprint(colaborador_routes.colaborador_blueprint)
    app.register_blueprint(planejamento_routes.planejamento_blueprint)
    app.register_blueprint(autenticacao_routes.autenticacao_blueprint)


app: Flask = Flask(__name__)

app.config.from_object(Desenvolvimento())

# CORS
CORS(
    app, resources={
        r"/autenticacao/*": {
            "origins": "*",
            "supports_credentials": True,
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        },
        r"/planejamento/*": {
            "origins": "*",
            "supports_credentials": True,
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        },
    }
)

# Inicia o banco de dados e migração
jwt.init_app(app)
db.init_app(app)
ma.init_app(app)
migrate.init_app(app, db)

register_blueprints(app)

if __name__ == "__main__":
    app.run()
