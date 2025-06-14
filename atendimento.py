class Atendimento:
    def __init__(self, id, paciente, especialidade, data_hora, status="Agendado"):
        self.id = id
        self.paciente = paciente
        self.especialidade = especialidade
        self.data_hora = data_hora
        self.status = status

    def __str__(self):
        info_atendimento = f"ID Atendimento: {self.id} | Data: {self.data_hora} | Status: {self.status}\n"
        info_atendimento += f" >> Paciente: {self.paciente.nome} (ID: {self.paciente.id})\n"
        info_atendimento += f" >> Especialidade: {self.especialidade.nome} (ID: {self.especialidade.id})"
        return info_atendimento
    
    
