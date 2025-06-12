from paciente import Paciente

class Clinica:
    def __init__(self):
        self.lista_pacientes = []
        self.proximo_id_paciente = 1
        self.especialidades = []
        self.atendimentos = []

#----METODO PARA GERENCIAR PACIENTES----
    def adicionar_paciente(self, nome, data_nascimento, telefone):

        novo_paciente =  Paciente(self.proximo_id_paciente, nome, data_nascimento, telefone) 
        self.lista_pacientes.append(novo_paciente)
        self.proximo_id_paciente += 1

        print("\n >> Paciente adicionado com sucesso! <<")
        print("==========================================\n")

    def listar_pacientes(self):

        print("\n --- Lista de Pacientes ---")
        if not self.lista_pacientes:
            print("Nenhum paciente cadastrado.")
        else:
            for paciente in self.lista_pacientes:
                print(paciente)
        print("==========================================\n")

    def buscar_paciente_id(self, id_paciente):
        
        for paciente in self.lista_pacientes:
            if paciente.id == id_paciente:
                return paciente
        raise ValueError("Paciente não encontrado.")
    
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
        else:
            raise ValueError(f"ERRO: Paciente id {paciente.id} não encontrado!")

    def remover_paciente(self, id_paciente):
        
        paciente = self.buscar_paciente_id(id_paciente)

        if paciente:
            print(f"Deletando paciente {paciente.nome} \n")
            self.lista_pacientes.remove(paciente)
            print("=====================================================\n")
            print("Paciente removido com sucesso!")

        else:
            raise ValueError(f"ERRO: Paciente id {paciente.id} não encontrado!")
