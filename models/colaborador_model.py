from sqlalchemy.orm import Mapped, mapped_column
from config.config_database import db


class Colaborador(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)  # noqa: E501
    codigo: Mapped[int] = mapped_column(unique=True)
    nome: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    leciona: Mapped[bool] = mapped_column()
