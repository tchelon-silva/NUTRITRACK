import mysql.connector


def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Tchelon1.",
            database="nutritrack"
        )

        print("Ligação ao MySQL efetuada com sucesso!")
        return conexao

    except mysql.connector.Error as erro:
        print(f"Erro ao ligar ao MySQL: {erro}")
        return None