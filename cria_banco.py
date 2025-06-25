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
banco.commit()
banco.close()