from clinica import Clinica

def formatar_data(data_str):
    
    data_limpa = "".join(filter(str.isdigit, data_str))
    
    if len(data_limpa) == 8:
        dia = data_limpa[0:2]
        mes = data_limpa[2:4]
        ano = data_limpa[4:8]
        return f"{dia}/{mes}/{ano}"
    else:
        return None
    
#=================================================================
def formatar_telefone(tel_str):
    
    tel_limpo = "".join(filter(str.isdigit, tel_str))

    if len(tel_limpo) == 11:
        ddd = tel_limpo[0:2]
        parte1 = tel_limpo[2:7] 
        parte2 = tel_limpo[7:11] 
        return f"({ddd}) {parte1}-{parte2}"
    else:
        return None
    
#=================================================================
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
        
        #=================================================================
        if opcao == '1':
            print("\n--- Gerenciar Pacientes ---")
            print("1 - Adicionar paciente")
            print("2 - Listar pacientes")
            print("3 - Atualizar paciente")
            print("4 - Remover paciente") 
            op_paciente = input("Digite qual ação a ser feita: ")

            if op_paciente == '1':
                print("\n--- Novo paciente ---")
                nome = input("Nome do paciente: ").capitalize()
                
                data_formatada = None
                while not data_formatada:
                    data_input = input("Data de nascimento (somente números, ex: 25042000): ")
                    data_formatada = formatar_data(data_input)
                    if not data_formatada:
                        print(">> Data inválida! Por favor, digite 8 números. <<")
                
                telefone_formatado = None
                while not telefone_formatado:
                    tel_input = input("Telefone com DDD (somente números, ex: 21912345678): ")
                    telefone_formatado = formatar_telefone(tel_input)
                    if not telefone_formatado:
                        print(">> Telefone inválido! Por favor, digite 11 números. <<")
                minha_clinica.adicionar_paciente(nome, data_formatada, telefone_formatado)

            elif op_paciente == '2':
                lista_pacientes = minha_clinica.listar_pacientes()

                for paciente_obj in lista_pacientes:
                    print(paciente_obj)

            elif op_paciente == '3':
                id_paciente = int(input("Digite o ID do paciente a ser atualizado: "))
                paciente_encontrado = minha_clinica.buscar_paciente_id(id_paciente)

                if paciente_encontrado:
                    print(f"Editando dados de: {paciente_encontrado.nome}")

                    novo_nome = input(f"Informe o novo nome(atual {paciente_encontrado.nome}): ").capitalize()
                    
                    nova_data_formatada = None
                    while not nova_data_formatada:
                        nova_data = input(f"Data de nascimento(atual {paciente_encontrado.data_nascimento}): ")
                        nova_data_formatada = formatar_data(nova_data)
                        if not nova_data_formatada:
                            print(">> Data inválida! Por favor, digite 8 números. <<")
                    
                    telefone_formatado = None
                    while not telefone_formatado:
                        novo_tel = input("Telefone com DDD (somente números, ex: 21912345678): ")
                        telefone_formatado = formatar_telefone(novo_tel)
                        if not telefone_formatado:
                            print(">> Telefone inválido! Por favor, digite 11 números. <<")

                    minha_clinica.atualizar_paciente(id_paciente, novo_nome, nova_data_formatada, telefone_formatado)

                else:
                    print(f">> ERRO: Paciente com ID {id_paciente} não encontrado.")
                    

            elif op_paciente == '4':     
                id_paciente = int(input("Digite o ID do paciente a ser removido: "))
                minha_clinica.remover_paciente(id_paciente)
        #=================================================================
        
        elif opcao == '2':
            print("\n--- Gerenciar Especialidades ---")
            print("1 - Adicionar especialidade")
            print("2 - Listar especialidades")
            print("3 - Atualizar especialidade")
            print("4 - Remover especialidade")            
            op_espec = input("Digite o número da ação que deseja: ")

            if op_espec == '1':
                especialidade = input("Nome da nova especialidade: ").capitalize()
                minha_clinica.adicionar_especialidade(especialidade)
            
            elif op_espec == '2':
                especialidades = minha_clinica.listar_especialidades()
                
                for espec_obj in especialidades:
                    print(espec_obj)
            
            elif op_espec == '3':
                id_espec = int(input("Digite o ID da especialidade a ser atualizada: "))
                espec_encontrada = minha_clinica.gerenciador_especialidades.buscar_especialidade_id(id_espec)

                if espec_encontrada:
                    novo_nome = input(f"Digite o nome da especialidade(atual: {espec_encontrada.nome}): ").capitalize()
                    minha_clinica.atualizar_especialidade(id_espec, novo_nome)
                else:
                    print(f">> ERRO: Especialidade com ID {id_espec} não encontrada.")
           
            elif op_espec == '4': 
                id_remover = int(input("Informe o ID da especialidade a ser removida: "))
                minha_clinica.remover_especialidade(id_remover)
        #=================================================================

     
        elif opcao == '3':
            print("\n--- Gerenciar Atendimentos ---")
            print("1 - Agendar atendimento")
            print("2 - Listar atendimentos")
            print("3 - Atualizar status")
            
            op_atend = input("Qual ação deseja realizar? ")

            if op_atend == '1':
                print("\n--- Agendar Novo Atendimento ---")
                pacientes = minha_clinica.listar_pacientes()
                for p_obj in pacientes:
                    print(p_obj)
                
                print("\n======================================")

                especialidades = minha_clinica.listar_especialidades()
                for e_obj in especialidades:
                    print(e_obj) 
                
                id_paciente = int(input("\nDigite o ID do Paciente: ")) 
                id_espec = int(input("Digite o ID da Especialidade: "))
                minha_clinica.agendar_atendimento(id_paciente, id_espec)
            
            elif op_atend == '2': 
                atendimentos = minha_clinica.listar_atendimentos()
                for at_obj in atendimentos:
                    print(f"\n{at_obj}")
                    
            elif op_atend == '3':
                id_atend = int(input("Digite o ID do Atendimento a ser atualizado: "))
                novo_status = input("Digite o novo status (Ex: Realizado, Cancelado): ").upper()
                minha_clinica.atualizar_status_atendimento(id_atend, novo_status)
        #=================================================================
   
        
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()