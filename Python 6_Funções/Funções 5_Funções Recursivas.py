'''Funções Recursiva:

Chama a si mesma:

def regressiva_1(x):
   print(x)
   regressiva_1(x - 1) 


def regressiva_2(x):
   if x <= 0:
        print("Acabou")
    else:
        print(x)
        regressiva_2(x-1)


Comparando Iteração X Recursão - Verificação maior numero sem MAX:'''

# a) Iteração:
def encontrar_maior_elemento_iterativo(lista):
    """ Encontra o maior elemento em uma lista de números inteiros de forma não recursiva.
    Args lista: A lista de números inteiros.
    Returns: O maior elemento da lista. """

    if len(lista) <= 1: # se lista tiver no máximo 1 elemento, ele é o maior.
        return lista[0]

    maior_elemento = lista[0]
    for numero in lista[1:]:
        if numero > maior_elemento:
            maior_elemento = numero

    return maior_elemento


# Main Program
lista_exemplo = [7, 2, 5, 1, 4, 3, 6]
maior_elemento = encontrar_maior_elemento_iterativo(lista_exemplo)
print(f"O maior elemento da lista é: {maior_elemento}")


# b) Recursão
def encontrar_maior_elemento(lista):
    """ Retorna o maior elemento de uma lista usando recursão."""
    if len(lista) == 1:
        return lista[0]             # Se só tem 1 numero, ele é o maior.

    maior_elemento = lista[0]       # Passo recursivo.
    for numero in lista[1:]:
        if numero > maior_elemento:
            maior_elemento = numero

    return maior_elemento


# Main Program
lista_exemplo = [7, 2, 5, 1, 4, 3, 6]
maior_elemento = encontrar_maior_elemento(lista_exemplo)
print(f"O maior elemento da lista é: {maior_elemento}")


''' Exemplos de funções com Recursão:

Exemplo 1: Sequencia Simples:'''

def nao_recursiva(inicio, fim, passo):
    for y in range (10, -1, -1):
        print(y, end=' ')
    print('Acabou')

def recursiva(x):
    print(x, end=' ')
    if x > 0:
        recursiva(x-1)
    else:
        print('Acabou')


# Main Program
nao_recursiva(10, -1, -1)
recursiva(10)


''' Exemplo 2: Calculo Fatorial'''

def fatorial_nao_recursivo(n):
    fatorial = 1
    if n == 0 or n == 1:
        return fatorial
    else:
        for x in range(2, n + 1):
            fatorial = fatorial * x
        return fatorial


def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        fatorial = n * fatorial_recursivo(n-1)
        return fatorial


# Main Program
resultado = fatorial_nao_recursivo(5)
print(resultado)

vfatorial = fatorial_recursivo(5)
print(f'Resultado recursivo: {vfatorial}')



''' Exemplo 3: Sequencia Fibonacci'''

def sequenciar_fibonacci(n):
    """Determina o n-esimo objeto da sequencia Fibonacci"""
    if n == 0 or n == 1:
        return 1
    else:
        sequencia = sequenciar_fibonacci(n - 1) + sequenciar_fibonacci(n - 2)
        return sequencia


# Main Program:
vfibo = sequenciar_fibonacci(6)  # 6o numero da sequencia fibonacci.
print(vfibo)

print(help(sequenciar_fibonacci)) # exibe a docstring da função.



'''Exemplo 4: Torres de Hanói 
É um quebra-cabeça matemático e de lógica que envolve a movimentação de discos entre três pinos ou torres,
onde discos devem ser movidos de uma torre inicial para uma torre destino, respeitando estas regras:
- Apenas um disco por vez pode ser movido.
- Um disco nunca pode ser colocado sobre um disco menor.
- Todos os discos começam na torre A e devem ser transferidos para a torre C usando a torre B como auxiliar.'''

def mover_disco(origem, destino):
    '''Registra a movimentação dos discos nas torres.'''
    disco = origem.pop()        # pop() remove, e guarda, o último item da lista, que representa o disco no topo da torre.
    destino.append(disco)       # Coloca esse disco no topo da torre destino.

def imprimir_torres(torre_A, torre_B, torre_C):
    '''Exibe o estado atual das três torres. Ajuda a visualizar o progresso passo a passo da resolução.'''
    print("A:", torre_A)
    print("B:", torre_B)
    print("C:", torre_C)
    print()

def torres_de_hanoi_recursivo(num_discos, origem, destino, auxiliar):
    '''Argumentos:
    num_discos: quantos discos precisam ser movidos.
    origem: lista que representa a torre de onde os discos estão saindo.
    destino: torre final.
    auxiliar: torre intermediária.'''
    if num_discos == 1:                                 # Se tiver apenas 1 disco, move direto da origem para o destino.
        mover_disco(origem, destino)
        imprimir_torres(torre_A, torre_B, torre_C)
    else:
        torres_de_hanoi_recursivo(num_discos - 1, origem, auxiliar, destino)        # Move discos de cima(N_discos - 1), da origem para a torre auxiliar.
        mover_disco(origem, destino)                                                # Move o disco maior(base da torre), da origem para o destino.
        imprimir_torres(torre_A, torre_B, torre_C)
        torres_de_hanoi_recursivo(num_discos - 1, auxiliar, destino, origem)        # Move discos de cima(N_discos - 1) da torre auxiliar para o destino.


# Main Program
num_disco = 7
torre_A = list(range(num_disco, 0, -1))    # Inicializa torre A com [7,6,5,4,3,2,1]: range(num_disco, 0, -1) cria torre de discos, do maior para o menor.
torre_B = []
torre_C = []

# Mostrando o estado inicial
imprimir_torres(torre_A, torre_B, torre_C)
torres_de_hanoi_recursivo( num_disco, torre_A, torre_C, torre_B)                    # Inicia o algoritmo recursivo