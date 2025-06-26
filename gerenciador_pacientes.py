import sqlite3
from paciente import Paciente

class GerenciadorPacientes:
    def __init__(self, db_name='clinica.db'):
        self.db_name = db_name
    
    def adicionar_paciente(self, nome, data_nascimento, telefone):
        banco = None  
        try:
            banco = sqlite3.connect(self.db_name)
            cursor = banco.cursor()
            cursor.execute(
                "INSERT INTO pacientes(nome, data_nascimento, telefone) VALUES (?, ?, ?)", 
                (nome, data_nascimento, telefone)
            )
            banco.commit()
            print("\n >> Paciente adicionado com sucesso! <<")

        except Exception as e:
            print(f"\n>> ERRO ao adicionar paciente: {e} <<")
            
        finally:
            if banco:
                banco.close()

    def listar_pacientes(self):
        banco = None
        try:
            banco = sqlite3.connect(self.db_name)
            cursor = banco.cursor()
            cursor.execute("SELECT * FROM pacientes")
            pacientes_encontrados = cursor.fetchall()
            
            lista_de_objetos_paciente = []
            if pacientes_encontrados:
                for p in pacientes_encontrados:
                    paciente = Paciente(id=p[0], nome=p[1], data_nascimento=p[2], telefone=p[3])
                    lista_de_objetos_paciente.append(paciente)
            return lista_de_objetos_paciente

        except Exception as e:
            print(f"\n>> ERRO ao listar pacientes: {e} <<")
            return []  
            
        finally:
            if banco:
                banco.close()

    def buscar_paciente_id(self, id_paciente):
        banco = None
        try:
            banco = sqlite3.connect(self.db_name)
            cursor = banco.cursor()
            cursor.execute("SELECT * FROM pacientes WHERE id = ?", (id_paciente,))
            paciente_tuple = cursor.fetchone()
            
            if paciente_tuple:
                return Paciente(id=paciente_tuple[0], nome=paciente_tuple[1], data_nascimento=paciente_tuple[2], telefone=paciente_tuple[3])
            return None

        except Exception as e:
            print(f"\n>> ERRO ao buscar paciente: {e} <<")
            return None # Retorna None em caso de erro
            
        finally:
            if banco:
                banco.close()
    
    def atualizar_paciente(self, id_paciente, novo_nome, nova_data, novo_telefone):
        banco = None
        try:
            banco = sqlite3.connect(self.db_name)
            cursor = banco.cursor()
            cursor.execute("""
                UPDATE pacientes 
                SET nome = ?, data_nascimento = ?, telefone = ?
                WHERE id = ?
            """, (novo_nome, nova_data, novo_telefone, id_paciente))
            
            
            if cursor.rowcount == 0:
                print(f"\n>> ERRO: Paciente com ID {id_paciente} não encontrado para atualização. <<")
            else:
                banco.commit()
                print("\n>> Paciente atualizado com sucesso! <<")

        except Exception as e:
            print(f"\n>> ERRO ao atualizar paciente: {e} <<")

        finally:
            if banco:
                banco.close()

    def remover_paciente(self, id_paciente):
        banco = None
        try:
            banco = sqlite3.connect(self.db_name)
            cursor = banco.cursor()
            cursor.execute("DELETE FROM pacientes WHERE id = ?", (id_paciente,))

            if cursor.rowcount == 0:
                # Se rowcount for 0, nenhuma linha foi deletada, o que significa que o ID não existia
                print(f"\n>> ERRO: Paciente com ID {id_paciente} não encontrado para remoção. <<")
            else:
                banco.commit()
                print("\n>> Paciente removido com sucesso! <<")

        except Exception as e:
            print(f"\n>> ERRO ao remover paciente: {e} <<")
            
        finally:
            if banco:
                banco.close()