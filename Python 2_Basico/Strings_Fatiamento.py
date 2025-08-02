'''
Fatiamento em Python

Python armazena os caracteres de uma string como uma lista [],
por isto acessa por posição dentro da lista.
'''

nome = 'Alessandra Silva Ferreira'

print(nome[0])
print(nome[0:])
print()

print(nome[11:16]) 
#a ultima posição (15) deve ser identificada com um numero a mais (16)
print()

print(nome[17:])
print(nome[0:25:2])
#a ultima posição (24) deve ser identificada com um numero a mais (25)
print()


print(nome[-1]) #1a posição, de tras para frente
print(nome[-2]) #2a posição, de tras para frente
print(nome[::-1]) #toda a string, de tras para frente
print()