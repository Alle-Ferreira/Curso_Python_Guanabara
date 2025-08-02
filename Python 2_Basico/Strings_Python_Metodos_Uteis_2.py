#Exercicio 1:
nome = "AlEssAndrA"
print(nome.upper())
print(nome.lower())
print(nome.title())
print()

#Exercicio 2:
mensagem = '  Ola, Mundo!  '
print(mensagem.strip() + '!') #retira todos os espaços
print(mensagem.lstrip() + '!') #retira espaços á direita (left)
print(mensagem.rstrip() + '!') #retira espaços á esquerda (right)
print()

#Exercicio 3:
menu = "Parmeggiana"
print(menu.center(20))
print(menu.center(20,'#'))
print('###' + menu + '###')
print()

#Exercicio 4:
vogais = 'aeiou'
print(' '.join(vogais))
print('*'.join(vogais))
print()