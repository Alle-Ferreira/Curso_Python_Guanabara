'''Exercício 061 - Progressão Aritmética_v.02
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
- O primeiro termo é o primeiro número da sequência.
- A razão é a diferença constante entre termos consecutivos.
'''
print('=' * 40)
print('Termos de Progressão Aritmética'.center(40))
print('=' * 40)

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
contador = 0
resposta = 'S'

while contador < 10:
    print(termo, end = ', ')
    contador += 1
    termo = termo + razao
print('fim da progressão')
print()

'''Exercício 062 - Super Progressão Aritmética_v.03
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''
def progressao_aritmetica():
    primeiro_termo = int(input('\nDigite o primeiro termo: '))
    razao = int(input('Digite a razão: '))
    termo = primeiro_termo
    contador = 0
    while contador < 10:
        print(termo, end = ', ')
        contador += 1
        termo = termo + razao
print('fim da progressão')
print()

print('=' * 40)
print('Termos de Progressão Aritmética'.center(40))
print('=' * 40)

continua = 'S'
while continua == 'S':
    progressao_aritmetica()
    continua = input('\nGostaria de verificar outra progressão? Responda [S]/[N]:').upper().strip()
print('fim da progressão')
print()


'''Exercício 063 - Sequência de Fibonacci_v.04
Crie um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
Dicas:
- A sequência de Fibonacci é formada por uma sucessão de números em que cada termo, depois dos dois primeiros, é a soma dos dois anteriores. Por exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
- A sequência de Fibonacci começa com os números 0 e 1.       
'''

fibonacci = [0, 1]
contador = 3
sequencia = 0
termos = int(input('Quantos termos da sequencia Fibonacci dever ser exibidos? '))

while contador <= termos:
    sequencia = fibonacci[-1] + fibonacci[-2]
    contador += 1
    fibonacci.append(sequencia)
print(fibonacci)
print()


'''Exercício 064 - Tratando Vários Valores_v.05
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

numero = 0
contador = 0
soma = 0

while numero != 999:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    print('Errou! Tente novamente.')
    contador += 1
    soma = soma + numero
print(f'Finalmente! Você precisou digitar {contador} números até descobrir o número para encerrar o programa.')
print(f'O somatório dos números digitados é {soma}.')


'''Exercício 065 - Maior e Menor Valores
a) Crie um programa que leia vários números inteiros pelo teclado.
b) O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. O programa deve continuar lendo números até que o usuário decida parar. 
c) No final da execução, mostre:
- a média entre todos os valores;
- qual foi o maior valor lido;
- qual foi o menor valor lido. 
''' 

numeros = []
soma = 0
contador = 0
continua = 'S'

while continua == 'S':
    numero = int(input('Digite um número inteiro: '))
    numeros.append(numero)
    contador += 1
    soma = soma + numero
    continua = input('\nQuer incluir outro número? Responda [S]/[N]: ').upper().strip()
print(f'Você digitou {contador} números, com somatório igual a {soma}.')
print(f'A média dos números digitados é {soma / contador}.')
print(f'O maior número digitado foi {max(numeros)}, e o menor número digitado foi {min(numeros)}')
print()