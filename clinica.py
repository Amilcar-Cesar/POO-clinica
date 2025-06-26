from gerenciador_atendimentos import GerenciadorAtendimentos
from gerenciador_especialidades import GerenciadorEspecialidades
from gerenciador_pacientes import GerenciadorPacientes

class Clinica:
    def __init__(self):
        self.gerenciador_pacientes = GerenciadorPacientes()
        self.gerenciador_especialidades = GerenciadorEspecialidades()
        self.gerenciador_atendimentos = GerenciadorAtendimentos(self.gerenciador_pacientes, self.gerenciador_especialidades)


#===================================================================     
    #----METODO PARA GERENCIAR PACIENTES----
    def adicionar_paciente(self,nome, data_nascimento, telefone):
        self.gerenciador_pacientes.adicionar_paciente(nome, data_nascimento, telefone)
    
    def listar_pacientes(self):
        return self.gerenciador_pacientes.listar_pacientes()
   
    def buscar_paciente_id(self, id_paciente):
        return self.gerenciador_pacientes.buscar_paciente_id(id_paciente)

    def atualizar_paciente(self,id_paciente, novo_nome, nova_data, novo_telefone):
        self.gerenciador_pacientes.atualizar_paciente(id_paciente,  novo_nome, nova_data, novo_telefone)
   
    def remover_paciente(self,id_paciente):
        self.gerenciador_pacientes.remover_paciente(id_paciente)

   #=================================================================
    #----METODO PARA GERENCIAR ESPECIALIDADES----
    def adicionar_especialidade(self, nome):
        self.gerenciador_especialidades.adicionar_especialidade(nome)

    def listar_especialidades(self):
        return self.gerenciador_especialidades.listar_especialidades()

    def buscar_especialidade_id(self, id_especialidade):
        return self.gerenciador_especialidades.buscar_especialidade_id

    def atualizar_especialidade(self,id_especialidade, novo_nome):
        self.gerenciador_especialidades.atualizar_especialidade(id_especialidade, novo_nome )

    def remover_especialidade(self,id_especialidade):
        self.gerenciador_especialidades.remover_especialidade(id_especialidade)

#===================================================================
    #----METODO PARA GERENCIAR ATENDIMENTOS----
    def agendar_atendimento(self,id_paciente, id_especialidade):
        self.gerenciador_atendimentos.agendar_atendimento(id_paciente,id_especialidade)

    def listar_atendimentos(self):
        return self.gerenciador_atendimentos.listar_atendimentos()

    def atualizar_status_atendimento(self,id_atendimento, novo_status):
        self.gerenciador_atendimentos.atualizar_status_atendimento(id_atendimento, novo_status)
    