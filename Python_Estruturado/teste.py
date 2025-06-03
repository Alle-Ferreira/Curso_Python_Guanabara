
def menu():
    menu = """
    Escolha a operação que gostaria de realizar:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Pix
    [0] Sair

    """
    return input()


def deposito(saldo, deposito_valor, extrato, /): # passagem por posição: '/' no final
    if deposito_valor > 0:
        saldo += deposito_valor
        extrato += f'Deposito no valor de: R$ {deposito_valor:.2f}\n'
        print(msg_confirmacao)
    else:
        print(msg_acao_invalida)
    return saldo, extrato


def saque(*, saldo, saque_valor, extrato, limite_saque_valor, LIMITE_SAQUES_DIA, qtdade_saques_dia):   # passagem por nome: '*' no inicio
    if saque_valor > saldo:
        print('Não será possível realizar esta operação: saldo Insuficiente.')
    elif saque_valor > limite_saque_valor:
        print('Não será possível realizar esta operação: o valor excede o limite por saque.')
    elif qtdade_saques_dia > LIMITE_SAQUES_DIA:
        print('Não será possível realizar esta operação: a operação excede o limite de saques diários.')
    elif saque_valor > 0:
        saldo -= saque_valor
        extrato += f'Saque no valor de: R$ {saque_valor: .2f}\n'
        qtdade_saques_dia += 1
        print(msg_confirmacao)
    else:
         print(msg_acao_invalida)
    return saldo, extrato


def extratocliente (saldo, /, *, extrato): # saldo posicional '/', extrato nomeado '*'
    if not extrato:
        print('Não foram realizadas movimentações no período')
        print("FIM".center(36,'='))
    else:
        print(extrato)
        print(f'\nSaldo atual: R$ {saldo:.2f}')
        print("FIM".center(36,'='))
    return

def pix (saldo, pix_valor, limite_pix_valor, valor_sum_pix_dia, LIMITE_PIX_DIA, extrato): 
    if pix_valor > saldo:
        print('Não será possível realizar esta operação: saldo Insuficiente.')
    elif pix_valor > limite_pix_valor:
        print('Não será possível realizar esta operação: o valor excede o limite de transferência.')
    elif (valor_sum_pix_dia + pix_valor) > LIMITE_PIX_DIA:
        print('Não será possível realizar esta operação: a operação excede o limite de transferências diários.')
    elif pix_valor > 0:
        saldo -= pix_valor
        extrato += f'Pix no valor de: R$ {pix_valor: .2f}\n'
        valor_sum_pix_dia += pix_valor
        print(msg_confirmacao)
    else:
        print(msg_acao_invalida) 
    return  saldo, extrato


LIMITE_SAQUES_DIA = 3
LIMITE_PIX_DIA = 800
limite_saque_valor = 500
limite_pix_valor = 500

extrato = '' #string
saldo = 0
qtdade_saques_dia = 0
valor_sum_pix_dia = 0

msg_sem_saldo = 'Não será possível sacar o dinheiro, por falta de saldo.'
msg_acao_invalida = 'Operação inválida. Por favor, informe um valor válido.'
msg_confirmacao = 'Operação realizada com sucesso!\n'

while True:
    opcao = input(menu)
    
    if opcao == '1': 
        print('Operação selecionada: Depósito.')
        deposito_valor = float(input("Informe o valor a depositar: "))
        saldo, extrato = deposito(saldo, deposito_valor, extrato)

    elif opcao == '2':
        print ('Operação selecionada: Saque.')
        saque_valor = float(input("Informe o valor a sacar: "))
        saldo, extrato = saque(
            saldo = saldo,
            saque_valor = saque_valor,
            extrato = extrato,
            limite_saque_valor = limite_saque_valor,
            qtdade_saques_dia = qtdade_saques_dia,
            limite_saques_dia = LIMITE_SAQUES_DIA,)
        
    elif opcao == '3':
        print("EXTRATO".center(36,'='))

    elif opcao == '4':
        print ('Operação selecionada: Transferência por Pix.')
        pix_valor = float(input("Informe o valor a transferir: "))
        
    elif opcao == '0':
        print('Acesso Encerrado. Obrigada por ser nosso cliente!')
        break
    else:
        print(msg_acao_invalida) 
        print()