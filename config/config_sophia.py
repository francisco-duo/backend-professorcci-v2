import os
from dotenv import load_dotenv

load_dotenv()


class ConfigSophia():
    """
    ConfigSophia

    v0.0.1

    Descrição:
        - Classe de configuração para os serviços do sistema de gestão
        acadêmica sophia.
        - Utiliza a biblioteca python-dotenv para objeter as variáveis de
        ambiente para dar valor aos atributos da classe.
        - O método gerar_acesso() retorna um dicionário contendo as credênciais
        necessárias para conectar o serviço

    Atributos:
        # usuario: str
        # senha: str
        + autenticacao: str
        + colaboradores: str
        + turmas: str

    Métodos:
        gerar_acesso(): dict
    """
    __usuario: str = os.getenv("SOPHIA_USUARIO")
    __senha: str = os.getenv("SOPHIA_SENHA")
    autenticacao: str = os.getenv("SOPHIA_AUTENTICACAO")
    colaboradores: str = os.getenv("SOPHIA_COLABORADORES")
    turmas: str = os.getenv("SOPHIA_TURMAS")

    def gerar_acesso(self) -> dict:
        return {"usuario": self.__usuario, "senha": self.__senha}
