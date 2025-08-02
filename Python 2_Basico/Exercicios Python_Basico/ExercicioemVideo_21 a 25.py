'''
Desafio 21:
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
1. Necessário baixar uam biblioteca EXTERNA ao Python, pelo Terminal: pip install pygame (feito)
2. O arquivo MP3 precisa estar na mesma pasta.

APARENTEMENTE OS ARQUIVOS ESTÃO EM LUGAR DIVERSO DE ONDE RODA O PYTHON

import pygame
import os

pygame.init()

caminho_mp3 = os.path.join(os.path.dirname('d:/3. Cursos/Estacio/Liguagens com Python/CursoemVideo_Guanabara/Python_Estruturado'), 'alone-296348.mp3')

pygame.mixer.music.load(caminho_mp3)
pygame.mixer.music.play()
pygame.event.wait()
'''

'''
Desafio 022:
Crie um programa que leia o nome completo de uma pessoa e mostre: 
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.
'''

nome_completo = input('Qual sem nome e sobrenome? ')

print(f'O nome em letras maisculas: {nome_completo.upper()}.')
print(f'O nome em letras maisculas: {nome_completo.lower()}.')

qtdade_espaco_nome = nome_completo.count(' ')
print(f'Seu nome inteiro tem {len(nome_completo) - qtdade_espaco_nome} letras.')     # Excluí os espaços na contagem

nomes = nome_completo.split()
print(f'Seu primeiro nome é {nomes[0]}, e tem {len(nomes[0])} letras.') 
print()


'''
Desafio 023:
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''
# Sintaxe 1
numero = int(input('Digite um numero entre 1 e 9999? '))

milhar = numero // 1000
sobra_milhar= numero % 1000

centena = sobra_milhar // 100
sobra_centena = sobra_milhar % 100

dezena = sobra_centena // 10
sobra_dezena = sobra_centena % 10

unidade = sobra_dezena

print(milhar)
print(centena)
print(dezena)
print(unidade)
print()

# Sintaxe 2
numero = int(input('Digite um numero entre 1 e 9999? '))

milhar = numero // 1000 % 10
centen = numero // 100 % 10
dezena = numero // 10 % 10
unidad = numero // 1 % 10

print(milhar)
print(centena)
print(dezena)
print(unidade)
print()


'''
Desafio 024:
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''
#Sintaxe 1:
cidade_natal = input('Em qual cidade você nasceu? ').upper().strip()
if 'SANTO' in cidade_natal[:5]:
    print('Temos vários santos nas cidades brasileiras, não acha?')
else:
    print('Sua cidade não tem santo...que pena!')

#Sintaxe 2: 
cidade = input('Em qual cidade você nasceu? ').strip()
print(cidade[:5].upper() == 'SANTO')
print()


'''
Desafio 025:
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''
#Sintaxe 1:
nome_completo = 'Gleison Oliveira'
print(nome_completo)
if 'Silva' in nome_completo:
    print('Voce tambem é da família Silva!')
else:
    print('Nao somos da mesma familia...')
print()

#Sintaxe 2:
nome = input('Qual o seu nome completo?').strip()
print(f'Seu nome tem Silva? {'SILVA' in nome.upper()}')
print()