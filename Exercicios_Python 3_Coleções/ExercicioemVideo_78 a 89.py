'''
Listas em Python


Exercício 078 - Maior e Menor valores na Lista

Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

numeros = []

for numero in range(5):
    numero = int(input('Insira o número: '))
    numeros.append(numero)
print(f'Os valores digitados foram {sorted(numeros)}')

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f'O maior valor da lista é o numero {maior_numero}, e sua posição na lista é {numeros.index(maior_numero)}')
print(f'O menor valor da lista é o numero {menor_numero}, e sua posição na lista é {numeros.index(menor_numero)}')
print()

'''
Exercicio 079 - Valores Únicos em uma Lista
Crie um programa onde o usuário possa digitar vários valores e cadastre-os em uma lista. Não deve aceitar valores duplicados. No final, mostre a lista de valores únicos digitados, em ordem crescente.'''

numeros_2 = []

resposta = 'S'                                          # Sintaxe 1
while resposta == 'S':                              
    numero = int(input('Insira o número: '))
    if numero not in numeros_2:
        numeros_2.append(numero)
    else:
        print('Este número já existe na lista.')
    resposta = input('Quer digitar outro numero? S/N: ').upper()
print(sorted(numeros_2))
print()


while True:                                             # Sintaxe 2
    numero = int(input('Insira o número: '))
    if numero not in numeros_2:
        numeros_2.append(numero)
    else:
        print('Este número já existe na lista.')
    resposta = input('Quer digitar outro numero? S/N: ').upper()
    if resposta != 'S':
        break
print(sorted(numeros_2))
print()

'''
Exercicio 080 - Lista Ordenada
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

numeros = []

for numero in range(5):
    numero = int(input('Insira o número: '))
    if len(numeros) == 0:           # Qdo lista vazia
        numeros.append(numero)
    elif numero > numeros[-1]:      # Qdo maior que o ultimo numero
        numeros.append(numero)
    else:
        posicao = 0
        while posicao < len(numeros):
            if numero <= numeros[posicao]:
                numeros.insert(posicao, numero)
                break
            posicao += 1
print(numeros)

'''
Exercicio 081 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

numeros_1 = []
contador = 0

while True:                                            
    numero = int(input('Insira o número: '))
    numeros_1.append(numero)
    contador += 1
    resposta = input('Quer digitar outro numero? S/N: ').upper()
    if resposta != 'S':
        break
    
print(f'Voce digitou {contador} numeros.')
print(sorted(numeros_1, reverse=True))

if 5 in numeros_1:
    print('O numero 5 está na lista')
else:
    print('O numero 5 não está na lista')
print()


'''
Exercicio 082 - Dividindo Valores em Várias Listas
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
numeros = []
numero_par = []
numero_impar = []

