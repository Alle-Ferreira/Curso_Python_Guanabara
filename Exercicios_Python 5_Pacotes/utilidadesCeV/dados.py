# I - Validação das Entradas de Dados

#1. Função leia_float(msg)
def leia_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print('Erro: por favor, digite um número decimal válido.')


#2. Função leia_int(msg)
def leia_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('Erro: por favor, digite um número inteiro válido.')


#3. Função leia_sn(msg)
def leia_resposta(msg):
    while True:
        resposta = input(msg).strip().upper()
        if resposta in ('S', 'N'):
            return resposta
        print('Erro: digite apenas S ou N.')


# 4. Função para leitura de valores monetarios
def leia_Dinheiro(msg):
    while True:
        entrada = input(msg).strip()
        # Remover R$, espaços e normalizar decimal
        entrada = entrada.replace('R$', '').replace('r$', '').replace(' ', '').replace('.', '').replace(',', '.')
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print('\033[31mERRO! Por favor, digite um valor monetário válido.\033[m')