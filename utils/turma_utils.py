from asyncio.log import logger

from services.service_sophia import ServiceSophia

from models.turma_model import Turma
from models.colaborador_model import Colaborador
from config.config_database import db, salvar, rollback


def _inserir_turmas_no_db() -> None:
    """Insere as turmas no banco de dados."""

    try:
        for turma in ServiceSophia().listar_turmas():
            colaborador_da_turma = turma["colaborador"]
            disciplina_por_professor = turma["professoresDisciplinas"]

            # Verifica se os colaboradores estão
            # armazenados corretamente no servico
            if colaborador_da_turma is not None and colaborador_da_turma:
                for disciplina in disciplina_por_professor:
                    for colaborador in disciplina["colaboradores"]:
                        try:
                            consultar_colaborador = db.session.query(
                                Colaborador).filter_by(codigo=colaborador["codigo"]).first()  # noqa: E501

                            if consultar_colaborador:
                                modelo_turma = Turma(
                                    codigo=turma["codigo"],
                                    nome=turma["nome"],
                                    curso=turma["curso"]["descricao"],
                                    disciplina=disciplina["nome"],
                                    fk_colaborador=consultar_colaborador.id
                                )
                                salvar(modelo_turma)
                        except Exception as err_modelos:
                            return logger.error("Erro ao consultar colaborador ou inserir turma\n\nDescrição do erro:\n   {}".format(err_modelos))  # noqa: E501

                            rollback()
    except Exception as err_listar_turma:
        return logger.error("Erro ao listar turmas\n\nDescrição do erro:\n   {}".format(err_listar_turma))  # noqa: E501


if __name__ == "__main__":
    _inserir_turmas_no_db()
