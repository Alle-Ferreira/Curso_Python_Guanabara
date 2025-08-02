# 1. Atribuindo valores

nota1 = 8
nota2 = 9


# 2. Calculando Dados

media = (nota1 + nota2) / 2


# 3. Imprimindo Dados

print('A média das notas é: ', media)


# 4. Entrada e Saida de dados: Input e Print

numero = input('Digite valor: ')
print(type(numero))

numero = int(input('Digite valor: '))
print(type(numero))

numero = float(input('Digite valor: '))
print(type(numero))


''' 5. Validando a Entrada de Dados: método .is()

Exemplos de uso:
Valida se um campo de entrada possui o tipo de dado definido.
Qdo nao validado, retorna False.

# .isdecimal()
# .isprintable()    verifica se todos os caracteres numa string são imprimíveis.
# .isidentifier()   verifica se uma string é identificador válido, como nomes de variáveis, funções, etc.
# .istitle()
'''

# .isnumeric()
# Verifica tipo de dado numerico.
numero = input('Digite sua senha numérica: ')
print(numero.isnumeric())
print()

# .isalpha()
# Verifica tipo de dado alfabetico.
numero = input('Digite sua senha alfabética: ')
print(numero.isalpha())
print()

# .isalnum()
# Verifica tipo de dado alfanumerico.
numero = input('Digite sua senha alfanumérica: ')
print(numero.isalnum())
print()

# .isupper() e .islower()
# Verifica tipo de dado em cx alta/baixa.
numero = input('Digite sua senha com letras maiusculas: ')
print(numero.isupper())
print()



''' 6. Eval

eval() é uma função embutida em Python que avalia (executa) uma string como uma expressão Python.
Ela interpreta a string como código Python no contexto atual e retorna o resultado da expressão.'''

resultado = eval("2 + 3")
print(resultado)  # Saída: 5
