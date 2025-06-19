from especialidade import Especialidade

class GerenciadorEspecialidades:
    def __init__(self):
        self.lista_especialidades = []
        self.proximo_id_especialidade = 1

    def adicionar_especialidade(self, nome):

        nova_especialidade = Especialidade(self.proximo_id_especialidade, nome) 
        self.lista_especialidades.append(nova_especialidade)
        self.proximo_id_especialidade += 1

        print("\n >> Especialidade adicionada com sucesso! <<")
        print("==========================================\n")

    def listar_especialidades(self):
        
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
            print("\n >> Especialidade atualizada com sucesso! <<")    
            
        else:
            print("\n>>ERRO: Especialidade não encontrada. <<")


    def remover_especialidade(self, id_especialidade):

        especialidade = self.buscar_especialidade_id(id_especialidade)

        if especialidade:
            print(f"Removendo {especialidade.nome}..")
            self.lista_especialidades.remove(especialidade)
            print("\n>> Especialidade removida com sucesso! <<")
            print("=========================================\n")
        else:
            print("ERRO: Especialidade não encontrada.")