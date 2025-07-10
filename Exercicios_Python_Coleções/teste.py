def calculo_fatorial(numero=1):
    fator = 1
    for contador in range(numero, 0, -1):
        fator *= contador
    return fator


numero = int(input('Insira o numero a ser calculado: '))
print(f'O fatorial de {numero} é igual a {calculo_fatorial(numero)}')
