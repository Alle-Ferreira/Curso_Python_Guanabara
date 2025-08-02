'''Listas em Python

Listas são variáveis compostas.
Tudo em Python é objeto. Lista é um objeto.
- Armazena sequencialmente qualquer tipo de objeto, inclusive outras listas.
- Ao contrário das Tuplas, listas podem ser editadas.
- São declaradas dentro de colchetes [a]
- Os objetos separados por vírgulas: [a, b, c]
- No momento da criação, pode-se declarar uma lista vazia []
'''

frutas = ['laranja', 'maça', 'uva']
carro = ['Ferrari', 'F8', 4200000, 2020, 2900, 'Sao Paulo', True]
usuario = []

''' 
1. Listas Simples

a) Declarando listas com Construtor list(): pede um elemento iterável.
- Iterable pode ser uma sequência, um container que suporte iteração, ou um objeto iterador.
- Nao coloca um objeto, e sim cada caracter como um elemento.
'''
letras = list(('a', 'b', 'c'))          # retorna a lista ['a', 'b', 'c']
palavra = list('python')                # retorna a lista ['p', 'y', 't', 'h', 'o', 'n']
numeros = list((1, 2, 3))               # retorna a lista [1, 2, 3].


''' 
b) Declarando listas com Construtor list() + função range():
Colocará cada numero do intervalo como um elemento.
'''
numeros = list(range(10))       # retorna [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
valores = list (range(4,11))    # retorna [4, 5, 6, 7, 8, 9, 10]


'''
c) Acessando objetos das listas
A primeira posição à esquerda das listas é o ZERO.
Índices negativo: conta a partir do último elemento, como -1.
'''
frutas = ['laranja', 'maça', 'uva']
print(frutas [-1])                      # exibe o ultimo objeto da lista.       Retorna: 'uva'
print (frutas [-2])                     # exibe o penultimo objeto da lista.    Retorna: 'maça'


'''
2. Fatiamento: acessando conjuntos de valores da lista em uma sequencia.

Sintaxe:  lista[Inicio:Final:Step]

I - Indice Inicial: [0]
F - Indice Final: a posição definida como final NÃO será incluida no retorno.            
S - Indice do Step: define o intervalo do salto

- Indice Negativo na posição do STEP: inverte ordem, iniciando contagem pelo ultimo registro.
'''

lista = ['ba', 'be', 'bi', 'bo', 'bu', 'ca', 'ce', 'ci']

print(lista[2:])           # inicio na posição 2 ('bi' até o final)
print(lista[:2])           # final na posição 1 (2-1): 'ba', e 'be'
print(lista[1:3])          # inicio na posição 1 / final na posição 2 (3-1)
print(lista[0:3:2])        # inicio na posição 0 / final na posição 3 / step 2
print(lista[::])           # sem definição de intervalos: trará TDS os elementos da lista.
print(lista[::-1])         # 'espelha' a lista, invertendo a ordem de leitura


''' 
3.  Listas Compostas ou Aninhadas

Listas podem armazenar objetos, então podem armazenar outras listas tbm.
É uma estrutura bidimensional (tabela), acessível por indices de linha e coluna.

Estrutura: [[,],[,]]
'''
lista_matriz = [[1,'a', 2], ['b', 3, 4], [6, 5, 'c']]

matriz = [
    ['a', 1, 2],            # linha 0
    ['b', 3, 4],            # Linha 1
    ['c', 5, 6]             # Linha 2 ou -1
]

'''
a) Acessando listas aninhadas: lista [linha][coluna]

- Primeiro identificador é da linha.
- Segundo identificador é da coluna.
'''

matriz [0]          #exibe toda a 1a. linha.                            Retorna: ['a', 1, 2]
matriz [0][0]       #exibe o elemento na 1a. linha e 1a coluna.         Retorna: 'a'
matriz [0][-1]      #exibe o elemento na 1a. linha e ultima coluna.     Retorna: 2
matriz [-1][-1]     #exibe o elemento na ultima linha e ultima coluna.  Retorna: 6

for letra in matriz:        
    print(letra[0]) #exibe objetos na posição 0 de cada linha, um em cada linha.

'''
b) Editando listas aninhadas'''

matriz[0] = ['d', 'meia', 2]                # substitui toda a linha 0 [1, 'a', 2]
matriz[1][2] = 1                            # substitui o '4' na linha 1


# Exemplo de Uso de listas compostas/aninhadas:

turma = []
aluno = []

for c in range(5):                          # laço para inserção de 5 alunos
    aluno.append(int(input('Matricula: ')))
    aluno.append(input('Nome: '))

    turma.append(aluno[:])                  # [:] faz cópia do aluno na turma
    aluno.clear()                           # esvazia a lista aluno


# Atenção para o uso do enumerate() em listas aninhadas: 
# O Enumerate só aceita 02 parametros, então, precisa "empacotar" a lista e depois "desempacotar":

notas_turma = [['Ale', 'Python', 'Brasilia']]

for indice, dados in enumerate(notas_turma):
    nome, curso, cidade = dados
    print('Alunos Estacio - 2025'.center(60))
    print(f'Nr. Aluno: {indice} - {nome}/{cidade} - Curso {curso}.')
