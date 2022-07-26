import sqlite3 as lite

# Banco de dados
conect = lite.connect("lista.db")


def inserir(i):
    with conect:
        cur = conect.cursor()
        query = "INSERT INTO Tarefas (nome) VALUES(?)"
        cur.execute(query, i)


def selecionar():
    lista_tarefas = []
    with conect:
        cur = conect.cursor()
        cur.execute("SELECT * FROM Tarefas")
        row = cur.fetchall()
        for r in row:
            lista_tarefas.append(r)
    return lista_tarefas


def deletar(i):
    with conect:
        cur = conect.cursor()
        query = "DELETE FROM Tarefas WHERE id=?"
        cur.execute(query, i)


def atualizar(i):
    with conect:
        cur = conect.cursor()
        query = "UPDATE Tarefas SET nome=? WHERE id=?"
        cur.execute(query, i)


print(selecionar())

"""
with conect:
    cur = conect.cursor()
    cur.execute(
        "CREATE TABLE Tarefas (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)  ")
"""