while True:                                            
    numero = int(input('Insira o número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        numero_par.append(numero)
    else:
        numero_impar.append(numero)
    resposta = input('Quer digitar outro numero? S/N: ').upper()
    if resposta != 'S':
        break
print(sorted(numeros))
print(sorted(numero_par))
print(sorted(numero_impar))
print()

'''
Exercicio 083 - Validando Expressões Matemáticas
Crie um programa que vai ler uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
expressao = input('Digite uma expressão matemática: ')
pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')           # Abre um parêntese, adiciona.
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()             # Fecha um parêntese, excluindo o par deste.
        else:
            pilha.append(')')       # Fecha sem ter aberto -> erro
            break

if len(pilha) == 0:
    print('A expressão está válida!')
else:
    print('A expressão está inválida!')


'''
Exercicio 084 - Lista Composta e Análise de Dados
Crie um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista composta. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Um lista com as pessoas mais pesadas.
C) Uma lista com as pessoas mais leves.
'''
pessoas = []
pessoa = []
maior_peso = []
menor_peso = []
contador = 0
peso_total = 0

while True:  
    pessoa.append(input('Nome: '))                        
    peso = (float(input('Peso: ')))
    pessoa.append(peso)
    peso_total += peso

    pessoas.append(pessoa[:])               # [:] faz cópia dos dados da pessoa na lista pessoas
    pessoa.clear()                          # esvazia a lista pessoa, p/receber dados da proxima pessoa
    contador += 1

    resposta = input('Quer digitar outro numero? S/N: ').upper()
    if resposta != 'S':
        break

peso_medio = peso_total / len(pessoas)

for pessoa in pessoas:
    if pessoa[1] > peso_medio:              # referencia ao peso
        maior_peso.append(pessoa[0])
    else:
        menor_peso.append(pessoa[0])

print(f'\nTotal de pessoas cadastradas: {contador}')
print(f'Peso médio: {peso_medio:.2f} kg')
print(f'Pessoas com peso acima da média: {maior_peso}')
print(f'Pessoas com peso abaixo ou igual à média: {menor_peso}')
print()


'''
Exercicio 085 - Listas com pares e ímpares
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
numeros = []
numeros_pares = []
numeros_impares = []

for numero in range(7):
    numero = int(input('Insira o número: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)       

print(sorted(numeros_pares))                    # ordena a lista e dps exibe
print(sorted(numeros_impares))                  # ordena a lista e dps exibe

numeros.append(numeros_pares)                   # insere a lista dentro da lista 'numeros'
numeros.append(numeros_impares)                 # insere a lista dentro da lista 'numeros'
print(numeros)

'''
Exercicio 086 - Matriz em Python
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com números lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''
matriz = []
objeto = []

while len(matriz) < 3:
    for numero in range(3):
        numero = int(input('Insira um número: '))
        objeto.append(numero)

    matriz.append(objeto[:])
    objeto.clear()
print()  

print('Matriz resultante:'.center(15))
for objeto in matriz:
    for valor in objeto:
        print(f'[{valor:^3}]', end='')  # Valor centralizado em 5 espaços
    print()                             # muda de linha, apos exibir cada linha da tabela
print()


'''
Exercicio 087 - Mais sobre Matriz em Python
Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
matriz = []
objeto = []
soma_pares = 0
soma_coluna3 = 0

while len(matriz) < 3:
    for numero in range(3):
        numero = int(input('Insira um número: '))
        objeto.append(numero)
        if numero % 2 == 0:
            soma_pares += numero
    matriz.append(objeto[:])
    objeto.clear()
print()

print('Matriz resultante:'.center(15))
for objeto in matriz:
    for valor in objeto:
        print(f'[{valor:^3}]', end='')  # Valor centralizado em 5 espaços
    print()                             # muda de linha, apos exibir cada linha da tabela
print()

for lista in matriz:                    # percorre cada lista/linha da matriz e pega o elemento na posição 2:
    soma_coluna3 += lista[2]
print(f'A soma dos valores da terceira coluna é {soma_coluna3}')

maior_valor_2alinha = max(matriz[1])
print(f'O maior valor da segunda linha é {maior_valor_2alinha}')

print(f'O somatório dos numeros pares digitados é {soma_pares}')  
print()

'''
Exercicio 088 - Palpites para a Mega Sena
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint

jogos = []

nr_jogos = int(input('Quantos jogos você que fazer? '))

for numero in range(nr_jogos):
    # lista palpite, vazia dentro do 1o laço (for): é limpa sempre q sai do 2o laço (while)
    palpite = []  

    while len(palpite) < 6:
        numero = randint(1, 60)
        if numero not in palpite:
            palpite.append(numero)
    palpite.sort()
    jogos.append(palpite)

for indice, jogo in enumerate(jogos, start=1):
    print(f'Jogo {indice}: {jogo}')
print()


'''
Exercicio 089 - Boletim com Listas Compostas
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
notas_turma = []

while True:
    boletim_aluno = []                  # esvazia a lista notas_aluno

    nome = input('Nome do Aluno: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    notamedia = (nota1 + nota2)/2

    boletim_aluno.append([nome, nota1, nota2, notamedia])
    notas_turma.append(boletim_aluno)

    resposta = input('\nQuer digitar outro numero? S/N: ').upper()
    if resposta != 'S':
        break

print('\nBOLETIM TURMA 1 - 2025')
for indice, dados_aluno in enumerate(notas_turma):
    nome, nota1, nota2, notamedia = dados_aluno
    print(f'Nr. Aluno: {indice:<2} - Nome: {nome:<16} - Nota média {notamedia:>8.2f}.')
print()

indice = int(input('Para visualizar o detalhamento das notas do aluno, informe o "Nr. Aluno": '))
print(f'\nDetalhamento - Aluno: {nome}')
print(f'Nota 1: {nota1:.2f}')
print(f'Nota 2: {nota2:.2f}')
print(f'Média : {notamedia:.2f}')
print()