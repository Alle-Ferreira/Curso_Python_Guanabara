numero_primo = int(input('Digite o numero a ser verificado: '))

if numero_primo <= 1: 
    print(f'O número {numero_primo} não é um número primo.')
else:
    for indicador in range (2, numero_primo):
        if numero_primo % indicador == 0:
            print(f'O número {numero_primo} não é um número primo.')
            print(f'Ele é divisível por {indicador}.')
            break
    else:
        print(f'O número {numero_primo} é um número primo.')