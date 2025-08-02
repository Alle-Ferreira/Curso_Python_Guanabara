#Strings de Multiplas Linhas ou Strings Triplas

print('Exercicio 1 - Formato 1')
#usando F para a função com variável.
nome = 'Guilherme'
mensagem = f'''
    Olá, meu nome é {nome},
e eu sou o professor da turma de Python.
    Você tem alguma dúvida?
'''
print(mensagem)
print()


print('Exercicio 2 - Formato 2')
print('''
    ##### Escolha a Opção desejada: #### 
    
    1 - Deposito
    2 - Saque
    3 - Extrato
    0 - Sair
    
     ''')
print()