#Fatiamento de Strings

#Exercicio Livre - CNPJ
print('Exercicio Livre - CNPJ')

cnpj = '10970821000104'
codigo_cnpj_1 = cnpj[0:14:2]
codigo_cnpj_2 = cnpj[1:14:2]
msg_verificacao = ('Complete os numeros faltantes (' + codigo_cnpj_1+ ') para completar o CNPJ: ')

print('Validação Tipo_1')
print('Quais os 5 primeiros caracteres do CNPJ?')
print(cnpj[:5])
print()

print(cnpj[-1])
print(cnpj[-6])
print()

print('Validação Tipo_2')
print('Quais os 5 últimos caracteres do CNPJ?')
print(cnpj[-6:-1])
#a ultima posição (-5) deve ser identificada com um numero a mais (-6)
print()

print('Cola: ' + codigo_cnpj_2)
print()

print('Validação Tipo_3')
validacao_cnpj = int(input(msg_verificacao))
if validacao_cnpj == codigo_cnpj_2:
    print('Codigo validado.')
    print()
else:
    print('Os numeros não conferem.')
    print()