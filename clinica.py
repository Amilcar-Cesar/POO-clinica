from paciente import Paciente
from especialidade import Especialidade
from atendimento import Atendimento
class Clinica:
    def __init__(self):
        self.lista_pacientes = []
        self.proximo_id_paciente = 1
        self.lista_especialidades = []
        self.proximo_id_especialidade = 1
        self.atendimentos = []
        self.proximo_id_atendimento = 1

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

#METODO PARA GERENCIAR ESPECIALIDADES

    def adicionar_especialidade(self, nome):

        nova_especialidade = Especialidade(self.proximo_id_especialidade, nome) 
        self.lista_especialidades.append(nova_especialidade)
        self.proximo_id_especialidade += 1

        print("\n >> Especialidade adicionada com sucesso! <<")
        print("==========================================\n")

    def listar_especialidade(self):
        
        print("----Lista de Especialidades----")
        if not self.lista_especialidades:
            print("Nenhuma especialidade cadastrada!")
        else:
            for especialidade in self.lista_especialidades:
                print(especialidade)
            print("==========================================\n")


    def buscar_especialidade_id(self, id_especialidade):
        
        for especialidade in self.lista_especialidades:
            if especialidade.id == id_especialidade:
                return especialidade
        return None
    
    def atualizar_especialidade(self,id_especialidade):
        
        especialidade = self.buscar_especialidade_id(id_especialidade)

        if especialidade:
            especialidade.nome = input(f"Atualize a especialidade (atual:{especialidade.nome}): ")
            print("\n >> Paciente atualizado com sucesso! <<")    
            
        else:
            print("\n>>ERRO: Especialidade não encontrada. <<")


    def remover_especialidade(self, id_especialidade):

        especialidade = self.buscar_especialidade_id(id_especialidade)

        if especialidade:
            print(f"Removendo {especialidade.nome}..")
            self.lista_especialidades.remove(id_especialidade)
            print("\n>> Especialidade removida com sucesso! <<")
            print("=========================================\n")
        else:
            print("ERRO: Especialidade não encontrada.")    

# METODO PARA GERENCIAR ATENDIMENTOS

    def agendar_atendimento(self,id_paciente, id_especialidade, data_hora):
        
        paciente = self.buscar_paciente_id(id_paciente)
        especialidade = self.buscar_especialidade_id(id_especialidade)

        if not paciente:
            print(">> ERRO: Paciente não encontrado. <<")
            return
        if not especialidade:
            print(">> ERRO: Especialidade não encontrada. <<")
            return
        #perguntar ao gemini
        novo_atendimento = Atendimento(self.proximo_id_atendimento, paciente, especialidade, data_hora)
        self.atendimentos.append(novo_atendimento)
        self.proximo_id_atendimento += 1
        print("\n>> Atendimento agendado com sucesso! <<")


    def listar_atendimentos(self):
        
        print("\n---Lista de atendimentos---")
        if not self.atendimentos:
            print("Nenhum atendimento agendado.")
        else:
            for atendimento in self.atendimentos:
                print(atendimento)
                print("-" *30)
        print("-----------------------------------")


    def buscar_atendimento(self,id_atendimento):
        
        for atendimento in self.atendimentos:
            if atendimento.id == id_atendimento:
                return atendimento
        return None
    
    def atualizar_status_atendimento(self, id_atendimento, novo_status):

        atendimento = self.buscar_atendimento(id_atendimento)

        if atendimento:
            atendimento.status = novo_status
            print(f"\n>> Status do atendimento {id_atendimento} atualizado para {novo_status}.")
        else:
            print("\n>> ERRO: Atendimento não encontrado. <<")