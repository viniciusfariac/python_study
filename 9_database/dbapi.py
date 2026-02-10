import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "clientes.db")
cursor = con.cursor()
cursor.row_factory =  sqlite3.Row

def create_table(con, cursor):
    cursor.execute("CREATE TABLE clientes (id INT AUTOINCREMENT PRIMARY KEY, nome VARCHAR(100), email VARCHAR(100));")

def insert(con,cursor, nome, email):
    try:
        data = (nome, email)
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
        con.commit()
    except Exception as exc:
        print(f"Erro no banco {exc}")
        con.rollback()

def update(con, cursor, id, nome, email):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome = ? email = ? WHERE id = ?;", data)
    con.commit()

def remove(con, cursor, id):
    data = (id, )
    cursor.execute("DELETE FROM clientes WHERE id = ?;", data)
    con.commit()

def insert_many(con, cursor, data):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    con.commit()

def select (con, cursor, nome):
    cursor.execute("SELECT * FROM clientes WHERE nome = ?;", nome)
    result = cursor.fetchone()
    print(dict(result))
    for row in result:
        print(row)



nome = "Vinicius Faria"
email = "viniciusfaria@gmail.com"

data_updatemany = [
    ("vini", "vini@gmail"),
   ("rapha", "rapha@gmail")
]

# insert_many(con, cursor, data_updatemany)

select(con, cursor, ("vini", ))