import datetime
from atendimento import Atendimento

class GerenciadorAtendimentos:
    def __init__(self,gerenciador_pacientes, gerenciador_especialidades):
        self.atendimentos = []
        self.proximo_id_atendimento = 1
        self.gerenciador_pacientes = gerenciador_pacientes
        self.gerenciador_especialidades = gerenciador_especialidades


    def agendar_atendimento(self,id_paciente, id_especialidade):
        
        paciente = self.gerenciador_pacientes.buscar_paciente_id(id_paciente)
        especialidade = self.gerenciador_especialidades.buscar_especialidade_id(id_especialidade)

        if not paciente:
            print(">> ERRO: Paciente não encontrado. <<")
            return
        if not especialidade:
            print(">> ERRO: Especialidade não encontrada. <<")
            return
        
        data_agendamento = datetime.datetime.now()

        novo_atendimento = Atendimento(self.proximo_id_atendimento, paciente, especialidade, data_agendamento)
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
        #SELECT 
        for atendimento in self.atendimentos:
            if atendimento.id == id_atendimento:
                return atendimento
        return None
    
    def atualizar_status_atendimento(self, id_atendimento, novo_status):
        #SET atendimentos WHERE status = ?
        atendimento = self.buscar_atendimento(id_atendimento)

        if atendimento:
            atendimento.status = novo_status
            print(f"\n>> Status do atendimento {id_atendimento} atualizado para {novo_status}.")
        else:
            print("\n>> ERRO: Atendimento não encontrado. <<")