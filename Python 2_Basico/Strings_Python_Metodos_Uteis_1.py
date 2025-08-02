#Métodos Úteis

#1. Maiúsculas, Mínúsculas e Títulos:

#Exemplo:
curso = "pYThoN"
print(curso.upper())
print(curso.lower())
print(curso.title())

#2. Eliminando espaços em branco:

#Exemplo:
curso = "  Python  "
print(curso.strip()) #todos os espaços
print(curso.lstrip()) #espaços á direita (left)
print(curso.rstrip()) #espaços á esquerda (right)

#3. Junções e Centralizações

#Exemplo:
curso = "Python"
print(curso.center(10,'*'))
#centraliza e completa espaços p/para atingir nr de caracteres definido.
print(' '.join(curso))
print('*'.join(curso))
#inclui o caracter definido (' ', '*') à variavel (curso)

