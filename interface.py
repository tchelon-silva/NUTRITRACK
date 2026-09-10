import tkinter as tk
from tkinter import ttk, messagebox

from auth import (
    registar_utilizador,
    fazer_login
)

from database import carregar_dados

from services import (
    adicionar_registo,
    listar_registos,
    consultar_consumo_diario,
    definir_objetivos,
    acompanhar_objetivos,
    remover_registo
)


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def formatar_numero(valor):
    # Formata os números para apresentação.
    if valor == int(valor):
        return str(int(valor))

    return f"{valor:.2f}"


# ============================================================
# JANELA DE REGISTO DE UTILIZADOR
# ============================================================

def janela_registo(janela_principal):

    janela = tk.Toplevel(janela_principal)

    janela.title("NUTRITRACK - Criar conta")
    janela.geometry("450x450")

    titulo = tk.Label(
        janela,
        text="Criar conta",
        font=("Arial", 22, "bold")
    )
    titulo.pack(pady=25)

    # Nome
    tk.Label(
        janela,
        text="Nome:"
    ).pack()

    entrada_nome = tk.Entry(
        janela,
        width=35
    )
    entrada_nome.pack(pady=5)

    # Email
    tk.Label(
        janela,
        text="Email:"
    ).pack()

    entrada_email = tk.Entry(
        janela,
        width=35
    )
    entrada_email.pack(pady=5)

    # Password
    tk.Label(
        janela,
        text="Password:"
    ).pack()

    entrada_password = tk.Entry(
        janela,
        width=35,
        show="*"
    )
    entrada_password.pack(pady=5)

    mensagem = tk.Label(
        janela,
        text="",
        wraplength=350
    )
    mensagem.pack(pady=15)

    def registar():

        nome = entrada_nome.get().strip()
        email = entrada_email.get().strip()
        password = entrada_password.get().strip()

        if not nome or not email or not password:

            mensagem.config(
                text="Todos os campos são obrigatórios."
            )

            return

        sucesso, resultado = registar_utilizador(
            nome,
            email,
            password
        )

        mensagem.config(
            text=resultado
        )

        if sucesso:

            entrada_nome.delete(0, tk.END)
            entrada_email.delete(0, tk.END)
            entrada_password.delete(0, tk.END)

    botao_registar = tk.Button(
        janela,
        text="Registar",
        width=25,
        command=registar
    )
    botao_registar.pack(pady=5)

    botao_voltar = tk.Button(
        janela,
        text="Voltar",
        width=25,
        command=janela.destroy
    )
    botao_voltar.pack(pady=5)


# ============================================================
# JANELA DE LOGIN
# ============================================================

def janela_login(janela_principal):

    janela = tk.Toplevel(janela_principal)

    janela.title("NUTRITRACK - Iniciar sessão")
    janela.geometry("450x400")

    titulo = tk.Label(
        janela,
        text="Iniciar sessão",
        font=("Arial", 22, "bold")
    )
    titulo.pack(pady=30)

    # Email
    tk.Label(
        janela,
        text="Email:"
    ).pack()

    entrada_email = tk.Entry(
        janela,
        width=35
    )
    entrada_email.pack(pady=5)

    # Password
    tk.Label(
        janela,
        text="Password:"
    ).pack()

    entrada_password = tk.Entry(
        janela,
        width=35,
        show="*"
    )
    entrada_password.pack(pady=5)

    mensagem = tk.Label(
        janela,
        text="",
        wraplength=350
    )
    mensagem.pack(pady=15)

    def login():

        email = entrada_email.get().strip()
        password = entrada_password.get().strip()

        if not email or not password:

            mensagem.config(
                text="Email e password são obrigatórios."
            )

            return

        sucesso, utilizador, resultado = fazer_login(
            email,
            password
        )

        mensagem.config(
            text=resultado
        )

        if sucesso:

            janela.destroy()

            janela_principal_utilizador(
                janela_principal,
                utilizador
            )

    botao_login = tk.Button(
        janela,
        text="Iniciar sessão",
        width=25,
        command=login
    )
    botao_login.pack(pady=5)

    botao_voltar = tk.Button(
        janela,
        text="Voltar",
        width=25,
        command=janela.destroy
    )
    botao_voltar.pack(pady=5)


