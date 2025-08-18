''' Exercícios com Tuplas

Exercício 072 - Numero por Extenso

Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
# Tupla com os números por extenso de 0 a 20

numeros_em_tupla = (                                          
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze',
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)
while True:   # Validação: só aceitar números entre 0 e 20
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número {numeros_em_tupla[numero]}.\n')      # Exibir o número por extenso
        break
    print('Número inválido! Tente novamente.')
print()


'''Exercício 073 - Tuplas com Times de Futebol

Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time do Sao Paulo.
'''
classificacao = (
    (1, 'Flamengo'),
    (2, 'Cruzeiro'),
    (3, 'Bragantino'),
    (4, 'Palmeiras'),
    (5, 'Bahia'),
    (6, 'Fluminense'),
    (7, 'Atlético-MG'),
    (8, 'Botafogo'),
    (9, 'Mirassol'),
    (10, 'Corinthians'),
    (11, 'Grêmio'),
    (12, 'Ceará'),
    (13, 'Vasco'),
    (14, 'São Paulo'),
    (15, 'Santos'),
    (16, 'Vitória'),
    (17, 'Internacional'),
    (18, 'Fortaleza'),
    (19, 'Juventude'),
    (20, 'Sport')
)
classificacao_ordenada = sorted(classificacao, key=lambda x: x[1])  # ordena pelo nome (índice 1)

print('-=' * 15)
print(f'Classificação do Brasileirão:')
for posicao, nome in classificacao:
    print(f'{nome}: {posicao}')
print('-=' * 15)
print()

print(f'05 melhores: {classificacao[0:5]}\n')
print(f'Zona de rebaixamento: {classificacao[-4:]}\n')

for posicao, nome in classificacao:
    if nome == 'São Paulo':
        print(f'O time do São Paulo ficou na {posicao}\n') 
        break  

print('-=' * 15)
print(f'Classificação do Brasileirão:')
for posicao, nome in classificacao_ordenada:
    print(f'{nome}: {posicao}')
print('-=' * 15)
print()


'''Exercicio 074 -  Maior e menor valores em Tupla

Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados 
e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint

# Sintaxe 1: Criando a tupla, a partir de uma lista:

numeros_em_lista = []
for numero in range(5):
    numeros_em_lista.append(randint(0, 100))
numeros_em_tupla = tuple(numeros_em_lista)

print("Números gerados:", numeros_em_tupla)
print("Menor valor:", min(numeros_em_tupla))
print("Maior valor:", max(numeros_em_tupla))

# Sintaxe 2: Criando a tupla diretamente:

numeros2 = tuple(randint(0, 100) for numero in range(5))
print("Números gerados:", numeros2)


'''Exercício Python 075 - Análise de dados em uma Tupla

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
# Sintaxe 1: Criando a tupla por meio de uma lista

numeros_lista = []
numeros_pares = []

for numero in range(10):
    numero = int(input('Insira um número: '))
    numeros_lista.append(numero)
print(f'Numeros da lista: ', numeros_lista)

numeros_tupla = tuple(numeros_lista)
print(f'Numeros da tupla: ', numeros_tupla)

if 3 in numeros_tupla:
    print(f'Posição do numero 3: {numeros_tupla.index(3)}')
else:
    print(f'O numero 3 não foi digitado nenhuma vez.')

print(f'Qtdade de ocorrencias do numero 9: {numeros_tupla.count(9)}')

print('Numero pares: ', end = ' ')
for numero in numeros_tupla:
    if numero % 2 == 0:
        print(numero, end = ' ')
print()


# Sintaxe 2: Criando a tupla diretamente

numeros = (int(input('Insira um número: ')),
           int(input('Insira um número: ')),
           int(input('Insira um número: ')),
           int(input('Insira um número: '))
           )
print()


'''Exercício Python 076 - Lista de Preços com Tupla 

Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

produtos = (
    ('maça', 1.50),
    ('banana', 1.0),
    ('uva', 2.0)
)

for nome, preco in produtos:                    # Formato simples
    print(f'{nome}: R$ {preco:.2f}')
print()


print('Lista de Preços'.center(30))
print('-' * 30)
print(f'{"Produto":<15}{"Preço":^15}')          # Formato Tabulado
print('-' * 30)
for nome, preco in produtos:
    print(f'{nome:<20}R${preco:>8.2f}')
print('-' * 30)
print()


'''Exercício Python 077 - Contando vogais em Tupla
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
jogos = ('Genhin', 'Immortal', 'TFT', 'SkyChildren')
VOGAIS = ('A', 'E', 'I', 'O', 'U')

for jogo in jogos:
    print(f'\nNa palavra "{jogo.upper()}" temos as vogais: ', end=' ')
    for letra in jogo.upper():
        if letra in VOGAIS:
            print(letra, end=' ')
