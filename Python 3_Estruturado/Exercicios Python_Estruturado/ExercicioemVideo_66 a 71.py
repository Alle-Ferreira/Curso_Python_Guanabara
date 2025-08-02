'''Exercício 066 - Vários Números com Flag
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).   
'''
# SINTAXE 1
numero = 0
contagem = 0
soma = 0
while True:
    numero = int(input('Digite um número inteiro ou "999" para parar: '))
    if numero == 999:
        break
    else:
        contagem += 1
        soma = soma + numero
        resposta = input('Gostaria de informar outro numero? S/N: ').upper().strip()
        if resposta != 'S':
            break
print(f'Vc digitou {contagem} números. E a soma deles é {soma}')
print()


# SINTAXE 2
soma = 0
contagem = 0
while True:
    numero = int(input('Digite um número inteiro ou "999" para parar: '))
    if numero == 999:
        break
    contagem += 1
    soma += numero
    print(f'Vc digitou {contagem} números. E a soma deles é {soma}')
print()


'''Exercício 067 - Tabuada_v.03
Crie um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.   
'''

numero = 0
while True:
    numero = int(input('\nEscolha um número inteiro, para ver sua tabuada: '))
    if numero < 0:
        break
    print(('_.') * 10)
    for multiplicador in range (0, 11):
        print(f' {numero} * {multiplicador:2} = {numero * multiplicador}')
    print(('_.') * 10)
print('\nO programa foi interrompido, pois não é válido para numeros negativos.')


'''Exercício 068 - Jogo do Par ou Ímpar_v.04
Crie um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
'''

from random import randint

vitorias = 0
somatorio = 0

while True:
    escolha_jogador = int(input('''\nVoce prefere par ou impar?
[1] Par
[2] Impar
O que vc escolhe?   '''))
    if escolha_jogador not in [1, 2]:
        print('Escolha inválida. Programa encerrado')
        break
    else:
        numero_jogador = int(input('Agora escolha o seu numero: '))
        numero_computador = randint(0, 11)
        somatorio = numero_computador + numero_jogador
        print(f'Eu escolhi {numero_computador} e você escolheu {numero_jogador} então deu {somatorio}.')

        if (somatorio % 2 == 0 and escolha_jogador == 1) or (somatorio % 2 != 0 and escolha_jogador == 2):
            print('Voce ganhou!')
            vitorias += 1
        else:
            if vitorias > 1:
                print(f'Você perdeu deste vez! Mas teve {vitorias} vitorias.')
            elif vitorias == 1:
                print(f'Vc perdeu esta, então terminamos empatados: 1 x 1')
            else:
                print('Uau! Já perdeu!? Você é muito ruim nisto!')
            break
print()


'''Exercicio 069
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
'''

pessoas = []
pessoas = []
maior_idade = 0
homens = 0
jovens_mulheres = 0

while True:
    idade = int (input('Informe a idade do indivíduo: '))
    if idade > 18:
        maior_idade += 1

    genero = ' '
    while genero not in 'MF':
        genero = input('Informe o genero (M/F): ').upper().strip()
    if genero == 'M':
        homens += 1
    elif genero == 'F' and idade < 20:
        jovens_mulheres += 1
    
    pessoas.append({'idade': idade, 'genero': genero})

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Gostaria de continuar cadastrando pessoas? [S/N]: ').upper().strip()
    if resposta != 'S':
        break
print(f'''
Foram cadastrados {homens} homem(ns); 
Foram cadastradas {maior_idade} pessoa(s) com mais de 18 anos; 
e {jovens_mulheres} mulher(es) com idade inferior a 20 anos.''')
print()


'''Exercício Python 070 - Estatísticas em produtos
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
'''
produtos = []
custo_carrinho = 0
qte_itens_caros = 0
preco_mais_baixo = None
nome_preco_menor = ''

while True:
    print('Insira nome e preço do produto, separados por vírgula: ')
    nome, preco = input().strip().split(',')
    preco = float(preco)

    produtos.append((nome, preco))
    custo_carrinho += preco

    if preco > 1000:
        qte_itens_caros += 1
        
    if preco_mais_baixo is None or preco < preco_mais_baixo:
        preco_mais_baixo = preco
        nome_preco_menor = nome

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Gostaria de continuar cadastrando pessoas? [S/N]: ').upper().strip()
    if resposta != 'S':
        break

print('\nResumo do Carrinho:')
print(f'Total gasto: R${custo_carrinho:.2f}')
print(f'Produtos que custam mais de R$1000: {qte_itens_caros}')
print(f'Produto mais barato: {nome_preco_menor} - R$ {preco_mais_baixo:.2f}')


'''Exercício 071 - Simulador de Caixa Eletronico
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
'''
def notas_100(valor_saque):
    qtde_notas_100 = int(valor_saque // 100)
    residual_100 = valor_saque % 100
    print(f'Notas de cem: {qtde_notas_100}')

    if residual_100 >= 50:
        valor_saque = residual_100
        notas_50(valor_saque)
    return(valor_saque)

def notas_50(valor_saque):
    qtde_notas_50 = int(valor_saque // 50)
    residual_50 = valor_saque % 50
    print(f'Notas de cinquenta: {qtde_notas_50}')

    if residual_50 >= 10:
        valor_saque = residual_50
        notas_10(valor_saque)
    return(valor_saque)

def notas_10(valor_saque):
    qtde_notas_10 = int(valor_saque // 10)
    residual_10 = valor_saque % 10
    print(f'Notas de dez: {qtde_notas_10}')

    if residual_10 >= 5:
        valor_saque = residual_10
        notas_5(valor_saque)
    else:
        valor_saque = residual_10
        notas_1(valor_saque)
    return(valor_saque)

def notas_5(valor_saque):
    qtde_notas_5 = int(valor_saque // 5)
    residual_5 = valor_saque % 5
    print(f'Notas de cinco: {qtde_notas_5}')

    if residual_5 >= 1:
        valor_saque = residual_5
        notas_1(valor_saque)
    return(valor_saque)

def notas_1(valor_saque):
    qtde_notas_1= int(valor_saque // 1)
    print(f'Notas de um: {qtde_notas_1}')
    return(valor_saque)

residual = 0
valor_saque = int(input('Informe o valor a sacar: '))

if valor_saque >= 100:
    notas_100(valor_saque)
elif 50 <= valor_saque < 100:
    notas_50(valor_saque)
elif 10 <= valor_saque < 50:
    notas_10(valor_saque)
elif 5 <= valor_saque < 10:
    notas_5(valor_saque)
else:
    notas_1(valor_saque)

