from database import carregar_dados
from auth import registar_utilizador, fazer_login

from services import (
    adicionar_registo,
    listar_registos,
    consultar_consumo_diario,
    definir_objetivos,
    acompanhar_objetivos,
    remover_registo,
    validar_data
)

# Pede um texto não vazio.
def pedir_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Erro: o campo não pode ficar vazio.")

# Pede um número ao utilizador.
def pedir_numero(mensagem, permitir_zero=False):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if permitir_zero:
                if valor >= 0:
                    return valor
            else:
                if valor > 0:
                    return valor
            print("Erro: introduza um valor válido.")
        except ValueError:
            print("Erro: introduza um número válido.")

# Pede um número inteiro.
def pedir_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: introduza um número inteiro.")

# Pede uma data válida no formato DD/MM/AAAA.
def pedir_data():
    while True:
        data = input("Data (DD/MM/AAAA): ").strip()

        if validar_data(data):
            return data

        print("Data inválida. Introduza uma data no formato DD/MM/AAAA.")

# Permite escolher uma refeição.
def escolher_refeicao():
    refeicoes = {
        "1": "pequeno-almoço",
        "2": "almoço",
        "3": "lanche",
        "4": "jantar"
    }

    while True:
        print("\nEscolha a refeição:")
        print("1 - Pequeno-almoço")
        print("2 - Almoço")
        print("3 - Lanche")
        print("4 - Jantar")

        opcao = input("Opção: ").strip()

        if opcao in refeicoes:
            return refeicoes[opcao]

        print("Erro: opção inválida.")

# Permite escolher a unidade de medida.
def escolher_unidade():
    unidades = {
        "1": "g",
        "2": "ml",
        "3": "unidade"
    }

    while True:
        print("\nEscolha a unidade de medida:")
        print("1 - g")
        print("2 - ml")
        print("3 - unidade")

        opcao = input("Opção: ").strip()

        if opcao in unidades:
            return unidades[opcao]

        print("Erro: opção inválida.")

# Formata números para apresentação.
def formatar_numero(valor):
    if valor == int(valor):
        return str(int(valor))

    return f"{valor:.2f}"


# 1. REGISTAR ALIMENTO
def menu_adicionar_registo(dados, id_utilizador):

    print("\n" + "=" * 60)
    print("REGISTAR ALIMENTO")
    print("=" * 60)

    data = pedir_data()

    refeicao = escolher_refeicao()

    alimento = pedir_texto("Nome do alimento: ")

    quantidade = pedir_numero("Quantidade consumida: ")

    quantidade_por_unidade = pedir_numero(
        "Quantidade correspondente a cada unidade: "
    )

    unidade = escolher_unidade()

    print("\nValores nutricionais correspondentes a cada unidade:")

    calorias = pedir_numero(
        "Valor energético (kcal): ",
        permitir_zero=True
    )

    proteinas = pedir_numero(
        "Proteínas (g): ",
        permitir_zero=True
    )

    hidratos = pedir_numero(
        "Hidratos de carbono (g): ",
        permitir_zero=True
    )

    gorduras = pedir_numero(
        "Gorduras (g): ",
        permitir_zero=True
    )

    sucesso, mensagem = adicionar_registo(
        dados,
        data,
        refeicao,
        alimento,
        quantidade,
        quantidade_por_unidade,
        unidade,
        calorias,
        proteinas,
        hidratos,
        gorduras,
        id_utilizador
    )

    print(f"\n{mensagem}")

    if sucesso:
        quantidade_total = quantidade * quantidade_por_unidade

        calorias_total = quantidade * calorias

        proteinas_total = quantidade * proteinas

        hidratos_total = quantidade * hidratos

        gorduras_total = quantidade * gorduras

        print("\nResumo do consumo:")
        print("-" * 60)

        print(
            f"Quantidade total: "
            f"{formatar_numero(quantidade_total)} "
            f"{unidade}"
        )

        print(
            f"Calorias: "
            f"{formatar_numero(calorias_total)} kcal"
        )

        print(
            f"Proteínas: "
            f"{formatar_numero(proteinas_total)} g"
        )

        print(
            f"Hidratos de carbono: "
            f"{formatar_numero(hidratos_total)} g"
        )

        print(
            f"Gorduras: "
            f"{formatar_numero(gorduras_total)} g"
        )


# 2. LISTAR REGISTOS

