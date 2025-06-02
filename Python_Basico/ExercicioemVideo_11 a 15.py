'''
Desafio 011:
Desenvolva um programa que leia largura e altura de uma parede, 
calcule a sua área e a quantidade de tinta necessária para pintá-la,
considerando que cada litro de tinta pinta uma área de 2 mts quadrados.
'''

largura_parede = float(input('Insira a largura da parede em metros (use ponto para casas decimais): '))
altura_parede = float(input('Insira a altura da parede em metros (use ponto para casas decimais): '))

litro_tinta = 2   # 2mts quadrados
area_parede = largura_parede * altura_parede
total_tinta_parede = area_parede / litro_tinta

print(f'Sua parede tem uma área de {area_parede} mts2.')
print(f'Voce precisará de {total_tinta_parede:.2f} lts de tinta para pintar toda a parede.')
print()


'''
Desafio 012:
Desenvolva um programa que leia o preço de um produto, 
e mostre seu novo preço com desconto de 5%.
'''

percentual_desconto = 0.05      # 5% 

preco_produto = float(input('Insira o preço de etiqueta do produto. Use ponto para separar as casas decimais: R$ '))
print('Para pagamento a vista, há um desconto de 5%, sobre valor de etiqueta do produto.')

desconto_avista = preco_produto * percentual_desconto
preco_desconto = preco_produto - desconto_avista

print(f'Para o produto selecionado, o desconto será de R$ {desconto_avista:.2f}, então o valor a pagar é de R$ {preco_desconto:.2f}')
print()

'''
Desafio 013:
Desenvolva um programa que leia o salário de um funcionario, 
e mostre seu novo salário, com aumento de 15%.
'''
percentual_aumento = 0.15     # 15%

salario_funcionario = float(input('Qual o valor em reais do salario a ser reajustado? Use ponto para separar as casas decimais: R$ '))
salario_reajustado = salario_funcionario + (salario_funcionario * percentual_aumento)

print(f'O salário reajustado terá o valor de R$ {salario_reajustado:.2f}.')
print()


'''
Desafio 014:
Desenvolva um programa que converta uma temperatura, 
informada em graus Celsius, para graus Fahrenheit.
'''
# fahrenheit_para_celsius = (5/9) * (temperatura_fahrenheit - 32)
# (para inserir caracteres sobrescritos, segure o alt e digite 167)

temperatura_celsius = float(input('Qual a temperatura em graus Celsius? C = '))
celsius_para_fahrenheit = ((9/5) * temperatura_celsius) + 32

print(f'A temperatura informada em Cº equivale a {celsius_para_fahrenheit:.1f} Fº.')
print()


'''
Desafio 015:
Desenvolva um programa que pergunta a quantidade de km rodados por um carro alugado, 
e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que a locação custa R$ 60,00/dia e R$ 0,15 por km rodado.
'''

km_rodado = float(input('Quantos km o veículo rodou? Use ponto para separar as casas decimais: '))
qtdade_dias_locado = int(input('Insira o numero de dias em que o veículo ficou alugado: '))
print()

custo_locacao_dia = 60.00   # reais 
custo_locacao_km = 0.15     # reais
total_custo_locacao = custo_locacao_dia * qtdade_dias_locado
total_custo_km_rodado = custo_locacao_km * km_rodado
total_a_pagar = total_custo_locacao + total_custo_km_rodado

print(f'O custo de locação por dia é de R$ {custo_locacao_dia:.2f}\nPor {qtdade_dias_locado} dia(s) locado, o valor a pagar pela locação é R$ {total_custo_locacao:.2f}')
print(f'Já o custo de locação por km rodado é de R$ {custo_locacao_km}\nComo o veículo rodou {km_rodado} km, o valor a pagar pelos kms rodados é R$ {total_custo_km_rodado:.2f}')
print(f'Então, o valor total a pagar é de R$ {total_a_pagar:.2f}')
print()
