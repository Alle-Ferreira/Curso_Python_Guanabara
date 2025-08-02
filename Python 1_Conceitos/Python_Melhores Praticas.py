''' Melhores Práticas:

1. Tabulação:

a) Estruturas aninhadas em Python são representadas por 4 espaçamentos:'''

def funcao_exemplo(x, y):
    if x > y:
        print(x)

'''
b) Entre a declaração da função e o programa principal:
   - Espaçãmento de 2 linhas
   - Declaração de "Inicio do Programa Principal"'''

def funcao_exemplo(x, y):
    if x > y:
        print(x)


# Inicio Programa Principal // Main Program:
funcao_exemplo(8, 5)


'''
2. Docstrings (""" """)

a) Declaração:
   - Importante usar para documentar funções.
   - Devem ser inseridas logo abaixo do nome da função.'''

def funcao_exemplo(x, y): 
    """Compara as variávei x e y"""
    if x > y:
        print(x)


# Inicio Programa Principal // Main Program:
funcao_exemplo(3, 8)

'''
b) Consulta: 
   - Para localizar documentação de uma função, na área do programa principal digite:
     help(funcao_exemplo)
   - O sistema retornará a docstring dentro da função:
    """Compara as variávei x e y"""   
'''