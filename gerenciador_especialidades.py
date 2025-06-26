import sqlite3
from especialidade import Especialidade

class GerenciadorEspecialidades:
    def __init__(self, db_name='clinica.db'):
        self.db_name = db_name

    def adicionar_especialidade(self, nome):
        banco = None
        try:
            banco = sqlite3.connect(self.db_name)
            cursor = banco.cursor()
            cursor.execute("INSERT INTO especialidades (nome) VALUES (?)", (nome,))
            banco.commit()
            print("\n >> Especialidade adicionada com sucesso! <<")

        except sqlite3.IntegrityError:
            print(f"\n>> ERRO: A especialidade '{nome}' já existe. <<")
        except Exception as e:
            print(f"\n>> ERRO ao adicionar especialidade: {e} <<")
            
        finally:
            if banco:
                banco.close()
    
    def listar_especialidades(self):
        banco = None
        try:
            banco = sqlite3.connect(self.db_name)
            cursor = banco.cursor()
            cursor.execute("SELECT * FROM especialidades")
            especialidades_encontradas = cursor.fetchall()
            
            lista_de_objetos_especialidade = []
            if especialidades_encontradas:
                for e in especialidades_encontradas:
                    especialidade = Especialidade(id=e[0], nome=e[1])
                    lista_de_objetos_especialidade.append(especialidade)
            return lista_de_objetos_especialidade

        except Exception as e:
            print(f"\n>> ERRO ao listar especialidades: {e} <<")
            return []
            
        finally:
            if banco:
                banco.close()

    def buscar_especialidade_id(self, id_especialidade):
        banco = None
        try:
            banco = sqlite3.connect(self.db_name)
            cursor = banco.cursor()
            cursor.execute("SELECT * FROM especialidades WHERE id = ?", (id_especialidade,))
            especialidade_tuple = cursor.fetchone()
            
            if especialidade_tuple:
                return Especialidade(id=especialidade_tuple[0], nome=especialidade_tuple[1])
            return None

        except Exception as e:
            print(f"\n>> ERRO ao buscar especialidade: {e} <<")
            return None
        
        finally:
            if banco:
                banco.close()

    def atualizar_especialidade(self, id_especialidade, novo_nome):
        banco = None
        try:
            banco = sqlite3.connect(self.db_name)
            cursor = banco.cursor()
            cursor.execute("UPDATE especialidades SET nome = ? WHERE id = ?", (novo_nome, id_especialidade))
            
            if cursor.rowcount == 0:
                print(f"\n>> ERRO: Especialidade com ID {id_especialidade} não encontrada para atualização. <<")
            else:
                banco.commit()
                print("\n >> Especialidade atualizada com sucesso! <<")    
        
        except sqlite3.IntegrityError:
             print(f"\n>> ERRO: A especialidade '{novo_nome}' já existe. <<")
        except Exception as e:
            print(f"\n>> ERRO ao atualizar especialidade: {e} <<")
            
        finally:
            if banco:
                banco.close()

    def remover_especialidade(self, id_especialidade):
        banco = None
        try:
            banco = sqlite3.connect(self.db_name)
            cursor = banco.cursor()
            cursor.execute("DELETE FROM especialidades WHERE id = ?", (id_especialidade,))

            if cursor.rowcount == 0:
                print(f"\n>> ERRO: Especialidade com ID {id_especialidade} não encontrada para remoção. <<")
            else:
                banco.commit()
                print("\n>> Especialidade removida com sucesso! <<")

        except Exception as e:
            print(f"\n>> ERRO ao remover especialidade: {e} <<")
            
        finally:
            if banco:
                banco.close()