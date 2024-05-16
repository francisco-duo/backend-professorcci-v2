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
        """Retorna uma lista com os colaboradores cadastrados no sophia"""
        try:
            return requests.get(
                self.colaboradores, headers=self.conectar_com_o_sophia()
            ).json()
        except Exception as err_listar_colaboradores:
            logger.error(
                f"Erro ao listar colaboradores {err_listar_colaboradores}"
            )
            return []

    def listar_turmas(self) -> list:
        """Retorna uma lista com as turmas cadastradas no sophia"""
        try:
            return requests.get(
                self.turmas, headers=self.conectar_com_o_sophia()
            ).json()
        except Exception as err_listar_turmas:
            logger.error(f"Erro ao listar turmas\n{err_listar_turmas}")


if __name__ == "__main__":
    conexao = ServiceSophia().listar_turmas()
    print(conexao[0])
