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