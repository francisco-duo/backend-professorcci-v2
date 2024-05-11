import requests
from asyncio.log import logger

from config.config_sophia import ConfigSophia


class ServiceSophia(ConfigSophia):
    """
    """
    def conectar_com_o_sophia(self) -> dict:
        try:
            return {
                "token": requests.post(
                    self.autenticacao, json=self.gerar_acesso()
                ).text
            }
        except Exception as err_conexao:
            logger.error(f"Erro ao conectar com o serviço {err_conexao}")

    def listar_colaboradores(self) -> list:
        try:
            return requests.get(
                self.colaboradores, headers=self.conectar_com_o_sophia()
            ).json()
        except Exception as err_listar_colaboradores:
            logger.error(
                f"Erro ao listar colaboradores {err_listar_colaboradores}"
            )
            return []


if __name__ == "__main__":
    conexao = ServiceSophia().conectar_com_o_sophia()
    print(conexao)
