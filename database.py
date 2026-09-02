import json

from models import RegistoAlimentar, ObjetivosNutricionais


def nome_ficheiro_utilizador(id_utilizador):
    # Cria o nome do ficheiro JSON específico de cada utilizador.
    return f"dados_utilizador_{id_utilizador}.json"


def criar_dados_vazios():
    # Cria a estrutura inicial da aplicação.
    return {
        "registos": [],
        "objetivos": None
    }


def carregar_dados(id_utilizador):
    """
    Carrega os dados do ficheiro JSON do utilizador.
    Se o ficheiro não existir, cria uma estrutura vazia.
    Se o ficheiro tiver JSON inválido, informa o utilizador e inicia sem dados.
    """

    nome_ficheiro = nome_ficheiro_utilizador(id_utilizador)

    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as ficheiro:
            dados_json = json.load(ficheiro)

    except FileNotFoundError:
        print("Ficheiro de dados não encontrado.")
        print("Será criado automaticamente quando forem guardados dados.")
        return criar_dados_vazios()

    except json.JSONDecodeError:
        print("Erro: o ficheiro JSON contém dados inválidos.")
        return criar_dados_vazios()

    except OSError as erro:
        print(f"Erro ao ler o ficheiro: {erro}")
        return criar_dados_vazios()

    try:
        # A variável "registos" vai guardar todos os registos do ficheiro json que serão transformados (método RegistoAlimentar.de_dicionario) em objetos (que contem só valores e não chave-valor).
        registos = []

        for registo in dados_json.get("registos", []):
            registos.append(RegistoAlimentar.de_dicionario(registo))

        objetivos = None

        if dados_json.get("objetivos"):
            objetivos = ObjetivosNutricionais.de_dicionario(
                dados_json["objetivos"]
            )

        return {
            "registos": registos,
            "objetivos": objetivos
        }

    except (KeyError, TypeError, ValueError) as erro:
        print(f"Erro na estrutura dos dados: {erro}")
        print("A aplicação será iniciada sem dados.")
        return criar_dados_vazios()


def guardar_dados(dados, id_utilizador):
    # Transforma os objetos em dicionário e guarda os dados da aplicação no ficheiro Json.

    nome_ficheiro = nome_ficheiro_utilizador(id_utilizador)

    dados_json = {
        "registos": [
            registo.para_dicionario()
            for registo in dados["registos"]
        ],
        "objetivos": (
            dados["objetivos"].para_dicionario()
            if dados["objetivos"] is not None
            else None
        )
    }

    try:
        with open(nome_ficheiro, "w", encoding="utf-8") as ficheiro:
            json.dump(
                dados_json,
                ficheiro,
                ensure_ascii=False,
                indent=4
            )

        return True

    except OSError as erro:
        print(f"Erro ao guardar os dados: {erro}")
        return False