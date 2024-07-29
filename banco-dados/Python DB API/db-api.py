import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")

cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


# Criando uma tabela
def criar_tabela(cursor):
    cursor.execute(
        "CREATE TABLE clientes \
        (id INTEGER PRIMARY KEY AUTOINCREMENT, \
        nome VARCHAR(100), \
        email VARCHAR(150) \
            )"
    )


# Inserir registros na tabela
def inserir_registro(conexao, cursor, data):
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", (data))
    conexao.commit()


data = ("Gesiel", "gesielrodrigues.dev@gmail.com")
# inserir_registro(conexao, cursor, data)


# Alterar registros na tabela (não esquecer da cláusula WHERE)
def alterar_registro(conexao, cursor, data):
    cursor.execute("UPDATE clientes SET email = ? WHERE id = ?;", (data))
    conexao.commit()


data = ("gesielrodrigues@hotmail.com", 1)
# alterar_registro(conexao, cursor, data)


# Remover registros na tabela (não esquecer da cláusula WHERE)
def excluir_registro(conexao, cursor, id):
    cursor.execute("DELETE FROM clientes WHERE id = ?;", (id,))
    conexao.commit()


# excluir_registro(conexao, cursor, 1)


# Incluir vários registros de uma vez
def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) values (?, ?)", dados)
    conexao.commit()


clientes = [
    ("Gesiel", "gesielrodrigues@hotmail.com"),
    ("Jose", "jose@gmail.com"),
    ("João", "joao@gmail.com"),
]
# inserir_muitos(conexao, cursor, clientes)


# Consultando os registros
def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes")


print(dict(recuperar_cliente(cursor, 2)))

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))
