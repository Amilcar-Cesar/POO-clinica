from atendimento import Atendimento
from clinica import Clinica
from especialidade import Especialidade
from paciente import Paciente


def menu_principal():
    minha_clinica = Clinica()
    while True:
        print("\n--- Sistema de Gerenciamento da Clínica ---")
        print("--- Gerenciar Pacientes ---")
        print("1. Adicionar Paciente")
        print("2. Listar Pacientes")
        print("3. Atualizar Paciente")
        print("4. Remover Paciente")
        print("\n--- Gerenciar Especialidades ---")
        print("5. Adicionar Especialidade")
        print("6. Listar Especialidades")
        print("7. Atualizar Especialidade")
        print("8. Remover Especialidade")
        print("\n9. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do paciente: ")
            data = input("Digite a data de nascimento (DD/MM/AAAA): ")
            tel = input("Digite o telefone: ")
            minha_clinica.adicionar_paciente(nome, data, tel)
        elif opcao == '2':
            minha_clinica.listar_pacientes()
        elif opcao == '3':
            id_paciente = int(input("Digite o ID do paciente que deseja atualizar: "))
            minha_clinica.atualizar_paciente(id_paciente)
        elif opcao == '4':
            id_paciente = int(input("Digite o ID do paciente que deseja remover: "))
            minha_clinica.remover_paciente(id_paciente)
        elif opcao == '5':
            nome_espec = input("Digite o nome da especialidade: ")
            minha_clinica.adicionar_especialidade(nome_espec)
        elif opcao == '6':
            minha_clinica.listar_especialidade()
        elif opcao == '7':
            id_espec = int(input("Digite o ID da especialidade que deseja atualizar: "))
            minha_clinica.atualizar_especialidade(id_espec)
        elif opcao == '8':
            id_espec = int(input("Digite o ID da especialidade que deseja remover: "))
            minha_clinica.remover_especialidade(id_espec)
        elif opcao == '9':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu principal
if __name__ == "__main__":
    menu_principal()