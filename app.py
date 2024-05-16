from flask import Flask

from routes import database_routes
from routes import colaborador_routes

from config.config_database import db
from config.config_migrate import migrate
from config.config_marshmallow import ma
from config.config_flask import Desenvolvimento

# Modelos de .models/
from models.colaborador_model import Colaborador  # noqa: F401
from models.turma_model import Turma  # noqa: F401


def register_blueprints(app: Flask):
    app.register_blueprint(database_routes.banco_blueprint)  # noqa: E501
    app.register_blueprint(colaborador_routes.colaborador_blueprint)  # noqa: E501


app: Flask = Flask(__name__)

app.config.from_object(Desenvolvimento())

# Inicia o banco de dados e migração
db.init_app(app)
ma.init_app(app)
migrate.init_app(app, db)

register_blueprints(app)

if __name__ == "__main__":
    app.run()
