"""
    Configurações necessárias para o funcionamento do sqlalchemy.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base

    Args:
        DeclarativeBase (class): herança da biblioteca sqlalchemy para criar
        tabelas sem a necessidade da linguagem sql.
    """
    pass


# Instância da classe SQLAlchemy
db: SQLAlchemy = SQLAlchemy(model_class=Base)


def salvar(objeto) -> None:
    """
    função: salvar

    Args:
        objeto (class): Modelo de tabela SQLAlchemy
    """
    db.session.add(objeto)
    db.session.commit()


def remover(objeto) -> None:
    """
    função: remover

    Args:
        objeto (class): Modelo de tabela SQLAlchemy
    """
    db.session.delete(objeto)
    db.session.commit()
