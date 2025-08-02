'''
Subprogramas: Escopo de Variáveis em Programas e sub-programas

1. Tipos de Variáveis

a) Variáveis locais: 

   São definidas pelo sub-programa, as quais tem seu escopo usualmente é o corpo do subprograma.
   - Normalmente podem ser dinamicas da pilha ou estáticas.
   - Mas no Python, todas as variáveis locais são dinâmicas da pilha.

b) Variáveis Globais: 

   São declaradas em definições de método, portanto precisam ser definida fora dele. 
   Caso haja uma variável local com o mesmo nome de uma variável global:
    - A global é implicitamente declarada como local dentro da função.
    - Para alterar a variável global, seria necessário explicitar, dentro de cada função, que o nome da variável é referente a ela. 
    - Isso pode ser feito com a palavra reservada 'global'.

    
Importante: 
Usaremos variáveis locais e globais com o mesmo nome somente para efeitos didáticos, pois nao se deve usar duas variáveis com o mesmo nome.'''


'''Exemplo 1 : Variaveis locais e globais, com nomes e escopos diferentes'''

def teste_escopo():
    x = 8       # Variável Local
    print(f'Na função teste_escopo, a variável global "n" vale ela mesma: {n}, pois não foi definida dentro da função')
    print(f'A variável local "x" só é válida dentro do escopo da função: {x}')


# Main Program
n = 2           # Variável Global
print(f'No programa principal, a variável global "n" vale ela mesma: {n}')

teste_escopo()


'''Exemplo 2 : Variaveis locais e globais de mesmo nome, mas escopo diferente'''

def teste_escopo(b):
    n = 6       # Variável Local
    x = 8 + b   # Variável Local
    print(f'''\n1. Na função teste_escopo:
    A) A variável GLOBAL "n" vale ela mesma, mas é usada apenas como o parametro recebido "b" = {b}
    B) pois, dentro da função, "n" terá o valor da variavel LOCAL: n = {n}
    C) A variável LOCAL "x", que é igual a (8 + b) só é válida dentro do escopo da função, que adiciona a ela o valor de "b" (parametro recebido): x = {x}''')


# Main Program
n = 2           # Variável Global
teste_escopo(n)

print(f'''\n2. No programa principal:
    A) A variável GLOBAL "n" vale ela mesma, pois não foi redefinida dentro da função teste_escopo: n = {n}
    B) As variáveis LOCAIS da função teste_escopo "x" e "b" inexistem fora da função.''')


'''Exemplo 3: Variaveis locais e globais dentro da função, com uso da palavra reservada GLOBAL'''

def teste_escopo(b):
    global n    # Define que "n" dentro da função é a varoável global
    n = 6       # Então, ao inves definir uma variavel local, esta linha atribuirá a "n" o valor "6" GLOBALMENTE (dentro e fora da função)
    x = 8 + b   # Variável Local
    print(f'''\n1. Na função teste_escopo:
    A) A variável GLOBAL "n" vale ela mesma, por ter sido especificada como Global dentro da função: n = {n}.
    B) E também é usada como o parametro recebido "b" = {b}.
    C) A variável LOCAL "x", que é igual a (8 + b) só é válida dentro do escopo da função, que adiciona a ela o valor de "b" (parametro recebido): x = {x}.''')


# Main Program
n = 2           # Variável Global
teste_escopo(n)

print(f'''\n2. No programa principal:
    A) A variável GLOBAL "n" é ela mesma, dentro e fora da função, devido ao uso da palavra reservada "global'.
    b) Mas por isto teve seu valor, redefinido dentro da função teste_escopo, alterado globalmente para n = {n}.
    B) As variáveis LOCAIS da função teste_escopo "x" e "b" inexistem fora da função.''')