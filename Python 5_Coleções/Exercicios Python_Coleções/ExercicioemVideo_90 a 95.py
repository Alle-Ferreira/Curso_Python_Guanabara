'''Dicionário em Python

Exercício Python 090 - Dicionário em Python
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
Parametro posterior:
- Situação: Aprovado (>= 7), Reprovado (<5) ou Recuperação.'''

cadastro = {}

cadastro['nome'] = input('Nome do aluno: ')
cadastro['media'] = float(input('Média do aluno: '))

if cadastro['media'] >= 7:
    situacao = 'Aprovado'
elif cadastro['media'] < 5:
    situacao = 'Reprovado'  
else:
    situacao = 'Recuperação'
cadastro['situacao'] = situacao

print(f"Nome: {cadastro['nome']}")
print(f"Média: {cadastro['media']} - Situação: {cadastro['situacao']}")

#Variação:

for chave, valor in cadastro.items():
    print(f'{chave} é igual a {valor}')

'''
Exercício Python 091 - Jogo de Dados em Python
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter

resultados = {}
# Começa no 1 para evitar confusão com o índice 0, que é o padrão em Python
for numero in range(1, 5):
    resultados[(f'Jogador {numero}')] = randint(1,6)
print('Valores sorteados:')

for jogador, valor in resultados.items():
    print(f'{jogador} tirou {valor}')
    sleep(1)

#item(1) retorna o segundo elemento do item, que é o valor do dado.
#ranking = sorted(resultados.items(), key=lambda x: x[1], reverse=True)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print()

for indice, (jogador, valor) in enumerate(ranking):
    print(f'{indice + 1}º lugar: {jogador} com {valor} pontos')

vencedor = ranking[0]
print(f'\nO vencedor foi {vencedor[0]} com {vencedor[1]} pontos.\n')


'''
Exercício Python 092 - Cadastro de Trabalhador em Python
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
Parametro posterior:
- Aposentadoria: mínimo 35 anos de contribuição.
'''
from datetime import datetime

cadastro = {}
data_atual = datetime.now()
ano_atual = data_atual.year
min_contribuicao = 35

cadastro['nome'] = input('Nome do Trabalhador: ')
cadastro['ctps'] = int(input('Numero da CTPS (se não houver, digite 0): '))
cadastro['ano_nascimento'] = int(input('Ano de Nascimento: '))
cadastro['idade'] = ano_atual - cadastro['ano_nascimento']

if cadastro['ctps'] != 0:
    cadastro['ano_contratacao'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário: '))

    tempo_contribuicao = ano_atual - cadastro['ano_contratacao']
    carecia_aposentadoria = min_contribuicao - tempo_contribuicao
    
    cadastro['idade_aposentadoria'] = cadastro['idade'] + carecia_aposentadoria

    print(f'Você pode se aposentar aos {cadastro['idade_aposentadoria']} anos.')
    if carecia_aposentadoria > 0:
        print(f'Você ainda tem carência de {carecia_aposentadoria} ano(s) de contribuição.')
    else:
        print('Você já pode se aposentar.')
else:
    print('Na ausencia dos dados da CTPS, não é possível calcular aposentadoria.')


'''Exercício Python 093 - Cadastro de Jogador de Futebol
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida, armazenando tudo em um dicionário. No final, tudo isso será mostrado na tela, incluindo o total de gols feitos na carreira.'''

jogador = {}        #nome, partida_gol, total_gols

jogador['nome'] = input('Nome do Jogador: ')
qtde_partidas = int(input('Quantas partidas jogou: '))

gols = []
for partida_gol in range (qtde_partidas):
    gols.append(int(input(f'Quantos gols na partida {partida_gol + 1}? ')))

jogador['partida_gol'] = gols
jogador['total_gols'] = sum(gols)

print('-' * 30)
print(f'\nO jogador {jogador['nome']} jogou {qtde_partidas} partidas, com total de {jogador['total_gols']} gols.\n')
print('-' * 30)

print('Histórico de Partidas'.center(30))
print('-' * 30)
for indice, partida_gol in enumerate (jogador['partida_gol'], start=1):
    print(f'Na partida {indice}, fez {partida_gol} gol(s).')
print('-' * 30)


'''Exercício Python 094 (Falso) - Unindo dicionários e listas
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

cadastros = []

while True:
    cadastro = {}

    cadastro['nome'] = input('Nome do aluno: ')
    cadastro['nota1'] = float(input('Nota 1 do aluno: '))
    cadastro['nota2'] = float(input('Nota 2 do aluno: '))
    cadastro['media'] = float(cadastro['nota1'] + cadastro['nota2']) / 2
    cadastros.append(cadastro)

    resposta = input('Deseja cadastrar outro aluno? [S/N]: ').strip().upper()
    if resposta != 'S':
        break

