def notas_100(valor_saque):
    qtde_notas_100 = int(valor_saque // 100)
    residual_100 = valor_saque % 100
    print(f'Notas de cem: {qtde_notas_100}')

    if residual_100 >= 50:
        valor_saque = residual_100
        notas_50(valor_saque)
    return(valor_saque)

def notas_50(valor_saque):
    qtde_notas_50 = int(valor_saque // 50)
    residual_50 = valor_saque % 50
    print(f'Notas de cinquenta: {qtde_notas_50}')

    if residual_50 >= 10:
        valor_saque = residual_50
        notas_10(valor_saque)
    return(valor_saque)

def notas_10(valor_saque):
    qtde_notas_10 = int(valor_saque // 10)
    residual_10 = valor_saque % 10
    print(f'Notas de dez: {qtde_notas_10}')

    if residual_10 >= 5:
        valor_saque = residual_10
        notas_5(valor_saque)
    else:
        valor_saque = residual_10
        notas_1(valor_saque)
    return(valor_saque)

def notas_5(valor_saque):
    qtde_notas_5 = int(valor_saque // 5)
    residual_5 = valor_saque % 5
    print(f'Notas de cinco: {qtde_notas_5}')

    if residual_5 >= 1:
        valor_saque = residual_5
        notas_1(valor_saque)
    return(valor_saque)

def notas_1(valor_saque):
    qtde_notas_1= int(valor_saque // 1)
    print(f'Notas de um: {qtde_notas_1}')
    return(valor_saque)

residual = 0
valor_saque = int(input('Informe o valor a sacar: '))

if valor_saque >= 100:
    notas_100(valor_saque)
elif 50 <= valor_saque < 100:
    notas_50(valor_saque)
elif 10 <= valor_saque < 50:
    notas_10(valor_saque)
elif 5 <= valor_saque < 10:
    notas_5(valor_saque)
else:
    notas_1(valor_saque)




