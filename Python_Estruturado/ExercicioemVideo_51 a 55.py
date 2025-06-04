'''
Exercicio 051 - Progressao Aritmetica
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

Dica: A Progressão Aritmética (P.A.) é uma sequência de números onde a diferença entre dois termos consecutivos é sempre a mesma. Essa diferença constante é chamada de razão da P.A..
'''
print('=' * 40)
print('Termos de Progressão Aritmética'.center(40))
print('=' * 40)

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
contador = 0

while contador < 10:
    print(termo, end=', ')
    termo = termo + razao
    contador += 1
print()


'''
Exercicio 052 - Números Primos
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

Dicas: 
- Número primo é um número natural, maior que 1, que não possui divisores além de 1 e ele mesmo. Ou seja, ele só pode ser dividido por 1 e por ele mesmo sem deixar resto.
- Números Naturais são números inteiros, positivos, que se agrupam num conjunto chamado de N, composto de um número ilimitado de elementos. Se um número é inteiro e positivo, podemos dizer que é um número natural.
'''

numero_primo = int(input('Digite o numero a ser verificado: '))

if numero_primo <= 1: 
    print(f'O número {numero_primo} não é um número primo.')
else:
    for indicador in range (2, numero_primo):
        if numero_primo % indicador == 0:
            print(f'O número {numero_primo} não é um número primo.')
            print(f'Ele é divisível por {indicador}.')
            break
    else:
        print(f'O número {numero_primo} é um número primo.')
print()


'''
Exercício 053 - Verificador de Palindromo
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''


'''Exercício 054 - Grupo da Maioridade 
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''


'''Exercício 055 - Maior e Menor da Sequência
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

