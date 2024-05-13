from asyncio.log import logger
from sqlalchemy.exc import IntegrityError

from models.colaborador_model import Colaborador
from config.config_database import salvar, consultar_colaborador, atualizar
from services.service_sophia import ServiceSophia


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


def atualizar_colaboradores_na_db():
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
                    consulta = consultar_colaborador(Colaborador, colaborador["email"])  # noqa: E501

                    if consulta:
                        consulta.codigo = colaborador["codigo"]
                        consulta.nome = colaborador["nome"]
                        consulta.email = colaborador["email"]
                        consulta.leciona = colaborador["leciona"]

                        atualizar()

            except Exception as err_consultar_colaborador:
                logger.error(f"Colaborador com código {colaborador['codigo']} não encontrado! \n{err_consultar_colaborador}")  # noqa: E501

            logger.info(f"Usuário atualizado com sucesso {colaborador.get('nome', '')}")  # noqa: E501
    except Exception as err_colaboradores:
        logger.error(f"Erro ao percorrer colaboradores {err_colaboradores}")  # noqa: E501


if __name__ == "__main__":
    inserir_colaboradores_na_db()
