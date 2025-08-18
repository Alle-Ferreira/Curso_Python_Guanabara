'''Funções em Python_2

Exercício Python 101 - Funções para Votação
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL (a partir de 65 anos) e OBRIGATÓRIO (acima de 18 anos) nas eleições.'''

from datetime import datetime

def idade_voto(ano_nascimento):
    data_atual = datetime.now()
    idade = data_atual.year - ano_nascimento
    if 18 <= idade <= 64:
        status = 'Voto Obrigatório'
    elif idade < 18:
        status = 'Voto Negado'
    else:
        status = 'Voto Opcional'
    return status


# Programa principal
ano_nascimento = int(input('Informe seu ano de nascimento: '))
status = idade_voto(ano_nascimento)
print(f'Status atual para a proxima votação: {status}')


'''Exercício Python 102 - Função para Fatorial
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def calculo_fatorial(numero=1, show='N'):
    fator = 1
    for contador in range(numero, 0, -1):
        if show == 'S':
            print(f'{contador} * {fator} = ({fator * contador})')
        fator *= contador
    return fator

numero = int(input('Insira o numero a ser calculado: '))
show = input('Quer vizualizar o calculo executado? Se sim, responda "S": ').strip().upper()
calculo_fatorial(numero, show)

print(f'O fatorial de {numero} é igual a {calculo_fatorial(numero)}')


'''Exercício Python 103 - Ficha do Jogador
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''

def ficha_jogador(nome='Nome não informado', gols=0):
    print(f'Nome do Jogador: {nome}')
    print(f'Total de gols: {gols}\n')


ficha_jogador('João')
ficha_jogador('João', 2)
ficha_jogador(gols=2)
ficha_jogador()


'''Exercício Python 104 - Validando entrada de dados em Python
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''

def leiaInt(entrada):                   # Define a função com um parâmetro (como o input faz)
    while True:                         # Laço infinito até o usuário acertar
        valor = input(entrada)          # Pede o valor ao usuário
        try:
            numero = int(valor)         # Tenta converter para inteiro
            return numero               # Se conseguir, retorna o número
        except ValueError:              # Se der erro, retorna o erro
            print('Erro: por favor, digite um número inteiro válido.')


# Programa principal
numero = leiaInt('Digite um numero inteiro: ')
print(f'Você digitou o número {numero}.')


'''Exercício Python 105 - Analisando e gerando Dicionários 
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
- Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''

def leia_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print('Erro: por favor, digite um número decimal válido.')

def avaliar_aluno(nota_final):  # Chamada dentro da função de cadastrar_notas: define a situacao_aluno.
    '''Define a situação do aluno, em função de sua nota_final'''
    if nota_final >= 7:
        return 'Aprovado'
    elif nota_final < 5:
        return 'Reprovado'  
    else:
        return 'Recuperação'

def cadastrar_notas():          # Retorna uma lista com os registros da turma de alunos.         
    '''Coleta nome, notas e a situação de vários alunos em um dicionário. 
    Depois insere cada dicionario na lista de registros_turma,
    e retorna a lista para o programa principal'''

    registros_turma = []

    while True:
        registro_aluno = {}

        registro_aluno['nome_aluno'] = input('Nome do aluno: ')
        registro_aluno['nota_final'] = leia_float('Nota final do aluno: ')
        registro_aluno['situacao_aluno'] = avaliar_aluno(registro_aluno['nota_final'])     #chama função avaliação_aluno()
        registros_turma.append(registro_aluno)      # armazena odicionario, com os dados do aluno, numa lista.

        resposta = input('Para cadastrar outro aluno digite "S": ').strip().upper()
        if resposta != 'S':
            break

    return registros_turma

def avaliar_turma(registros_turma):     # Recebe a lista com dados para avaliar resultados globais da turma.
    '''
    Recebe a lista registros_turma, com nomes e notas de todos os alunos.
    Verifica inicialmente se existem dados suficientes para analise, evitando ERRO na função.
    Define media, maior e menor notas.
    Retorna todas as informações da turma.
    '''
    if not registros_turma:
        print("Nenhum aluno foi registrado.")
        return

    notas = [aluno['nota_final'] for aluno in registros_turma]
    maior_nota = max(notas)
    menor_nota = min(notas)
    media_turma = sum(notas) / len(notas)

    alunos_aprovados = sum(aluno['situacao_aluno'] == 'Aprovado' for aluno in registros_turma)
    alunos_reprovados =sum(aluno['situacao_aluno'] == 'Reprovado' for aluno in registros_turma)
    alunos_recuperacao =sum(aluno['situacao_aluno'] == 'Recuperação' for aluno in registros_turma)

    return {
    'media': media_turma,
    'maior': maior_nota,
    'menor': menor_nota,
    'aprovados': alunos_aprovados,
    'reprovados': alunos_reprovados,
    'recuperacao': alunos_recuperacao}


# Main Program
registros_turma = cadastrar_notas()                 # registros_turma armanezará o retorno da função chamada: cadastrar_notas()
resultados = avaliar_turma(registros_turma)         # resultado armanezará o retorno da função chamada: avaliar_turma   
if resultados:                                      # Garante que não está vazio / None
    print(f"Foram avaliados {len(registros_turma)} alunos, com nota média de {resultados['media']:.2f}.")
    print(f"A maior nota foi {resultados['maior']:.2f}, e a menor nota foi {resultados['menor']:.2f}.")
    print(f"""O resultados dos alunos foram: {resultados['aprovados']} aprovado(s); {resultados['reprovados']} reprovado(s); e {resultados['recuperacao']} em recuperação.""")
else:
    print("Nenhum dado para exibir.")



'''Exercício Python 106 - Sistema interativo de ajuda em Python
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.'''    

cores = {                                   # Variável Global: declarar fora da função
    'sem cor': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxo': '\033[35m',
    'ciano': '\033[36m',
    'negrito': '\033[1m',
    'fundo_azul': '\033[44m',
    'fundo_verde': '\033[42m',
    'fundo_amarelo': '\033[43m',
}

def formatar_titulos(titulo, cor=0):
    tamanho = len(titulo) + 10
    print(cores['fundo_amarelo'], end='')
    print('-' * (tamanho))
    print(f'{titulo.center(tamanho)}')
    print('-' * (tamanho))
    print(cores['sem cor'], end='')

def acessar_help(comando):
    print(f'Documentação sobre o o comando/biblioteca {comando}:')
    help(comando)          # "help" acessa o pyhelp.


# Main Program
comando = ''
while True:
    formatar_titulos('Sistema de Ajuda com PyHelp')
    comando = input('Buscar função/biblioteca: ')
    if comando.upper() == "FIM":
        break
    else:
        acessar_help(comando)
formatar_titulos('Até Logo!')