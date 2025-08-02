'''NOTACOES SOBRE VARIAVEIS:

1. Caracteres especiais para alinhamento
'''

nome = input('Qual é o nome dele? ')
print(f'O nome dele é {nome}')
print(f'O nome dele é {nome:>20}')          # > Alinha a direita
print(f'O nome dele é {nome:<20}')          # < Alinha a esquerda
print(f'O nome dele é {nome:^20}')          # ^ Centraliza
print(f'O nome dele é {nome:20}')
print()


'''
2. Função eval():

A função eval() recebe uma string, mas trata como um valor numérico.
'''

entrada_dados = '1 + 2'
print(type(entrada_dados))      # class 'str'
print(entrada_dados)            # 1 + 2
print(eval(entrada_dados))      # 3


calculadora = eval(input("Insira a função a ser calculada: "))
print(calculadora)
print()

'''
3. Inversão exibição:
'''

texto = 'Hannah'

print(f'A palavra {texto} é um palíndromo: independente da ordem lida, será a mesma palavra.')
print(texto)
print(texto [::-1])