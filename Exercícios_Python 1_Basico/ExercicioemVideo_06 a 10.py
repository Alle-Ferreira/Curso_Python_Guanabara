'''
Desafio 006:
Crie um algoritmo que leia um numero, mostre o seu dobro, triplo, 
e a raiz quadrada.
'''

passe_mensal = float(input('Quanto custa o passe mensal do seu jogo favorito?\n(Use ponto, no lugar da vírgula, para informar valores decimais.): '))
print()
passe_bimestral = (passe_mensal * 2)
passe_trimestral = (passe_mensal * 3)
raiz_quadrada = passe_mensal ** (1/2)                        # Sintaxe 1

from math import sqrt                                     
raiz_quadrada_math = sqrt(passe_mensal)                      # Sintaxe 2

print(f'Em dois meses, vc terá gasto R$ {passe_bimestral}.')
print(f'Em três meses, vc terá gasto R$ {passe_trimestral}.')
print(f'A raiz quadrada de {passe_mensal} na Sintaxe 1 é {raiz_quadrada}.')
print(f'A raiz quadrada de {passe_mensal} na Sintaxe 2 é {raiz_quadrada_math}.')
print()


'''
Desafio 007:
Desenvolva um programa que leia as duas notas de um aluno, 
calcule a mostre a sua média.
'''

print('Pronto para inserir as 03 notas do aluno?\n(Use ponto, no lugar da vírgula, para informar valores decimais.): ')
print()
nota1 = float (input('Informe a Nota 1: '))
nota2 = float (input('Informe a Nota 2: '))
nota3 = float (input('Informe a Nota 3: '))
print()

media_notas = float ((nota1 + nota2 + nota3) / 3)
print(f'A media das notas é {media_notas}.')
print()


'''
Desafio 008:
Desenvolva um programa que leia um valor em metros, 
e o exiba convertido para centimetros e milimetros.
1mt = 100 cts
1mt = 1000 mlts
'''
largura_parede = float (input('Qual a largura da parede em metros?\n(Use ponto, no lugar da vírgula, para informar valores decimais.): '))
largura_centimetros = float (largura_parede * 100)
largura_milimetros = float (largura_parede * 1000)
print(f'Entao são {largura_centimetros} centímetros, ou {largura_milimetros} milímetros de largura.')
print()


'''
Desafio 009: Tabuada_v.01
Desenvolva um programa que leia um numero inteiro qualquer, 
e mostre na tela a sua tabuada.
'''

numero = int(input('Escolha um número, de 1 a 10, para ver sua tabuada: '))
print(('_.') * 10)
print(f'{numero:2} x  1 = {numero * 1:3}')     
print(f'{numero:2} x  2 = {numero * 2:3}')
print(f'{numero:2} x  3 = {numero * 3:3}')
print(f'{numero:2} x  4 = {numero * 4:3}')
print(f'{numero:2} x  5 = {numero * 5:3}')
print(f'{numero:2} x  6 = {numero * 6:3}')
print(f'{numero:2} x  7 = {numero * 7:3}')
print(f'{numero:2} x  8 = {numero * 8:3}')
print(f'{numero:2} x  9 = {numero * 9:3}')
print(f'{numero:2} x 10 = {numero * 10:3}')
print(('_.') * 10)
print()


'''
Desafio 010:
Desenvolva um programa que leia quanto dinheiro uma pessoa tem na carteira, 
e mostre quanto doláres ela pode comprar.
Considere a cotação US$ 1,00 = R$ 3,27
'''

valor_reais = float (input('Quanto voce tem de dinheiro na sua carteira?\nUse ponto, no lugar da vírgula, para informar valores decimais: R$  '))
cotacao_dolar = 3.27
valor_dolar = (valor_reais / cotacao_dolar)

print(f'Como a cotação do dólar está em R$ {cotacao_dolar:.2f}, com este valor de R$ {valor_reais:.2f} é possível comprar US$ {valor_dolar:.2f}.')
print()
