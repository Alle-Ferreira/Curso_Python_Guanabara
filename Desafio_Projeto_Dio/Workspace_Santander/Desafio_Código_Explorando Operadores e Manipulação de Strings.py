''' Explorando Operadores e Manipulação de Strings

DESAFIO 1
Descrição:
Uma loja online deseja aplicar descontos em seus produtos com base em cupons de desconto digitados pelos clientes.

Regras de desconto:
"DESCONTO10": 10% de desconto.
"DESCONTO20": 20% de desconto.
"SEM_DESCONTO": Sem desconto.
Entrada
Preço original do produto.
Código do cupom digitado.
Saída
Preço final após aplicar o desconto. Com duas casas decimais.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
100     DESCONTO10	90.00
200     DESCONTO20	160.00
50      SEM_DESCONTO	50.00

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.
'''

# SINTAXE 1

# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}
# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()
# TODO: Aplique o desconto se o cupom for válido
if cupom == "DESCONTO10":
  desconto = preco * 0.1
elif cupom == "DESCONTO20":
  desconto = preco * 0.2
else:
  desconto = 0
preco_final = preco - desconto
print(f'{preco_final:.2f}')


# SINTAXE 2

# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}
# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()
# Aplique o desconto se o cupom for válido
if cupom in descontos:
    desconto = preco * descontos[cupom]
else:
    desconto = 0.0  # Caso o cupom não seja válido
preco_final = preco - desconto
# Saída com duas casas decimais, sem texto adicional
print(f"{preco_final:.2f}")


'''
DESAFIO 2
Descrição
Uma empresa quer validar se os e-mails cadastrados pelos usuários estão no formato correto. Crie uma função que receba um e-mail e verifique se ele é válido, seguindo as regras:

Regras para um e-mail válido:

Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
Não pode começar ou terminar com "@".
Não pode conter espaços.
Entrada
Uma string contendo o e-mail a ser validado.
Saída
"E-mail válido" se o e-mail estiver no formato correto.
"E-mail inválido" caso contrário.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
usuario@gmail.com	E-mail válido
user@outlook.com	E-mail válido
usuario gmail.com	E-mail inválido

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.
'''

# SINTAXE 1

email = input().strip()                                             # Entrada do usuário

if "@" in email and " " not in email:                               # Verifica se tem "@" e se não tem espaço
    posicao_arroba = email.index("@") 
    if posicao_arroba != 0 and posicao_arroba != len(email) - 1:    # Verifica se o "@" não está na primeira nem na última posição
        parte_dominio = email[posicao_arroba + 1:]                  # Tudo após o "@"
        if "." in parte_dominio:                                    # Verifica se existe um "." depois do "@"
            print("E-mail válido")
        else:
            print("E-mail inválido")
    else:
        print("E-mail inválido")
else:
    print("E-mail inválido")


# SINTAXE 2

email = input().strip()                                             # Entrada do usuário

if "@" in email and " " not in email:                               # Verifique as regras do e-mail:
    posicao_arroba = email.index("@")
    if posicao_arroba != 0 and posicao_arroba != len(email) - 1:    # Garante que o @ não está na primeira nem na última posição
        print("E-mail válido")
    else:
        print("E-mail inválido")
else:
    print("E-mail inválido")