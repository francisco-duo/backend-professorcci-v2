from flask import Flask

from config.config_flask import Desenvolvimento
from config.config_database import db

# Modelos de .models/
from models.colaborador_model import Colaborador  # noqa: F401

app: Flask = Flask(__name__)
app.config.from_object(Desenvolvimento())

# Inicia o banco de dados
db.init_app(app)

# Cria as tabelas baseando-se nos modelos em ./models
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run()