# ============================================================
# JANELA REGISTAR ALIMENTO
# ============================================================

def janela_adicionar_alimento(
    janela_principal,
    dados,
    id_utilizador
):

    janela = tk.Toplevel(janela_principal)

    janela.title(
        "NUTRITRACK - Registar alimento"
    )

    janela.geometry("550x700")

    titulo = tk.Label(
        janela,
        text="Registar alimento",
        font=("Arial", 22, "bold")
    )
    titulo.pack(pady=20)

    frame = tk.Frame(janela)
    frame.pack()

    # Data
    tk.Label(
        frame,
        text="Data (DD/MM/AAAA):"
    ).grid(
        row=0,
        column=0,
        sticky="w",
        pady=7
    )

    entrada_data = tk.Entry(
        frame,
        width=30
    )
    entrada_data.grid(
        row=0,
        column=1,
        pady=7
    )

    # Refeição
    tk.Label(
        frame,
        text="Refeição:"
    ).grid(
        row=1,
        column=0,
        sticky="w",
        pady=7
    )

    refeicao = ttk.Combobox(
        frame,
        values=[
            "pequeno-almoço",
            "almoço",
            "lanche",
            "jantar"
        ],
        state="readonly",
        width=27
    )
    refeicao.grid(
        row=1,
        column=1,
        pady=7
    )
    refeicao.current(0)

    # Alimento
    tk.Label(
        frame,
        text="Nome do alimento:"
    ).grid(
        row=2,
        column=0,
        sticky="w",
        pady=7
    )

    entrada_alimento = tk.Entry(
        frame,
        width=30
    )
    entrada_alimento.grid(
        row=2,
        column=1,
        pady=7
    )

    # Quantidade
    tk.Label(
        frame,
        text="Quantidade consumida:"
    ).grid(
        row=3,
        column=0,
        sticky="w",
        pady=7
    )

    entrada_quantidade = tk.Entry(
        frame,
        width=30
    )
    entrada_quantidade.grid(
        row=3,
        column=1,
        pady=7
    )

    # Quantidade por unidade
    tk.Label(
        frame,
        text="Quantidade por unidade:"
    ).grid(
        row=4,
        column=0,
        sticky="w",
        pady=7
    )

    entrada_quantidade_unidade = tk.Entry(
        frame,
        width=30
    )
    entrada_quantidade_unidade.grid(
        row=4,
        column=1,
        pady=7
    )

    # Unidade
    tk.Label(
        frame,
        text="Unidade de medida:"
    ).grid(
        row=5,
        column=0,
        sticky="w",
        pady=7
    )

    unidade = ttk.Combobox(
        frame,
        values=[
            "g",
            "ml",
            "unidade"
        ],
        state="readonly",
        width=27
    )
    unidade.grid(
        row=5,
        column=1,
        pady=7
    )
    unidade.current(0)

    # Valores nutricionais
    separador = tk.Label(
        janela,
        text="Valores nutricionais por unidade",
        font=("Arial", 12, "bold")
    )
    separador.pack(pady=15)

    frame_nutrientes = tk.Frame(janela)
    frame_nutrientes.pack()

    # Calorias
    tk.Label(
        frame_nutrientes,
        text="Calorias (kcal):"
    ).grid(
        row=0,
        column=0,
        sticky="w",
        pady=5
    )

    entrada_calorias = tk.Entry(
        frame_nutrientes,
        width=25
    )
    entrada_calorias.grid(
        row=0,
        column=1,
        pady=5
    )

    # Proteínas
    tk.Label(
        frame_nutrientes,
        text="Proteínas (g):"
    ).grid(
        row=1,
        column=0,
        sticky="w",
        pady=5
    )

    entrada_proteinas = tk.Entry(
        frame_nutrientes,
        width=25
    )
    entrada_proteinas.grid(
        row=1,
        column=1,
        pady=5
    )

    # Hidratos
    tk.Label(
        frame_nutrientes,
        text="Hidratos de carbono (g):"
    ).grid(
        row=2,
        column=0,
        sticky="w",
        pady=5
    )

    entrada_hidratos = tk.Entry(
        frame_nutrientes,
        width=25
    )
    entrada_hidratos.grid(
        row=2,
        column=1,
        pady=5
    )

    # Gorduras
    tk.Label(
        frame_nutrientes,
        text="Gorduras (g):"
    ).grid(
        row=3,
        column=0,
        sticky="w",
        pady=5
    )

    entrada_gorduras = tk.Entry(
        frame_nutrientes,
        width=25
    )
    entrada_gorduras.grid(
        row=3,
        column=1,
        pady=5
    )

    def registar():

        try:

            data = entrada_data.get().strip()

            nome_refeicao = refeicao.get()

            alimento = entrada_alimento.get().strip()

            quantidade = float(
                entrada_quantidade.get().replace(",", ".")
            )

            quantidade_por_unidade = float(
                entrada_quantidade_unidade.get().replace(",", ".")
            )

            nome_unidade = unidade.get()

            calorias = float(
                entrada_calorias.get().replace(",", ".")
            )

            proteinas = float(
                entrada_proteinas.get().replace(",", ".")
            )

            hidratos = float(
                entrada_hidratos.get().replace(",", ".")
            )

            gorduras = float(
                entrada_gorduras.get().replace(",", ".")
            )

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Introduza valores numéricos válidos.",
                parent=janela
            )

            return

        sucesso, mensagem = adicionar_registo(
            dados,
            data,
            nome_refeicao,
            alimento,
            quantidade,
            quantidade_por_unidade,
            nome_unidade,
            calorias,
            proteinas,
            hidratos,
            gorduras,
            id_utilizador
        )

        if not sucesso:

            messagebox.showerror(
                "Erro",
                mensagem,
                parent=janela
            )

            return

        quantidade_total = (
            quantidade *
            quantidade_por_unidade
        )

        messagebox.showinfo(
            "Sucesso",
            (
                "Alimento registado com sucesso!\n\n"
                f"Quantidade total: "
                f"{formatar_numero(quantidade_total)} "
                f"{nome_unidade}\n"
                f"Calorias: "
                f"{formatar_numero(quantidade * calorias)} kcal\n"
                f"Proteínas: "
                f"{formatar_numero(quantidade * proteinas)} g\n"
                f"Hidratos: "
                f"{formatar_numero(quantidade * hidratos)} g\n"
                f"Gorduras: "
                f"{formatar_numero(quantidade * gorduras)} g"
            ),
            parent=janela
        )

        # Limpar campos
        entrada_data.delete(0, tk.END)
        entrada_alimento.delete(0, tk.END)
        entrada_quantidade.delete(0, tk.END)
        entrada_quantidade_unidade.delete(0, tk.END)
        entrada_calorias.delete(0, tk.END)
        entrada_proteinas.delete(0, tk.END)
        entrada_hidratos.delete(0, tk.END)
        entrada_gorduras.delete(0, tk.END)

    botao_registar = tk.Button(
        janela,
        text="Registar alimento",
        width=30,
        command=registar
    )
    botao_registar.pack(pady=20)

    botao_voltar = tk.Button(
        janela,
        text="Voltar",
        width=30,
        command=janela.destroy
    )
    botao_voltar.pack()


