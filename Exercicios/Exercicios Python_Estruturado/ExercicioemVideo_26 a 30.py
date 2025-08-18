'''
Desafio 26:
Faça um programa que leia uma frase pelo teclado e mostre 
quantas vezes aparece a letra "A", 
em que posição ela aparece a primeira vez 
e em que posição ela aparece a última vez.
'''
#Dica: rfind procura a partir da direita.

texto = input('Insira o texto a ser analisado: ').upper().strip()

print(f'A letra D aparece {texto.count('D')} vezes.')
print(f'A letra D aparece pela 1a vez na posição {texto.find('D')}.')
print(f'E aparece pela última vez na posição {texto.rfind('D')}.')        
print()

'''
Desafio 027:
Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.
'''

nome_completo = str(input('Qual o seu nome completo? ')).strip()
nomes = nome_completo.split()
print(f'Seu primeiro nome é {nomes [0]}.')
print(f'E seu último nome é {nomes [-1]}.')
print()

'''
Desafio 028:
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.

Funcionalidade extra: criar a ideia de que o computador está pensando por algum tempo.
Dica: biblioteca time, método sleep.
'''

from random import randint
from time import sleep

print('-=-' * 15)
print('Vamos jogar? \nEu vou pensar em um número entre 0 e 5, e vc tentará adivinhá-lo.')
print('Processing...')
sleep(3)

numero_computador = randint(0, 5)
numero_usuario = int(input('Tente adivinhar qual numero eu pensei: '))

if numero_computador == numero_usuario:
    print('Você me conhece bem! Leu meus pensamentos: escolheu o mesmo numero que eu!')
else:
    print(f'Você passou longe...eu pensei no numero {numero_computador}.')
print('-=-' * 15)
print()

'''
Desafio 029:
Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.

Funcionalidade extra: uso de cores
'''

velocidade_carro = float(input('A velocidade capturada pelo radar de velocidade foi de: '))

limite_velocidade = 80
multa_por_km_excedido = 7.00
excesso_velocidade = velocidade_carro - limite_velocidade
multa_por_excesso_velocidade = excesso_velocidade * multa_por_km_excedido

if velocidade_carro <= limite_velocidade:
     print('Medição dentro do limite de velocidade. Livre para seguir.')
else:
    print(f'''Voce dirigia a {velocidade_carro} km/hora, 
portanto ultrapassou o limite de velocidade permitido, de {limite_velocidade} km/hora . 
A multa pelo excesso de velocidade é de R$ {multa_por_excesso_velocidade:.2f}''')
print()


'''
Desafio 030:
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

numero_usuario = int(input('Escolha um número inteiro: '))
resto_divisao_numero = numero_usuario % 2

if resto_divisao_numero == 0:
    print('Este é um numero par.')
else:
    print('Este é um numero impar.')
print()