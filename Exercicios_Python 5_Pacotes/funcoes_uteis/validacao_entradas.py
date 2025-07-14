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