# ============================================================
# JANELA LISTAR REGISTOS
# ============================================================

def janela_listar_registos(
    janela_principal,
    dados
):

    janela = tk.Toplevel(janela_principal)

    janela.title(
        "NUTRITRACK - Registos alimentares"
    )

    janela.geometry("700x600")

    titulo = tk.Label(
        janela,
        text="Registos alimentares",
        font=("Arial", 22, "bold")
    )
    titulo.pack(pady=20)

    # Área de texto
    texto = tk.Text(
        janela,
        width=80,
        height=28
    )
    texto.pack(
        padx=20,
        pady=10
    )

    registos = listar_registos(dados)

    if not registos:

        texto.insert(
            tk.END,
            "Não existem registos alimentares."
        )

    else:

        data_atual = None

        for registo in registos:

            if registo.data != data_atual:

                data_atual = registo.data

                texto.insert(
                    tk.END,
                    f"\n{'=' * 60}\n"
                    f"DATA: {data_atual}\n"
                    f"{'=' * 60}\n"
                )

            quantidade_total = (
                registo.quantidade *
                registo.quantidade_por_unidade
            )

            nutrientes = registo.calcular_nutrientes()

            texto.insert(
                tk.END,
                f"\nID: {registo.id}\n"
            )

            texto.insert(
                tk.END,
                f"Refeição: "
                f"{registo.refeicao.capitalize()}\n"
            )

            texto.insert(
                tk.END,
                f"Alimento: "
                f"{registo.alimento}\n"
            )

            texto.insert(
                tk.END,
                f"Quantidade: "
                f"{formatar_numero(registo.quantidade)} x "
                f"{formatar_numero(registo.quantidade_por_unidade)} "
                f"{registo.unidade_medida} = "
                f"{formatar_numero(quantidade_total)} "
                f"{registo.unidade_medida}\n"
            )

            texto.insert(
                tk.END,
                f"Calorias: "
                f"{formatar_numero(nutrientes['calorias'])} kcal\n"
            )

            texto.insert(
                tk.END,
                f"Proteínas: "
                f"{formatar_numero(nutrientes['proteinas'])} g\n"
            )

            texto.insert(
                tk.END,
                f"Hidratos: "
                f"{formatar_numero(nutrientes['hidratos_carbono'])} g\n"
            )

            texto.insert(
                tk.END,
                f"Gorduras: "
                f"{formatar_numero(nutrientes['gorduras'])} g\n"
            )

    # Impedir edição
    texto.config(
        state=tk.DISABLED
    )

    botao_fechar = tk.Button(
        janela,
        text="Voltar",
        width=25,
        command=janela.destroy
    )

    botao_fechar.pack(
        pady=10
    )


