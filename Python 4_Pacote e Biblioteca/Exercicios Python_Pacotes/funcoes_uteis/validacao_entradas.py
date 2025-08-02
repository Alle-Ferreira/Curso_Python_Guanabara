# I - Validação das Entradas de Dados

#1. Função ler_float(entrada)

def ler_float(entrada):
    while True:
        try:
            return float(input(entrada))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número decimal válido.')
        except KeyboardInterrupt:
            print('\033[31mErro: entrada de dados interrompida pelo usuário.\033[0m')  

#2. Função ler_int(entrada)

def ler_int(entrada):
    while True:
        try:
            return int(input(entrada))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('\033[31mErro: entrada de dados interrompida pelo usuário.\033[0m')  


# 3. Função para leitura de valores monetarios

def ler_moeda(entrada):
    while True:
        entrada = input(entrada).strip()
        # Remover R$, espaços e normalizar decimal
        entrada = entrada.replace('R$', '').replace('r$', '').replace(' ', '').replace('.', '').replace(',', '.')
        try:
            valor = float(entrada)
            return valor
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('\033[31mErro: entrada de dados interrompida pelo usuário.\033[0m')  


#4. Função verificação sim/não: valida limitando as entradas aceitas (S/N)

def ler_resposta(entrada):
    while True:
        resposta = input(entrada).strip().upper()
        if resposta in ('S', 'N'):
            return resposta
        print('Erro: digite apenas S ou N.')