print('\nBOLETIM TURMA 1 - 2025')
print('-' * 45)
for indice, cadastro in enumerate(cadastros):
    print(f'{indice:<2} - Nome: {cadastro['nome']:<14} - Nota média {cadastro['media']:>4.2f}.')
print('-' * 45)
print()

indice = int(input('Para visualizar o detalhamento das notas do aluno, informe o "Nr. Aluno": '))

print('\nBoletim Escolar'.center(30))
print('-' * 30)
print(f'Aluno: {cadastros[indice]['nome']}')
print(f'Nota 1: {cadastros[indice]['nota1']:.1f}')
print(f'Nota 2: {cadastros[indice]['nota2']:.1f}')
print(f'Média: {cadastros[indice]['media']:.1f}')
print('-' * 30)


'''Exercício Python 094 - Unindo dicionários e listas (Correto)
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
cadastros = []

while True:
    cadastro = {}

    cadastro['nome'] = input('Nome: ')
    cadastro['idade'] = int(input('Idade: '))
    cadastro['genero'] = input('Genero F/M: ').upper()[0] # []pega só a primeira letra
    while cadastro['genero'] not in 'FM':
        print('Opção inválida! Digite F ou M.')
        cadastro['genero'] = input('Genero F/M: ').upper()[0]
    
    cadastros.append(cadastro.copy())   #.copy() evita modificar o mesmo dicionário a cada iteração do loop.

    resposta = input('Deseja cadastrar outra pessoa? [S/N]: ').strip().upper()
    if resposta != 'S':
        break

print('-' * 45)   
print(f'1. Total de pessoas cadastradas: {len(cadastros)}')
print('-' * 45)

media_idade = sum(cadastro['idade'] for cadastro in cadastros) / len(cadastros)
print(f'2. Média de idade: {media_idade:.2f}')
print('-' * 45)

print('3. Mulheres cadastradas:')
for cadastro in cadastros:
    if cadastro['genero'] == 'F':
        print(f'   Nome: {cadastro["nome"]} - Idade: {cadastro["idade"]}')
print('-' * 45)

print('4. Pessoas com idade acima da média:')
for cadastro in cadastros:
    if cadastro['idade'] > media_idade:
        print(f'   Nome: {cadastro["nome"]} - Gênero: {cadastro["genero"]} - Idade: {cadastro["idade"]}')
print('-' * 45)


'''Exercício Python 095 - Aprimorando os Dicionários
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

time = []                   # lista de dicionários, cada dicionário representa um jogador

while True:
    jogador = {}            # dados dicionario: nome, qtde_jogos, gols, total_gols
    gols_por_jogo = []      # dados dicionario: qtde gols por jogo
    
    jogador['nome'] = input('Nome do Jogador: ')
    jogador['qtde_jogos'] = int(input('Quantas jogos jogou: '))

    for jogo in range (jogador['qtde_jogos']):
        qtde_gols = int(input(f'Quantos gols na partida {jogo + 1}? '))
        gols_por_jogo.append(qtde_gols)

    jogador['gols'] = gols_por_jogo
    jogador['total_gols'] = sum(gols_por_jogo)

    time.append(jogador.copy())          #.copy() evita modificar o mesmo dicionário a cada iteração do loop.
    print(f"\n{jogador['nome']}: total de {jogador['total_gols']} gols, em {jogador['qtde_jogos']} jogos.\n")

    resposta = input('Quer inserir dados de outro jogador? S/N: ').upper().strip()
    if resposta != 'S':
        break

print('\nRESULTADOS DO TIME'.center(40))
print('-' * 40)
print(f"{'ID':<4} {'JOGADOR':<15} {'JOGOS':^7} {'GOLS':^6}")

for indice, jogador in enumerate(time):
    print(f"{indice:<4} {jogador['nome']:<15} {jogador['qtde_jogos']:^7} {jogador['total_gols']:^6}")
print('-' * 40)

while True:
    indice = int(input('\nInsira o numero "ID" do jogador, para ver detalhes da performance: '))

    if indice < 0 or indice >= len(time):
        print('Erro! Jogador não encontrado.')
    else:
        print(f"\nDESEMPENHO DO JOGADOR: {time[indice]['nome']}")
        print('-' * 40)
        print(f"Total de jogos: {time[indice]['qtde_jogos']}")
        print(f"Total de gols: {time[indice]['total_gols']}")
        print(f'Média de gols por jogo: {time[indice]["total_gols"] / time[indice]["qtde_jogos"]:.2f}')
        print('-' * 40)

        print('Histórico de gols por jogo:')
        for id, gol in enumerate(time[indice]['gols']):
            print(f'Partida {id + 1}: {gol} gol(s).')
        print('-' * 40)

    resposta = input('\nQuer ver resultados de outro jogador? S/N: ').upper()
    if resposta != 'S':
        break
print('Programa finalizado.')
print()