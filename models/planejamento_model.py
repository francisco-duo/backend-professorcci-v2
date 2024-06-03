from sqlalchemy.orm import Mapped, mapped_column
from config.config_database import db


class Planejamento(db.Model):
    """Modelo da tabela planejamento

    fields:
        id: int unique
        turma: str
        disciplinas: str
        taxonomias: str
        dt_inicio: date
        dt_termino: date
        dt_registro: date
        cod_classroom: str
        cod_classroom_material: str
        publicado: bool
    """
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)  # noqa: E501
    turma: Mapped[str] = mapped_column()
    disciplinas: Mapped[str] = mapped_column()
    taxonomias: Mapped[str] = mapped_column()
    dt_inicio: Mapped[str] = mapped_column()
    dt_termino: Mapped[str] = mapped_column()
    dt_registro: Mapped[str] = mapped_column()
    planejamento: Mapped[str] = mapped_column()
    cod_classroom: Mapped[str] = mapped_column()
    cod_classroom_material: Mapped[str] = mapped_column()
    publicado: Mapped[str] = mapped_column()
