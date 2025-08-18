'''
Exercício 036 - Aprovando emprestimo
Programa para aprovar o emprestimo bancario para a compra de uma casa. Pergunte:
- O valor da casa
- Salario do comprador
- Tempo de financiamento
Parametro: negar o emprestimo se a prestação exceder 30% do salário.'''

vlr_imovel = float(input('Qual o valor do imovel a ser financiado? '))
renda_comprador = float(input('Informe o seu salario mensal: '))
tempo_financiamento = int(input('Em quantos anos voce gostaria de financiar o imovel? '))

limite_faixa_salarial = 0.3
parcelas_financiamento = tempo_financiamento * 12
limite_prestacao_mensal = renda_comprador * limite_faixa_salarial
prestacao_mensal = vlr_imovel / parcelas_financiamento

print(f'O valor da prestação nesta simulação é de R$ {prestacao_mensal: .2f}')
print(f'O limite para a renda mensal de R$ {renda_comprador: .2f} seria uma prestação de até R$ {limite_prestacao_mensal: .2f}')
if prestacao_mensal > limite_prestacao_mensal:
    print(f'Como a prestação está acima do limite, não poderemos aprovar seu financiamento.')
else:
    print(f'Sendo assim, podemos aprovar seu financiamento, em {parcelas_financiamento} parcelas de R$ {prestacao_mensal}. Parabéns!')
print()
    

'''
Exercicio 037 - Conversor de base numerica
Programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão:
[1] Conversão binaria: bin() 0b
[2] Conversão octal: oct() 0o
[3] Conversão hexadecimal: hex() 0x

Parametro posterior: eliminar os 02 primeiros caracteres da resposta, que tipificam o tipo de dado (0b / 0o / 0x)
Atenção: a conversão é str, mas o numero é int. '''

numero = int(input('Insira o numero inteiro a ser convertido: '))
print('''Qual será a base de conversão?
[1] Converter para binário
[2] Converter para octal
[3] Converter para hexadecimal''')

base_conversao = int(input('Digite sua opção: '))

if base_conversao == 1:
    print(f'O valor de {numero} em conversão binaria tem o valor de {bin(numero)[2:]}.')
elif base_conversao == 2:
    print(f'O valor de {numero} em conversão octal tem o valor de {oct(numero)[2:]}.')
elif base_conversao == 3:
    print(f'O valor de {numero} em conversão hexadecimal tem o valor de {hex(numero)[2:]}')
else:
    print('Esta não é uma opção válida.')
print()


'''
Exercicio 038 - Comparando múmeros
Programa que leia dois numeros inteiros e compare-os, mostrando uma das respostas:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

numero_a = int(input('Insira o primeiro numero: '))
numero_b = int(input('Insira o primeiro numero: '))

if numero_a > numero_b:
    print(f'O número {numero_a} é maior que o número {numero_b}.')
elif numero_b > numero_a:
    print(f'O número {numero_b} é maior que o número {numero_a}.')
else:
    print('Não existe valor maior, os dois são iguais')
print()


'''
Exercicio 039 - Ano de Nascimento
Programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
Alistamento: 18 anos'''

from datetime import date

idade_minima = 18
ano_nascimento = int(input('Em qual ano voce nasceu (formato aaaa)? ' ))
ano_alistamento = ano_nascimento + idade_minima
idade_atual = date.today().year - ano_nascimento

if idade_atual == idade_minima:
    print(f'Já está no momento de você se alistar: o alistamento deve ser feito aos {idade_minima} anos.')
elif idade_atual > idade_minima:
    print(f'Você tem {idade_atual}, já passou da hora de você se alistar! Seu alistamento deveria ter sido em {ano_alistamento}.')
else:
    print(f'Falta um tempinho: temos {idade_minima - idade_atual} ano(s) até o seu alistamento. Seu alistamento deverá ser feito em {ano_alistamento}.')
print()


'''
Exercicio 040 - Média das Notas
Programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

nota_1 = float(input('Insira a 1a nota do aluno: '))
nota_2 = float(input('Insira a 2a nota do aluno: '))

nota_media = (nota_1 + nota_2) / 2
print(f'Com notas {nota_1} e {nota_2}, a nota média do aluno é {nota_media}')

if nota_media >= 7.0:
    print('Ele foi aprovado.')
elif 5 <= nota_media < 7:
    print('O aluno precisará passar pela recuperação.')
else:
    print('O aluno foi reprovado, sem possibilidade de recuperação.')
print()