# ============================================================
# JANELA CONSULTAR CONSUMO DIÁRIO
# ============================================================

def janela_consumo_diario(
    janela_principal,
    dados
):

    janela = tk.Toplevel(janela_principal)

    janela.title(
        "NUTRITRACK - Consumo diário"
    )

    janela.geometry("500x400")

    titulo = tk.Label(
        janela,
        text="Consultar consumo diário",
        font=("Arial", 20, "bold")
    )
    titulo.pack(pady=30)

    tk.Label(
        janela,
        text="Data (DD/MM/AAAA):"
    ).pack()

    entrada_data = tk.Entry(
        janela,
        width=30
    )
    entrada_data.pack(pady=10)

    resultado = tk.Label(
        janela,
        text="",
        font=("Arial", 12),
        justify="left"
    )
    resultado.pack(pady=20)

    def consultar():

        data = entrada_data.get().strip()

        consumo = consultar_consumo_diario(
            dados,
            data
        )

        if consumo is None:

            resultado.config(
                text=f"Não existem registos para {data}."
            )

            return

        texto = (
            f"Consumo do dia {data}\n\n"
            f"Calorias: "
            f"{formatar_numero(consumo['calorias'])} kcal\n"
            f"Proteínas: "
            f"{formatar_numero(consumo['proteinas'])} g\n"
            f"Hidratos de carbono: "
            f"{formatar_numero(consumo['hidratos_carbono'])} g\n"
            f"Gorduras: "
            f"{formatar_numero(consumo['gorduras'])} g"
        )

        resultado.config(
            text=texto
        )

    botao_consultar = tk.Button(
        janela,
        text="Consultar",
        width=25,
        command=consultar
    )
    botao_consultar.pack(pady=5)

    botao_voltar = tk.Button(
        janela,
        text="Voltar",
        width=25,
        command=janela.destroy
    )
    botao_voltar.pack(pady=5)


# ============================================================
# JANELA OBJETIVOS NUTRICIONAIS
# ============================================================

