from flask import Flask

from app.routes import database_routes
from app.routes import colaborador_routes

from app.config.config_database import db
from app.config.config_migrate import migrate
from app.config.config_marshmallow import ma
from app.config.config_flask import Desenvolvimento as dev

# Modelos de .models/
from app.models.colaborador_model import Colaborador  # noqa: F401


def create_app(config_settings=None) -> Flask:
    app: Flask = Flask(__name__)

    if config_settings is not None:
        app.config.from_object(config_settings)
    else:
        pass

    # Inicia o banco de dados e migração
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(database_routes.banco_blueprint)  # noqa: E501
    app.register_blueprint(colaborador_routes.colaborador_blueprint)  # noqa: E501
