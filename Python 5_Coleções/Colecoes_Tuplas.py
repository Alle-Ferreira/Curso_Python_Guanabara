''' 
Coleções Python: classe Tuplas

São sequências imutáveis, tipicamente usadas para armazenar coleções de itens heterogêneos. 
Elas são aplicadas também quando é necessário utilizar uma sequência imutável de dados homogêneos. 
Ao contrário das Listas, Tuplas são imutáveis.
Expressa por valores separados por virgulas, entre parenteses: 

tuplas = (,)

Importante: 
# O uso das vírgulas é o que gera a tupla, e não o uso de parênteses. 
  Os parênteses são opcionais, exceto no caso em que queremos gerar uma tupla vazia.
# Tuplas podem conter itens distintos:
  Exemplo: 
  pessoa = ('Gustavo', 39, 'M', 99.88)


1. Sintaxe de Declaração: 

- Separando os itens por vírgulas: a, b, c ou (a, b, c)
- Se nenhum argumento for passado, o construtor cria uma tupla vazia: ().
- Usando o construtor do tipo tuple: tuple() ou tuple(iterable)
(iterable pode ser uma sequência, um container que suporte iteração ou um objeto iterador.)
Por exemplo:

tuple('abc')        retorna      ('a', 'b', 'c') 
tuple( [1, 2, 3] )  retorna      (1, 2, 3). 
'''

# Exemplo Sintaxe_1: o ultimo elemento da Tupla tbm deve ser seguido de vírgula.
marcas = ('gol', 'celta', 'palio',)
pais = ('Brasil',)


# Exemplo Sintaxe_2: considera cada letra como um elemento.
letras = tuple('python') 
numeros = tuple([1, 2, 3, 4])


''' 
2. Sintaxe de acesso: semelhante a das tuplas'''

frutas = ('laranja', 'maça', 'uva',)

frutas [0]
frutas [-1]


'''
3. Tuplas Aninhadas

Tuplas são objetos, então Tuplas podem armazenar outras Tuplas.
Podem criar estruturas bidimensionais (tabelas), acessíveis por linhas e colunas.'''

# 3.1. Sintaxe de declaração: parecida com a das tuplas.

matriz = (
    (1,'a', 2),
    ('b', 3, 4),
    (6, 5, 'c'),
)

# 3.2. Sintaxe de acesso: igual a das tuplas.

matriz [0]          #exibe toda a 1a. linha
matriz [0][0]       #exibe o elemento na 1a. linha e 1a coluna.
matriz [0][-1]      #exibe o elemento na 1a. linha e ultima coluna.
matriz [-1][-1]     #exibe o elemento na ultima linha e ultima coluna.

print(matriz [0])
print(matriz [0][0])
print(matriz [0][-1])
print(matriz [-1][-1])
print()

'''
4. Fatiamento
Usado para extrair um conjunto de valores, em uma sequencia.

Sintaxe:
print(tupla[I:F:S])

I - Indice Inicial 
F - Indice Final
S - Indice do Step
    
Lembretes:
# A 1a posição inicial à direita é ZERO, não 1.
# A posição definida como final não será incluida no retorno.
# A posição definida como STEP define o intervalo do salto.
# Indice Negativo na posição do STEP: inverte ordem, iniciando contagem pelo ultimo registro.'''
    
# 4.1. Sintaxe de Declaração: parecida com a das tuplas.

tupla = ('ba', 'be', 'bi', 'bo', 'bu', 'ca', 'ce', 'ci',)

print(tupla[2:])           # inicio na posição 2 ('bi' até o final)
print(tupla[:2])           # final na posição 1 (2-1): 'ba', e 'be'
print(tupla[1:3])          # inicio na posição 1 / final na posição 2 (3-1)
print(tupla[0:3:2])        # inicio na posição 0 / final na posição 3 / step 2
print(tupla[::])           # sem definição de intervalos: trará TDS os elementos da tupla.
print(tupla[::-1])         # 'espelha' a tupla, invertendo a ordem de leitura
print()


'''
5. Exibição de Tuplas

Por padrão, o print() termina com uma quebra de linha (\n).
Mas você pode mudar isso com o parâmetro END:   end =' '  end = ','

Para exibir o indice na tupla, pode ser usado o ENUMERATE ou o INDEX:
Importante: Se a tupla tiver valores repetidos, o .index() sempre retornará o índice da 1a ocorrência.'''

premios = ('Casa', 'Carro', 'Viagem', 'Curso')
cores = ('Amarelo', 'Azul', 'Verde')

# 5.1. Na mesma linha

print(premios)                              # printa a tupla: ('Casa', 'Carro', 'Viagem', 'Curso')

print(premios [0])                          # printa o item

print(premios [1:4], '\n')                  # printa uma tupla com os itens selecionados: ('Carro', 'Viagem', 'Curso')

for premio in premios:
    print(premio, end = ' ')                # printa os itens da tupla, com a separação definida, mas na mesma linha
print()


# 5.2. Cada item em uma linha:

for premio in premios:
    print(premio)                           # printa cada item da tupla em uma linha
print()

for premio in range(0, len(premios)):       # printa os itens no range, um em cada linha
    print(premios[premio])
print()


# 5.3. Cada item em uma linha + indice do item na tupla:

for premio in range(0, len(premios)):       # printa os itens no range + indice, um em cada linha
    print(f'{premio} - {premios[premio]}')
print()

for indice, premio in enumerate(premios):   # printa cada item da tupla + indice, em cada linha
        print(f'{indice} - {premio}')                        
print()

for premio in premios:                      # printa cada item da tupla + indice, em cada linha (ver obs. acima sobre uso do index)
    print(f'{premios.index(premio)}: {premio}')
print()


# 5.4. Ordenando a exibição dos itens de uma tupla:

print(sorted(premios))                      # Transforma a tupla em uma lista, e a ordena por ordem alfabetica
print()

print(cores + premios)                      # Exibe duas tuplas, na ordem que são apresentadas: 1o cores, dps premios


# 5.5. Analisando/Localizando itens das tuplas:

print(len(cores))                           # conta qtos itens tem na tupla
print(len(cores + premios))                 # conta qtos itens tem nas duas tupla

print(cores.count('Azul'))                  # conta o numero de ocorrencias do item
print(cores.index('Azul'))                  # mostra a posição da 1a ocorrencia
print(cores.index('Azul', 1))               # mostra a posição da 1a ocorrencia, a partir da posição definida (1)


# 5.6. Exceção de edição da tupla: DEL

del(cores)                                  # deleta toda a tupla
del(cores[0])  # Não existe edição parcial: apresentará erro