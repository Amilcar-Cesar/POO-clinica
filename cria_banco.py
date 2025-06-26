import sqlite3

banco = sqlite3.connect("clinica.db")
cursor = banco.cursor()

print("Criando a tabela  'Pacientes'...")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pacientes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               data_nascimento TEXT NOT NULL,
               telefone TEXT); """)

print("Tabela criada com sucesso!")

print("Criando a tabela especialidades")

cursor.execute("""
CREATE TABLE IF NOT EXISTS especialidades(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL UNIQUE); """)

print("Tabela criada com sucesso!")

print("Criando a tabela atendimentos")

cursor.execute("""CREATE TABLE IF NOT EXISTS atendimentos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_paciente INTEGER NOT NULL,
                id_especialidade INTEGER NOT NULL,
                data_atendimendo TEXT NOT NULL,
                status TEXT NOT NULL,
                observações TEXT,
               
                FOREIGN KEY (id_paciente) REFERENCES pacientes (id),
                FOREIGN KEY (id_especialidade) REFERENCES especialidades (id)
               );""")

print("Tabela atendimentos criada com sucesso.")
banco.commit()
banco.close()