def menu_listar_registos(dados):

    print("\n" + "=" * 70)
    print("REGISTOS ALIMENTARES")
    print("=" * 70)

    registos = listar_registos(dados)

    if not registos:
        print("Não existem registos alimentares.")
        return

    data_atual = None

    for registo in registos:

        if registo.data != data_atual:

            data_atual = registo.data

            print(f"\n--- {data_atual} ---")

        quantidade_total = (
            registo.quantidade *
            registo.quantidade_por_unidade
        )

        nutrientes = registo.calcular_nutrientes()

        print(f"\nID: {registo.id}")

        print(f"Refeição: {registo.refeicao.capitalize()}")

        print(f"Alimento: {registo.alimento}")

        print(
            f"Quantidade: "
            f"{formatar_numero(registo.quantidade)} x "
            f"{formatar_numero(registo.quantidade_por_unidade)} "
            f"{registo.unidade_medida} = "
            f"{formatar_numero(quantidade_total)} "
            f"{registo.unidade_medida}"
        )

        print(
            f"Calorias: "
            f"{formatar_numero(nutrientes['calorias'])} kcal"
        )

        print(
            f"Proteínas: "
            f"{formatar_numero(nutrientes['proteinas'])} g"
        )

        print(
            f"Hidratos: "
            f"{formatar_numero(nutrientes['hidratos_carbono'])} g"
        )

        print(
            f"Gorduras: "
            f"{formatar_numero(nutrientes['gorduras'])} g"
        )


# 3. CONSULTAR CONSUMO DIÁRIO
def menu_consultar_consumo(dados):

    print("\n" + "=" * 60)
    print("CONSULTAR CONSUMO DIÁRIO")
    print("=" * 60)

    data = pedir_data()

    consumo = consultar_consumo_diario(
        dados,
        data
    )

    if consumo is None:

        print(
            f"\nNão existem registos para {data}."
        )

        return

    print(
        f"\nConsumo do dia {data}:"
    )

    print("-" * 60)

    print(
        f"Calorias: "
        f"{formatar_numero(consumo['calorias'])} kcal"
    )

    print(
        f"Proteínas: "
        f"{formatar_numero(consumo['proteinas'])} g"
    )

    print(
        f"Hidratos de carbono: "
        f"{formatar_numero(consumo['hidratos_carbono'])} g"
    )

    print(
        f"Gorduras: "
        f"{formatar_numero(consumo['gorduras'])} g"
    )


# 4. DEFINIR OBJETIVOS
def menu_definir_objetivos(dados, id_utilizador):

    print("\n" + "=" * 60)
    print("DEFINIR OBJETIVOS DIÁRIOS")
    print("=" * 60)

    calorias = pedir_numero("Objetivo de calorias (kcal): ")

    proteinas = pedir_numero("Objetivo de proteínas (g): ")

    hidratos = pedir_numero(
        "Objetivo de hidratos de carbono (g): "
    )

    gorduras = pedir_numero("Objetivo de gorduras (g): ")

    sucesso, mensagem = definir_objetivos(
        dados,
        calorias,
        proteinas,
        hidratos,
        gorduras,
        id_utilizador
    )

    print(f"\n{mensagem}")


# 5. ACOMPANHAR OBJETIVOS
def menu_acompanhar_objetivos(dados):

    print("\n" + "=" * 60)
    print("ACOMPANHAR OBJETIVOS")
    print("=" * 60)

    if dados["objetivos"] is None:
        print("Ainda não foram definidos objetivos.")
        return

    data = pedir_data()

    resultado = acompanhar_objetivos(
        dados,
        data
    )

    if resultado is None:
        print(f"\nNão existem registos para {data}.")
        return

    print(
        f"\nComparação dos objetivos "
        f"com o consumo de {data}:"
    )

    apresentar_objetivo(
        "Calorias",
        resultado["calorias"],
        "kcal"
    )

    apresentar_objetivo(
        "Proteínas",
        resultado["proteinas"],
        "g"
    )

    apresentar_objetivo(
        "Hidratos de carbono",
        resultado["hidratos_carbono"],
        "g"
    )

    apresentar_objetivo(
        "Gorduras",
        resultado["gorduras"],
        "g"
    )


# Apresenta a comparação entre objetivo e consumo.
def apresentar_objetivo(
    nome,
    dados_objetivo,
    unidade
):

    objetivo = dados_objetivo["objetivo"]

    consumido = dados_objetivo["consumido"]

    diferenca = dados_objetivo["diferenca"]

    print(f"\n{nome}:")

    print(
        f"  Objetivo: "
        f"{formatar_numero(objetivo)} {unidade}"
    )

    print(
        f"  Consumido: "
        f"{formatar_numero(consumido)} {unidade}"
    )

    if diferenca > 0:

        print(
            f"  Ainda falta: "
            f"{formatar_numero(diferenca)} {unidade}"
        )

    elif diferenca == 0:

        print(
            "  Objetivo atingido!"
        )

    else:

        print(
            f"  Excedido: "
            f"{formatar_numero(abs(diferenca))} "
            f"{unidade}"
        )


