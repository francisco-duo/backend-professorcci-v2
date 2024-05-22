from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Mapped, mapped_column
from config.config_database import db


class Usuario(db.Model):
    __tablename__ = "USUARIOS"

    id: Mapped[int] = mapped_column(
        autoincrement=True, primary_key=True, unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def verificar_senha(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<Usuario {self.username}>"
