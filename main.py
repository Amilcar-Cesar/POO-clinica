from clinica import Clinica

def menu_principal():
    minha_clinica = Clinica()
    while True:
        print("\n--- Sistema de Gerenciamento da Clínica ---")
        print("1 - Pacientes")
        print("2 - Especialidades")
        print("3 - Atendimentos")
        print("4. Sair")
        print("===============================")
        
        opcao = input("Escolha uma opção: ")
        
        
        if opcao == '1':
            print("\n--- Gerenciar Pacientes ---")
            print("1 - Adicionar paciente")
            print("2 - Listar pacientes")
            print("3 - Atualizar paciente")
            print("4 - Remover paciente")
            
            op_paciente = input("Digite qual ação a ser feita: ")

            if op_paciente == '1':
                print("\n--- Novo paciente ---")
                nome = input("Nome do paciente: ")
                data = input("Data de nascimento (DD/MM/AAAA): ")
                tel = input("Telefone: ")
                minha_clinica.adicionar_paciente(nome, data, tel)
            
            elif op_paciente == '2':
                minha_clinica.listar_pacientes()
            
            elif op_paciente == '3':
                id_paciente = int(input("Digite o ID do paciente a ser atualizado: "))
                minha_clinica.atualizar_paciente(id_paciente)
            
            elif op_paciente == '4':     
                id_paciente = int(input("Digite o ID do paciente a ser removido: "))
                minha_clinica.remover_paciente(id_paciente)
            
        
        elif opcao == '2':
            print("\n--- Gerenciar Especialidades ---")
            print("1 - Adicionar especialidade")
            print("2 - Listar especialidades")
            print("3 - Atualizar especialidade")
            print("4 - Remover especialidade")
            
            op_espec = input("Digite o número da ação que deseja: ")

            if op_espec == '1':
                especialidade = input("Nome da nova especialidade: ")
                minha_clinica.adicionar_especialidade(especialidade)
            elif op_espec == '2':
                
                minha_clinica.listar_especialidades()
            elif op_espec == '3':
                 
                id_espec = int(input("Digite o ID da especialidade a ser atualizada: "))
                minha_clinica.atualizar_especialidade(id_espec)
            elif op_espec == '4':
            
                id_remover = int(input("Informe o ID da especialidade a ser removida: "))
                minha_clinica.remover_especialidade(id_remover)

        
        elif opcao == '3':
            print("\n--- Gerenciar Atendimentos ---")
            print("1 - Agendar atendimento")
            print("2 - Listar atendimentos")
            print("3 - Atualizar status")
            
            op_atend = input("Qual ação deseja realizar? ")

            if op_atend == '1':
                print("\n--- Agendar Novo Atendimento ---")
                minha_clinica.listar_pacientes()
                minha_clinica.listar_especialidades() 
                id_paciente = int(input("Digite o ID do Paciente: ")) 
                id_espec = int(input("Digite o ID da Especialidade: "))
                minha_clinica.agendar_atendimento(id_paciente, id_espec)
            elif op_atend == '2': 
                minha_clinica.listar_atendimentos()
            elif op_atend == '3':
                id_atend = int(input("Digite o ID do Atendimento a ser atualizado: "))
                novo_status = input("Digite o novo status (Ex: Realizado, Cancelado): ")
                minha_clinica.atualizar_status_atendimento(id_atend, novo_status)
        
        # CORRIGIDO: Usando ELIF
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        
        # Agora este ELSE só será executado se nenhuma das opções (1, 2, 3, 4) for escolhida.
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()