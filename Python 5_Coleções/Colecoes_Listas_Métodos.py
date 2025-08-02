
''' Métodos das Listas

1. Métodos de Inclusão em Listas'''

marcas = ['gol', 'celta', 'palio']
marcas2 = ['Volvo', 'Fiat']
marcas3 = []
numeros = [1, 30, 21, 2, 9, 65, 34, 0, 1, 2]
numeros2= [94, 102, 305, 47, 97,302]
exclusao = ['lista', 'para', 'exclusao']

numeracao = numeros             # sintaxe ERRADA: não cria cópia, cria VINCULO
numeracao = numeros[:]          # age como o copy: cria uma copia dos objetos da lista 

'''
a) Método .append(): adiciona objetos à lista.'''

marcas.append('duster')
numeros.append(7)
marcas.append(marcas2)              # Insere 'marcas2' como um objeto da lista: ['gol', 'celta', 'palio', 'duster', ['Volvo', 'Fiat']]

'''
b) Método .copy(): cria a mesma lista numa instancia diferente.
# Em instancia diferente, não sofre as alterações posteriores na lista original.'''

numeros.copy()                  # copia para nova lista
numeracao = numeros.copy()      # copia para a nova lista, com o nome declarado "numeracao"

'''
c) Método .extend: adiciona uma lista inteira a outra lista já existente.'''

numeros.extend([94, 102, 305, 47, 97,302])          # adiciona os objetos listados
numeros.extend(numeros2)                            # adiciona a lista nominada

'''
d) Método .insert(,): permite posicionar a inserção.'''

marcas2.insert(1, 'VW')                             # marcas2 = ['Volvo', 'VW', 'Fiat']


'''
2. Métodos de Indexação:

a) Index: informa indice da 1a ocorrencia do objeto na lista.'''

print(numeros.index(94))                        # Informa a posição do número "94" na lista.

'''
b) Enumerate: exibe o índice do objeto dentro da lista.'''

for indice, numero in enumerate(numeros):       # Enumera todos os objetos da lista
    print(indice, numero)


'''
3. Métodos de Exclusão

a) .remove(): remove o objeto especificado.
- Necessita que o objeto seja especificado.
- A partir do inicio, identifica 1 objeto para remoção de cada vez.
- Se o objeto estiver repetido na lista, remove apenas a 1a ocorrencia.

Se não existir na lista, o programa apresentará ERRO. Na dúvida, usar estrutura IF.
'''
numeros.remove(47)

'''
b) .clear(): apaga TDS os objetos da lista.'''

exclusao.clear()

'''
c) .pop(): retira objeto populado, a partir da posição.
# Sem identificar o posição do objeto, retirará o ultimo populado.'''

numeros.pop()
numeros.pop(16)
numeros.pop(-5)


'''
4. Métodos de Contagem

a) .count(): verifica quantas vezes o objeto aparece na lista.'''

print(numeros.count(0))
print(numeros.count(1))
print(numeros.count(2))

'''
b) len(): verifica a qtdade de objetos da lista'''

print(len(numeros))

if len(numeros) == 0:                   # Verifica se uma lista está vazia
    print('lista vazia')


'''
5. Métodos de Ordenamento:

a) .sort() / sorted(): ordena por letra alfabetica ou numeração crescente'''

marcas.sort()                           # Sort: Não permite o print na mesma linha
print(marcas)

print(sorted(marcas))                   # Sorted: permite ordenar e printar na mesma linha

'''
b) .reverse(): 'espelha' a lista, invertendo a ordem dos objetos.'''

numeros.reverse()

'''
c) .sort() / sorted() com Reverse'''

numeros.sort(reverse=True)              # Ordena a lista descrescente, mas não funciona com o print 
print(numeros)                         

print(sorted(numeros, reverse=True))    # Sorted retorna nova lista ordenada

'''
d) Função anonima lambda + len: ordena pelo tamanho do objeto.'''

marcas.sort(key=lambda x: len(x))               # Sintaxe com Sort: ordenamento crescente

print(sorted(marcas, key=lambda x: len(x)))     # Sintaxe com Sorted: ordenamento crescente

'''
e) Função anonima lambda + len + reverse: ordena decrescente, pelo tamanho do objeto.'''

marcas.sort(key=lambda x: len(x), reverse=True)             # Sintaxe com Sort: ordenamento decrescente

print(sorted(marcas, key=lambda x: len(x), reverse=True))   # Sintaxe com Sorted: ordenamento decrescente
