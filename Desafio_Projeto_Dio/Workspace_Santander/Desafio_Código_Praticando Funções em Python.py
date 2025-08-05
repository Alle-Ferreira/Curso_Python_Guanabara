'''
DESAFIO 1

Descrição
Uma clínica médica quer automatizar seu sistema de atendimento. Crie uma função que organize os pacientes em ordem de prioridade com base na idade e na urgência do caso.

Critérios de Prioridade:

Pacientes acima de 60 anos têm prioridade.
Pacientes que apresentam a palavra "urgente" na ficha têm prioridade máxima.
Os demais pacientes são atendidos por ordem de chegada.
Entrada
Um número inteiro n, representando a quantidade de pacientes.
n linhas seguintes, cada uma contendo os dados de um paciente no formato: nome, idade, status
nome: string representando o nome do paciente.
idade: número inteiro representando a idade do paciente.
status: string que pode ser "urgente" ou "normal".
Saída
A saída deve exibir a lista dos pacientes ordenada de acordo com as regras de prioridade, no formato: Ordem de Atendimento: nome1, nome2, nome3, ...
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
3
Carlos, 40, normal
Ana, 70, normal
Bruno, 30, urgente
Ordem de Atendimento: Bruno, Ana, Carlos

4
Paula, 30, normal
Ricardo, 60, normal
Tiago, 60, urgente
Amanda, 50, urgente
Ordem de Atendimento: Tiago, Amanda, Ricardo, Paula

5
João, 65, normal
Maria, 80, urgente
Lucas, 50, normal
Fernanda, 25, normal
Pedro, 90, urgente
Ordem de Atendimento: Pedro, Maria, João, Lucas, Fernanda'''

n = int(input().strip())                    # Entrada do número de pacientes
pacientes = []                              # Lista para armazenar pacientes

for paciente in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
def prioridade(paciente):
    nome, idade, status = paciente
    if status.lower() == "urgente":
        return (0, -idade)  # prioridade máxima: mais velho primeiro
    elif idade >= 60:
        return (1, -idade)  # idosos:  mais velho primeiro
    else:
        return (2, 0)       # normal: por ordem de chegada

pacientes.sort(key=prioridade)

# TODO: Exiba a ordem de atendimento com título e vírgulas:
nomes = [paciente[0] for paciente in pacientes]
print('Ordem de Atendimento: ' + ', '.join(nomes))


'''
DESAFIO 2

Descrição
Uma pousada deseja automatizar seu sistema de reservas. Crie uma função que receba uma lista de quartos disponíveis e uma lista de reservas solicitadas. A função deve verificar quais reservas podem ser aceitas e quais devem ser recusadas por falta de disponibilidade.

Entrada
Uma lista contendo os números dos quartos disponíveis.
Uma lista contendo os números dos quartos solicitados pelos clientes.
Saída
Uma mensagem informando quais reservas foram confirmadas e quais foram recusadas.

Entrada	
101 102 103 104
102 105 101 103	
Saída
Reservas confirmadas: 102 101 103
Reservas recusadas: 105

Entrada	
201 202 203 204 205
205 202 208 201 203	
Saída
Reservas confirmadas: 205 202 201 203
Reservas recusadas: 208

Entrada	
10 20 30 40 50
25 30 10 40 50 60
Saída	
Reservas confirmadas: 30 10 40 50
Reservas recusadas: 25 60
'''

def processar_reservas():
    quartos_disponiveis = set(map(int, input().split()))    # Entrada dos quartos disponíveis
    reservas_solicitadas = list(map(int, input().split()))  # Entrada das reservas solicitadas

    # TODO: Crie o processamento das reservas:
    confirmadas = []
    recusadas = [] 

    # TODO: Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos: 
    for quarto in reservas_solicitadas:
        if quarto in quartos_disponiveis:
            confirmadas.append(quarto)
            quartos_disponiveis.remove(quarto)             # Remove para não permitir duplicidade
        else:
            recusadas.append(quarto)    

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()


'''Notas:

1. map(int, ...)
map() aplica a função int a cada item da lista resultante de .split().
Isso converte cada string (ex: '101') em um número inteiro. Exemplo:

map(int, ['101', '102', '103'])   => um iterador com [101, 102, 103]

2. set(...)
set() transforma o resultado em um conjunto de valores únicos (sem repetições).
Muito usado para verificar disponibilidade, evitar duplicatas, etc. Exemplo:

set([101, 102, 103])   => {101, 102, 103}'''