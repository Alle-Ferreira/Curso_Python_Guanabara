'''
Exercício 041:
Programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER
Cliente: Confederação Nacional de Natação
'''

from datetime import date

ano_nascimento = int(input('Em qual ano nasceu o atleta (formato aaaa)? ' ))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <=9:
    print(f'Você tem {idade} anos. Sua classificação: Mirim')
elif 9 < idade <= 14:
    print(f'Você tem {idade} anos. Sua classificação: Infantil')
elif 14 < idade <= 19:
    print(f'Você tem {idade} anos. Sua classificação: Júnior')
elif 19 < idade <= 25:
    print(f'Você tem {idade} anos. Sua classificação: Sênior')
else:
    print(f'Você tem {idade} anos. Sua classificação: Master')
print()



'''
Exercício 042:
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes
'''

print('-=-'* 16)
print('Verificador de Triangulo'.center(48))
print('-=-'* 16)

segmento_a= float(input('Qual o tamanho do segmento A, em centimetros? '))
segmento_b = float(input('Qual o tamanho do segmento B, em centimetros? '))
segmento_c= float(input('Qual o tamanho da segmento C, em centimetros? '))

if (segmento_a < (segmento_b + segmento_c)) and (segmento_b < (segmento_a + segmento_c)) and (segmento_c < (segmento_a + segmento_b)):
    print('Estas retas podem formar um triangulo.')
    if segmento_a == segmento_b == segmento_c:
        print('Este é um triangulo equilátero.')
    elif segmento_a == segmento_b or segmento_a == segmento_c or segmento_c == segmento_b:
        print('Este é um triangulo isósceles.')
    else:
        print('Este é uma triangulo escaleno.')
else:
    print('Estas retas não podem formar um triangulo.')
print()


'''
Exercicio 043 - Indice de Massa Corporal (IMC)
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC), 
e mostre seu status de acordo com a tabela abaixo:

IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 24,9: Peso Ideal
25 até 29,9: Sobrepeso
30 até 39,9: Obesidade
Acima de 40: Obesidade Mórbida

Parametro: IMC = peso (em kg) / (altura (em metros)²). 
Explicação:
- Peso (em kg): A massa corporal da pessoa em quilogramas.
- Altura (em metros): A altura da pessoa em metros.
- Altura (em metros)²: A altura elevada ao quadrado (altura x altura). 
'''

peso = float(input('Qual o seu peso atual? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)

print(f'Seu indice de massa corporal é {imc: .2f}')

if imc < 18.5: 
    print('Você está abaixo do peso ideal para sua altura.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal para sua altura.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Seu IMC é considerado obesidade. Seria melhor você emagrecer um pouquinho...')
else:
    print('Seu peso é considerado obesidade mórbida. Cuidado!')
print()


'''
Exercicio 044
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros
'''
compras = 4500.00
desconto_avcartão = -0.05
desconto_avcheqdinheiro = -0.10
juros_parcelado2x = 0.00
juros_parcelado3x = 0.20

print('-=-' * 22)
print('Loja online - Pagamento'.center(66))
print('-=-' * 22)
print(f'''
Suas compras totalizam R$ {compras}. Escolha se método de pagamento:

[1] Pagto à vista, no cartão de crédito: {- desconto_avcartão * 100}% de desconto
[2] Pagto à vista, em dinheiro ou cheque: {- desconto_avcheqdinheiro * 100}% de desconto
[3] Pagto parcelado, em até 2x: {juros_parcelado2x * 100}% juros
[4] Pagto parcelado, a partir de 3x: {juros_parcelado3x * 100}% juros\n''')

meio_pagto = int(input('Forma de pagamento: '))
pagto2x = compras + (compras * juros_parcelado2x)
pagto3x = compras + (compras * juros_parcelado3x)

if meio_pagto not in range (1, 5):          # o ultimo marcador do range é ignorado.
    print('Opção inválida.') 
elif meio_pagto == 1:
    print(f'O valor total a pagar é R$ {compras + (compras * desconto_avcartão): .2F}')
elif meio_pagto == 2:
    print(f'O valor total a pagar é R$ {compras + (compras * desconto_avcheqdinheiro): .2F}')
else:
    parcelas = int(input('Em quantas vezes você quer parcelar suas compras? '))
    if parcelas <= 2:
        print(f'O valor total a pagar é R$ {pagto2x: .2F}, dividido em {parcelas} parcelas de R$ {(pagto2x / parcelas): .2F}.')
    else:          
        print(f'O valor total a pagar é R$ {pagto3x: .2F}, dividido em {parcelas} parcelas de R$ {(pagto3x / parcelas): .2F}.')
print()
print('-=-' * 22)
print()

'''
Exercicio 045 - Pedra Papel Tesoura
Programa para jogar Jokenpô.
Regras: pedra quebra tesoura, tesoura corta papel, papel embrulha pedra.
'''

#Sintaxe 1

from time import sleep
from random import randint

escolhas = [(1, 'pedra'), (2, 'papel'), (3, 'tesoura')]             # Lista de opções com números

print('''
Ola! 
Agora nós vamos jogar Jokempô. 
Sabe qual é este jogo? É aquele do "pedra, papel e tesoura."\n
Você pode fazer sua opção, escolhendo pelo número:''')

for numero, nome in escolhas:
    print(f'[{numero}] {nome}')

print('\nQuando eu contar 3, cada um faz sua escolha, combinado?')
print('1..')
sleep(2)
print('2..')
sleep(2)
print('3..')

escolha_usuario = int(input('Sua escolha: '))                       # Entrada do jogador   
escolha_computador = randint(1, 3)                                  # "Entrada" do computador

for numero, nome in escolhas:                                       # Identifica o 'nome' da escolha do computador
    if numero == escolha_computador:
        nome_escolha_computador = nome
        break

if escolha_usuario not in range (1, 4):                             # Verifica se foi uma escolha válida
    print('Escolha inválida. Tente novamente.\n')
elif escolha_usuario == escolha_computador:                   
    print(f'Eu também escolhi {nome_escolha_computador}! Empate!')
else:
    print(f'Eu escolhi {nome_escolha_computador}.')
    if escolha_usuario == 1:
        if escolha_computador == 3:
            print(f'Você venceu! A pedra quebra a tesoura.' )
        elif escolha_computador == 2:
            print(f'Então você perdeu...o papel embrulha a pedra.')
    elif escolha_usuario == 2:
        if escolha_computador == 1:
            print(f'Parabéns! Ganhou! O papel embrulha a pedra.')
        elif escolha_computador == 3:
            print(f'Então você perdeu...a tesoura corta o papel.')
    else:
        if escolha_computador == 1:
            print(f'Então você perdeu...a pedra quebra a tesoura.')
        elif escolha_computador == 2:
            print(f'Você ganhou! A tesoura corta o papel')
print()



#Sintaxe 2: limitada a posição dos itens numa lista:

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint (0, 2)

print(
''' Suas opçoes:
[0] Pedra
[1] Papel
[2] Tesoura
''')

jogador = int(input('Qual é a sua jogada? '))
print(f'Jogador jogou {itens[jogador]}.')                # a variavel 'jogador' tem um numero atribuido, que corresponderá a uma posição na lista.
print(f'Computador jogou {itens[computador]}.')          # a variavel 'computador' tem um numero atribuido, que corresponderá a uma posição na lista.