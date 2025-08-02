'''Estruturas Condicionais

1. IF: estrutura condicional simples, composta por UNICO desvio
Exemplo de código usando IF: 
'''

print('Exercicio_1: IF')
saldo = 2000.0

saque = float(input('Informe o valor do saque:'))
if saldo >= saque:
    print('Saque realizado com sucesso')
    print()
if saldo < saque:
    print('Saldo insuficiente')
    print()


'''
2. IF / ELSE: estrutura condicional composta por DOIS desvios
Se a expessão testada no IF for verdadeira, o bloco de codigo do IF será executado.
Se a expessão testada no IF for falsa, o bloco de codigo do ELSE será executado.
Exemplo do mesmo código, usando IF e ELSE:
'''

print('Exercicio_2: IF/ELSE')
saldo = 2000

saque = float(input('Informe o valor do saque:'))
if saldo >= saque:
    print('Saque realizado com sucesso')
    print()
else:
    #Este trecho do código deixou de ser necessario: (saldo < saque:) 
    print('Saldo insuficiente')
    print()


'''
3. IF / ELIF / ELSE: estrutura condicional composta por MAIS DE DOIS desvios
   O ELIF pode se repetir quantas vezes forem necessárias para testar as condições.
Exemplo do mesmo código, enriquecido, para uso de IF, ELIF, e ELSE:
'''
print('Exercicio_3: IF/ELIF/ELSE')

saldo = 2000

opcao = int(input('Informe uma opção: \n[1] Sacar [2] Extrato: '))
print()
if opcao == 1:
    saque = float(input('Informe a quantia desejada para saque:'))
    if saldo >= saque:
        print('Saque realizado com sucesso')
        print()
    else:
        print('Saldo insuficiente')
        print()
elif opcao == 2:
    print("Exibindo o extrato...")
    print()
else:
    print('Opçao inválida')
    print()


''' 3.1. IF Aninhado '''
print('Exercicio_4: IF Aninhado_1')

cheque_especial = 450
saldo = 2000
conta_normal = 1
conta_universitaria = 2

tipo_conta = int(input('Informe seu tipo de conta: \n[1] conta normal \n[2] conta universitaria \nMinha conta é uma :'))
print()
saque = float(input("Informe o valor a sacar: "))
if tipo_conta == 1:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
        print()
    elif (saldo + cheque_especial) >= saque:
        print('Saque realizado com limite do cheque especial.')
        print()
    else:
        print('Não foi possível realizar a operação: Saldo insuficiente.')
        print()  
elif tipo_conta == 2:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
        print()
    else:
        print('Saldo insuficiente.')
        print()


print('Exercicio_5: IF Aninhado_2') 
'''
Com a conta_normal FALSE, a aplicação ignora esta possibilidade, e considera apenas regra para a conta_universitaria
Com as duas contas FALSE, ele ignora as duas possibilidades e vai direto para o ELSE.'''

conta_universitaria = True
conta_normal = False

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso')
        print()
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com limite do cheque especial.')
        print()
    else:
        print('Não foi possível realizar a operação: Saldo insuficiente.')
        print()
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
        print()
    else:
        print('Não foi possível realizar a operação: Saldo insuficiente.')
        print()
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o gerente.")
    print()


'''
4. IF Ternário
If Ternario permite escrever as condições em uma linha de código. Ele é composto por:

- 1a parte: retorno caso a expressão retorne verdadeira
- 2a parte: é a expressão lógica
- 3a parte: retorno caso a expressão não seja atendida
'''
print('Exercicio_6: IF Ternário')

status = 'Sucesso' if saldo >=saque else "Falha"
print(f'{status} ao realizar a operação.')
print()