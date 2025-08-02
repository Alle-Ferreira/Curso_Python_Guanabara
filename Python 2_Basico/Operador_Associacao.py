#Operadores de Associação
#São usados para verificar se um objeto está presente em usa sequencia
#Pode verificar em uma lista [], ou numa string "".
#Python trata letras maiúsculas/minúsculas, e acentuação como caracteres diferentes

#Exercicio Pratico 1
print("Exercicio Pratico 1")
curso = "Curso Python"
frutas = ['laranja', 'uva', 'limao']
saques = [1500, 100]

print("Python" in curso)
print('maça' not in frutas)
print(200 in saques)
print()

#Exercicio Pratico 2
print("Exercicio Pratico 2")

frutas = ['limão', 'uva']
curso = "Curso de python"

print('laranja' in frutas)
print('limão' not in frutas)
print("py" in curso)