import bcrypt
from mysql_database import criar_conexao


def registar_utilizador(nome, email, password):
    conexao = criar_conexao()

    if conexao is None:
        return False, "Não foi possível ligar à base de dados."

    try:
        cursor = conexao.cursor()

        # Verificar se o email já existe
        cursor.execute(
            "SELECT id FROM utilizadores WHERE email = %s",
            (email,)
        )

        if cursor.fetchone() is not None:
            return False, "Já existe um utilizador com esse email."

        # Criar hash da password
        password_hash = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        # Inserir utilizador
        cursor.execute(
            """
            INSERT INTO utilizadores (nome, email, password_hash)
            VALUES (%s, %s, %s)
            """,
            (nome, email, password_hash.decode("utf-8"))
        )

        conexao.commit()

        return True, "Utilizador registado com sucesso!"

    except Exception as erro:
        conexao.rollback()
        return False, f"Erro ao registar utilizador: {erro}"

    finally:
        cursor.close()
        conexao.close()


def fazer_login(email, password):
    conexao = criar_conexao()

    if conexao is None:
        return False, None, "Não foi possível ligar à base de dados."

    try:
        cursor = conexao.cursor(dictionary=True)

        # Procurar o utilizador pelo email
        cursor.execute(
            "SELECT * FROM utilizadores WHERE email = %s",
            (email,)
        )

        utilizador = cursor.fetchone()

        if utilizador is None:
            return False, None, "Email ou password incorretos."

        # Comparar a password introduzida com o hash guardado
        password_correta = bcrypt.checkpw(
            password.encode("utf-8"),
            utilizador["password_hash"].encode("utf-8")
        )

        if not password_correta:
            return False, None, "Email ou password incorretos."

        return True, utilizador, "Login efetuado com sucesso!"

    except Exception as erro:
        return False, None, f"Erro ao fazer login: {erro}"

    finally:
        cursor.close()
        conexao.close()