'''
Desafio 31:
Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
e R$0,45 para viagens mais longas.
'''

km_viagem_curta= 200
custo_km_viagem_curta= 0.50
custo_km_viagem_longa= 0.45

distancia_viagem = float(input('Qual a quilometragem do percurso? '))

if distancia_viagem <= km_viagem_curta:
    print(f'''Esta é uma viagem curta. 
A passagem para este percurso custa R$ {distancia_viagem * custo_km_viagem_curta:.2f}''')
else:
    print(f'''Esta é uma viagem longa. 
A passagem para este percurso custa R$ {distancia_viagem * custo_km_viagem_longa:.2f}''')
print()


'''
Desafio 032:
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

Parametro: 
- Anos bissextos são divisiveis por 4, 
- Exceto anos multiplos de 100, mas que não sao multiplos de 400

Incremento: permita opção de analisar o ano atual, digitando '0'
'''
from datetime import date

ano_verificado = int(input('Qual o ano a ser analisado? Caso seja atual, apenas digite 0: '))

if ano_verificado == 0:
    ano_verificado = date.today().year

if ano_verificado % 4 == 0 and ano_verificado % 100 != 0 or ano_verificado % 400 == 0:
    print(f'{ano_verificado} é um ano bissexto.')
else:
    print(f'{ano_verificado} não é um ano bissexto.')
print()


'''
Desafio 033:
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

a = int(input('Insira um numero inteiro: '))
b = int(input('Insira outro numero inteiro: '))
c = int(input('Insira o ultimo numero inteiro: '))
print()

menor = c
if a < b and a < c:                             
    menor = a
if b < a and b < c:                            
    menor = b

maior = c
if a > b and a > c:                             
    maior = a
if b > a and b > c:                            
    maior = b

print(f'O numero {menor} é o menor numero.')
print(f'O numero {maior} é o maior numero.')
print()


'''
Desafio 034:
Escrevaum programaque pergunte o salário de um funcionário e calcule o valor do seu aumento. Parasalários superiores aR$1250,00, calcule um aumento de 10%. Paraos inferiores ou iguais, o aumento é de 15%.
'''

salario_base = 1250.00
indice_salario_superior = 0.10   # 10%
indice_salario_inferior = 0.15   # 15%

salario_atual = float(input('Qual o salario do funcionario? '))

if salario_atual <= salario_base:
    salario_reajustado = salario_atual + (salario_atual * indice_salario_inferior)
else:
    salario_reajustado = salario_atual + (salario_atual * indice_salario_superior)

print(f'O salario reajustado será de R$ {salario_reajustado:.2f}')
print()


'''
Desafio 035:
Desenvolva um programa que leia o comprimento de três retas 
e diga ao usuário se elas podem ou não formar um triângulo.

Condição existencia de um triângulo: 
- A soma de dois lados de um triângulo deve ser sempre maior que o terceiro lado. 
'''

print('-=-'* 16)
print('Verificador de Triangulo'.center(48))
print('-=-'* 16)

cateto_a= float(input('Qual o tamanho do segmento A, em centimetros? '))
cateto_b = float(input('Qual o tamanho do segmento B, em centimetros? '))
hipotenusa= float(input('Qual o tamanho da hipotenusa, em centimetros? '))

if cateto_a < cateto_b + hipotenusa and cateto_b < cateto_a + hipotenusa and hipotenusa < cateto_a + cateto_b:
    print('Estas retas podem formar um triangulo.')
else:
    print('Estas retas não podem formar um triangulo.')
print()