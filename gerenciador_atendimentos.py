# gerenciador_atendimentos.py (Versão Robusta com Banco de Dados)
import sqlite3
import datetime
from atendimento import Atendimento
from paciente import Paciente
from especialidade import Especialidade

class GerenciadorAtendimentos:
    def __init__(self, gerenciador_pacientes, gerenciador_especialidades, db_name='clinica.db'):
        self.db_name = db_name
        self.gerenciador_pacientes = gerenciador_pacientes
        self.gerenciador_especialidades = gerenciador_especialidades

    def agendar_atendimento(self, id_paciente, id_especialidade):
        banco = None
        try:
            banco = sqlite3.connect(self.db_name)
            cursor = banco.cursor()
            
           
            if not self.gerenciador_pacientes.buscar_paciente_id(id_paciente):
                print(f"\n>> ERRO: Paciente com ID {id_paciente} não existe. <<")
                return
            if not self.gerenciador_especialidades.buscar_especialidade_id(id_especialidade):
                print(f"\n>> ERRO: Especialidade com ID {id_especialidade} não existe. <<")
                return

            data_agendamento = datetime.datetime.now()
            status_inicial = "Agendado"
            
            cursor.execute("""
                INSERT INTO atendimentos (id_paciente, id_especialidade, data_atendimento, status)
                VALUES (?, ?, ?, ?)
            """, (id_paciente, id_especialidade, data_agendamento.isoformat(), status_inicial))
            
            banco.commit()
            print("\n>> Atendimento agendado com sucesso! <<")

        except Exception as e:
            print(f"\n>> ERRO ao agendar atendimento: {e} <<")
        finally:
            if banco:
                banco.close()

    def listar_atendimentos(self):
        banco = None
        lista_de_atendimentos = []
        try:
            banco = sqlite3.connect(self.db_name)
            cursor = banco.cursor()
            sql = """
            SELECT 
                at.id, at.status, at.data_atendimento,
                p.id, p.nome, p.data_nascimento, p.telefone,
                e.id, e.nome
            FROM 
                atendimentos AS at
            JOIN pacientes AS p ON at.id_paciente = p.id
            JOIN especialidades AS e ON at.id_especialidade = e.id
            ORDER BY at.id
            """
            cursor.execute(sql)
            resultados = cursor.fetchall()

            for linha in resultados:
                at_id, at_status, at_data, p_id, p_nome, p_nasc, p_tel, e_id, e_nome = linha
                paciente_obj = Paciente(p_id, p_nome, p_nasc, p_tel)
                especialidade_obj = Especialidade(e_id, e_nome)
                data_obj = datetime.datetime.fromisoformat(at_data)
                atendimento_obj = Atendimento(at_id, paciente_obj, especialidade_obj, data_obj, at_status)
                lista_de_atendimentos.append(atendimento_obj)
        except Exception as e:
            print(f"\n>> ERRO ao listar atendimentos: {e} <<")
        finally:
            if banco:
                banco.close()
        return lista_de_atendimentos
    
    
    def atualizar_status_atendimento(self, id_atendimento, novo_status):
        banco = None
        try:
            banco = sqlite3.connect(self.db_name)
            cursor = banco.cursor()
            cursor.execute("UPDATE atendimentos SET status = ? WHERE id = ?", (novo_status, id_atendimento))
            if cursor.rowcount == 0:
                print(f"\n>> ERRO: Atendimento com ID {id_atendimento} não encontrado. <<")
            else:
                banco.commit()
                print("\n>> Status do atendimento atualizado com sucesso! <<")
        except Exception as e:
            print(f"\n>> ERRO ao atualizar status: {e} <<")
        finally:
            if banco:
                banco.close()