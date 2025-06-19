class Atendimento:
    def __init__(self, id, paciente, especialidade, data_hora, status="Agendado"):
        self.id = id
        self.paciente = paciente
        self.especialidade = especialidade
        self.data_hora = data_hora
        self.status = status

    def __str__(self):
        data_formatada = self.data_hora.strftime("%d/%m/%Y ás %H:%M:%S") 
        
        info_atendimento = f"ID Atendimento: {self.id} | Data: {data_formatada} | Status: {self.status}\n"
        info_atendimento += f" >> Paciente: {self.paciente.nome} (ID: {self.paciente.id})\n"
        info_atendimento += f" >> Especialidade: {self.especialidade.nome} (ID: {self.especialidade.id})"
        return info_atendimento
    
    
