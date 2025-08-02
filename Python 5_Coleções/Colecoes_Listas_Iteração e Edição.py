
'''
Iteração e Manipulação de Listas

1. Editando listas
'''
numeros = [21]
frutas = []
exponenciacao = []
numero = 23
lista_numerica = [8, 2, 5, 4, 9, 3, 0]

'''
a) Inserção
- .insert(): permite definir o posicionamento do novo objeto na lista.
- .append(): por padrão insere objeto no final da lista.
'''

frutas.insert(0, 'melão')               # Retorna ['melão', 'morango']
frutas.insert(1, 'maçã')                # Retorna ['melão', 'maçã', 'morango']

numeros.append(22)                      # numeros = [21, 22]
numeros.append(numero)                  # numeros = [21, 22, 23]
frutas.append('morango')                # frutas = ['morango']

frutas.append(['morango', 'abacaxi', 'figo']) # Colocando objetos dentro do [], aceita inserção da lista como 1 objeto.

for numero in numeros:                        # percorre cada objeto da lista
    exponenciacao.append(numero ** 2)         # Retorna [441], e na linha seguinte [441, 484], e dps [441, 484, 529]

exponenciacao = [numero ** 2 for numero in numeros]     # Retorna lista completa [441, 484, 529]

'''
b) Exclusão em listas:
- comando del[] 
- método .pop(): elimina por posição. Sem parametro, elimina o ultimo objeto.
- método .remove(): elimina por valor. Se o valor não existir, apresentará erro de código
'''
del numeros[0]                          # Elimina o objeto na posição zero.
del numeros                             # Elimina TODA a lista.

frutas.pop()                            # Elimina o ultimo objeto da lista.
frutas.pop(1)                           # Elimina objeto na posição 1 da lista.

frutas.remove('melão')                  # Elimina o objeto de == valor
if 'morango' in frutas:                 # Uso do IF evita erros de código, por inexistencia do valor na lista.
    frutas.remove('morango')

'''
c) Concatenando listas com .extend()
Adiciona uma lista inteira a outra lista já existente.'''

numeros.extend([94, 102, 305, 47, 97,302])          # adiciona os objetos listados
numeros.extend(lista_numerica)                      # adiciona a lista nominada


'''
d) Atribuição: substitui o objeto, a partir da posição.
'''
lista_numerica[2] = 16                  # Substitui o objeto na posição 2 pelo numero "16"


'''
e) Ordenando listas com sort()
'''

lista_numerica.sort()                   # Ordena a lista do menor para o maior
lista_numerica.sort(reverse=True)       # Ordena a lista inversamente


''' 
2. Iterando Listas

a) Iterando Listas com comando FOR

- Usando a compreensão de lista: [x for x in iterable]'
- Usa o comando FOR para percorrer os dados de uma lista.
'''

marcas = ['gol', 'celta', 'palio']
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for marca in marcas:                # Percorre cada objeto da lista.
    print(marca)                    # Apresenta cada objeto da lista em uma linha.

''' 
b) Enumerando conteúdo de Listas com comandos FOR, IN, e ENUMERATE:

Exibe o índice do objeto dentro da lista.
Estabelecer as duas variaveis a serem exibidas (indice e carro)
As variáveis serão parte de uma função 'f', e por isto entre {}'''

for indice, marca in enumerate(marcas):
    print(f'{indice}:{marca}')

''' 
c) Compreensão de Listas: comandos FOR, IN, e IF

Permite aplicar fitros ou modificações nos elementos de uma lista existente.
- Declare a variavel a ser exibida (numero) e a lista de origem (numeros)
- Declare a nova lista (pares) onde a coleção será armazenada.'''

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

pares = [numero for numero in numeros if numero % 2 == 0]