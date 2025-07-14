'''Funções em Python_1

Exercício Python 096 - Função que calcula área
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.''' 

def titulos(titulo):
    tamanho = len(titulo) + 10
    print('-' * (tamanho))
    print(f'{titulo.center(tamanho)}')
    print('-' * (tamanho))

def area_retangulo(largura, comprimento):
    area = largura * comprimento
    return area


titulos('Calculo de Área')

largura = float(input('Largura (mts): '))
comprimento = float(input('Comprimento (mts): '))
area_retangulo(largura, comprimento)

print(f'Área do terreno, com {largura} mts x {comprimento} mts, é de {largura * comprimento:.2f} m²\n')    


'''Exercício Python 097 - Um print especial
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''

def escreva(texto):
    tamanho = len(texto) + 4
    print('-' * (tamanho))
    print(f'{texto.center(tamanho)}')
    print('-' * (tamanho))


escreva('Olá, Mundo!')

texto_2 = 'Python é uma linguagem de programação incrível!'
escreva(texto_2)


'''Exercício Python 098 - Função de Contador
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''  

from time import sleep

def contagem(inicio, fim, passo):
    print('\n' + '-' * 40)
    print(f'Contagem de {inicio} até {fim}, contando de {passo} em {passo}:')
    sleep(1)

    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = -passo

    contador = inicio
    if inicio < fim:
        while contador <= fim:
            print(f'{contador}', end=' ', flush=True)   #flush=True garante que o print seja exibido na hora.
            sleep(0.5)
            contador += passo               # Vai aumentando, passo a passo até o final
        print('FIM')
    else:
        while contador >= fim:          
            print(f'{contador}', end=' ', flush=True)   #flush=True garante que o print seja exibido na hora.
            sleep(0.5)
            contador -= passo               # Vai diminuindo, passo a passo ate o final
        print('FIM')

    print('\n' + '-' * 40)


contagem(1, 10, 1)                      # a) de 1 até 10, de 1 em 1
contagem(10, 0, 2)                      # b) de 10 até 0, de 2 em 2

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)


'''Exercício Python 099 - Escrevendo Funções
Faça um programa que tenha uma função chamada maior() que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''    

def maior(*numeros):
    print(f'Foram informados os valores: ', end='')
    for numero in numeros:
        print(f'{numero}', end=', ')
    print(f'e maior valor é {max(numeros)}.\n')


maior(1, 2, 3, 4, 5)
maior(6, 8, 10, 7, 9, 11)
maior(30, 25, 20, 15, 10, 5)


'''Exercício Python 100 - Funções para sortear e somar
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint

def sorteia(inicio, fim, qtdade):
    lista_sorteada = []             #list comprehension: lista_sorteada = [randint(inicio, fim) for _ in range(qtdade)]
    for numero in range(qtdade):
        numero = randint(inicio, fim)
        lista_sorteada.append(numero)
    return lista_sorteada

def soma_par(lista):
    pares = []                      #list comprehension: pares = [numero for numero in lista if n % 2 == 0]
    for numero in lista:         
        if numero % 2 == 0:
            pares.append(numero)
    return pares


lista_sorteada = sorteia(0, 999, 5)
print(f'Os numeros sorteados foram: {lista_sorteada}')

pares = soma_par(lista_sorteada)
print(f'Os numeros pares da lista são:{pares} ')
print(f'Soma dos pares: {sum(pares)}\n')
