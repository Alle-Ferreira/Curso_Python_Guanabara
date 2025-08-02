'''Exemplos de Funções

1. Chamada da função variável'''

escolha = input("Escolha uma opção de função: 1 ou 2:") 

if escolha == '1':
    def func1(x):
        return x + 1
    s = func1(10)
else:
    def func2(x):
        return x + 2
    s = func2(10)
print(s,'\n')



'''
2. Chamada de fuso horario com timezone'''

def fuso_brasilia():
    from datetime import datetime
    from zoneinfo import ZoneInfo  

    hora_bsb = datetime.now(ZoneInfo("America/Sao_Paulo"))    # list comprehension
    print(hora_bsb.strftime("%H:%M"))

    return hora_bsb

# Main Program
horario_brasilia = fuso_brasilia()


# Outros fatiamentos com datetime:
print(horario_brasilia.year)
print(horario_brasilia.strftime("%d/%m"))


'''
3. Verificação maior numero sem MAX:'''

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

