'''
Aula 014 - Estruturas Eepetição: WHILE

- Repetição com teste lógico
- Repete até alcançar a condição (obrigatória)

while not apple:
    if floor:
        step
    if no floor:
       jump
    if coin:
        pick up
pick up apple
'''

# Exemplo 1: com limite (pode usar for/in ou while)

inicio = 1
while inicio < 10:
    print('Inicio')
    inicio = inicio + 1
print('fim do intervalo', '\n')


# Exemplo 2: sem limite (somente while)

for repeticao in range(1, 4):           #nr de repetições limitado
    numero = int(input('Digite um numero: '))
    if numero == 7:
        print('Acertou! Este é o meu numero favorito!')    
    else:
        print('Errou!')
        if repeticao < 3:
            print('Vamos tentar novamente? ')
print('fim', '\n')


numero1 = 0
while numero1 != 9:                                 #while: nr de repetições ilimitado
    numero1 = int(input('Digite um numero: '))
    if numero1 == 9:
        print('Acertou! Este é o meu numero favorito!')
    else:
        print('Errou! Tente novamente.')    
print('fim', '\n')


fruta = 'o'
resposta = 's'
while fruta != 'uva' and resposta in ('s', 'sim'):
    fruta = input('Qual a minha fruta favorita? ').strip().lower()     #remove espaços, deixa em minúsculo
    if fruta !='uva':
        resposta = input('A minha não é esta. Quer tentar adivinhar? [s/n] ').strip().lower()  
    else:
        print('Acertou! Esta é a minha fruta favorita! Até a próxima.')
print('fim', '\n')


numeros = 1
par = impar = 0
while numeros != 0:
    numeros = int(input('Digite um numero: '))
    if numeros % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Voce digitou {par} numeros pares, e {impar} numeros impares', '\n')