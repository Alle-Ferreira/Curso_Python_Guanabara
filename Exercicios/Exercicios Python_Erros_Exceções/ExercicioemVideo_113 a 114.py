'''
Tratamento de Erros e Exceções

- ValueError: tipo da variável correto, mas valor é inadequado
- TypeError: tipo da variável não ser suportado
- KeyboardInterrupt: usuário interrompe o programa sem executar, geralmente usanso Ctrl + C.
- ZeroDivisionError

Exercício Python 113 - Funções aprofundadas em Python
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''
def ler_int(entrada):
    while True:
        try:
            return int(input(entrada))
        except (ValueError, TypeError): 
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[0m')
        except KeyboardInterrupt:
            print('\033[31mErro: entrada de dados interrompida pelo usuário.\033[0m')           


def ler_float(entrada):
    while True:
        try:
            return float(input(entrada))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número decimal válido.')
        except KeyboardInterrupt:
            print('\033[31mErro: entrada de dados interrompida pelo usuário.\033[0m')  


# Programa principal
numero = ler_int('Digite um numero inteiro: ')
print(f'Você digitou o número {numero}.')

fracao = ler_float('Digite um valor fracionado, separado por ponto: ')
print(f'Você digitou o número {fracao}.')


'''
Exercício Python 114 - Site está acessível?
Crie um código em Python que teste se um site está acessível pelo computador usado.
'''
from urllib.request import urlopen
from urllib.error import URLError

try:
    site = urlopen('http://www.checktudo.com.br')
except URLError:
    print('O site está indisponível no momento.')
else:
    print('Site disponível.')
    print(site.read())              #faz a leitura do site


