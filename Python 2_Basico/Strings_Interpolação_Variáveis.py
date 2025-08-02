#Interpoção de Variáveis
#Usando sintaxe da versão atual e das versões anteriores do Python:
#'%' e o FORMAT, em interpolação de strings, cairam em desuso.

nome = 'Alessandra'
idade = 36
profissao = "Analista de Sistemas"
linguagem = 'Python'

#1. Old Style: Método %
#Compatível com Python_2, em desuso, pois se alterar a ordem das variáveis ao listar, a variavel será apresentada fora de ordem msm. 

print('1. Old Style: Método %')
print('Olá! Me chamo %s, tenho %d de idade, trabalho como %s, e estou aprendendo programação com a linguagem %s.' % (nome, idade, profissao, linguagem))
print()

#2. Método FORMAT
#Compatível com Python_2, em desuso pelo msm motivo do método %
#Para minimizar risco, vc pode inserir a posição da variável na lista, lembrando que a lista inicia no zero.

print('2. Método FORMAT')
print('Olá! Me chamo {}, tenho {} de idade, trabalho como {}, e estou aprendendo programação com a linguagem {}.' .format(nome, idade, profissao, linguagem))
#preenche as variáveis na ordem em que elas aparecem na lista.
print() 

print('Olá! Me chamo {0}, tenho {1} de idade, trabalho como {2}, e estou aprendendo programação com a linguagem {3}.' .format(nome, idade, profissao, linguagem))
#voce pode definir a posição que a variável aparecerá, e tbm repetir a variável no texto.
print() 

print('Olá! Me chamo {name}, tenho {age} de idade, trabalho como {profession}, e estou aprendendo programação com a linguagem {language}.' .format(name=nome, age=idade, profession=profissao, language=linguagem))
#voce pode nomear a variável, minimizando o risco de erro
print() 

#2.1. Método FORMAT com um Dicionário

print('2.1. Método FORMAT com um Dicionário')
pessoa = {'nome': 'Alessandra', 'idade': '36', 'profissao': 'Analista de Sistemas', 'linguagem': 'Python'} #usando um dicionário

print('Olá! Me chamo {nome}, tenho {idade} de idade, trabalho como {profissao}, e estou aprendendo programação com a linguagem {linguagem}.' .format(**pessoa))
#vincula todas as variáveis ao dicionário PESSOA.
print() 

#3. Método atual: F-STRING
#Melhor legibilidade e assetividade do código.

print('3. Método atual: F-STRING')
print(f'Olá! Me chamo {nome}, tenho {idade} de idade, trabalho como {profissao}, e estou aprendendo programação com a linguagem {linguagem}.')
print() 

#3.1. Formatando FLOAT com F-STRING

PI = 3.14159

print('3.1. Formatando FLOAT com F-STRING')
print(f'Valor de PI: {PI: .2f}') #limita a 2 casas decimais dps do pto
print(f'Valor de PI: {PI: 10.2f}') #define em 10 caracteres antes do pto
print()