def janela_objetivos(
    janela_principal,
    dados,
    id_utilizador
):

    janela = tk.Toplevel(janela_principal)

    janela.title(
        "NUTRITRACK - Objetivos nutricionais"
    )

    janela.geometry("650x650")

    titulo = tk.Label(
        janela,
        text="Objetivos nutricionais",
        font=("Arial", 22, "bold")
    )
    titulo.pack(pady=20)

    # --------------------------------------------------------
    # DEFINIR OBJETIVOS
    # --------------------------------------------------------

    frame = tk.Frame(janela)
    frame.pack()

    tk.Label(
        frame,
        text="Calorias (kcal):"
    ).grid(
        row=0,
        column=0,
        sticky="w",
        pady=6
    )

    entrada_calorias = tk.Entry(
        frame,
        width=25
    )
    entrada_calorias.grid(
        row=0,
        column=1,
        pady=6
    )

    tk.Label(
        frame,
        text="Proteínas (g):"
    ).grid(
        row=1,
        column=0,
        sticky="w",
        pady=6
    )

    entrada_proteinas = tk.Entry(
        frame,
        width=25
    )
    entrada_proteinas.grid(
        row=1,
        column=1,
        pady=6
    )

    tk.Label(
        frame,
        text="Hidratos de carbono (g):"
    ).grid(
        row=2,
        column=0,
        sticky="w",
        pady=6
    )

    entrada_hidratos = tk.Entry(
        frame,
        width=25
    )
    entrada_hidratos.grid(
        row=2,
        column=1,
        pady=6
    )

    tk.Label(
        frame,
        text="Gorduras (g):"
    ).grid(
        row=3,
        column=0,
        sticky="w",
        pady=6
    )

    entrada_gorduras = tk.Entry(
        frame,
        width=25
    )
    entrada_gorduras.grid(
        row=3,
        column=1,
        pady=6
    )

    def guardar_objetivos():

        try:

            calorias = float(
                entrada_calorias.get().replace(",", ".")
            )

            proteinas = float(
                entrada_proteinas.get().replace(",", ".")
            )

            hidratos = float(
                entrada_hidratos.get().replace(",", ".")
            )

            gorduras = float(
                entrada_gorduras.get().replace(",", ".")
            )

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Introduza valores numéricos válidos.",
                parent=janela
            )

            return

        sucesso, mensagem = definir_objetivos(
            dados,
            calorias,
            proteinas,
            hidratos,
            gorduras,
            id_utilizador
        )

        if sucesso:

            messagebox.showinfo(
                "Sucesso",
                mensagem,
                parent=janela
            )

        else:

            messagebox.showerror(
                "Erro",
                mensagem,
                parent=janela
            )

    botao_guardar = tk.Button(
        janela,
        text="Guardar objetivos",
        width=30,
        command=guardar_objetivos
    )
    botao_guardar.pack(pady=15)

    # --------------------------------------------------------
    # ACOMPANHAR OBJETIVOS
    # --------------------------------------------------------

    separador = tk.Label(
        janela,
        text="Acompanhar objetivos",
        font=("Arial", 14, "bold")
    )
    separador.pack(pady=15)

    tk.Label(
        janela,
        text="Data (DD/MM/AAAA):"
    ).pack()

    entrada_data = tk.Entry(
        janela,
        width=30
    )
    entrada_data.pack(pady=5)

    resultado = tk.Label(
        janela,
        text="",
        justify="left",
        font=("Arial", 11)
    )
    resultado.pack(pady=15)

    def acompanhar():

        if dados["objetivos"] is None:

            resultado.config(
                text="Ainda não foram definidos objetivos."
            )

            return

        data = entrada_data.get().strip()

        comparacao = acompanhar_objetivos(
            dados,
            data
        )

        if comparacao is None:

            resultado.config(
                text=f"Não existem registos para {data}."
            )

            return

        def linha(nome, dados_objetivo, unidade):

            diferenca = dados_objetivo["diferenca"]

            if diferenca > 0:

                estado = (
                    f"Falta: "
                    f"{formatar_numero(diferenca)} "
                    f"{unidade}"
                )

            elif diferenca == 0:

                estado = "Objetivo atingido!"

            else:

                estado = (
                    f"Excedido: "
                    f"{formatar_numero(abs(diferenca))} "
                    f"{unidade}"
                )

            return (
                f"{nome}\n"
                f"  Objetivo: "
                f"{formatar_numero(dados_objetivo['objetivo'])} "
                f"{unidade}\n"
                f"  Consumido: "
                f"{formatar_numero(dados_objetivo['consumido'])} "
                f"{unidade}\n"
                f"  {estado}\n"
            )

        texto = (
            f"Comparação de {data}\n\n"
            + linha(
                "Calorias",
                comparacao["calorias"],
                "kcal"
            )
            + "\n"
            + linha(
                "Proteínas",
                comparacao["proteinas"],
                "g"
            )
            + "\n"
            + linha(
                "Hidratos de carbono",
                comparacao["hidratos_carbono"],
                "g"
            )
            + "\n"
            + linha(
                "Gorduras",
                comparacao["gorduras"],
                "g"
            )
        )

        resultado.config(
            text=texto
        )

    botao_acompanhar = tk.Button(
        janela,
        text="Acompanhar objetivos",
        width=30,
        command=acompanhar
    )
    botao_acompanhar.pack(pady=5)

    botao_voltar = tk.Button(
        janela,
        text="Voltar",
        width=30,
        command=janela.destroy
    )
    botao_voltar.pack(pady=15)


