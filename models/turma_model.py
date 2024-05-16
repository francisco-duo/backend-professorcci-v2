from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from config.config_database import db


class Turma(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)  # noqa: E501
    codigo: Mapped[int] = mapped_column()
    nome: Mapped[str] = mapped_column()
    curso: Mapped[str] = mapped_column()
    disciplina: Mapped[str] = mapped_column()
    fk_colaborador: Mapped[int] = mapped_column(ForeignKey("colaborador.id"))
    colaborador = relationship("Colaborador")
