#Interpoção de Variáveis
#Usando sintaxe da versão atual e das versões anteriores do Python:
#'%' e o FORMAT, em interpolação de strings, cairam em desuso.

nome = 'Alessandra'
idade = 36
profissao = "Analista de Sistemas"
linguagem = 'Python'
saldo= 45.435
dados = {'nome': 'Alessandra', 'idade': '36'} #usando dicionário


#Exercício 1
print('Exercicio 1: Old Style - Método %')
print('Nome: %s Idade: %d' % (nome, idade))
print()

#Exercício 2
print('Exercicio 2: Método format')
print('Nome: {} Idade: {}' .format(nome, idade))
print('Nome: {0} Idade: {1} Nome: {0}' .format(nome, idade))
print('Nome: {name} Idade: {age}' .format(name=nome, age=idade))
print('Nome: {nome} Idade: {idade}' .format(**dados))
print()

#Exercício 3
print('Exercicio 3: Método f-string')
print(f'Nome: {nome} Idade: {idade} Saldo: {saldo}')
print(f'Nome: {nome} Idade: {idade} Saldo: {saldo: 5.2f}')
print()