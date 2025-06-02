#Exercício 3

nome = input ('Digite seu nome, por favor: ')
sobrenome = input('Agora digite seu sobrenome: ')
print(f'Olá, {nome} {sobrenome}. Gostei do seu nome!')
print()

numero1 = int (input ('Digite valor: '))
numero2 = int (input('Digite outro valor: '))
soma = numero1 + numero2
print(f'A soma entre {numero1} e {numero2} é igual a {soma}')
print()

#Exercício 4

senha = input('Digite sua senha com letras e números, ' \
'sem espaços, e com a primeira letra maiúscula: ')

print('É alfanumerica?', senha.isalnum())
print('Tem espaços?', senha.isspace())
print('A primeira letra é maiúcula?', senha.istitle())
print()

'''Desafio 004:
Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo,
e todas as informações possiveis sobre ele.
'''

idade = input('Quantos anos ele tem? ')
print(type(idade))
print(idade.isnumeric())
print(idade.isalpha())
print(idade.isalnum())
print(idade.isdecimal())
print(idade.isprintable())
print(idade.isidentifier())
print(idade.istitle())
print()

'''
Desafio 005:
Faça um programa que leia um numero inteiro, 
e mostre na tela o seu sucessor e o seu antecessor.
'''
idade = int(input('Quantos anos voce tem? '))
idade_2026 = (idade + 1)
idade_2024 = (idade - 1)

print(f'Em 2024 vc tinha {idade_2024} anos.')
print(f'E em 2026 vc terá {idade_2026} anos.')
print()