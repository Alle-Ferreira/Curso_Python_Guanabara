'''
1. Fatiamento de Strings

Python armazena os caracteres de uma string como uma lista [],
por isto acessa por posiçao dentro da lista.
'''

texto = 'Fatiamento em Python'
print(texto)

print(texto[5:21])
print(texto[:21])
print(texto[0:10])
print(texto[0:10:2])
print()


'''
2. Contagem de Strings: LEN e COUNT
'''

texto = 'Métodos de Contagem em Python'
print(texto)

print(len(texto))                       # len()    conta caracteres

print(texto.count('o'))                 # .count() conta objetos
print(texto.count('o', 0, 13))          # .count( , , )   objeto, posição inicial, posição limite.
print(len(texto.strip()))               # Exclui espaços desnecessários(antes e depois da string), e conta sem estes.
print()


'''
3. Análise/Localização em Strings: IN / FIND
IN: analisa a afirmativa e responde com TRUE ou FALSE
FIND: informa a posição do 1o objeto procurado dentro da string (ignora os demais).  
Maiúsculas e minúsculas, com ou sem acento, são tratados como caracteres distintos.
'''

texto = 'Análise e Localização de caracteres em uma String'
print(texto)

print(texto.find('string'))             # .find()
print(texto.find('ca'))                 # .find()   mostra posição do 1o a aparecer ('ca' na 12a posição).
print(texto.find('ca', 13))             # .find(,)  mostra posição do 1o, a partir da posição definida ('ca' na 25a).
print(texto.rfind('ca'))                # .rfind()  procura a partir da direita
print(texto.lower().find('string'))     # colocar tudo no mesmo padrão, facilita a busca.


print('Análise' in texto)               # TRUE    
print('Analise' in texto)               # FALSE
print('ANÁLISE' in texto)               # FALSE
print()


'''
4. Transformação de Strings
Altera apenas para exibição, NÃO ALTERA o formato do dado armazenado.
É possível executar mais de uma alteração simultaneamente:
'''

texto = '   Transformação em Strings  '
texto_em_lista = ['Transformação', 'em', 'Strings']

print(texto.strip())                                # .strip()         remove espaços inúteis na string.
print(texto.rstrip())                               # .rstrip()        remove espaços no final (à direita) na string.
print(texto.lstrip())                               # .lstrip()        remove espaços no início (à esquerda) na string.
print(texto.upper())                                # .upper()         coloca letras em maiúscula.
print(texto.lower())                                # .lower()         coloca letras em minúscula. 
print(texto.capitalize())                           # .capitalize()    coloca a 1a letra de uma frase em maiúscula.
print(texto.title())                                # .title()         coloca a 1a letra das palavras em maiúscula.
print(texto.upper().strip())                        # Coloca em maiúscula e exclui espaços desnecessários.
print()

print(texto.replace('em Strings', 'Numérica'))      # .replace(,)   substitui caracteres dentro da string.
print(texto.split())                                # .split() separa objetos da string em listas, pelo espaçamento.
print(" ".join(texto_em_lista))                     # ''.join() transforma objetos da lista, numa string.
print()


# Para alterar, precisa incluir a estancia de atribuição no código.
texto = texto.strip().replace('Strings', 'String')  
print(texto)
print()

# Apos separar a string (que é uma lista) em várias listas, é possivel localizar os objetos da lista:
print(texto_em_lista[0])
print(texto_em_lista[1])
print(texto_em_lista[2])
print(texto_em_lista[2][5])              # Traz o caractere na posição 5, do objeto na posição 2 da lista.
print()