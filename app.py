from flask import Flask

from config.config_flask import Desenvolvimento
from config.config_database import db
from config.config_migrate import migrate

# Modelos de .models/
from models.colaborador_model import Colaborador  # noqa: F401

app: Flask = Flask(__name__)
app.config.from_object(Desenvolvimento())

# Inicia o banco de dados e migração
db.init_app(app)
migrate.init_app(app, db)


if __name__ == "__main__":
    app.run()