# ============================================================
# JANELA REMOVER REGISTO
# ============================================================

def janela_remover_registo(
    janela_principal,
    dados,
    id_utilizador
):

    janela = tk.Toplevel(janela_principal)

    janela.title(
        "NUTRITRACK - Remover registo"
    )

    janela.geometry("650x550")

    titulo = tk.Label(
        janela,
        text="Remover registo",
        font=("Arial", 22, "bold")
    )
    titulo.pack(pady=20)

    texto = tk.Text(
        janela,
        width=70,
        height=20
    )
    texto.pack(
        padx=15,
        pady=10
    )

    registos = listar_registos(dados)

    if not registos:

        texto.insert(
            tk.END,
            "Não existem registos para remover."
        )

    else:

        for registo in registos:

            nutrientes = registo.calcular_nutrientes()

            texto.insert(
                tk.END,
                f"ID: {registo.id}\n"
                f"Data: {registo.data}\n"
                f"Refeição: {registo.refeicao}\n"
                f"Alimento: {registo.alimento}\n"
                f"Calorias: "
                f"{formatar_numero(nutrientes['calorias'])} kcal\n"
                f"{'-' * 50}\n"
            )

    texto.config(
        state=tk.DISABLED
    )

    tk.Label(
        janela,
        text="ID do registo a remover:"
    ).pack(pady=5)

    entrada_id = tk.Entry(
        janela,
        width=20
    )
    entrada_id.pack(pady=5)

    def remover():

        try:

            id_registo = int(
                entrada_id.get()
            )

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Introduza um ID válido.",
                parent=janela
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmar",
            "Tem a certeza que pretende remover este registo?",
            parent=janela
        )

        if not confirmar:
            return

        sucesso, mensagem = remover_registo(
            dados,
            id_registo,
            id_utilizador
        )

        if sucesso:

            messagebox.showinfo(
                "Sucesso",
                mensagem,
                parent=janela
            )

            janela.destroy()

        else:

            messagebox.showerror(
                "Erro",
                mensagem,
                parent=janela
            )

    botao_remover = tk.Button(
        janela,
        text="Remover registo",
        width=25,
        command=remover
    )
    botao_remover.pack(pady=10)

    botao_voltar = tk.Button(
        janela,
        text="Voltar",
        width=25,
        command=janela.destroy
    )
    botao_voltar.pack()


# ============================================================
# JANELA PRINCIPAL DO UTILIZADOR
# ============================================================

