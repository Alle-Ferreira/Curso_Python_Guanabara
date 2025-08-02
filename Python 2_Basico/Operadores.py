'''
1. Operadores Aritmeticos

+ Adição
- Subtração
* Multiplicação          ** Exponenciação
/ Divisao Simples        // Divisão Inteira
                          % Resto da Divisão

= Atribui valor          == Igual


1.1. Ordem de Precedencia:

1o) entre parenteses ()
2o) exponenciação **
3o) multiplicação, divisão, divisão inteira, resto de divisão
4o) adição, subração
'''

print(5 + 3 * 2)   #11
print((5+3) * 2)   #16

print((3*5)+(4**2))    #31
print(3*5+4**2)        #31
print(3*(5+4)**2)      #243
print()

numero1 = int(input('O 1o numero é '))
numero2 = int(input('O 20 numero é '))
print(f'A soma dos valores é {numero1+numero2}')
print()

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
exponenciacao = numero1 ** numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2 
divisao_resto = numero1 % numero2

print(soma)
print(subtracao)
print(multiplicacao)
print(exponenciacao)
print(divisao)
print(divisao_inteira)
print(divisao_resto)
print(f'A soma é {soma}, a multiplicação é {multiplicacao}, e a divisão é {divisao}')
print()

# Raiz Quadrada

numero = int(input("Escolha outro numero inteiro:"))
raiz_quadrada = numero ** (1/2)
print(f'A raiz quadrada de {numero} é {raiz_quadrada}.')
print()