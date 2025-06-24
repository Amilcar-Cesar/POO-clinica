from paciente import Paciente
import sqlite3

class GerenciadorPacientes:
    def __init__(self, db_name='clinica.db'):
        self.db_name = db_name
        

    
    def adicionar_paciente(self, nome, data_nascimento, telefone):

        banco = sqlite3.connect(self.db_name)
        cursor = banco.cursor()
        cursor.execute(
            "INSERT INTO pacientes(nome, data_nascimento, telefone) VALUES (?, ?, ?)", (nome, data_nascimento, telefone)
        )
        banco.commit()
        banco.close()

        print("\n >> Paciente adicionado com sucesso! <<")
        print("==========================================\n")

    def listar_pacientes(self):

        banco = sqlite3.connect(self.db_name)
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM pacientes")
        pacientes_encontrados = cursor.fetchall()
        
        lista_de_objetos_paciente = []
        banco.close()
        
        print("\n --- Lista de Pacientes ---")
        
        if not pacientes_encontrados:
            print("Nenhum paciente cadastrado.")
        else:
            for p in pacientes_encontrados:
                paciente = Paciente(id=p[0],nome=p[1],data_nascimento=p[2],telefone=p[3])
                lista_de_objetos_paciente.append(paciente)
        
        return lista_de_objetos_paciente
        
        

    def buscar_paciente_id(self, id_paciente):
        
        banco = sqlite3.connect(self.db_name)
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM pacientes WHERE id = ?", (id_paciente,))
        resultado = cursor.fetchone()
        banco.close()

        if resultado:
            return Paciente(
                id=resultado[0],
                nome=resultado[1],
                data_nascimento=resultado[2],
                telefone=resultado[3]
            )
    
        return None

        
    
    def atualizar_paciente(self, id_paciente):

        paciente = self.buscar_paciente_id(id_paciente)
            
        if paciente:
            print(f"Editando paciente: {paciente.nome}")
            novo_nome = input(f"Novo nome (atual:{paciente.nome}): ")
            nova_data = input(f"Nova data de nascimento(atual:{paciente.data_nascimento}): ")
            novo_telefone = input(f"Novo telefone (atual:{paciente.telefone}): ")

            paciente.nome = novo_nome
            paciente.data_nascimento = nova_data
            paciente.telefone = novo_telefone
            
            print("\n>> Paciente atualizado com sucesso! <<")
        else:
            print(f"\nERRO: Paciente com ID {id_paciente} não encontrado!")

    def remover_paciente(self, id_paciente):
        
        banco = sqlite3.connect(self.db_name)
        cursor = banco.cursor()
        paciente = self.buscar_paciente_id(id_paciente)
        
        if paciente:
            print("=====================================================\n")
            print(f"Deletando paciente {paciente.nome} \n")
            cursor.execute("DELETE FROM pacientes WHERE id= ?", (id_paciente,))
            print("Paciente removido com sucesso!\n")
            banco.commit()
        else:
            print(f"ERRO: Paciente id {paciente.id} não encontrado!")
        
        banco.close()
        
        
