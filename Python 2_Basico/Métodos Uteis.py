'''
1.  ord()?
A função ord() retorna o valor numérico Unicode (inteiro) de um único caractere.

ord('A')  # Saída: 65
ord('a')  # Saída: 97

A codificação Unicode atribui um número único a cada caractere. A função ord() permite descobrir qual número representa determinado caractere.

Caractere	ord()
'A'	65
'B'	66
'a'	97
'0'	48
'é'	233
'''


letra = 'z'
codigo = ord(letra)
print(f"O código Unicode de '{letra}' é {codigo}")

# O código Unicode de 'z' é 122


'''1.1. Combinando com chr()

ord() → caractere para número
chr() → número para caractere
'''

print(ord('A'))   # 65
print(chr(65))    # 'A'


'''Aplicações comuns

Criptografia básica (como cifra de César)
Comparações alfabéticas (A < B < C porque 65 < 66 < 67)
Conversão entre letras e números
Tratamento de entradas de teclado ou arquivos binários

Atenção
ord() aceita apenas um caractere. Se passar mais, dá erro:'''