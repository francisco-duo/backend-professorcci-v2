from asyncio.log import logger
from sqlalchemy.exc import IntegrityError

from app.models.colaborador_model import Colaborador
from app.config.config_database import salvar
from app.services.service_sophia import ServiceSophia


def inserir_colaboradores_na_db():
    """
    inserir_colaboradores_na_db: function

    descrição:
        Obtém todos os colaboradores do service ServiceSophia().
        Percorre a o retorno do método da classe ServiceSophia() e então
        salva no banco de dados com a função salvar()
    """
    try:
        for colaborador in ServiceSophia().listar_colaboradores():
            try:
                if colaborador["leciona"] and colaborador["email"] is not None:  # noqa: E501
                    colaborador_modelo = Colaborador(
                        codigo=colaborador.get("codigo"),
                        nome=colaborador.get("nome"),
                        email=colaborador["email"],
                        leciona=colaborador.get("leciona")
                    )

                    salvar(colaborador_modelo)
            except IntegrityError:
                logger.warning(f"O colaborador {colaborador['nome']} já existe na base de dados")  # noqa: E501
            except Exception as err_inserir_colaborador:
                logger.error(f"Erro ao inserir o colaborador {colaborador['nome']}: {err_inserir_colaborador}")  # noqa: E501

            logger.info(f"Usuário armazenado com sucesso {colaborador.get('nome', '')}")  # noqa: E501
    except Exception as err_colaboradores:
        logger.error(f"Erro ao percorrer colaboradores {err_colaboradores}")  # noqa: E501


if __name__ == "__main__":
    inserir_colaboradores_na_db()
