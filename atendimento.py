class Atendimento:
    def __init__(self, id, paciente, especialidade, data_hora, status):
        self.id = id
        self.paciente = paciente
        self.especialidade = especialidade
        #datetimenow
        self.data_hora = [] 
        self.status = status
    
    
    def marcar_realizado(self):
        self.status = "Realizado"

    def cancelar(self):
        self.status = "Cancelado"    
