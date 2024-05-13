from asyncio.log import logger
from sqlalchemy.exc import IntegrityError

from models.colaborador_model import Colaborador
from config.config_database import salvar
from services.service_sophia import ServiceSophia


def inserir_colaboradores_na_db():
    try:
        for colaborador in ServiceSophia().listar_colaboradores():
            try:
                if colaborador["leciona"]:  # noqa: E501
                    colaborador_modelo = Colaborador(
                        codigo=colaborador.get("codigo"),
                        nome=colaborador.get("nome"),
                        email=colaborador["email"] if colaborador["email"] is not None else "none@email.com",  # noqa: E501
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
