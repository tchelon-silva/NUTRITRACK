from datetime import datetime

from models import (
    RegistoAlimentar,
    ObjetivosNutricionais
)

from database import guardar_dados

REFEICOES_VALIDAS = [
    "pequeno-almoço",
    "almoço",
    "lanche",
    "jantar"
]

UNIDADES_VALIDAS = [
    "g",
    "ml",
    "unidade"
]

# Verifica se a data está no formato DD/MM/AAAA.
def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except (ValueError, TypeError):
        return False

# Verifica se a refeição é válida.
def validar_refeicao(refeicao):
    return (refeicao.lower() in REFEICOES_VALIDAS)

# Verifica se a unidade de medida é válida.
def validar_unidade(unidade):
    return(unidade.lower() in UNIDADES_VALIDAS)

# Obtém um novo ID para o próximo registo.
def obter_novo_id(dados):
    if not dados["registos"]:
        return 1
    maior_id = max(registo.id for registo in dados["registos"])
    return maior_id + 1

# Calcula o total nutricional consumido numa determinada data.
def calcular_consumo_do_dia(dados, data):
    consumo = {
        "calorias": 0,
        "proteinas": 0,
        "hidratos_carbono": 0,
        "gorduras": 0
    }

    for registo in dados["registos"]:
        if registo.data == data:
            nutrientes = (registo.calcular_nutrientes())
            consumo["calorias"] += (nutrientes["calorias"])
            consumo["proteinas"] += (nutrientes["proteinas"])
            consumo["hidratos_carbono"] += (nutrientes["hidratos_carbono"])
            consumo["gorduras"] += (nutrientes["gorduras"])

    return consumo

# Adiciona um novo registo alimentar.
def adicionar_registo(
    dados,
    data,
    refeicao,
    alimento,
    quantidade,
    quantidade_por_unidade,
    unidade_medida,
    calorias_por_unidade,
    proteinas_por_unidade,
    hidratos_carbono_por_unidade,
    gorduras_por_unidade,
    id_utilizador
):
    if not validar_data(data):
        return False, "Data inválida."
    if not validar_refeicao(refeicao):
        return False, "Refeição inválida."
    if not alimento.strip():
        return False, ("O nome do alimento não pode estar vazio.")
    if quantidade <= 0:
        return False, ("A quantidade deve ser superior a zero.")
    if quantidade_por_unidade <= 0:
        return False, ("A quantidade correspondente à unidade deve ser superior a zero.")
    if not validar_unidade(unidade_medida):
        return False, ("Unidade de medida inválida.")
    if calorias_por_unidade < 0:
        return False, ("As calorias não podem ser negativas.")
    if proteinas_por_unidade < 0:
        return False, ("As proteínas não podem ser negativas.")
    if hidratos_carbono_por_unidade < 0:
        return False, ("Os hidratos de carbono não podem ser negativos.")
    if gorduras_por_unidade < 0:
        return False, ("As gorduras não podem ser negativas.")

    registo = RegistoAlimentar(
        obter_novo_id(dados),
        data,
        refeicao.lower(),
        alimento.strip(),
        quantidade,
        quantidade_por_unidade,
        unidade_medida.lower(),
        calorias_por_unidade,
        proteinas_por_unidade,
        hidratos_carbono_por_unidade,
        gorduras_por_unidade
    )

    dados["registos"].append(registo)

    if guardar_dados(dados, id_utilizador):
        return True, ("Registo adicionado com sucesso.")
    return False, ("O registo foi criado, mas ocorreu um erro ao guardar os dados.")

# Devolve os registos ordenados por data.
def listar_registos(dados):
    return sorted(
        dados["registos"],
        key=lambda registo: datetime.strptime(registo.data, "%d/%m/%Y")
    )

# Consulta o consumo nutricional de uma determinada data.
def consultar_consumo_diario(dados, data):
    if not validar_data(data):
        return None

    existem_registos = any(
        registo.data == data
        for registo in dados["registos"]
    )

    if not existem_registos:
        return None

    return calcular_consumo_do_dia(dados, data)

# Define ou altera os objetivos nutricionais diários.
def definir_objetivos(
    dados,
    calorias,
    proteinas,
    hidratos_carbono,
    gorduras,
    id_utilizador
):
    if calorias <= 0:
        return False, ("O objetivo de calorias deve ser superior a zero.")
    if proteinas <= 0:
        return False, ("O objetivo de proteínas deve ser superior a zero.")
    if hidratos_carbono <= 0:
        return False, ("O objetivo de hidratos de carbono deve ser superior a zero.")
    if gorduras <= 0:
        return False, ("O objetivo de gorduras deve ser superior a zero.")

    dados["objetivos"] = ObjetivosNutricionais(
        calorias,
        proteinas,
        hidratos_carbono,
        gorduras
    )

    if guardar_dados(dados, id_utilizador):
        return True, ("Objetivos guardados com sucesso.")
    return False, ("Ocorreu um erro ao guardar os objetivos.")

# Compara o consumo de um determinado dia com os objetivos definidos.
def acompanhar_objetivos(
    dados,
    data
):
    if dados["objetivos"] is None:
        return None

    consumo = consultar_consumo_diario(dados, data)

    if consumo is None:
        return None

    objetivos = dados["objetivos"]

    return {
        "calorias": {
            "objetivo": objetivos.calorias,
            "consumido": consumo["calorias"],
            "diferenca": (objetivos.calorias - consumo["calorias"])
        },

        "proteinas": {
            "objetivo": objetivos.proteinas,
            "consumido": consumo["proteinas"],
            "diferenca": (objetivos.proteinas - consumo["proteinas"])
        },

        "hidratos_carbono": {
            "objetivo": objetivos.hidratos_carbono,
            "consumido": consumo["hidratos_carbono"],
            "diferenca": (objetivos.hidratos_carbono - consumo["hidratos_carbono"])
        },

        "gorduras": {
            "objetivo": objetivos.gorduras,
            "consumido": consumo["gorduras"],
            "diferenca": (objetivos.gorduras - consumo["gorduras"])
        }
    }

# Remove um registo através do seu ID.
def remover_registo(dados, id_registo, id_utilizador):
    for registo in dados["registos"]:
        if registo.id == id_registo:
            dados["registos"].remove(registo)

            if guardar_dados(dados, id_utilizador):
                return True, ("Registo removido com sucesso.")

            return False, ("O registo foi removido, mas ocorreu um erro ao guardar.")

    return False, ("Não foi encontrado nenhum registo com esse ID.")