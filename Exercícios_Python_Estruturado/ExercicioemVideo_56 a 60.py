'''Exercício 056 - Análise de Dados do Grupo
Desenvolva um programa que leia o nome, idade e sexo de várias pessoas. No final, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos
'''
pessoas = []                              
contador_pessoas = 0
somatorio_idade = 0
contador_mulheres_menos_20 = 0
homem_mais_velho = ('', 0, 'M')                                                 # nome, idade, genero                          
resposta = 'S'                                                                  # Inicializa a variável resposta para entrar no loop

while resposta == 'S':
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    genero = input('Digite o gênero (M/F): ').strip().upper()
    
    pessoas.append((nome, idade, genero))                                       # Define que: [0]nome, [1]idade, [2]gênero
    contador_pessoas += 1
    somatorio_idade += idade
    
    if genero == 'M' and idade > homem_mais_velho [1]:
        homem_mais_velho = [nome, idade, genero]
    elif genero == 'F' and idade < 20:
        contador_mulheres_menos_20 += 1
    resposta = input('\nDeseja continuar? (S/N): ').strip().upper()

media_idade = (somatorio_idade / contador_pessoas)                              # media_idade = sum(pessoa[1] for pessoa in pessoas) / len(pessoas)

print(f'Média de idade do grupo: {somatorio_idade / contador_pessoas:.2f}')
print(f'Número de mulheres com menos de 20 anos: {contador_mulheres_menos_20}')
print(f'Homem mais velho tem {homem_mais_velho[1]} anos e se chama {homem_mais_velho[0]}.')
print()


'''Exercício 057 - Validação de Dados
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor válido.
'''

genero = input('Digite o gênero (M/F): ').strip().upper()

while genero not in ('M', 'F'):
    print('Gênero inválido. Tente novamente.')
    genero = input('Digite o gênero (M/F): ').strip().upper()
if genero == 'F':
    print('Você digitou F, feminino.')
elif genero == 'M':
    print('Você digitou M, masculino.')


'''Exercício 058 - Jogo da Adivinhação
Melhore o jogo do Exercicio 028 onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint
from time import sleep

print('-=-' * 25)
print('Vamos jogar? \nEu vou pensar em um número entre 0 e 10, e vc tentará adivinhá-lo.')
print('Processing...')
sleep(1)

numero_usuario = int(input('Tente adivinhar qual numero eu pensei: '))
numero_computador = 0
contador = 1

while numero_usuario != numero_computador:
    print(f'Você passou longe...eu pensei no numero {numero_computador}. Vamos novamente!')
    numero_computador = randint(0, 10)
    contador += 1
    print('Processing...\n')
    sleep(1)
    numero_usuario = int(input('Qual numero eu pensei: '))
print('Ah! Aí sim! Leu meus pensamentos: escolheu o mesmo numero que eu!')
print(f'Foram {contador} tentativas até você acertar!')
print('-=-' * 25)
print()



'''Exercício 059 - Criando um Menu de Opções
Crie um programa que leia dois números e mostre na tela a seguinte menu de opções:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
O programa deverá realizar a operação solicitada em cada caso.
'''
print('=-=' * 25)
print('Calculadora Python')
print('=-=' * 25)


operacao = 4
while operacao == 4:
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    operacao = int(input('''
Escolha o tipo de operação a ser realizada:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
'''))

if operacao == 1:
    print(f'A soma de {numero1} + {numero2} é igual a {numero1 + numero2}.')
elif operacao == 2:
    print(f'A multiplicação de {numero1} * {numero2} é igual a {numero1 * numero2}.')
elif operacao == 3:
    if numero1 > numero2:
        print(f'O maior número entre {numero1} e {numero2} é {numero1}.')
    elif numero2 > numero1:
        print(f'O maior número entre {numero1} e {numero2} é {numero2}.')
    else:
        print(f'Os números {numero1} e {numero2} são iguais.')
elif operacao == 5:
    print('Saindo do programa...')  
else:
    print('Opção inválida.')
print()


'''Exercício 060 - Cálculo do Fatorial
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
Dicas: 
- Fatorial é o produto de todos os números inteiros positivos até o número dado.
- from math import factorial
'''

# Sintaxe 1: Calculo manual
indice = 1
fatorial = 1

while indice <= numero_inteiro:
    fatorial = fatorial * indice
    print(fatorial, end=', ')
    indice += 1

print(f' O fatorial de {numero_inteiro} é igual a {fatorial}.')
print()


# Sintaxe 2: Usando a biblioteca math, factorial(n)
from math import factorial

numero_inteiro = int(input('Digite um número para calcular o fatorial: '))
fatorial = factorial(numero_inteiro)
print(f'O fatorial de {numero_inteiro} é igual a {fatorial}.')
print()