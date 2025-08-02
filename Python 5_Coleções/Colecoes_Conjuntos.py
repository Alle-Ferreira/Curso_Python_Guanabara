# Conjuntos ou Sets

# Um set e uma colecao que nao contem duplicacoes.
# Sao usados para representar conjuntos matematicos.
# Sao usados para eliminar itens duplicados em um iteravel.

# 1. Tipos de Sintaxe
# Pode ser usado sem o construtor SET, ou apenas usando {}
# Conjunto/Set NAO ordena as Listas e Tuplas.

# 1.1. Exemplo Sintaxe com SET: mais usada

iteravel = 'abacaxi'
lista_numeros = [1, 2, 3, 2, 1, 4]
tupla_marcas = ('palio', 'gol', 'duster', 'palio', 'gol',)

print(set(lista_numeros))
print(set(iteravel))
print(set(tupla_marcas))
print()

# 1.2. Exemplo Sintaxe com {}: pouco usada

linguagens = {'python', 'java', 'php', 'java'}
numeros = {1, 2, 3, 2, 1, 4}
marcas = {'palio', 'gol', 'duster', 'palio', 'gol'}

print(linguagens)
print(numeros)
print(marcas)
print()


# 2. Acessando os dados

# 2.1. Indexação e Fatiamento: 
# Conjunto/Set NÃO suporta Indexação ou fatiamento.

# Para indexar ou fatiar, é necessário antes converter para lista.

numeros = {1, 2, 3, 2, 1, 4}

numeros = list(numeros)
print(numeros[0])
print()

# 2.2. Iteração do conjunto:
# A forma usual de percorrer um conjunto é com comando FOR.

marcas = {'palio', 'gol', 'duster', 'palio', 'gol'}

for marca in marcas:
    print(marca)
    print()

# 2.3. Enumerando os objetos do conjunto.
# Usada para identificar o indice do objeto dentro do laço FOR.

for indice, marca in enumerate(marcas):
    print(f'{indice}: {marca}')
    print()