def janela_principal_utilizador(
    janela_principal,
    utilizador
):

    # Esconder janela inicial
    janela_principal.withdraw()

    # ID do utilizador
    id_utilizador = utilizador["id"]

    # Carregar dados específicos do utilizador
    dados = carregar_dados(
        id_utilizador
    )

    # Criar janela
    janela = tk.Toplevel(
        janela_principal
    )

    janela.title(
        "NUTRITRACK - Menu Principal"
    )

    janela.geometry(
        "600x650"
    )

    nome = utilizador["nome"]

    # Título
    titulo = tk.Label(
        janela,
        text="NUTRITRACK",
        font=("Arial", 26, "bold")
    )
    titulo.pack(
        pady=(35, 5)
    )

    # Boas-vindas
    boas_vindas = tk.Label(
        janela,
        text=f"Olá, {nome}!",
        font=("Arial", 16)
    )
    boas_vindas.pack(
        pady=(0, 25)
    )

    # --------------------------------------------------------
    # REGISTAR ALIMENTO
    # --------------------------------------------------------

    botao_registar = tk.Button(
        janela,
        text="Registar alimento",
        width=30,
        command=lambda: janela_adicionar_alimento(
            janela,
            dados,
            id_utilizador
        )
    )
    botao_registar.pack(
        pady=6
    )

    # --------------------------------------------------------
    # LISTAR REGISTOS
    # --------------------------------------------------------

    botao_listar = tk.Button(
        janela,
        text="Listar registos alimentares",
        width=30,
        command=lambda: janela_listar_registos(
            janela,
            dados
        )
    )
    botao_listar.pack(
        pady=6
    )

    # --------------------------------------------------------
    # CONSULTAR CONSUMO
    # --------------------------------------------------------

    botao_consumo = tk.Button(
        janela,
        text="Consultar consumo diário",
        width=30,
        command=lambda: janela_consumo_diario(
            janela,
            dados
        )
    )
    botao_consumo.pack(
        pady=6
    )

    # --------------------------------------------------------
    # OBJETIVOS
    # --------------------------------------------------------

    botao_objetivos = tk.Button(
        janela,
        text="Objetivos nutricionais",
        width=30,
        command=lambda: janela_objetivos(
            janela,
            dados,
            id_utilizador
        )
    )
    botao_objetivos.pack(
        pady=6
    )

    # --------------------------------------------------------
    # REMOVER REGISTO
    # --------------------------------------------------------

    botao_remover = tk.Button(
        janela,
        text="Remover registo",
        width=30,
        command=lambda: janela_remover_registo(
            janela,
            dados,
            id_utilizador
        )
    )
    botao_remover.pack(
        pady=6
    )

    # --------------------------------------------------------
    # LOGOUT
    # --------------------------------------------------------

    def logout():

        janela.destroy()

        janela_principal.deiconify()

    botao_logout = tk.Button(
        janela,
        text="Logout",
        width=30,
        command=logout
    )
    botao_logout.pack(
        pady=(20, 6)
    )

    # --------------------------------------------------------
    # FECHAR APLICAÇÃO
    # --------------------------------------------------------

    def fechar():

        janela.destroy()
        janela_principal.destroy()

    janela.protocol(
        "WM_DELETE_WINDOW",
        fechar
    )


# ============================================================
# MENU INICIAL
# ============================================================

def criar_janela():

    janela = tk.Tk()

    janela.title(
        "NUTRITRACK - Planeador Alimentar"
    )

    janela.geometry(
        "500x450"
    )

    # Título
    titulo = tk.Label(
        janela,
        text="NUTRITRACK",
        font=("Arial", 26, "bold")
    )
    titulo.pack(
        pady=(60, 5)
    )

    # Subtítulo
    subtitulo = tk.Label(
        janela,
        text="Planeador Alimentar",
        font=("Arial", 15)
    )
    subtitulo.pack(
        pady=(0, 45)
    )

    # Criar conta
    botao_registo = tk.Button(
        janela,
        text="Criar conta",
        width=30,
        command=lambda: janela_registo(janela)
    )
    botao_registo.pack(
        pady=10
    )

    # Login
    botao_login = tk.Button(
        janela,
        text="Iniciar sessão",
        width=30,
        command=lambda: janela_login(janela)
    )
    botao_login.pack(
        pady=10
    )

    # Sair
    botao_sair = tk.Button(
        janela,
        text="Sair",
        width=30,
        command=janela.destroy
    )
    botao_sair.pack(
        pady=10
    )

    janela.mainloop()


# ============================================================
# INÍCIO DA APLICAÇÃO
# ============================================================

if __name__ == "__main__":

    criar_janela()