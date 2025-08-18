'''
Exercicio 046 - Contagem Regressiva
Programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0, com uma pausa de 1 segundo entre eles.
'''

#Sintaxe 1
from time import sleep

contador = 10

while contador > 0:
    print(contador)
    contador = contador - 1
    sleep(1)
print('Pow! Pow! Bum, bum!')
print()

#Sintaxe 2
#from time import sleep

for contador2 in range (10, -1, -1):  
    print(contador2)
    sleep(1)
print('Pow! Pow! Bum, bum!')
print()
#Para mostrar o '0' é necessário incluir o '-1' na posição final, pq o ultimo do range é ignorado.
#Para mostrar regressivo, necessário incluir '-1' tbm.

'''
Exercicio 047- Contagem de Pares
Programa que mostre na tela todos os numeros pares, no intervalo entre 1 e 50.
'''

#Sintaxe 1: Conta qtos são.
contador = 0
for pares in range (1, 51):
    if pares % 2 == 0:
        contador += 1
print(contador)
print()


#Sintaxe 2: Mostra quais sao
for pares in range (1, 51):
    if pares % 2 == 0:
        print(pares, end = ', ')   #exibe numeros na mesma linha, separados por ', '
print()


#Sintaxe 3: Pula de 2 em 2
for pares in range (2, 51, 2):     #inicia já no 1o numero par, e vai de de 2 em 2.
    print(pares, end = ', ')  
print()


'''
Exercicio 048_A - Soma multiplos de 3
Programa que calcule a soma entre todos os numeros multiplos de 3, e que se encontrem no intervalo entre 1 e 500.
'''

#Sintaxe 1:
soma_trio = 0

for trio in range (0, 501):
    if trio % 3 == 0:
        soma_trio += trio
print(soma_trio)
print()

#Sintaxe 2: Pula de 3 em 3
soma_triade = 0

for triade in range (0, 501, 3):
    soma_triade += triade
print(soma_triade)
print()


'''
Exercicio 048_B - Soma impares, multiplos de 3
Programa que calcule a soma entre todos os numeros IMPARES, multiplos de 3, e que se encontrem no intervalo entre 1 e 500.
'''

#Sintaxe 1:
soma_trio = 0

for trio in range (1, 501):
    if trio % 3 == 0 and trio % 2 == 1:
        soma_trio += trio
print(soma_trio)
print()

#Sintaxe 2: Pula de 3 em 3
soma_triade = 0

for triade in range (3, 501, 3):        #Lembrete: deve iniciar no primeiro objeto procurado ('3')
    if triade % 2 == 1:
        soma_triade += triade
print(soma_triade)
print()

#Sintaxe 3: separa os numeros pares logo no range
soma_triplos = 0

for triplos in range (1, 501, 2):       #como começa no 1, pulando de 2 em 2, serão somente impares.
    if triplos % 3 == 0:
        soma_triplos += triplos
print(soma_triplos)


'''
Exercicio 049 - Tabuada_v.02
Refaça o DESAFIO 009 - Tabuada_v.01, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for:
'''

numero = int(input('Escolha um número inteiro, para ver sua tabuada: '))
print()

print(('_.') * 10)
for multiplicador in range (0, 11):
    print(f' {numero} * {multiplicador:2} = {numero * multiplicador}')
print(('_.') * 10)
print()


'''
Exercicio 050 - Soma dos Pares
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

soma_numeros = 0
count_pares = 0

for numeros in range (0, 6):
    numero = int(input('Escolha um número inteiro: '))
    if numero % 2 == 0:
        soma_numeros += numero
        count_pares += 1
print(f'''
Você digitou {count_pares} numeros pares.
A soma dos numeros pares digitados é igual a {soma_numeros}.''')
print()