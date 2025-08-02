# Tuplas: Metodos

marcas = ('gol', 'celta', 'palio',)
numeros = (1, 30, 21, 2, 9, 65, 34,)

# 1. Métodos com mesma sintaxe das Listas

# 1.1. Iterar: igual às Listas
# Usa o comando FOR para percorrer os dados de uma lista.
# Apresenta cada retorno de registro em uma linha.

for marca in marcas:
    print(marca)
    print()

# 1.2. Enumerar: igual às Listas
# Exibe o índice do objeto dentro da lista.
# Usar os comandos FOR, IN, e ENUMERATE:
# Estabelecer as duas variaveis a serem exibidas (indice e carro)
# As variáveis serão parte de uma função 'f', e por isto entre {}

for indice, marca in enumerate(marcas):
    print(f'{indice}:{marca}')
    print()
    
# 2. Métodos da Classe Tuple

marcas = ('gol', 'celta', 'palio',)

# 2.1. Count

marcas.count('gol')
marcas.count('celta')

# 2.2. Index

marcas.index('gol')
marcas.index('celta')

# 2.3. Len

len(marcas)