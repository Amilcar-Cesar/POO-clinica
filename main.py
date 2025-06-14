from atendimento import Atendimento
from clinica import Clinica
from especialidade import Especialidade
from paciente import Paciente


def menu_principal():
    minha_clinica = Clinica()
    while True:
        print("\n--- Sistema de Gerenciamento da Clínica ---")
        print("--- Pacientes ---")
        print("1. Adicionar Paciente | 2. Listar Pacientes")
        print("--- Especialidades ---")
        print("3. Adicionar Especialidade | 4. Listar Especialidades")
        print("--- Atendimentos ---")
        print("5. Agendar Atendimento")
        print("6. Listar Atendimentos")
        print("7. Atualizar Status de Atendimento")
        print("\n8. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do paciente: ")
            data = input("Data de nascimento (DD/MM/AAAA): ")
            tel = input("Telefone: ")
            minha_clinica.adicionar_paciente(nome, data, tel)
        elif opcao == '2':
            minha_clinica.listar_pacientes()
        elif opcao == '3':
            nome_espec = input("Nome da especialidade: ")
            minha_clinica.adicionar_especialidade(nome_espec)
        elif opcao == '4':
            minha_clinica.listar_especialidade()
        elif opcao == '5':
            print("\n--- Agendar Novo Atendimento ---")
            # Para facilitar, listamos as opções disponíveis para o usuário
            minha_clinica.listar_pacientes()
            minha_clinica.listar_especialidade()
            id_paciente = int(input("Digite o ID do Paciente: "))
            id_espec = int(input("Digite o ID da Especialidade: "))
            data_hora = input("Digite a data e hora (ex: 20/10/2025 14:30): ")
            minha_clinica.agendar_atendimento(id_paciente, id_espec, data_hora)
        elif opcao == '6':
            minha_clinica.listar_atendimentos()
        elif opcao == '7':
            id_atend = int(input("Digite o ID do Atendimento a ser atualizado: "))
            novo_status = input("Digite o novo status (Ex: Realizado, Cancelado): ")
            minha_clinica.atualizar_status_atendimento(id_atend, novo_status)
        elif opcao == '8':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()