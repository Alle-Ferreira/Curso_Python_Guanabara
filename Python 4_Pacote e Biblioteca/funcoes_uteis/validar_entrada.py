'''I - Validação das Entradas de Dados

def ler_float(entrada)
def ler_int(entrada)
def ler_moeda(entrada)          função para leitura de valores monetarios
def ler_resposta(entrada)       função verificação S/N (valida limitando as entradas aceitas)
def ler_int_cor(entrada)        valida entrada de numero inteiro, com resposta de erro colorida
'''

cores = {                             # Melhor declarar como variavel global, fora das funções.
'padrao': '\033[m',
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

def ler_float(entrada):
    while True:
        try:
            return float(input(entrada))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número decimal válido.')
        except KeyboardInterrupt:
            print('\033[31mErro: entrada de dados interrompida pelo usuário.\033[0m')  

def ler_int(entrada):
    while True:
        try:
            return int(input(entrada))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número válido.')
        except KeyboardInterrupt:
            print('\033[31mErro: entrada de dados interrompida pelo usuário.\033[0m') 

def ler_moeda(entrada):            
    while True:
        entrada = input(entrada).strip()
        # Remover R$, espaços e normalizar decimal
        entrada = entrada.replace('R$', '').replace('r$', '').replace(' ', '').replace('.', '').replace(',', '.')
        try:
            valor = float(entrada)
            return valor
        except (ValueError, TypeError):
            print('Erro: por favor, digite um valor válido.')
        except KeyboardInterrupt:
            print('\033[31mErro: entrada de dados interrompida pelo usuário.\033[0m')  

def ler_resposta(entrada):
    while True:
        resposta = input(entrada).strip().upper()
        if resposta in ('S', 'N'):
            return resposta
        print(f'\n{cores["vermelho"]}Erro: digite apenas S ou N.{cores["padrao"]}')

def ler_int_cor(entrada):
    while True:
        try:
            return int(input(entrada))
        except (ValueError, TypeError):
            print(f'{cores["vermelho"]}Por favor, digite um número válido.{cores["padrao"]}')
        except KeyboardInterrupt:
            print(f'\n{cores["vermelho"]}Erro: entrada de dados interrompida pelo usuário.{cores["padrao"]}')
            return 0
