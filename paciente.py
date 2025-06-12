class Paciente:
    def __init__(self, id, nome, data_nascimento, telefone):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.telefone = telefone

        
    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Nascimento: {self.data_nascimento} | Telefone: {self.telefone}."
    