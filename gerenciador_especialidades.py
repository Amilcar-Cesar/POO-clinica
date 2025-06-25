from especialidade import Especialidade
import sqlite3

class GerenciadorEspecialidades:
    def __init__(self,db_name='clinica.db'):
            self.db_name = db_name
        

    def adicionar_especialidade(self, nome):

        banco = sqlite3.connect(self.db_name)
        cursor = banco.cursor()
        cursor.execute("INSERT INTO especialidades (nome) VALUES(?)",(nome,))
        banco.commit()
        banco.close()
        print("\n >> Especialidade adicionada com sucesso! <<")
        print("==========================================\n")

#=============================================================================
    def listar_especialidades(self):
        
        banco = sqlite3.connect(self.db_name)
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM especialidades")
        especialidades_encontradas = cursor.fetchall()
        banco.close()
        
        lista_de_objetos_especialidades = []
        print("----Lista de Especialidades----")
        if not especialidades_encontradas:
            print("Nenhuma especialidade cadastrada!")
        else:
            for e in especialidades_encontradas:
                especialidade = Especialidade(id=e[0], nome=e[1])
                lista_de_objetos_especialidades.append(especialidade)
            return lista_de_objetos_especialidades
            

#=============================================================================
    def buscar_especialidade_id(self, id_especialidade):
        
        banco = sqlite3.connect(self.db_name)
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM especialidades WHERE id = ?",(id_especialidade,))
        resultado = cursor.fetchone()
        banco.close()

        if resultado:
            return Especialidade(
                id=resultado[0],
                nome=resultado[1]
            )
        return None
    
#=============================================================================
    def atualizar_especialidade(self,id_especialidade):
        
        especialidade = self.buscar_especialidade_id(id_especialidade)
        banco = sqlite3.connect(self.db_name)
        cursor = banco.cursor()

        if especialidade:
            novo_nome = input(f"Atualize a especialidade (atual:{especialidade.nome}): ").capitalize()
            cursor.execute("""UPDATE especialidades 
                           SET nome = ?
                           WHERE id = ?""",(novo_nome, id_especialidade))
            banco.commit()
            banco.close()
            print("\n >> Especialidade atualizada com sucesso! <<")    
            
        else:
            print("\n>>ERRO: Especialidade não encontrada. <<")

#=============================================================================
    def remover_especialidade(self, id_especialidade):

        especialidade = self.buscar_especialidade_id(id_especialidade)
        
        if especialidade:
            print(f"Removendo {especialidade.nome}..")
            banco = sqlite3.connect(self.db_name)
            cursor = banco.cursor
            cursor.execute("DELETE FROM especialidades WHERE id = ?",(id_especialidade))
            banco.commit()
            banco.close()
            print("\n>> Especialidade removida com sucesso! <<")
            print("=========================================\n")
        else:
            print("ERRO: Especialidade não encontrada.")