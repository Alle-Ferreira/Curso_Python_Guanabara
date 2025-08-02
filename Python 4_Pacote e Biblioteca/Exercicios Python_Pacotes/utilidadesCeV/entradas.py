# I - Validação das Entradas de Dados

#1. Função ler_float(entrada)

def ler_float(entrada):
    while True:
        try:
            return float(input(entrada))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número decimal válido.')


#2. Função ler_int(entrada)

def ler_int(entrada):
    while True:
        try:
            return int(input(entrada))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número inteiro válido.')


#3. Função ler_sn(entrada)

def ler_resposta(entrada):
    while True:
        resposta = input(entrada).strip().upper()
        if resposta in ('S', 'N'):
            return resposta
        print('Erro: digite apenas S ou N.')


# 4. Função para leitura de valores monetarios

def ler_moeda(entrada):
    while True:
        entrada = input(entrada).strip()
        # Remover R$, espaços e normalizar decimal
        entrada = entrada.replace('R$', '').replace('r$', '').replace(' ', '').replace('.', '').replace(',', '.')
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print('\033[31mERRO! Por favor, digite um valor monetário válido.\033[m')