# 6. REMOVER REGISTO
def menu_remover_registo(dados, id_utilizador):

    print("\n" + "=" * 60)
    print("REMOVER REGISTO")
    print("=" * 60)

    if not dados["registos"]:
        print("Não existem registos para remover.")
        return

    menu_listar_registos(dados)

    id_registo = pedir_inteiro(
        "\nID do registo a remover: "
    )

    sucesso, mensagem = remover_registo(
        dados,
        id_registo,
        id_utilizador
    )

    print(f"\n{mensagem}")


# MENU PRINCIPAL
def mostrar_menu():

    print("\n")
    print("=" * 60)
    print("                 NUTRITRACK")
    print("              Planeador Alimentar")
    print("=" * 60)

    print("1 - Registar alimento")
    print("2 - Listar registos alimentares")
    print("3 - Consultar consumo diário")
    print("4 - Definir objetivos")
    print("5 - Acompanhar objetivos")
    print("6 - Remover registo")
    print("0 - Logout")

    print("=" * 60)


def menu_registo_utilizador():

    print("\n================================")
    print("       CRIAR CONTA")
    print("================================")

    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    password = input("Password: ").strip()

    if not nome or not email or not password:
        print("Todos os campos são obrigatórios.")
        return

    sucesso, mensagem = registar_utilizador(
        nome,
        email,
        password
    )

    print(mensagem)


def menu_login():

    print("\n================================")
    print("       INICIAR SESSÃO")
    print("================================")

    email = input("Email: ").strip()
    password = input("Password: ").strip()

    if not email or not password:
        print("Email e password são obrigatórios.")
        return None

    sucesso, utilizador, mensagem = fazer_login(
        email,
        password
    )

    print(mensagem)

    if sucesso:
        return utilizador

    return None


# MENU DE AUTENTICAÇÃO
def mostrar_menu_autenticacao():

    print("\n")
    print("=" * 60)
    print("                 NUTRITRACK")
    print("              Planeador Alimentar")
    print("=" * 60)

    print("1 - Criar conta")
    print("2 - Iniciar sessão")
    print("0 - Sair")

    print("=" * 60)


def menu_autenticacao():

    while True:

        mostrar_menu_autenticacao()

        opcao = input(
            "Escolha uma opção: "
        ).strip()

        if opcao == "1":

            menu_registo_utilizador()

        elif opcao == "2":

            utilizador = menu_login()

            if utilizador is not None:
                return utilizador

        elif opcao == "0":

            print(
                "\nObrigado por utilizar o NUTRITRACK!"
            )

            return None

        else:

            print(
                "\nErro: opção inválida."
            )


# MENU DO UTILIZADOR AUTENTICADO
def menu_principal(dados, id_utilizador):

    while True:

        mostrar_menu()

        opcao = input(
            "Escolha uma opção: "
        ).strip()

        if opcao == "1":

            menu_adicionar_registo(
                dados,
                id_utilizador
            )

        elif opcao == "2":

            menu_listar_registos(dados)

        elif opcao == "3":

            menu_consultar_consumo(dados)

        elif opcao == "4":

            menu_definir_objetivos(
                dados,
                id_utilizador
            )

        elif opcao == "5":

            menu_acompanhar_objetivos(dados)

        elif opcao == "6":

            menu_remover_registo(
                dados,
                id_utilizador
            )

        elif opcao == "0":

            print(
                "\nSessão terminada com sucesso."
            )

            return

        else:

            print(
                "\nErro: opção inválida."
            )


def main():

    print("\nBem-vindo ao NUTRITRACK!")

    # Permite iniciar e terminar várias sessões sem fechar a aplicação.
    while True:

        # É necessário criar uma conta ou iniciar sessão.
        utilizador = menu_autenticacao()

        # Se o utilizador escolher "Sair", termina a aplicação.
        if utilizador is None:
            return

        # Depois do login, os dados são carregados do ficheiro
        # específico desse utilizador.
        id_utilizador = utilizador["id"]

        dados = carregar_dados(id_utilizador)

        print(
            f"\nOlá, {utilizador['nome']}!"
        )

        # Abre o menu principal do utilizador autenticado.
        # Quando for feito logout, esta função termina
        # e o programa volta ao menu de autenticação.
        menu_principal(
            dados,
            id_utilizador
        )


if __name__ == "__main__":
    main()